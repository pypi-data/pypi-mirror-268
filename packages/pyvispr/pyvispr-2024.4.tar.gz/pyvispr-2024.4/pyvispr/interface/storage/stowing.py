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

# from pyvispr.interface.window.main import runner_wdw_t
from os.path import dirname as ExtractPathPart
from pathlib import Path as path_t

import PyQt6.QtWidgets as wdgt
from json_any.task.storage import StoreAsJSON
from pyvispr.constant.path import HOME_FOLDER
from pyvispr.flow.visual.graph import graph_t

last_save_location = HOME_FOLDER
last_save_as_script_location = HOME_FOLDER


def SaveWorkflow(manager, /) -> None:
    """"""
    global last_save_location

    filename = wdgt.QFileDialog.getSaveFileName(
        manager,
        "Save Workflow",
        str(last_save_location),
        "pyVispr Workflows (*.json.*)",
    )
    if (filename is None) or (filename[0].__len__() == 0):
        return
    filename = filename[0]

    last_save_location = ExtractPathPart(filename)

    _Save(manager.whiteboard.graph, filename)


def SaveWorkflowAsScript(manager, /) -> None:
    """"""
    global last_save_as_script_location

    filename = wdgt.QFileDialog.getSaveFileName(
        manager,
        "Save Workflow as Script",
        str(last_save_as_script_location),
        "Python Scripts (*.py)",
    )
    if (filename is None) or (len(filename[0]) == 0):
        return
    filename = filename[0]

    last_save_as_script_location = ExtractPathPart(filename)

    _SaveAsScript(manager.whiteboard.graph, filename)


def _Save(graph: graph_t, filename: str, /) -> None:
    """"""
    path = StoreAsJSON(
        graph, filename, should_continue_on_error=True, should_overwrite_path=True
    )
    if isinstance(path, path_t):
        wdgt.QMessageBox.about(
            None,
            "Workflow Successfully Saved",
            f"Workflow Successfully Saved in: {path}.",
        )
    else:
        error = "\n".join(path)
        wdgt.QMessageBox.warning(
            None, "Workflow Saving Failure", f"Workflow Saving Failure:\n{error}"
        )


def _SaveAsScript(graph: graph_t, filename: str, /) -> None:
    """"""
    with open(filename, mode="w") as accessor:
        graph.Run(script_accessor=accessor)
