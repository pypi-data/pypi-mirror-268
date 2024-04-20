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

import dataclasses as dtcl
import traceback as tbck
import typing as h
from enum import Enum as enum_t

from json_any import JsonStringOf
from logger_36 import LOGGER
from pyvispr.constant.socket import OUTPUT_SET, OUTPUT_UNSET
from pyvispr.flow.descriptive.node import node_t as description_t
from pyvispr.flow.functional.socket import input_t, output_t
from sio_messenger.instance import MESSENGER


class state_e(enum_t):
    disabled = 0
    todo = 1
    doing = 2
    done = 3


@dtcl.dataclass(slots=True, repr=False, eq=False)
class node_t:
    """
    The description is shared among all the functional nodes.

    links[idx]: Outbound links of node of index idx in list "nodes":
        - None if node has no outbound links.
        - If not None, dictionary with:
            - key=name of output and...
            - value=list of alternating target nodes and name of target inputs.
    """

    UNIQUE_NAME_SEPARATOR: h.ClassVar[str] = "_"
    UNIQUE_OUTPUT_NAME_SEPARATOR: h.ClassVar[str] = "__"

    description: description_t
    inputs: dict[str, input_t]
    outputs: dict[str, output_t]
    unique_name: str | None = None
    state: state_e = state_e.todo

    @classmethod
    def NewForDescription(cls, description: description_t, /) -> node_t:
        """"""
        description.Activate()

        inputs = {_nme: input_t() for _nme in description.input_names}
        outputs = {_nme: output_t() for _nme in description.output_names}

        return cls(
            description=description,
            inputs=inputs,
            outputs=outputs,
        )

    def SetUniqueName(self, uid: int, /) -> None:
        """"""
        self.unique_name = f"{self.description.name}{node_t.UNIQUE_NAME_SEPARATOR}{uid}"

    def UniqueOutputName(self, output_name: str, /) -> str:
        """"""
        return f"{self.unique_name}{node_t.UNIQUE_OUTPUT_NAME_SEPARATOR}{output_name}"

    def OffsetUnicity(self, offset: int, /) -> None:
        """"""
        _, uid = self.unique_name.split(node_t.UNIQUE_NAME_SEPARATOR)
        self.SetUniqueName(int(uid) + offset)

        for input_ in self.inputs.values():
            if (source_output_name := input_.source_output_name) is None:
                continue

            source, output_name = source_output_name.split(
                node_t.UNIQUE_OUTPUT_NAME_SEPARATOR
            )
            name, uid = source.split(node_t.UNIQUE_NAME_SEPARATOR)
            uid = int(uid) + offset
            input_.source_output_name = (
                f"{name}{node_t.UNIQUE_NAME_SEPARATOR}"
                f"{uid}{node_t.UNIQUE_OUTPUT_NAME_SEPARATOR}"
                f"{output_name}"
            )

    def InvalidateInputValue(self, /, *, name: str | None = None) -> None:
        """"""
        if self.state in (state_e.todo, state_e.disabled):
            return

        if name is None:
            for input_ in self.inputs.values():
                input_.Invalidate()
        else:
            self.inputs[name].Invalidate()

        self.InvalidateOutputValues()

    def InvalidateOutputValues(self) -> None:
        """"""
        if self.state in (state_e.todo, state_e.disabled):
            return

        for output in self.outputs.values():
            output.Invalidate()

        self.state = state_e.todo
        MESSENGER.Transmit(self.state, self)
        MESSENGER.Transmit(OUTPUT_UNSET, self)

    @property
    def can_run(self) -> bool:
        """
        It must have been checked that the state is not disabled.

        This method is meant to be called from functional.graph.Run,
        i.e., after visual.Run has read the ii_values
        to set the corresponding node input values if appropriate.
        Appropriate means: the corresponding inputs have mode "full" (actually,
        not "link") and they are not linked to outputs.
        """
        return (self.description.n_inputs == 0) or all(
            self.inputs[_elm].has_value or self.description.inputs[_elm].has_default
            for _elm in self.inputs
        )

    def Run(self, /, *, script_accessor: h.TextIO = None) -> None:
        """
        It must have been checked that the state is not disabled.
        """
        self.state = state_e.doing
        MESSENGER.Transmit(self.state, self)

        should_save_as_script = script_accessor is not None

        if should_save_as_script:
            if self.description.n_outputs > 1:
                output_assignments = (
                    self.UniqueOutputName(_elm) for _elm in self.outputs
                )
                output_assignments = ", ".join(output_assignments) + " = "
            else:
                output_assignments = ""
        else:
            output_assignments = None

        if self.description.n_inputs > 0:
            anonymous_args = []
            named_args = {}
            anonymous_args_script = []
            named_args_script = []
            value_script = None

            for name, description in self.description.inputs.items():
                input_ = self.inputs[name]
                if input_.has_value:
                    value = input_.value
                    if should_save_as_script:
                        if input_.is_linked:
                            value_script = input_.source_output_name
                        else:
                            value_script = _EncodedValue(value)
                else:
                    value = description.default_value
                    if should_save_as_script:
                        value_script = _EncodedValue(value)
                    assert description.has_default

                if description.has_default:
                    named_args[name] = value
                    if should_save_as_script:
                        named_args_script.append(f"{name}={value_script}")
                else:
                    anonymous_args.append(value)
                    if should_save_as_script:
                        anonymous_args_script.append(value_script)

            if should_save_as_script:
                arguments = ", ".join(anonymous_args_script + named_args_script)
                script_accessor.write(
                    f"{output_assignments}{self.description.module.__name__}_"
                    f"{self.description.actual.name}({arguments})\n"
                )
                output_values = _FakeOutputs(self.description.n_outputs, "Done")
            else:
                output_values = self._SafeOutputValues(anonymous_args, named_args)
        elif should_save_as_script:
            script_accessor.write(
                f"{output_assignments}{self.description.module.__name__}_{self.description.actual.name}()\n"
            )
            output_values = _FakeOutputs(self.description.n_outputs, "Done")
        else:
            output_values = self._SafeOutputValues(None, None)

        # Since output values are computed here, it makes more sense to directly set them, as opposed to returning them
        # and letting the caller doing it. Hence, _SetOutputValue is meant for internal use, whereas SetInputValue is
        # meant for external use.
        output_names = self.description.output_names
        n_outputs = output_names.__len__()
        if n_outputs > 1:
            for name, value in zip(output_names, output_values):
                self._SetOutputValue(name, value)
        elif n_outputs > 0:
            self._SetOutputValue(output_names[0], output_values)

        self.state = state_e.done
        MESSENGER.Transmit(self.state, self)

    def _SafeOutputValues(
        self,
        anonymous_args: h.Sequence[h.Any] | None,
        named_args: dict[str, h.Any] | None,
        /,
    ) -> h.Any | None:
        """"""
        try:
            if anonymous_args is None:
                output = self.description.Function()
            else:
                output = self.description.Function(*anonymous_args, **named_args)
        except Exception as exception:
            output = _FakeOutputs(self.description.n_outputs, None)
            lines = tbck.format_exception(exception)
            as_str = "\n".join(lines[:1] + lines[2:])
            LOGGER.error(f"Error while running {self.unique_name}:\n{as_str}")

        return output

    def SetInputValue(self, name: str, value: h.Any, /) -> None:
        """"""
        self.inputs[name].value = value

    def _SetOutputValue(self, name: str, value: h.Any, /) -> None:
        """"""
        self.outputs[name].value = value
        MESSENGER.Transmit(OUTPUT_SET, self)


def _EncodedValue(value: h.Any, /) -> str:
    """"""
    as_str, issues = JsonStringOf(value)
    if issues is None:
        as_str = as_str.replace('"', '\\"')
        return f'ObjectFromJsonString("{as_str}")'

    return "__VALUE_NOT_ENCODABLE_BY_JSON_any__"


def _FakeOutputs(n_outputs: int, fake_value: h.Any, /) -> h.Any | tuple[h.Any, ...]:
    """"""
    if n_outputs > 1:
        return n_outputs * (fake_value,)
    return fake_value
