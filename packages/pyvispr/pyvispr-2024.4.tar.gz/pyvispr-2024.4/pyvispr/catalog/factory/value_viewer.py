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

import collections.abc as cllt
import pprint as pprt
import typing as h

import PyQt6.QtGui as qtui
import PyQt6.QtWidgets as wdgt
from PyQt6.QtCore import QThreadPool as thread_manager_t
from pyvispr.extension.qt6 import ExecuteApp, QtApp
from pyvispr.runtime.backend import SCREEN_BACKEND


def pyVisprValueViewer(value: h.Any, /) -> None:
    """"""
    app, should_exec = QtApp()
    value_viewer = value_viewer_t(value, wdgt.QApplication.activeWindow())
    value_viewer.show()
    ExecuteApp(app, should_exec)
    # TODO: Solve the following error:
    #     QBasicTimer::stop: Failed. Possibly trying to stop from a different thread
    #     The code below makes it disappear, but the table is not correctly populated then.
    # if value_viewer.thread_manager is not None:
    #     value_viewer.thread_manager.waitForDone()
    # Test also somewhere (not here though; it does not work):
    # value_viewer.thread_manager.moveToThread(wdgt.QApplication.instance().thread())


class value_viewer_t(wdgt.QMainWindow):
    def __init__(self, value: h.Any, wdw: wdgt.QWidget, /) -> None:
        """"""
        super().__init__(wdw)

        if _ValueIsASequenceOfSequences(value):
            self.value = value

            self.viewer = wdgt.QTableView()
            self.viewer.setEnabled(False)

            self.model = qtui.QStandardItemModel(self.viewer)
            self.model.setColumnCount(max(_elm.__len__() for _elm in self.value))

            self.viewer.setModel(self.model)

            self.thread_manager = thread_manager_t()
            self.thread_manager.start(self.PopulateTable)
        else:
            as_str = pprt.pformat(value, width=120, compact=True, sort_dicts=False)
            self.viewer = wdgt.QTextEdit(as_str)
            self.value = self.model = self.thread_manager = None

        done = wdgt.QPushButton("Done")

        layout = wdgt.QVBoxLayout()
        layout.addWidget(self.viewer)
        layout.addWidget(done)

        central = wdgt.QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

        self.setWindowTitle("pyVispr Value Viewer")

        SCREEN_BACKEND.CreateMessageCanal(done, "clicked", self.close)

    def PopulateTable(self) -> None:
        """"""
        self.value: cllt.Iterable[cllt.Iterable]
        self.viewer: wdgt.QTableView
        self.model: qtui.QStandardItemModel

        for row in self.value:
            cells = map(str, row)
            cells = map(qtui.QStandardItem, cells)
            self.model.appendRow(cells)

        self.viewer.resizeRowsToContents()
        self.viewer.resizeColumnsToContents()

        self.viewer.setEnabled(True)

        self.value = None


def _ValueIsASequenceOfSequences(value: h.Any, /) -> bool:
    """"""
    return (
        isinstance(value, cllt.Iterable)
        and hasattr(value, "__len__")
        and (value.__len__() > 0)
        and isinstance(value[0], cllt.Iterable)
        and hasattr(value[0], "__len__")
        and (value[0].__len__() > 0)
        and not isinstance(value[0][0], cllt.Iterable)
    )


# from __future__ import annotations
# import PyQt6.QtCore as qtcr
# class table_model_t(qtcr.QAbstractTableModel):
#     @classmethod
#     def NewWithData(cls, data: cllt.Iterable[cllt.Iterable]) -> table_model_t:
#         """"""
#         output = cls()
#
#         output._data = data
#         output.n_rows = data.__len__()
#         output.n_cols = max(_elm.__len__() for _elm in data)
#
#         return output
#
#     def rowCount(self, _: qtcr.QModelIndex = None) -> int:
#         """"""
#         return self.n_rows
#
#     def columnCount(self, _: qtcr.QModelIndex = None) -> int:
#         """"""
#         return self.n_cols
#
#     def data(
#         self,
#         index: qtcr.QModelIndex,
#         role: qtcr.Qt.ItemDataRole = qtcr.Qt.ItemDataRole.DisplayRole,
#     ) -> str | None:
#         """"""
#         if role == qtcr.Qt.ItemDataRole.DisplayRole:
#             r_idx = index.row()
#             if 0 <= r_idx < self.n_rows:
#                 row = self._data[r_idx]
#                 c_idx = index.column()
#                 if 0 <= c_idx < row.__len__():
#                     return row[c_idx]
