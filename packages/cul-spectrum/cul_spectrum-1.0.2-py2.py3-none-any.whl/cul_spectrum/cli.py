#!/usr/bin/env python

"""CLI entry point for Spectrum."""

import csv
import json
import sys

import click

from .client import Client


@click.group()
@click.option(
    "--url",
    envvar="SPECTRUM_URL",
    default="https://localhost:8080",
    prompt="Spectrum URL",
)
@click.option(
    "--token",
    envvar="SPECTRUM_TOKEN",
    prompt="Authorization token",
)
@click.pass_context
def main(ctx, url, token):
    """Console client for the CUL Spectrum REST API."""
    ctx.ensure_object(dict)
    ctx.obj["CLIENT"] = Client(url, token=token)


@main.command()
@click.option("--uuid")
@click.option("--name")
@click.option("--csv-file", type=click.Path(exists=True))
@click.option(
    "--out-format",
    default="csv",
    type=click.Choice(["csv", "json"], case_sensitive=False),
)
@click.pass_context
def set_uuid(ctx, uuid, name, csv_file, out_format):
    """Add AIPs by UUID and Name, or a CSV list"""

    # Input options
    if uuid and name:
        csv_fields = ["http_status", "http_body"]
        results = ctx.obj["CLIENT"].set_uuid(uuid, name)
    elif csv_file:
        csv_fields = ["uuid", "name", "http_status", "http_body"]
        with open(csv_file, "r") as file:
            reader = csv.DictReader(file)
            results = ctx.obj["CLIENT"].set_uuids(reader)
    else:
        click.echo("You must provide --uuid and --name, or a --csv-file path")
        exit(1)

    # Output options
    if out_format.lower() == "csv":
        writer = csv.DictWriter(sys.stdout, fieldnames=csv_fields)
        writer.writeheader()

        if isinstance(results, dict):
            results = [results]

        writer.writerows(results)
    elif out_format.lower() == "json":
        click.echo(json.dumps(results, indent=4))
    else:
        click.secho("Output format: {out_format} is not implemented", fg="red")
        exit(1)

    exit(0)


if __name__ == "__main__":
    main()  # pragma: no cover
