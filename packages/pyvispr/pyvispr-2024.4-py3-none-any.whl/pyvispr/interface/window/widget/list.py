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

import PyQt6.QtWidgets as wdgt
from PyQt6.QtCore import Qt as constant_e
from pyvispr.constant.widget.list import COL_SIZE_PADDING
from pyvispr.runtime.backend import SCREEN_BACKEND


@dtcl.dataclass(slots=True, repr=False, eq=False)
class list_wgt_t(wdgt.QListWidget):
    filter_wgt: wdgt.QLineEdit = dtcl.field(init=False)
    element_name: dtcl.InitVar[str] = ""

    def __post_init__(self, element_name: str) -> None:
        """"""
        wdgt.QListWidget.__init__(self)
        self.setSelectionMode(wdgt.QAbstractItemView.SelectionMode.NoSelection)

        self.filter_wgt = wdgt.QLineEdit()
        self.filter_wgt.setPlaceholderText(f"Filter {element_name}")
        self.filter_wgt.setClearButtonEnabled(True)
        SCREEN_BACKEND.CreateMessageCanal(self.filter_wgt, "textEdited", self.Filter)

        self.Reload()

    def AddDisabledItem(self, text: str, /) -> None:
        """"""
        self.addItem(text)
        _DisableItem(self.item(self.count() - 1))

    def Reload(self) -> None:
        """"""
        self.clear()
        self.ActualReload()
        self.sortItems()

        width = self.sizeHintForColumn(0) + COL_SIZE_PADDING
        self.setFixedWidth(width)
        self.filter_wgt.setFixedWidth(width)

    def ActualReload(self) -> None:
        """"""
        raise NotImplementedError

    def Filter(self, new_filter: str, /) -> None:
        """"""
        if new_filter.__len__() > 0:
            matched_items = self.findItems(
                new_filter, constant_e.MatchFlag.MatchContains
            )

            for item_idx in range(self.count()):
                node_item = self.item(item_idx)

                if node_item not in matched_items:
                    node_item.setHidden(True)
                else:
                    node_item.setHidden(False)
        else:
            for item_idx in range(self.count()):
                self.item(item_idx).setHidden(False)

    def SelectedItemsOrAll(self) -> tuple[wdgt.QListWidgetItem, ...]:
        """"""
        output = self.selectedItems()

        if output.__len__() == 0:
            output = (self.item(_row) for _row in range(self.count()))
            output = filter(ItemIsEnabled, output)

        return tuple(output)


def _DisableItem(item: wdgt.QListWidgetItem, /) -> None:
    """"""
    item.setFlags(item.flags() & ~constant_e.ItemFlag.ItemIsEnabled)


def ItemIsEnabled(item: wdgt.QListWidgetItem, /) -> bool:
    """"""
    return (
        item.flags() & constant_e.ItemFlag.ItemIsEnabled
    ) == constant_e.ItemFlag.ItemIsEnabled
