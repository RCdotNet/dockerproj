"""
Just a module
"""
#!/usr/bin/env python

import click

@click.command()
def hello():
    """
    Just a function
    """
    click.echo('Hello RCdotNet!')

if __name__ == '__main__':
    hello()
    