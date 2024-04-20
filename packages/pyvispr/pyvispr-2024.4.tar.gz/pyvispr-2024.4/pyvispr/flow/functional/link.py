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

from pyvispr.flow.functional.node_isolated import node_t


@dtcl.dataclass(slots=True, repr=False, eq=False)
class outbound_links_t(dict[str, list[tuple[node_t, str]]]):
    """
    Per node outbound links.
    """

    def Add(
        self,
        source: node_t,
        output_name: str,
        target: node_t,
        input_name: str,
        /,
    ) -> None:
        """"""
        if (links := self.get(output_name)) is None:
            self[output_name] = [(target, input_name)]
        elif (target, input_name) in links:
            raise ValueError(
                f"Link {output_name} ⮞ {target.unique_name}.{input_name} already present."
            )
        else:
            links.append((target, input_name))

        source_output_name = source.UniqueOutputName(output_name)
        value = source.outputs[output_name].value
        target.inputs[input_name].Connect(source_output_name, value)

    def Remove(
        self, output_name: str | None, target: node_t | None, input_name: str | None, /
    ) -> None:
        """"""
        for current_out, links in self.items():
            for current_target, current_in in links:
                if _LinksMatch(
                    output_name,
                    target,
                    input_name,
                    current_out,
                    current_target,
                    current_in,
                ):
                    current_target.inputs[current_in].Disconnect()

        if output_name is None:
            self.clear()
            return

        if target is None:
            # Could be del self[output_name] directly. Implemented indirectly for "coherence" with the other cases.
            self[output_name] = []
        elif input_name is None:
            self[output_name] = [
                _elm for _elm in self[output_name] if _elm[0] is not target
            ]
        else:
            self[output_name].remove((target, input_name))
        if self[output_name].__len__() == 0:
            del self[output_name]

    def __contains__(self, item: str | node_t | tuple[node_t, str], /) -> bool:
        """"""
        if isinstance(item, str):
            return dict.__contains__(self, item)

        if isinstance(item, node_t):
            return any(any(item is _lnk[0] for _lnk in _elm) for _elm in self.values())

        return any(item in _elm for _elm in self.values())


def _LinksMatch(
    output_name: str | None,
    target: node_t | None,
    input_name: str | None,
    current_out: str,
    current_target: node_t,
    current_in: str,
    /,
) -> bool:
    """"""
    if output_name is None:
        return True
    if current_out != output_name:
        return False

    if target is None:
        return True
    if current_target is not target:
        return False

    if input_name is None:
        return True
    return current_in == input_name
