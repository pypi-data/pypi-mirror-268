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

import PyQt6.QtWidgets as wdgt
from PyQt6.QtCore import Qt as constant_e
from PyQt6.QtGui import QMouseEvent, QPainter
from pyvispr.config.appearance.color import GRID_PEN
from pyvispr.config.appearance.geometry import (
    NODE_HEIGHT_TOTAL,
    NODE_WIDTH_TOTAL,
    WHITEBOARD_HEIGHT,
    WHITEBOARD_WIDTH,
)
from pyvispr.flow.functional.node_isolated import state_e
from pyvispr.flow.visual.graph import graph_t
from pyvispr.flow.visual.link import link_t
from pyvispr.flow.visual.node import node_t


@dtcl.dataclass(slots=True, repr=False, eq=False)
class whiteboard_t(wdgt.QGraphicsView):
    zoom_factor: h.ClassVar[float] = 1.25

    grid: wdgt.QGraphicsItemGroup = dtcl.field(init=False, default=None)
    graph: graph_t = dtcl.field(init=False, default=None)

    def __post_init__(self) -> None:
        """"""
        # Otherwise, complaint about super-init not having been called.
        wdgt.QGraphicsView.__init__(self)

        self.setMinimumSize(WHITEBOARD_WIDTH, WHITEBOARD_HEIGHT)
        self.setSizePolicy(
            wdgt.QSizePolicy.Policy.MinimumExpanding,
            wdgt.QSizePolicy.Policy.MinimumExpanding,
        )
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        # Used to not work in conjunction with selectable RectItems.
        self.setDragMode(wdgt.QGraphicsView.DragMode.RubberBandDrag)

        self.SetGraph()

    def AddGrid(self) -> None:
        """"""
        if self.graph is None:
            raise RuntimeError(
                "Whiteboard grid can be added only after a graph has been created."
            )

        grid = wdgt.QGraphicsItemGroup()
        min_row = -NODE_HEIGHT_TOTAL * 4
        max_row = -2 * min_row
        min_col = -NODE_WIDTH_TOTAL * 5
        max_col = -2 * min_col
        for row in range(min_row, max_row + 1, NODE_HEIGHT_TOTAL):
            line = wdgt.QGraphicsLineItem(min_col, row, max_col, row)
            line.setPen(GRID_PEN)
            grid.addToGroup(line)
        for col in range(min_col, max_col + 1, NODE_WIDTH_TOTAL):
            line = wdgt.QGraphicsLineItem(col, min_row, col, max_row)
            line.setPen(GRID_PEN)
            grid.addToGroup(line)
        grid.setZValue(0)

        self.grid = grid
        self.graph.addItem(grid)

    def ToggleGridVisibility(self) -> None:
        """"""
        self.grid.setVisible(not self.grid.isVisible())

    def SetGraph(
        self, *, graph: graph_t | None = None, is_update: bool = False
    ) -> None:
        """"""
        if graph is None:
            self.graph = graph_t()
        elif is_update:
            self.graph.MergeWith(graph)
        else:
            self.graph = graph

        if not is_update:
            self.AddGrid()
            self.setScene(self.graph)

    def mousePressEvent(self, event: QMouseEvent, /) -> None:
        """"""
        if event.buttons() != constant_e.MouseButton.LeftButton:
            wdgt.QGraphicsView.mousePressEvent(self, event)
            return

        view_position = event.pos()
        scene_position = self.mapToScene(view_position)
        item: node_t | link_t | None = None
        # Used to be: deviceTransform=self.graph.views()[0].transform()
        for current_item in self.graph.items(
            scene_position, deviceTransform=self.transform()
        ):
            if isinstance(current_item, (node_t, link_t)):
                item = current_item
                break
        if item is None:
            wdgt.QGraphicsView.mousePressEvent(self, event)
            return

        item: node_t | link_t
        if isinstance(item, node_t):
            item_position = item.mapFromScene(scene_position)
            if (item.in_btn is not None) and item.in_btn.contains(item_position):
                item_global_pos = self.mapToGlobal(view_position)
                self.graph.AddLinkMaybe(item, False, item_global_pos)
            elif (item.out_btn is not None) and item.out_btn.contains(item_position):
                item_global_pos = self.mapToGlobal(view_position)
                self.graph.AddLinkMaybe(item, True, item_global_pos)
            elif item.config_btn.contains(item_position):
                item.ToggleIIDialog()
            elif item.state_btn.contains(item_position):
                pass
            elif item.remove_btn.contains(item_position):
                menu = wdgt.QMenu()
                cancel_action = menu.addAction("Close Menu")
                no_action = menu.addAction("or")
                no_action.setEnabled(False)
                invalidate_action = menu.addAction("Invalidate Node")
                if item.functional.state is state_e.disabled:
                    operation = "Enable"
                else:
                    operation = "Disable"
                disable_action = menu.addAction(f"{operation} Node")
                remove_action = menu.addAction("Remove Node")

                item_global_pos = self.mapToGlobal(view_position)
                selected_action = menu.exec(item_global_pos)

                if (selected_action is None) or (selected_action is cancel_action):
                    return
                if selected_action is invalidate_action:
                    item.functional.Invalidate()
                elif selected_action is disable_action:
                    item.functional.ToggleAbility()
                if selected_action is remove_action:
                    self.graph.RemoveNode(item)
            else:
                wdgt.QGraphicsView.mousePressEvent(self, event)
        else:
            links = item.LinksToBeRemoved(self.mapToGlobal(view_position))
            if isinstance(links, h.Sequence):
                if links[0] is None:
                    self.graph.RemoveLink(item)
                else:
                    self.graph.RemoveLink(
                        item, output_name=links[0][0], input_name=links[0][1]
                    )

    def wheelEvent(self, event, /) -> None:
        """"""
        if event.modifiers() == constant_e.KeyboardModifier.ControlModifier:
            scale_factor = (
                1 / whiteboard_t.zoom_factor
                if event.angleDelta().y() > 0
                else whiteboard_t.zoom_factor
            )
            self.scale(scale_factor, scale_factor)
