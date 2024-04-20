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
from PyQt6.QtCore import QPoint, QPointF
from PyQt6.QtGui import QPainterPath, QPolygonF
from pyvispr.config.appearance.color import (
    LINK_BRUSH_ARROW,
    LINK_PEN_EMPTY,
    LINK_PEN_FULL,
)
from pyvispr.config.appearance.geometry import LINK_MIN_HORIZONTAL_SHIFT
from pyvispr.flow.visual.node import node_t


@dtcl.dataclass(slots=True, repr=False, eq=False)
class link_t(wdgt.QGraphicsPathItem):
    """
    Note: Using QGraphicsItemGroup as a base class in order to group the path and the arrow together somehow "hides" the
    path from mouse events: when clicked the scene items are the group (not of interest) and the path (of interest), but
    as a path item instead of a link_t.
    """

    source_node: node_t
    target_node: node_t
    arrow: wdgt.QGraphicsPolygonItem | None = None
    source_point: dtcl.InitVar[QPointF | None] = None
    target_point: dtcl.InitVar[QPointF | None] = None

    def __post_init__(
        self, source_point: QPointF | None, target_point: QPointF | None
    ) -> None:
        """"""
        # Otherwise, complaint about super-init not having been called.
        wdgt.QGraphicsPathItem.__init__(self)

        arrow = QPolygonF()
        arrow.append(QPointF(10, 0))
        arrow.append(QPointF(0, 10))
        arrow.append(QPointF(0, -10))
        arrow.append(QPointF(10, 0))
        self.arrow = wdgt.QGraphicsPolygonItem(arrow)
        self.arrow.setPen(LINK_PEN_FULL)
        self.arrow.setBrush(LINK_BRUSH_ARROW)
        self.arrow.setZValue(1)

        if self.source_node.functional.needs_running:
            pen = LINK_PEN_EMPTY
        else:
            pen = LINK_PEN_FULL
        self.setPen(pen)

        self.SetPath(source_point, target_point, is_creation=True)
        self.SetTooltip()
        self.setZValue(1)

    def SetPath(
        self,
        source_point: QPointF,
        target_point: QPointF,
        /,
        *,
        is_creation: bool = False,
    ) -> None:
        """"""
        if is_creation:
            translation = source_point
        else:
            translation = source_point - QPointF(self.path().elementAt(0))
        polygon = self.arrow.polygon()
        polygon.translate(translation)
        self.arrow.setPolygon(polygon)

        tangent = 0.4 * (target_point - source_point)
        tangent.setY(0)
        if tangent.x() < 0:
            tangent.setX(-tangent.x())
        if tangent.x() < LINK_MIN_HORIZONTAL_SHIFT:
            tangent.setX(LINK_MIN_HORIZONTAL_SHIFT)

        path = QPainterPath(source_point)
        path.cubicTo(source_point + tangent, target_point - tangent, target_point)
        self.setPath(path)

    def SetTooltip(self) -> None:
        """"""
        self.setToolTip(
            "\n".join(f"{_elm[0]} ⮞ {_elm[1]}" for _elm in self.UnderlyingFunctionals())
        )

    def UnderlyingFunctionals(self) -> tuple[tuple[str, str], ...]:
        """"""
        output = []

        source = self.source_node.functional
        target = self.target_node.functional
        for output_name, sockets in source.links.items():
            output.extend(
                (output_name, _elm[1]) for _elm in sockets if _elm[0] is target
            )

        return tuple(output)

    def LinksToBeRemoved(
        self, position: QPoint, /
    ) -> tuple[tuple[str, str] | None, bool] | None:
        """
        /!\\ Strange behavior (Qt bug?): Sometimes a mouse press on a different link (or even in the background)
        calls the mousePressEvent callback of the previously pressed link; and this repeats several times,
        until clicking far away from any link!!!
        """
        menu = wdgt.QMenu()
        cancel_action = menu.addAction("Close Menu")
        no_action = menu.addAction("or Remove Link(s):")
        no_action.setEnabled(False)

        underlying_links = self.UnderlyingFunctionals()
        n_links = underlying_links.__len__()
        menu_actions = n_links * [None]
        for link_idx, link in enumerate(underlying_links):
            menu_actions[link_idx] = menu.addAction(link[0] + "->" + link[1])
        if n_links > 1:
            all_action = menu.addAction("Remove All")
            menu_actions.append(all_action)
        else:
            all_action = None

        selected_action = menu.exec(position)

        if (selected_action is None) or (selected_action is cancel_action):
            return None

        if selected_action is all_action:
            return None, True

        return (
            underlying_links[menu_actions.index(selected_action)],
            n_links == 1,
        )
