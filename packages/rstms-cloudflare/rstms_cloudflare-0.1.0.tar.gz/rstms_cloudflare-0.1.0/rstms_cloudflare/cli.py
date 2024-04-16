"""Console script for rstms_cloudflare."""

import json
import sys

import click
import click.core
import CloudFlare

from .exception_handler import ExceptionHandler
from .shell import _shell_completion
from .version import __timestamp__, __version__

header = f"{__name__.split('.')[0]} v{__version__} {__timestamp__}"

RECORD_TYPES = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT", "SRV", "LOC"]
MAX_ZONES = 128


def fail(msg):
    click.echo(msg, err=True)
    sys.exit(-1)


def output(context, result):
    if context.json:
        click.echo(json.dumps(result))
    else:
        click.echo(result)


def parse_name(name, domain):
    if name == "@":
        name = domain
    else:
        name = ".".join([name, domain])
    name = name.strip(".")
    return name


def get_zones(context):
    return context.client.zones.get(params={"per_page": MAX_ZONES})


def get_zone_id(context, domain):
    zones = get_zones(context)
    for z in zones:
        if z["name"] == domain:
            return z["id"]
    fail(f"domain not found: '{domain}'")


def get_zone_records(context, domain):
    records = {}
    zone_id = get_zone_id(context, domain)
    records = context.client.zones.dns_records.get(zone_id, params={"per_page": MAX_ZONES})
    return records


class Context:
    def __init__(self):
        pass


def _ehandler(ctx, option, debug):
    ctx.obj = dict(ehandler=ExceptionHandler(debug))
    ctx.obj["debug"] = debug


@click.group(name="cloudflare")
@click.version_option(message=header)
@click.option("-d", "--debug", is_eager=True, is_flag=True, callback=_ehandler, help="debug mode")
@click.option(
    "--shell-completion",
    is_flag=False,
    flag_value="[auto]",
    callback=_shell_completion,
    help="configure shell completion",
)
@click.option("-q", "--quiet", is_flag=True)
@click.option("-t", "--token", envvar="CLOUDFLARE_AUTH_TOKEN")
@click.option("-d", "--domain", envvar="DOMAIN")
@click.option("-i", "--instance", envvar="INSTANCE")
@click.option("-j", "--json", is_flag=True)
@click.pass_context
def cli(ctx, debug, shell_completion, token, domain, instance, json, quiet):
    ctx.obj = Context()
    ctx.obj.client = CloudFlare.CloudFlare(token=token)
    ctx.obj.domain = domain
    ctx.obj.instance = instance
    ctx.obj.json = json
    ctx.obj.quiet = quiet


def format_dns_record(r):
    out = f"{r['type']} "
    if r["type"] == "MX":
        out += f"{r['priority']} "
    out += f"{r['name']} {r['content']} {r['ttl']}"
    return out


@cli.command
@click.argument("domain", required=False)
@click.argument("record_type", type=click.Choice(RECORD_TYPES), required=False)
@click.argument("name", required=False)
@click.pass_obj
def list(context, domain, record_type, name):
    if domain is None:
        domain = context.domain

    zone_records = get_zone_records(context, domain)

    if name is not None:
        name = ".".join([name, domain])

    records = []
    for record in zone_records:
        if record_type in [None, record["type"]]:
            if name in [None, record["name"]]:
                records.append(record)

    if context.json:
        click.echo(json.dumps(records))
    else:
        for record in records:
            click.echo(format_dns_record(record))


@cli.command
@click.pass_obj
def domains(context):
    zones = get_zones(context)
    if context.json:
        output(context, zones)
    else:
        for zone in zones:
            click.echo(zone["name"])


@cli.command
@click.argument("domain", required=False)
@click.pass_obj
def zone(context, domain):
    if domain is None:
        domain = context.domain

    zone_id = get_zone_id(context, domain)

    click.echo(context.client.zones.dns_records.export(zone_id))


@cli.command
@click.argument("domain")
@click.argument("type", type=click.Choice(RECORD_TYPES))
@click.argument("name")
@click.argument("content")
@click.option("-t", "--ttl", default=60)
@click.option("-p", "--priority", default=10)
@click.pass_obj
def create(context, domain, type, name, content, ttl, priority):
    zone_id = get_zone_id(context, domain)
    name = parse_name(name, domain)
    record = dict(type=type, name=name, content=content, ttl=ttl)
    if type in ["A", "CNAME", "TXT"]:
        pass
    elif type == "MX":
        record["priority"] = priority
    else:
        fail(f"Unsupported record type: {type}")

    ret = context.client.zones.dns_records.post(zone_id, data=record)

    if context.json:
        click.echo(json.dumps(ret))
    else:
        if not context.quiet:
            click.echo(ret["id"])


@cli.command
@click.option("-p", "--priority")
@click.argument("domain")
@click.argument("type", type=click.Choice(RECORD_TYPES))
@click.argument("name")
@click.pass_obj
def delete(context, domain, type, name, priority):
    records = get_zone_records(context, domain)
    name = parse_name(name, domain)

    for record in records:
        if record["type"] == type and record["name"] == name:
            if priority and (priority != record.get("priority", None)):
                continue
            zone_id = record["zone_id"]
            record_id = record["id"]
            ret = context.client.zones.dns_records.delete(zone_id, record_id)
            if context.json:
                click.echo(json.dumps(ret))
            else:
                if not context.quiet:
                    click.echo(ret["id"])
            sys.exit(0)
    if not context.quiet:
        fail("record not found")
    sys.exit(-1)


if __name__ == "__main__":
    sys.exit(cli())
