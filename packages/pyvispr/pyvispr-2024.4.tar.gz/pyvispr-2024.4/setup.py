# Copyright CNRS/Inria/UniCA
# Contributor(s): Eric Debreuve (since 2017)
#
# eric.debreuve@cnrs.fr
#
# This software is governed by the CeCILL  license under French law and
# abiding by the rules of distribution of free software.  You can  use,
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info".
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# In this respect, the user's attention is drawn to the risks associated
# with loading,  using,  modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean  that it is complicated to manipulate,  and  that  also
# therefore means  that it is reserved for developers  and  experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or
# data to be ensured and,  more generally, to use and operate it in the
# same conditions as regards security.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.

import re as rgex
import site
from datetime import datetime as date_time_t
from importlib import util
from pathlib import Path as path_t
from typing import Dict

import platformdirs as fldr
from setuptools import setup
from setuptools.command.install import install as install_base_t

HERE = path_t(__file__).parent.resolve()
LOCAL_DOCUMENTATION = HERE / "documentation" / "wiki"
ASCIIDOC_DESCRIPTION = "description.asciidoc"


def DescriptionFromAsciidoc(documentation: path_t, /) -> Dict[str, str]:
    """"""
    output = {}

    pattern = rgex.compile(r":([A-Z_]+): +(.+)\n?", flags=rgex.ASCII)

    with open(documentation) as accessor:
        for line in accessor.readlines():
            if (match := pattern.fullmatch(line)) is not None:
                name = match.group(1)
                value = match.group(2)
                output[name] = value

    return output


DESCRIPTION = DescriptionFromAsciidoc(LOCAL_DOCUMENTATION / ASCIIDOC_DESCRIPTION)
PACKAGES = [
    DESCRIPTION["IMPORT_NAME"],
    f"{DESCRIPTION['IMPORT_NAME']}.catalog",
    f"{DESCRIPTION['IMPORT_NAME']}.catalog.factory",
    f"{DESCRIPTION['IMPORT_NAME']}.config",
    f"{DESCRIPTION['IMPORT_NAME']}.config.appearance",
    f"{DESCRIPTION['IMPORT_NAME']}.constant",
    f"{DESCRIPTION['IMPORT_NAME']}.constant.widget",
    f"{DESCRIPTION['IMPORT_NAME']}.extension",
    f"{DESCRIPTION['IMPORT_NAME']}.flow",
    f"{DESCRIPTION['IMPORT_NAME']}.flow.descriptive",
    f"{DESCRIPTION['IMPORT_NAME']}.flow.functional",
    f"{DESCRIPTION['IMPORT_NAME']}.flow.visual",
    f"{DESCRIPTION['IMPORT_NAME']}.interface",
    f"{DESCRIPTION['IMPORT_NAME']}.interface.storage",
    f"{DESCRIPTION['IMPORT_NAME']}.interface.window",
    f"{DESCRIPTION['IMPORT_NAME']}.interface.window.widget",
    f"{DESCRIPTION['IMPORT_NAME']}.runtime",
]
EXCLUDED_PACKAGES = (
    f"{DESCRIPTION['IMPORT_NAME']}.documentation",
)
ENTRY_POINTS = {
    "gui_scripts": [
        "pyvispr=pyvispr.run:Main",
        "pyvispr-node-installer=pyvispr.install:Main",
    ],
}


long_description = (HERE / "README.rst").read_text(encoding="utf-8")

repository_url = (
    f"https://"
    f"{DESCRIPTION['REPOSITORY_SITE']}/"
    f"{DESCRIPTION['REPOSITORY_USER']}/"
    f"{DESCRIPTION['REPOSITORY_NAME']}/"
)
documentation_url = f"{repository_url}/{DESCRIPTION['DOCUMENTATION_SITE']}"


class install_t(install_base_t):
    @staticmethod
    def InstallationFolder() -> path_t | None:
        """"""
        for folder in site.getsitepackages() + [site.USER_SITE]:
            folder = path_t(folder)
            if folder.is_dir() and (folder / DESCRIPTION["IMPORT_NAME"]).is_dir():
                return folder / DESCRIPTION["IMPORT_NAME"]
        return None

    def run(self) -> None:
        """"""
        install_base_t.run(self)

        if DESCRIPTION["CONFIG_FOLDER"] != "None":
            config_folder = fldr.user_config_path(
                appname=DESCRIPTION["CONFIG_FOLDER"], ensure_exists=True
            )
        else:
            config_folder = None
        installation_folder = install_t.InstallationFolder()
        if installation_folder is None:
            raise RuntimeError("Setup process cannot determine the package "
                               "installation folder.")

        if config_folder is None:
            raise RuntimeError("Setup process cannot create the package "
                               "config folder.")
        catalog_folder = config_folder / "catalog"
        for node in (installation_folder / "catalog" / "factory").glob("*.py"):
            now = date_time_t.now().isoformat(sep="-", timespec="microseconds")
            now = "".join(filter(str.isdigit, now))
            found_s = catalog_folder.glob(f"{node.stem}_[0-9][0-9]*.py")
            for found in found_s:
                if found.is_symlink():
                    # Previous factory version: remove before below update.
                    found.unlink()
                else:
                    # Normally, not a previous factory version; Do not overwrite.
                    continue
            (catalog_folder / f"{node.stem}_{now}.py").symlink_to(node)


def CheckCoherenceBetweenDeclarationAndReality() -> None:
    """"""
    folders = [DESCRIPTION["IMPORT_NAME"]]
    for node in (HERE / DESCRIPTION["IMPORT_NAME"]).rglob("*"):
        if node.is_dir() and not str(node).startswith("."):
            node = node.relative_to(HERE)
            node = ".".join(node.parts)
            if not (
                (node in EXCLUDED_PACKAGES)
                or any(node.startswith(_fld + ".") for _fld in EXCLUDED_PACKAGES)
            ):
                folders.append(node)
    folders = sorted(folders)

    packages = sorted(PACKAGES)
    if packages != folders:
        raise ValueError(
            f"Mismatch between declared and found packages:\n"
            f"    - Declared=\n      {packages}\n"
            f"    - Found=\n      {folders}\n"
            f"    - Undeclared=\n      {set(folders).difference(packages)}\n"
            f"    - Nonexistent=\n      {set(packages).difference(folders)}"
        )


def Version() -> str:
    """"""
    where = HERE / DESCRIPTION["IMPORT_NAME"] / "version.py"
    spec = util.spec_from_file_location(where.stem, where)
    module = spec.loader.load_module(spec.name)

    output = module.__version__
    if isinstance(output, str) and rgex.fullmatch(r"20[0-9]{2}\.[1-9][0-9]*", output):
        return output

    raise ValueError(f"{output}: Invalid version")


def Requirements() -> tuple[str, ...]:
    """"""
    with open(HERE / "requirements.txt") as accessor:
        output = accessor.readlines()

    return tuple(output)


if __name__ == "__main__":
    #
    CheckCoherenceBetweenDeclarationAndReality()
    # fmt: off
    setup(
        cmdclass={"install": install_t},
        #
        author=DESCRIPTION["AUTHOR"],
        author_email=DESCRIPTION["EMAIL"],
        #
        name=DESCRIPTION["PYPI_NAME"],
        description=DESCRIPTION["SHORT_DESCRIPTION"],
        long_description=long_description,
        long_description_content_type="text/x-rst",
        license=DESCRIPTION["LICENSE_SHORT"],
        version=Version(),
        #
        classifiers=[
            f"Topic :: {DESCRIPTION['PYPI_TOPIC']}",
            f"Intended Audience :: {DESCRIPTION['PYPI_AUDIENCE']}",
            f"License :: OSI Approved :: {DESCRIPTION['LICENCE_LONG']} ({DESCRIPTION['LICENSE_SHORT']})",
            f"Programming Language :: Python :: {DESCRIPTION['PY_VERSION']}",
            f"Development Status :: {DESCRIPTION['PYPI_STATUS']}",
        ],
        keywords=DESCRIPTION["KEYWORDS"],
        #
        url=repository_url,
        project_urls={
            "Documentation": documentation_url,
            "Source": repository_url,
        },
        #
        packages=PACKAGES,
        entry_points=ENTRY_POINTS,
        python_requires=f">={DESCRIPTION['PY_VERSION']}",
        install_requires=Requirements(),
    )
