#!/usr/bin/env python
import os
import pathlib

import click

from tekra import project


@click.group()
@click.pass_context
def cli(ctx: click.Context):
    ctx.ensure_object(dict)
    try:
        ctx.obj['project'] = project.open_project(pathlib.Path.cwd())
    except Exception:
        ctx.obj['project'] = None


@cli.command()
@click.pass_context
@click.argument('name', type=str)
@click.argument('path', type=click.Path(exists=True), default=pathlib.Path.cwd())
@click.option('--description', type=str, default=None)
@click.option('--author', type=str, default=None)
def create_project(ctx: click.Context, name, path, description, author):
    project.create_project(
        path=pathlib.Path(path),
        name=name,
        description=description or name,
        author=author or os.getlogin(),
        version='0.1.0'
    )


if __name__ == '__main__':
    cli(obj={})
