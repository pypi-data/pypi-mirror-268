#  Copyright (c) 2023. OCX Consortium https://3docx.org. See the LICENSE
"""generator CLI commands."""
# System imports
from __future__ import annotations
import sys

# Third party
import typer
from typing_extensions import Annotated
from loguru import logger

# Project
from ocx_databinding import __version__
from ocx_databinding import generator

databinding = typer.Typer()

CONFIG_FILE = "xsdata.xml"

logger.enable("ocx_databinding")

# Logging config for application
config = {
    "handlers": [
        {"sink": sys.stdout, "format": "{time} - {message}"},
        {"sink": str.join(__name__, ".log"), "serialize": True},
    ],
}


@databinding.command()
def generate(
    source: Annotated[
        str,
        typer.Argument(
            help=" The input source can be either a filepath, "
            "uri or a directory containing xml, json, xsd and wsdl files."
        ),
    ],
    package: Annotated[
        str, typer.Argument(help="The name of the databinding destination folder")
    ],
    schema_version: Annotated[
        str, typer.Argument(help="The source schema version number.")
    ],
    docstring_style: Annotated[
        str, typer.Argument(help="The style for generating class documentation")
    ] = "Google",
    structure_style: Annotated[
        str, typer.Argument(help=" Output structure style.")
    ] = "single-package",
    slots: Annotated[
        bool, typer.Option(help="Enable __slots__, python>=3.10 Only")
    ] = True,
    recursive: Annotated[
        bool,
        typer.Option(
            help="Search files recursively in the source directory if the source is a file."
        ),
    ] = False,
):
    """Generate code from xml schemas, webservice definitions and any xml or json document.
    The input source can be either a filepath, uri or a directory containing  xml, json, xsd and wsdl files.

    """
    return generator.call_xsdata(
        source=source,
        package_name=package,
        version=schema_version,
        slots=slots,
        recursive=recursive,
        structure_style=structure_style,
        docstring_style=docstring_style,
    )


@databinding.command()
def version():
    """Print the version number and exit."""
    print(__version__)


def main():
    """CLI entry point."""
    databinding()
