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

import dataclasses as dtcl
import typing as h

from pyvispr.flow.functional.node_linked import node_t


@dtcl.dataclass(repr=False, eq=False)
class graph_t(list[node_t]):
    """
    Cannot be sloted because of QThread issue with weak reference (see visual.graph).
    """

    next_node_uid: int = 1

    def AddNode(self, node: node_t, /) -> None:
        """"""
        node.SetUniqueName(self.next_node_uid)
        self.next_node_uid += 1
        self.append(node)

    def RemoveNode(self, node: node_t, /) -> None:
        """"""
        node.Invalidate()

        node.RemoveLink(None, None, None)
        for predecessor in self._PredecessorsOfNode(node):
            for output_name in predecessor.outputs:
                predecessor.RemoveLink(output_name, node, None)

        self.remove(node)
        if self.__len__() == 0:
            self.next_node_uid = 1

    def _PredecessorsOfNode(
        self, target: node_t, /, *, input_name: str | None = None
    ) -> tuple[node_t, ...]:
        """"""
        output = set()

        for node in self:
            if input_name is None:
                if target in node.links:
                    output.add(node)
            elif (target, input_name) in node.links:
                return (node,)

        if input_name is None:
            return tuple(output)

        return ()

    def InvalidateAllNodes(self) -> None:
        """"""
        for node in self:
            node.Invalidate()

    def Run(self, /, *, script_accessor: h.TextIO = None) -> set[node_t]:
        """"""
        nodes_to_be_run = set(filter(lambda _elm: _elm.needs_running, self))
        should_save_as_script = script_accessor is not None

        while (n_to_be_run := nodes_to_be_run.__len__()) > 0:
            runnable_nodes = tuple(filter(lambda _elm: _elm.can_run, nodes_to_be_run))
            if runnable_nodes.__len__() == 0:
                break

            for node in runnable_nodes:
                output_names = node.description.output_names
                n_outputs = output_names.__len__()

                if should_save_as_script and (n_outputs > 0):
                    if n_outputs > 1:
                        for idx in range(n_outputs - 1):
                            script_accessor.write(
                                node.UniqueOutputName(output_names[idx]) + ", "
                            )
                    script_accessor.write(
                        node.UniqueOutputName(output_names[-1]) + " = "
                    )

                node.Run(script_accessor=script_accessor)
                node.SendOutputsToSuccessors()

            nodes_to_be_run.difference_update(runnable_nodes)

        if (n_to_be_run > 0) and should_save_as_script:
            script_accessor.write(
                'print("Workflow saving was incomplete due to some nodes not being runnable.")'
            )

        return nodes_to_be_run
