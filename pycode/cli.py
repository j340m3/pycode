# -*- coding: utf-8 -*-

import click

@click.command()
def main(args=None): #pragma no cover
    """Console script for pycode"""
    click.echo("Replace this message by putting your code into "
               "pycode.cli.main")
    click.echo("See click documentation at /")
    from . import main


if __name__ == "__main__": #pragma no cover
    main()
