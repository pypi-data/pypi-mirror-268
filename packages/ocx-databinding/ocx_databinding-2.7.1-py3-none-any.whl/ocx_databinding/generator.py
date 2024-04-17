#  Copyright (c) 2023. OCX Consortium https://3docx.org. See the LICENSE
"""Generate code from xml schemas, webservice definitions and any xml or json document."""
# System imports
from pathlib import Path
import subprocess
from typing import Union

# Third party packages
from loguru import logger
import packaging.version
import xsdata.exceptions
from packaging.version import parse


# Project imports


def remove_module_imports(init_py: Path):
    """Remove module imports."""

    content = init_py.read_text()
    start = content.find("__all__")  # __all__  comes after the import statements
    all_types = content[start:]
    init_py.write_text(all_types)


def package_version(
    name: str,
    major: int,
    minor: int,
    micro: int,
    pr1: str,
    pr2: str,
    is_pre_release: bool = False,
) -> str:
    """Generate the databinding package name.

    Args:
        name: The package name
        major: Major version
        minor: Minor version
        micro: Micro version
        pr1: Pre-release tag 1
        pr2: Pre-release tag 2
        is_pre_release: True if a pre-release, False otherwise

    Returns:
         The formatted package string

    """
    if is_pre_release:
        return f"{name}_{major}{minor}{micro}{pr1}{pr2}"
    else:
        return f"{name}_{major}{minor}{micro}"


def xsdata_generate(
    source: str,
    package: str,
    slots: bool,
    recursive: bool,
    structure_style: str,
    docstring_style: str,
) -> str:
    """
       Generate an xsdata command for generating Python classes from XML schema.

    Args:
        source (str): The path to the XML schema file or directory.
        package (str): The Python package name for the generated classes.
        slots (bool): Whether to generate classes with __slots__.
        recursive (bool): Whether to generate classes recursively for imported schemas.
        structure_style (str): The style of generated class structure.
        docstring_style (str): The style of generated class docstrings.

    Returns:
        str: The xsdata command for generating Python classes.

    Examples:
        >>> xsdata_generate("schema.xsd", "my_package", True, False, "dataclass", "google")
        'xsdata generate schema.xsd --package my_package --structure-style dataclass --docstring-style google --slots'
    """
    command = (
        f"xsdata generate {source} "
        f"--package {package} --structure-style {structure_style} "
        f"--docstring-style {docstring_style}"
    )
    if slots:
        command = f"{command} --slots"
    if recursive:
        command = f"{command} --recursive"
    return command


def call_xsdata(
    source: Union[str, Path],
    package_name: str,
    version: str,
    structure_style: str = "single-package",
    docstring_style: str = "Google",
    stdout: bool = False,
    recursive: bool = True,
    slots: bool = False,
) -> bool:
    """
    Call xsdata subprocess to generate Python data bindings.

    Args:
        source: The source URL or local file path of the XML schema.
        package_name: The name of the package to generate.
        version: The version of the package.
        structure_style: The style of the generated package structure (default: "single-package").
        docstring_style: The style of the generated docstrings (default: "Google").
        stdout: Whether to print the output to stdout (default: False).
        recursive: Whether to generate bindings for all imported schemas (default: True).
        slots: Whether to generate classes with __slots__ (default: True).

    Returns:
        bool: True if the xsdata generation is successful, False otherwise.
    """

    if "http" not in source:
        source = Path(source).resolve()
    package_folder = Path.cwd() / Path(package_name)
    package_folder.mkdir(parents=True, exist_ok=True)
    try:
        pr1, pr2 = "", ""
        v = parse(version)
        if v.is_prerelease:
            pr1, pr2 = v.pre
        databinding = package_version(
            name=package_name,
            major=v.major,
            minor=v.minor,
            micro=v.micro,
            is_pre_release=v.is_prerelease,
            pr1=pr1,
            pr2=pr2,
        )
        destination_folder = package_folder / Path(databinding)
        destination_folder.mkdir(parents=True, exist_ok=True)
        try:
            command_parameters = xsdata_generate(
                source=source,
                package=databinding,
                slots=slots,
                recursive=recursive,
                docstring_style=docstring_style,
                structure_style=structure_style,
            )
            logger.debug(
                f"Calling xsdata subprocess with parameters: {command_parameters}"
            )
            logger.debug(f"./Process executes in: {destination_folder.resolve()}")
            return_code = subprocess.call(
                command_parameters,
                shell=True,
                cwd=destination_folder.resolve(),
            )
            if return_code != 0:
                logger.error(f"xsdata generate failed with return code {return_code}")
                return False
            # Modify init.py to avoid circular reports
            init_py = destination_folder / "__init__.py"
            remove_module_imports(init_py)
            return True
        except xsdata.exceptions.CodeGenerationError as e:
            logger.error(f"xsdata generate failed:  {e}")
            return False
    except packaging.version.InvalidVersion as e:
        logger.error(e)
        return False
