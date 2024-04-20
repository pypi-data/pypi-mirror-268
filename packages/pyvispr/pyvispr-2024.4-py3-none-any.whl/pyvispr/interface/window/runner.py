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
from typing import cast

import PyQt6.QtWidgets as wdgt
from logger_36 import AddGenericHandler
from pyvispr import __version__
from pyvispr.constant.app import APP_NAME
from pyvispr.flow.visual.whiteboard import whiteboard_t
from pyvispr.interface.storage.loading import LoadWorkflow
from pyvispr.interface.storage.stowing import SaveWorkflow, SaveWorkflowAsScript
from pyvispr.interface.window.widget.list_node import node_list_wgt_t
from pyvispr.interface.window.widget.menu import AddEntryToMenu
from pyvispr.runtime.backend import SCREEN_BACKEND


@dtcl.dataclass(slots=True, repr=False, eq=False)
class runner_wdw_t(wdgt.QMainWindow):
    node_list: node_list_wgt_t
    whiteboard: whiteboard_t
    status_bar: wdgt.QStatusBar = dtcl.field(init=False)
    _ref_keeper: list = dtcl.field(init=False, default_factory=list)

    def __post_init__(self) -> None:
        """"""
        wdgt.QMainWindow.__init__(self)
        self.setWindowTitle(APP_NAME)

        log_area = wdgt.QTextEdit()
        log_area.setReadOnly(True)
        log_area.setLineWrapMode(wdgt.QTextEdit.LineWrapMode.NoWrap)
        AddGenericHandler(log_area.append, supports_html=True)

        tabs = wdgt.QTabWidget()
        tabs.addTab(self.whiteboard, "Workflow")
        tabs.addTab(log_area, "Messages")
        tabs.setStyleSheet("QTabWidget::tab-bar {alignment: center;}")

        layout = wdgt.QGridLayout()
        layout.addWidget(self.node_list, 1, 1)
        layout.addWidget(self.node_list.filter_wgt, 2, 1)
        layout.addWidget(tabs, 1, 2, 2, 1)

        central = wdgt.QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

        self._AddMenuBar()
        self.status_bar = self.statusBar()

        SCREEN_BACKEND.CreateMessageCanal(self.node_list, "itemClicked", self.AddNode)

    @classmethod
    def New(cls) -> runner_wdw_t:
        """"""
        node_list = node_list_wgt_t(element_name="Nodes")
        whiteboard = whiteboard_t()

        return cls(node_list=node_list, whiteboard=whiteboard)

    def _AddMenuBar(self) -> None:
        """"""
        menu_bar = self.menuBar()

        _ = _AddMenu(
            "py&Vispr",
            (
                ("About", self.OpenAboutDialog),
                ("Configure", self.OpenConfiguration),
                None,
                ("&Quit", lambda *_, **__: self.close(), {"shortcut": "Ctrl+Q"}),
            ),
            menu_bar,
            self,
        )

        reset_menu = _AddMenu(
            "Reset...",
            (
                (
                    "Now",
                    lambda *_, **__: self.whiteboard.graph.functional.InvalidateAllNodes(),
                ),
            ),
            None,
            self,
        )
        clear_menu = _AddMenu(
            "Clear...",
            (
                (
                    "Now",
                    lambda *_, **__: self.whiteboard.graph.Clear(),
                ),
            ),
            None,
            self,
        )
        self._ref_keeper.extend((reset_menu, clear_menu))
        _ = _AddMenu(
            "&Workflow",
            (
                ("About", self.OpenAboutWorkflowDialog),
                None,
                ("&Run", self.Run, {"shortcut": "Ctrl+R"}),
                None,
                ("&Save", lambda *_, **__: SaveWorkflow(self), {"shortcut": "Ctrl+S"}),
                ("L&oad", lambda *_, **__: LoadWorkflow(self), {"shortcut": "Ctrl+O"}),
                None,
                ("Save As Script", lambda *_, **__: SaveWorkflowAsScript(self)),
                None,
                reset_menu,
                clear_menu,
            ),
            menu_bar,
            self,
        )

        _ = _AddMenu(
            "&View",
            (
                ("Toggle Grid", self.whiteboard.ToggleGridVisibility),
                ("Align on Grid", self.AlignOnGrid),
            ),
            menu_bar,
            self,
        )

        _ = _AddMenu(
            "&Catalog",
            (("Refresh", lambda *_, **__: self.node_list.Reload()),),
            menu_bar,
            self,
        )

    def AddNode(self, item: wdgt.QListWidgetItem, /) -> None:
        """
        Calling directly on self.whiteboard.graph from the menu will not work if the graph changes.
        """
        self.whiteboard.graph.AddNode(item.text())

    def AlignOnGrid(self) -> None:
        """
        Calling directly on self.whiteboard.graph from the menu will not work if the graph changes.
        """
        self.whiteboard.graph.AlignOnGrid()

    def Run(self) -> None:
        """
        Calling directly on self.whiteboard.graph from the menu will not work if the graph changes.
        """
        self.whiteboard.graph.Run()

    def OpenAboutDialog(self, _: bool, /) -> None:
        """"""
        wdgt.QMessageBox.about(
            cast(wdgt.QWidget, self), "About pyVispr", f"pyVispr {__version__}"
        )

    def OpenConfiguration(self, _: bool, /) -> None:
        """"""
        wdgt.QMessageBox.about(
            cast(wdgt.QWidget, self),
            "pyVispr Configuration",
            "No configuration options yet\n",
        )

    def OpenAboutWorkflowDialog(self, _: bool, /) -> None:
        """"""
        wdgt.QMessageBox.about(
            cast(wdgt.QWidget, self),
            "About Workflow",
            f"Nodes:{self.whiteboard.graph.nodes.__len__()}/{self.whiteboard.graph.functional.__len__()}\n"
            f"Links:{self.whiteboard.graph.links.__len__()}",
        )


def _AddMenu(
    name: str,
    entries: tuple,
    parent_menu: wdgt.QMenuBar | wdgt.QMenu | None,
    parent_widget: wdgt.QWidget,
    /,
) -> wdgt.QMenu:
    """"""
    if parent_menu is None:
        output = wdgt.QMenu(name)
    else:
        output = parent_menu.addMenu(name)

    for entry in entries:
        if entry is None:
            output.addSeparator()
        elif isinstance(entry, wdgt.QMenu):
            output.addMenu(entry)
        else:
            if isinstance(entry[-1], dict):
                args = entry[:-1]
                kwargs = entry[-1]
            else:
                args = entry
                kwargs = {}
            AddEntryToMenu(output, parent_widget, *args, **kwargs)

    return output
