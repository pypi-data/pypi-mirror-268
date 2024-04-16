import toml
import click
from pathlib import Path

from svtter_template_creator import __version__, lib


@click.group()
def cli():
    pass


@click.command()
@click.option(
    "--name",
    prompt="template name",
    help="The template need to create",
    type=click.Choice(lib.get_choice()),
)
def create(name):
    """
    create template via name
    """
    lib.create(name)


@click.command()
def version():
    """show version information"""
    click.echo(f"ttc version is: {__version__}")


@click.command(help="write version to __init__.py and pyproject.toml")
@click.option("--version", help="The new verison!", required=True)
def write(version):
    filepath = "src/ttc/__init__.py"
    with open(filepath, "w") as f:
        f.write(f'__version__ = "{version}"')

    p = Path("./pyproject.toml")
    res = toml.load(p)
    res["tool"]["poetry"]["version"] = version
    # write back
    with open(p, "w") as f:
        toml.dump(res, f)


clist = [create, version, write]
for c in clist:
    cli.add_command(c)
