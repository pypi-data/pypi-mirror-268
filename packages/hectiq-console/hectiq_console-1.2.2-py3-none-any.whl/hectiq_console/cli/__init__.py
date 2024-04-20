import sys
import click

from .auth import auth_group
from hectiq_console import __version__

import click

import logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

@click.group()
def base():
    pass

@base.command("version")
def version():
    from hectiq_console import __version__, __path__
    click.echo(f"Version: {__version__}")
    click.echo(f"Located: {__path__}")

@base.command("download-model", help="Download a model from the Hectiq API.")
@click.option("--name", "-n", type=click.STRING, help="Name of the model.")
@click.option("--version", "-v", type=click.STRING, help="Version of the model.")
@click.option("--organization", "-o", type=click.STRING, help="Organization to download the model from.")
@click.option("--savepath", "-s", type=click.Path(), help="Path to save the model.", default=".")
def download_model(name:str, version: str, savepath: str, organization: str):

    from hectiq_console.functional import download_model, set_organization

    set_organization(organization)
    download_model(name=name, version=version, savepath=savepath)


def main():
    cli = click.CommandCollection(sources=[auth_group, base])
    # Standalone mode is False so that the errors can be caught by the runs
    cli(standalone_mode=False)
    sys.exit()


if __name__ == "__main__":
    main()
