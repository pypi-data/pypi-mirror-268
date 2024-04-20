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

from __future__ import annotations

import ast as prsr
import dataclasses as dtcl
import inspect as spct
from enum import Enum as enum_t
from pathlib import Path as path_t
from types import EllipsisType
from types import ModuleType as module_t
from typing import Any, Callable
from typing import NamedTuple as named_tuple_t

from conf_ini_g.phase.specification.parameter.type import type_t
from logger_36 import LOGGER
from pyvispr.catalog.parser import N_A_F_A
from pyvispr.constant.function import NO_ANNOTATION, NO_OUTPUT_NAMES
from pyvispr.extension.function import FirstFunctionAsAstNode
from pyvispr.extension.module import M_F_FromPathAndName, M_F_FromPyPathAndName
from pyvispr.flow.descriptive.socket import InputsFromAST, input_t
from pyvispr.runtime.socket import assign_when_importing_t


class source_e(enum_t):
    not_set = 0
    local = 1
    referenced = 2
    system = 3


class _function_t(named_tuple_t):
    """
    path: Either a path or py_path to module.
    """

    path: path_t | str
    name: str


@dtcl.dataclass(slots=True, repr=False, eq=False)
class node_t:
    name: str
    keywords: str
    short_description: str
    long_description: str
    source: source_e
    inputs: dict[str, input_t]
    outputs: dict[str, type_t | assign_when_importing_t | None]
    requires_completion: bool
    #
    proxy: _function_t
    actual: _function_t
    #
    # Of actual function, not proxy.
    module: module_t | None = dtcl.field(init=False, default=None)
    Function: Callable[..., Any] | None = dtcl.field(init=False, default=None)
    documentation: str | None = dtcl.field(init=False, default=None)

    @classmethod
    def NewForPath(cls, path: str | path_t, /) -> node_t | None:
        """"""
        if isinstance(path, str):
            path = path_t(path)
        path = path.expanduser()

        with open(path) as accessor:
            proxy_function = FirstFunctionAsAstNode(accessor.read())
        if proxy_function is None:
            LOGGER.error(f"No proper function found for node {path}")
            return None

        description = prsr.get_docstring(proxy_function)
        (
            name_,
            actual_path_,
            function_name_,
            input_ii_names,
            output_names,
        ) = N_A_F_A(description, proxy_function.name)

        if actual_path_ is None:
            source_ = source_e.local
            actual_path_ = path
        elif actual_path_.endswith(".py"):
            source_ = source_e.referenced
            actual_path_ = path_t(actual_path_)
        else:
            source_ = source_e.system

        inputs_, requires_completion_ = InputsFromAST(proxy_function, input_ii_names)

        if (output_names is None) or (output_names.__len__() == 0):
            outputs_ = {}
        elif output_names == NO_OUTPUT_NAMES:
            outputs_ = {NO_OUTPUT_NAMES: None}
            requires_completion_ = True
        else:
            outputs_ = {_elm.strip(): None for _elm in output_names.split(",")}

        proxy_ = _function_t(path=path, name=proxy_function.name)
        if actual_path_ == path:
            actual_ = proxy_
        else:
            actual_ = _function_t(path=actual_path_, name=function_name_)

        return cls(
            name=name_,
            keywords="",
            short_description="",
            long_description="",
            source=source_,
            inputs=inputs_,
            outputs=outputs_,
            requires_completion=requires_completion_,
            proxy=proxy_,
            actual=actual_,
        )

    @property
    def n_inputs(self) -> int:
        """"""
        return self.inputs.__len__()

    @property
    def input_names(self) -> tuple[str, ...]:
        """"""
        return tuple(self.inputs.keys())

    @property
    def input_types(self) -> tuple[type_t | assign_when_importing_t, ...]:
        """"""
        return tuple(_elm.type for _elm in self.inputs.values())

    @property
    def n_outputs(self) -> int:
        """"""
        return self.outputs.__len__()

    @property
    def output_names(self) -> tuple[str, ...]:
        """"""
        return tuple(self.outputs.keys())

    @property
    def output_types(self) -> tuple[type_t | assign_when_importing_t | None, ...]:
        """"""
        return tuple(self.outputs.values())

    def Activate(self) -> None:
        """"""
        if self.module is not None:
            return

        if self.source is source_e.system:
            ModuleAndFunction = M_F_FromPyPathAndName
        else:  # source_e.local or source_e.referenced
            ModuleAndFunction = M_F_FromPathAndName
        self.module, self.Function = ModuleAndFunction(
            self.actual.path, self.actual.name
        )
        self.documentation = spct.getdoc(self.Function)

        if self.proxy is self.actual:
            Function = self.Function
        else:
            # Always use the signature of the proxy function since it might have been corrected.
            _, Function = M_F_FromPathAndName(self.proxy.path, self.proxy.name)
        signature = spct.signature(Function)

        spct_inputs = signature.parameters
        for name, input_ in self.inputs.items():
            if input_.UpdateFromSignature(spct_inputs[name]):
                self.requires_completion = True

        if self.outputs.__len__() > 0:
            if self._UpdateOutputsFromSignature(signature.return_annotation):
                self.requires_completion = True

    def _UpdateOutputsFromSignature(self, outputs: Any, /) -> bool:
        """
        Note: requires_completion could be set here; However, for coherence with UpdateFromSignature, it is returned
        instead.
        """
        if outputs != NO_ANNOTATION:
            requires_completion = False
        else:
            outputs = Any
            requires_completion = True
        hint = type_t.NewFromTypeHint(outputs)
        if (hint.type is tuple) and (
            (hint.elements.__len__() != 2) or (hint.elements[1] is not EllipsisType)
        ):
            hints = hint.elements
        else:
            hints = (hint,)

        assert hints.__len__() == self.outputs.__len__(), (
            self.name,
            hints,
            self.outputs,
        )
        for name, hint in zip(self.outputs, hints):
            self.outputs[name] = hint

        return requires_completion
