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

import importlib as mprt
from importlib import util
from pathlib import Path as path_t
from types import FunctionType, ModuleType

from logger_36 import LOGGER


def ModuleForPath(path: path_t, /) -> ModuleType | None:
    """"""
    try:
        path = path_t(path).expanduser()
    except RuntimeError:
        return None
    if not path.is_file():
        return None

    spec = util.spec_from_file_location(path.stem, path)

    try:
        output = spec.loader.load_module(spec.name)
    except ImportError:
        return None

    return output


def M_F_FromPathAndName(
    path: str | path_t, function_name: str, /
) -> tuple[ModuleType | None, FunctionType | None]:
    """"""
    if isinstance(path, str):
        path = path_t(path)

    module = ModuleForPath(path)
    if module is None:
        return None, None

    return module, getattr(module, function_name, None)


def M_F_FromPyPathAndName(
    pypath: str, function_name: str, /
) -> tuple[ModuleType | None, FunctionType | None]:
    """"""
    try:
        module = mprt.import_module(pypath)
    except (
        Exception
    ) as exception:  # The documentation does not mention potential exceptions.
        LOGGER.error(f"Error while importing {pypath}.{function_name}:\n{exception}")
        return None, None

    return module, getattr(module, function_name, None)
