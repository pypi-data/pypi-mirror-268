
"""XMLTest XML validation helper"""

__version__ = "0.1a4"

from argparse import ArgumentParser, FileType
from sys import stdin
from os import get_terminal_size

from xml.etree.ElementTree import ParseError

from rich import box
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table

from .catalog import SchemaCatalog
from xmltest import test_instance_docs



def _error_to_str(error: Exception, verbose = False):
    if verbose:
        return str(error)
    if hasattr(error, "message"):
        s = error.message
    elif hasattr(error, "msg"):
        s = error.msg
    else:
        s = f"{error!r}"
    return s

def test_console():
    parser = ArgumentParser(description="Test an XML document for compliance with ETSI TS 103 120")
    parser.add_argument("-i", "--input", type=FileType('r'), default=stdin, help="Instance XML document to validate against the schema. If a directory is specified, xmltest will search and add any XML files recursively within the directory")
    parser.add_argument("-q", "--quiet", action="store_true", help="Suppress output")
    parser.add_argument("-v", action="count", help="Verbose. Can be specified multiple times to get more detailed output")
    pargs = parser.parse_args()

    verbosity = pargs.v if pargs.v else 0
    catalog = SchemaCatalog()
    schema = catalog.get_latest_schema()

    text = pargs.input.read()
    pargs.input.close()

    try:
        errors = list(schema.iter_errors(text))
    except ParseError as ex:
        errors = [ex]

    width = get_terminal_size().columns
    console = Console()
    table = Table(show_header=False, expand=True, box=box.ROUNDED)

    if pargs.quiet:
        if len(errors) > 0:
            exit(-1)
        else:
            exit(0)

    if len(errors) == 0:
        table.add_row(f"Issues{'[green]None[/]'.rjust(width, ' ')}")
    else:
        table.add_row(f"Issues{('[red]' + str(len(errors)) + '[/]').rjust(width-len(str(len(errors)))-1, ' ')}")
        for error in errors:
            table.add_section()
            table.add_row(f"[yellow]{_error_to_str(error, verbosity > 0)}[/]")
    console.print(table)    