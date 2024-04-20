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
from re import search as SearchRegEx

from PyQt6.QtCore import Qt as constant_e
from pyvispr.config.appearance.color import ORANGE_BRUSH
from pyvispr.flow.descriptive.node import node_t
from pyvispr.interface.window.widget.list import list_wgt_t
from pyvispr.runtime.catalog import NODE_CATALOG


@dtcl.dataclass(slots=True, repr=False, eq=False)
class node_list_wgt_t(list_wgt_t):
    nodes: dict[str, node_t] = dtcl.field(init=False, default_factory=dict)

    def ActualReload(self) -> None:
        """"""
        for node in NODE_CATALOG:
            self.nodes[node.name] = node

            self.addItem(node.name)
            item = self.item(self.count() - 1)
            if node.documentation is not None:
                item.setToolTip(node.documentation)
            if node.requires_completion:
                item.setForeground(ORANGE_BRUSH)

    def Filter(self, new_filter: str, /) -> None:
        """"""
        if new_filter.__len__() > 0:
            matched_items = self.findItems(
                new_filter, constant_e.MatchFlag.MatchContains
            )

            for item_idx in range(self.count()):
                node_item = self.item(item_idx)
                node_description = NODE_CATALOG.NodeDescription(node_item.text())

                if node_description.keywords is None:
                    mismatches_key_xpressions = True
                else:
                    mismatches_key_xpressions = (
                        new_filter not in node_description.keywords
                    )

                if node_description.short_description is None:
                    mismatches_short_description = True
                else:
                    mismatches_short_description = (
                        SearchRegEx(
                            "\b" + new_filter + "\b", node_description.short_description
                        )
                        is None
                    )

                if (
                    (node_item not in matched_items)
                    and mismatches_key_xpressions
                    and mismatches_short_description
                ):
                    node_item.setHidden(True)
                else:
                    node_item.setHidden(False)
        else:
            for item_idx in range(self.count()):
                self.item(item_idx).setHidden(False)
