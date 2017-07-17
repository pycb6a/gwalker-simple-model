import click

import small_model
from gw_rest_client import GwRestClient


@click.command()
def cli():
    client = GwRestClient()
    while client.has_next():
        step = client.get_next()
        getattr(small_model, step)()
        click.echo(client.get_data())
    click.echo(client.get_statistics())
