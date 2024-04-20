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
import typing as h
from pathlib import Path as path_t

import PyQt6.QtCore as qtcr
import PyQt6.QtWidgets as wdgt
from babelwidget.backend.generic.path_chooser import NewSelectedInputDocument
from pyvispr.catalog.installer import (
    ExistingUserPaths,
    InstallLocalFunction,
    InstallReferencedFunction,
    InstallSystemFunction,
    PathForSystem,
    UpdateFunction,
)
from pyvispr.config.appearance.behavior import TOO_MANY_SELECTED
from pyvispr.config.appearance.color import BLACK_BRUSH
from pyvispr.constant.app import APP_NAME
from pyvispr.extension.function import function_t
from pyvispr.flow.descriptive.node import source_e
from pyvispr.interface.window.widget.function_header import HeaderDialog, header_wgt_t
from pyvispr.interface.window.widget.list_file import file_list_wgt_t
from pyvispr.interface.window.widget.list_function import function_list_wgt_t
from pyvispr.interface.window.widget.list_module import module_list_wgt_t
from pyvispr.interface.window.widget.list_node import node_list_wgt_t
from pyvispr.runtime.backend import SCREEN_BACKEND


@dtcl.dataclass(slots=True, repr=False, eq=False)
class installer_wdw_t(wdgt.QMainWindow):
    node_list: node_list_wgt_t
    file_list: file_list_wgt_t
    module_list: module_list_wgt_t
    function_list: function_list_wgt_t
    recursivity_wgt: wdgt.QCheckBox
    # For retrieval of header dialog details.
    input_ii_names: str | None = dtcl.field(init=False, default=None)
    output_names: str | None = dtcl.field(init=False, default=None)
    final_header: str | None = dtcl.field(init=False, default=None)

    def __post_init__(self) -> None:
        """"""
        wdgt.QMainWindow.__init__(self)
        self.setWindowTitle(f"{APP_NAME} - Node Installer")

        catalog = _CatalogWidget(self.node_list)
        single = _SingleWidget(self.InstallUserFunction)
        multiple = _MultipleWidget(
            self.recursivity_wgt,
            self.file_list,
            self.ChooseUserFolder,
            self.InstallUserFolder,
        )
        system = _SystemWidget(
            self.module_list,
            self.function_list,
            self.InstallSystemFunction,
        )
        tabs = wdgt.QTabWidget()
        for widget, name in (
            (catalog, "Manage Installed"),
            (single, "Install Single"),
            (multiple, "Install Batch - User"),
            (system, "Install Batch - System"),
        ):
            tabs.addTab(widget, name)
        done = wdgt.QPushButton("Done")

        layout = wdgt.QVBoxLayout()
        layout.addWidget(tabs)
        layout.addWidget(done)

        central = wdgt.QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

        SCREEN_BACKEND.CreateMessageCanal(
            self.node_list, "itemClicked", self.CorrectHeaderOrUninstall
        )
        SCREEN_BACKEND.CreateMessageCanal(
            self.module_list, "itemClicked", self.LoadFunctions
        )
        SCREEN_BACKEND.CreateMessageCanal(done, "clicked", self.close)

    @classmethod
    def New(cls) -> installer_wdw_t:
        """"""
        node_list = node_list_wgt_t(element_name="Nodes")
        file_list = file_list_wgt_t(element_name="Python Files")
        module_list = module_list_wgt_t(element_name="Modules")
        function_list = function_list_wgt_t(element_name="Functions")
        recursivity_wgt = wdgt.QCheckBox("Search Recursively")

        file_list.setSelectionMode(
            wdgt.QAbstractItemView.SelectionMode.ExtendedSelection
        )
        function_list.setSelectionMode(
            wdgt.QAbstractItemView.SelectionMode.ExtendedSelection
        )

        return cls(
            node_list=node_list,
            file_list=file_list,
            module_list=module_list,
            function_list=function_list,
            recursivity_wgt=recursivity_wgt,
        )

    def LoadFunctions(self, item: wdgt.QListWidgetItem, /) -> None:
        """"""
        # self.setEnabled(False)
        # qtcr.QCoreApplication.processEvents()
        self.function_list.module = item.text()
        self.function_list.Reload()
        # self.setEnabled(True)

    def InstallUserFunction(self, mode: source_e, /) -> None:
        """"""
        path = NewSelectedInputDocument(
            "Select Python File",
            "Select Python File",
            SCREEN_BACKEND,
            mode="document",
            valid_types={"Python File": "py"},
        )
        if path is None:
            return

        self._InstallUserFunctionForPath(path, True, mode)
        self.node_list.Reload()

    def _InstallUserFunctionForPath(
        self, path: path_t, should_correct_header: bool, mode: source_e, /
    ) -> None:
        """"""
        function = function_t.NewFromPath(path)
        if function is None:
            return

        existing_s = ExistingUserPaths(function.name)
        if (existing_s.__len__() > 0) and _ShouldNotProceedWithInstallation(
            f"{path}: {function.name}"
        ):
            return

        for existing in existing_s:
            existing.unlink()

        if should_correct_header:
            header_dialog = HeaderDialog(
                None,
                function,
                self._HeaderRetrievalInitialization,
                self._RetrieveFinalHeader,
                self,
            )
            header_dialog.exec()
            if self.final_header is None:
                return

            header = self.final_header
        else:
            header = function.header
            self.output_names = function.output_names

        if mode is source_e.local:
            InstallFunction = InstallLocalFunction
        else:
            InstallFunction = InstallReferencedFunction
        InstallFunction(function, header, self.input_ii_names, self.output_names)

    def ChooseUserFolder(self) -> None:
        """"""
        path = NewSelectedInputDocument(
            "Select Base Folder", "Select Base Folder", SCREEN_BACKEND, mode="folder"
        )
        if path is None:
            return

        self.file_list.base_folder = path
        self.file_list.recursive_mode = self.recursivity_wgt.isChecked()
        self.file_list.Reload()

    def InstallUserFolder(self, mode: source_e, /) -> None:
        """"""
        if self.file_list.base_folder is None:
            return

        selected_s = self.file_list.SelectedItemsOrAll()
        should_correct_header = selected_s.__len__() < TOO_MANY_SELECTED
        for selected in selected_s:
            path = self.file_list.files[selected.text()]
            self._InstallUserFunctionForPath(path, should_correct_header, mode)

        self.node_list.Reload()

    def InstallSystemFunction(self) -> None:
        """"""
        if self.function_list.module is None:
            return

        selected_s = self.function_list.SelectedItemsOrAll()
        should_correct_header = selected_s.__len__() < TOO_MANY_SELECTED
        for selected in selected_s:
            function_display_name = selected.text()
            if "." in function_display_name:
                _, function_name = function_display_name.rsplit(".", maxsplit=1)
            else:
                function_name = function_display_name
            module_pypath = self.function_list.functions[function_display_name].pypath
            where = PathForSystem(module_pypath, function_name)
            if where.is_file() and _ShouldNotProceedWithInstallation(
                f"{module_pypath}.{function_name}"
            ):
                continue

            function = self.function_list.functions[function_display_name]
            if should_correct_header:
                header_dialog = HeaderDialog(
                    None,
                    function,
                    self._HeaderRetrievalInitialization,
                    self._RetrieveFinalHeader,
                    self,
                )
                header_dialog.exec()
                if self.final_header is None:
                    continue

                header = self.final_header
            else:
                header = function.header
                self.output_names = function.output_names

            InstallSystemFunction(
                module_pypath,
                function_name,
                function.imports,
                header,
                self.input_ii_names,
                self.output_names,
            )

        self.node_list.Reload()

    def CorrectHeaderOrUninstall(self, item: wdgt.QListWidgetItem, /) -> None:
        """"""
        node = self.node_list.nodes[item.text()]

        menu = wdgt.QMenu()
        correct_action = menu.addAction("Correct Definition")
        uninstall_menu = menu.addMenu("Uninstall...")
        _ = uninstall_menu.addAction("... Now")
        position = self.node_list.mapToGlobal(
            self.node_list.viewport().pos()
            + self.node_list.visualItemRect(item).topRight()
        )
        selected_action = menu.exec(position)
        if selected_action is None:
            return

        if selected_action is correct_action:
            proxy_function = function_t.NewFromPath(
                node.proxy.path, name=node.proxy.name
            )
            actual_function = function_t.NewFromPath(
                node.actual.path, name=node.actual.name
            )
            header_dialog = HeaderDialog(
                proxy_function,
                actual_function,
                self._HeaderRetrievalInitialization,
                self._RetrieveFinalHeader,
                self,
            )
            header_dialog.exec()

            if self.final_header is not None:
                UpdateFunction(
                    node.name,
                    proxy_function,
                    actual_function,
                    self.final_header,
                    self.input_ii_names,
                    self.output_names,
                    node.source,
                )
                node.requires_completion = False
                item.setForeground(BLACK_BRUSH)
        else:
            node.proxy.path.unlink()
            del self.node_list.nodes[item.text()]
            _ = self.node_list.takeItem(self.node_list.row(item))

    def _HeaderRetrievalInitialization(self) -> None:
        """"""
        self.input_ii_names = None
        self.output_names = None
        self.final_header = None

    def _RetrieveFinalHeader(
        self, header_wgt: header_wgt_t, header_dialog: wdgt.QDialog, /
    ) -> None:
        """"""
        if header_wgt.header_is_valid:
            self.input_ii_names = header_wgt.input_ii_names
            self.output_names = header_wgt.output_names
            self.final_header = header_wgt.header_final
            header_dialog.close()


def _CatalogWidget(node_list: node_list_wgt_t, /) -> wdgt.QWidget:
    """"""
    output = wdgt.QWidget()

    layout = wdgt.QVBoxLayout()
    layout.setAlignment(qtcr.Qt.AlignmentFlag.AlignCenter)

    layout.addWidget(node_list)
    layout.addWidget(node_list.filter_wgt)
    output.setLayout(layout)

    return output


def _SingleWidget(InstallUserFunction: h.Callable[[source_e], None], /) -> wdgt.QWidget:
    """"""
    output = wdgt.QWidget()

    local = wdgt.QPushButton("Select Python File For LOCAL Installation")
    referenced = wdgt.QPushButton("Select Python File For REFERENCED Installation")

    for widget in (local, referenced):
        widget.setSizePolicy(
            wdgt.QSizePolicy.Policy.Expanding,
            wdgt.QSizePolicy.Policy.Expanding,
        )

    layout = wdgt.QVBoxLayout()

    layout.addWidget(local)
    layout.addWidget(referenced)
    output.setLayout(layout)

    SCREEN_BACKEND.CreateMessageCanal(
        local, "clicked", lambda *args, **kwargs: InstallUserFunction(source_e.local)
    )
    SCREEN_BACKEND.CreateMessageCanal(
        referenced,
        "clicked",
        lambda *args, **kwargs: InstallUserFunction(source_e.referenced),
    )

    return output


def _MultipleWidget(
    recursivity_wgt: wdgt.QCheckBox,
    file_list: file_list_wgt_t,
    ChooseUserFolder: h.Callable[[], None],
    InstallUserFolder: h.Callable[[source_e], None],
    /,
) -> wdgt.QWidget:
    """"""
    output = wdgt.QWidget()

    select = wdgt.QPushButton(f"Select Base Folder")
    install_local = wdgt.QPushButton("Install Selected or All as LOCAL")
    install_referenced = wdgt.QPushButton("Install Selected or All as REFERENCED")

    select.setSizePolicy(
        wdgt.QSizePolicy.Policy.Expanding,
        wdgt.QSizePolicy.Policy.Expanding,
    )

    left = wdgt.QVBoxLayout()
    right = wdgt.QVBoxLayout()
    main_layout = wdgt.QHBoxLayout()

    left.addWidget(select)
    left.addWidget(recursivity_wgt)

    right.addWidget(file_list)
    right.addWidget(install_local)
    right.addWidget(install_referenced)

    main_layout.addLayout(left)
    main_layout.addLayout(right)

    output.setLayout(main_layout)

    SCREEN_BACKEND.CreateMessageCanal(select, "clicked", ChooseUserFolder)
    SCREEN_BACKEND.CreateMessageCanal(
        install_local,
        "clicked",
        lambda *args, **kwargs: InstallUserFolder(source_e.local),
    )
    SCREEN_BACKEND.CreateMessageCanal(
        install_referenced,
        "clicked",
        lambda *args, **kwargs: InstallUserFolder(source_e.referenced),
    )

    return output


def _SystemWidget(
    module_list: module_list_wgt_t,
    function_list: function_list_wgt_t,
    InstallSystemFunction_: h.Callable[[], None],
    /,
) -> wdgt.QWidget:
    """"""
    output = wdgt.QWidget()

    install = wdgt.QPushButton("Install Selected or All")

    layout = wdgt.QGridLayout()
    for col, widget in enumerate((module_list, function_list)):
        layout.addWidget(widget, 0, col)
        layout.addWidget(widget.filter_wgt, 1, col)
    layout.addWidget(install, 2, 0, 1, 2)

    output.setLayout(layout)

    SCREEN_BACKEND.CreateMessageCanal(install, "clicked", InstallSystemFunction_)

    return output


def _ShouldNotProceedWithInstallation(what: str, /, *, how_installed: str = "") -> bool:
    """"""
    answer_cancel = wdgt.QMessageBox.StandardButton.Cancel
    update = wdgt.QMessageBox()
    update.setWindowTitle(f'Proceed Updating "{what}"?')
    update.setText(
        f'"{what}" is already {how_installed}installed. '
        f"Would you like to proceed updating/overwriting its installation?"
    )
    update.setStandardButtons(answer_cancel | wdgt.QMessageBox.StandardButton.Ok)
    update.setDefaultButton(answer_cancel)
    answer = update.exec()

    return answer == answer_cancel
