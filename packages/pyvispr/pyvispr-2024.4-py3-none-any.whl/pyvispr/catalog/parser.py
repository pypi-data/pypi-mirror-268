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
import inspect as spct
from pathlib import Path as path_t

from pyvispr.constant.catalog import (
    ACTUAL_SOURCE,
    FUNCTION_NAME,
    INPUT_II_NAMES,
    NODE_NAME,
    OUTPUT_NAMES,
)
from pyvispr.extension.function import function_t
from pyvispr.extension.string_ import SplitAndStriped


def N_A_F_A(
    description: str, default_name: str, /
) -> tuple[str, str | None, str, str | None, str | None]:
    """"""
    description = dict(SplitAndStriped(_lne, ":") for _lne in description.splitlines())

    return (
        description.get(NODE_NAME, default_name),
        description.get(ACTUAL_SOURCE),
        description.get(FUNCTION_NAME, default_name),
        description.get(INPUT_II_NAMES),
        description.get(OUTPUT_NAMES),
    )


def AllFunctions(
    module_name: str, /, *, recursively: bool = False
) -> tuple[function_t | None, ...]:
    """"""
    functions = []
    modules = {module_name}
    parent_path = IsInnerModule_ = None
    while modules.__len__() > 0:
        module_or_name = modules.pop()
        if isinstance(module_or_name, str):
            module = mprt.import_module(module_or_name)
            parent_path = path_t(module.__path__[0])
            IsInnerModule_ = lambda _elm: IsInnerModule(_elm, parent_path)
        else:
            module = module_or_name

        functions.extend(
            (f"{module.__name__}.{elm[0]}", elm[1], module)
            for elm in spct.getmembers(module, IsFunction)
            if elm[0][0] != "_"
        )
        if recursively:
            modules.update(
                elm[1]
                for elm in spct.getmembers(module, IsInnerModule_)
                if elm[0][0] != "_"
            )

    filtered = {}
    for full_name, function, module in functions:
        if function in filtered:
            if filtered[function][0].__len__() > full_name.__len__():
                filtered[function] = (full_name, module)
        else:
            filtered[function] = (full_name, module)

    output = []
    for function, (full_name, module) in filtered.items():
        _, name = full_name.rsplit(".", maxsplit=1)
        output.append(function_t.NewFromInstance(function, name, module))

    return tuple(output)


def IsFunction(element: object, /) -> bool:
    """"""
    return spct.isfunction(element) or hasattr(element, "__call__")


def IsInnerModule(element: object, parent_path: path_t, /) -> bool:
    """"""
    return (
        spct.ismodule(element)
        and hasattr(element, "__path__")
        and path_t(element.__path__[0]).is_relative_to(parent_path)
    )
