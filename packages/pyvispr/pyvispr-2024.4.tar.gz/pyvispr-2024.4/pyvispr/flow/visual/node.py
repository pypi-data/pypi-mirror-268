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

import PyQt6.QtWidgets as wdgt
from conf_ini_g.interface.window.parameter.main import TypeAndValueWidgetsForType
from conf_ini_g.phase.specification.parameter.type import type_t
from logger_36 import LOGGER
from PyQt6.QtCore import QPointF, QRectF
from pyvispr.config.appearance.color import (
    BUTTON_BRUSH_CONFIG,
    BUTTON_BRUSH_REMOVE,
    BUTTON_BRUSH_STATE_TODO,
    INOUT_BRUSH_INACTIVE,
    NODE_BRUSH_RESTING,
    NODE_BRUSH_SELECTED,
    color_e,
)
from pyvispr.config.appearance.geometry import (
    BUTTON_WIDTH,
    NODE_HEIGHT_TOTAL,
    NODE_WIDTH_TOTAL,
)
from pyvispr.constant.widget.node import (
    HEIGHT_OF_BOTTOM_BUTTONS,
    HEIGHT_OF_LATERAL_BUTTONS,
    HORIZONTAL_FREE_SPACE,
    NEEDS_RUNNING,
    TOP_OF_BOTTOM_BUTTONS,
    WIDTH_OF_LATERAL_BUTTONS,
)
from pyvispr.flow.descriptive.socket import assignment_e
from pyvispr.flow.functional.node_linked import node_t as functional_t
from pyvispr.flow.visual.ii_value import invalid_ii_value_t
from pyvispr.runtime.backend import SCREEN_BACKEND
from pyvispr.runtime.socket import VALUE_NOT_SET, value_not_set_t
from str_to_obj import annotation_t


class ii_widget_p(wdgt.QWidget):
    def Assign(
        self,
        value: h.Any,
        stripe: type_t | annotation_t | None,
    ) -> None: ...

    def Text(self) -> str: ...


@dtcl.dataclass(slots=True, repr=False, eq=False)
class node_t(wdgt.QGraphicsRectItem):
    functional: functional_t
    label: wdgt.QGraphicsTextItem
    in_btn: wdgt.QGraphicsRectItem | None
    out_btn: wdgt.QGraphicsRectItem | None
    config_btn: wdgt.QGraphicsRectItem
    state_btn: wdgt.QGraphicsRectItem
    remove_btn: wdgt.QGraphicsRectItem
    ii_dialog: wdgt.QGraphicsProxyWidget

    interactive_inputs: dict[str, ii_widget_p] | None = dtcl.field(
        init=False, default=None
    )
    position_has_changed: bool = dtcl.field(init=False, default=False)

    def __post_init__(self) -> None:
        """"""
        # If using: self.setRect(QRectF(0, 0, NODE_WIDTH_TOTAL, NODE_HEIGHT_TOTAL)),
        # Python complains about super-init not having been called.
        wdgt.QGraphicsRectItem.__init__(
            self, QRectF(0, 0, NODE_WIDTH_TOTAL, NODE_HEIGHT_TOTAL)
        )

        for item in (
            self.label,
            self.in_btn,
            self.out_btn,
            self.config_btn,
            self.state_btn,
            self.remove_btn,
        ):
            if item is not None:
                item.setParentItem(self)

        self.setFlag(wdgt.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.setFlag(wdgt.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        self.setFlag(wdgt.QGraphicsItem.GraphicsItemFlag.ItemClipsChildrenToShape)
        self.setFlag(wdgt.QGraphicsItem.GraphicsItemFlag.ItemSendsGeometryChanges)
        self.setBrush(NODE_BRUSH_RESTING)
        self.setZValue(2)

        self.config_btn.setToolTip(self.details)

        self.setSelected(True)

    @classmethod
    def NewForFunctional(cls, functional: functional_t, /) -> node_t:
        """"""
        label = wdgt.QGraphicsTextItem()
        label.setHtml(functional.unique_name)
        label.setPos(BUTTON_WIDTH, 0)
        label.setTextWidth(NODE_WIDTH_TOTAL - 2 * BUTTON_WIDTH)
        # Causes a crash!
        # label.setTextInteractionFlags(constant_e.ItemSelectionMode.TextSelectableByMouse)

        if functional.description.n_inputs > 0:
            in_btn = wdgt.QGraphicsRectItem(
                QRectF(0, 0, WIDTH_OF_LATERAL_BUTTONS, HEIGHT_OF_LATERAL_BUTTONS)
            )
            in_btn.setBrush(INOUT_BRUSH_INACTIVE)
        else:
            in_btn = None

        if functional.description.n_outputs > 0:
            out_btn = wdgt.QGraphicsRectItem(
                QRectF(
                    NODE_WIDTH_TOTAL - WIDTH_OF_LATERAL_BUTTONS,
                    0,
                    WIDTH_OF_LATERAL_BUTTONS,
                    HEIGHT_OF_LATERAL_BUTTONS,
                )
            )
            out_btn.setBrush(INOUT_BRUSH_INACTIVE)
        else:
            out_btn = None

        config_btn_width = int(HORIZONTAL_FREE_SPACE / 2.5)
        config_btn = wdgt.QGraphicsRectItem(
            QRectF(
                WIDTH_OF_LATERAL_BUTTONS,
                TOP_OF_BOTTOM_BUTTONS,
                config_btn_width,
                HEIGHT_OF_BOTTOM_BUTTONS,
            )
        )
        config_btn.setBrush(BUTTON_BRUSH_CONFIG)

        state_btn = wdgt.QGraphicsRectItem(
            QRectF(
                WIDTH_OF_LATERAL_BUTTONS + config_btn_width,
                TOP_OF_BOTTOM_BUTTONS,
                config_btn_width,
                HEIGHT_OF_BOTTOM_BUTTONS,
            )
        )
        state_btn.setToolTip(NEEDS_RUNNING)
        state_btn.setBrush(BUTTON_BRUSH_STATE_TODO)

        remove_btn = wdgt.QGraphicsRectItem(
            QRectF(
                WIDTH_OF_LATERAL_BUTTONS + 2 * config_btn_width,
                TOP_OF_BOTTOM_BUTTONS,
                HORIZONTAL_FREE_SPACE - 2 * config_btn_width,
                HEIGHT_OF_BOTTOM_BUTTONS,
            )
        )
        remove_btn.setBrush(BUTTON_BRUSH_REMOVE)

        ii_dialog = wdgt.QGraphicsProxyWidget()
        ii_dialog.setZValue(2)

        return cls(
            functional=functional,
            label=label,
            in_btn=in_btn,
            out_btn=out_btn,
            config_btn=config_btn,
            state_btn=state_btn,
            remove_btn=remove_btn,
            ii_dialog=ii_dialog,
        )

    def AlignOnGrid(self) -> None:
        """"""
        position_x, position_y = (
            round(self.x() / NODE_WIDTH_TOTAL) * NODE_WIDTH_TOTAL,
            round(self.y() / NODE_HEIGHT_TOTAL) * NODE_HEIGHT_TOTAL,
        )
        self.setPos(position_x, position_y)

    @property
    def input_anchor_coordinates(self) -> QPointF:
        """"""
        return self._SocketCoordinates(True)

    @property
    def output_anchor_coordinates(self) -> QPointF:
        """"""
        return self._SocketCoordinates(False)

    def _SocketCoordinates(self, endpoint_is_input: bool, /) -> QPointF:
        """"""
        output = self.scenePos()
        output.setY(output.y() + int(0.5 * self.boundingRect().height()))

        if not endpoint_is_input:
            output.setX(output.x() + self.boundingRect().width())

        return output

    @property
    def details(self) -> str:
        """"""
        description = self.functional.description

        output = [f"Function: {description.module.__name__}.{description.actual.name}"]

        if description.n_inputs > 0:
            output.append("Input(s):")
            for name, input_ in description.inputs.items():
                if input_.has_default:
                    default = f" = {input_.default_value}"
                else:
                    default = ""
                output.append(f"    {name}:{input_.type.template_as_str}{default}")
        else:
            output.append("No Inputs")

        if description.n_outputs > 0:
            output.append("Output(s):")
            for name, stripe in description.outputs.items():
                output.append(f"    {name}:{stripe.template_as_str}")
        else:
            output.append("No Outputs")

        return "\n".join(output)

    def ToggleIIDialog(self) -> None:
        """
        IIDialog placement could be handled automatically with graphics anchors. Keeping manual management for the
        moment.
        """
        if self.interactive_inputs is not None:
            if self.ii_dialog.isVisible():
                self.ii_dialog.hide()
            else:
                self.ii_dialog.setPos(self.x(), self.y() + NODE_HEIGHT_TOTAL)
                self.ii_dialog.show()
            return

        interactive_inputs = {}
        n_widgets = 0
        layout = wdgt.QGridLayout()
        for i_idx, (name, record) in enumerate(
            self.functional.description.inputs.items()
        ):
            if record.assignment is assignment_e.full:
                type_wgt, value_wgt = TypeAndValueWidgetsForType(
                    record.type, SCREEN_BACKEND
                )
                interactive_inputs[name] = value_wgt
                n_widgets += 1

                layout.addWidget(wdgt.QLabel(name), i_idx, 0, 1, 1)
                layout.addWidget(type_wgt, i_idx, 1, 1, 1)
                layout.addWidget(value_wgt.library_wgt, i_idx, 2, 1, 1)

                if isinstance(value_wgt.library_wgt, wdgt.QStackedWidget):
                    widgets = (_elm for _elm in value_wgt.values)
                else:
                    widgets = (value_wgt,)
                for widget in widgets:
                    widget.SetAcknowledgeValueChangeFunction(self.functional.Invalidate)

        if n_widgets > 0:
            self.interactive_inputs = interactive_inputs

            widget = wdgt.QWidget()
            widget.setLayout(layout)
            widget.setStyleSheet(f"background-color: {color_e.deepskyblue.name()};")

            self.ii_dialog.setWidget(widget)
            self.ii_dialog.setPos(self.x(), self.y() + NODE_HEIGHT_TOTAL)

    def SetIIValue(self, input_name: str, value: h.Any, /) -> None:
        """"""
        if self.interactive_inputs is None:
            self.ToggleIIDialog()

        stripe = self.functional.description.inputs[input_name].type
        self.interactive_inputs[input_name].Assign(value, stripe)

    def IIValue(
        self, input_name: str | h.Sequence[str] | None = None, /
    ) -> h.Any | tuple[h.Any, ...] | dict[str, h.Any] | value_not_set_t:
        """"""
        if (interactive_inputs := self.interactive_inputs) is None:
            if input_name is None:
                return {}
            if isinstance(input_name, str):
                return VALUE_NOT_SET
            return ()

        output = {}

        functional = self.functional

        if input_name is None:
            input_names = functional.inputs
            stripe = dict
        elif isinstance(input_name, str):
            input_names = (input_name,)
            stripe = int
        else:
            input_names = input_name
            stripe = tuple

        for input_name in input_names:
            if (not functional.inputs[input_name].is_linked) and (
                input_name in interactive_inputs
            ):
                value_as_str = interactive_inputs[input_name].Text()
                expected_type = functional.description.inputs[input_name].type
                value, issues = expected_type.InterpretedValueOf(value_as_str)
                if issues.__len__() > 0:
                    value = invalid_ii_value_t(issues)
                    LOGGER.error("\n".join(issues))
            else:
                value = VALUE_NOT_SET
            output[input_name] = value

        if stripe is dict:
            return output
        if stripe is tuple:
            return tuple(output[_elm] for _elm in input_names)
        return output[input_names[0]]

    def itemChange(
        self, change: wdgt.QGraphicsItem.GraphicsItemChange, data: h.Any, /
    ) -> h.Any:
        """"""
        if change is wdgt.QGraphicsItem.GraphicsItemChange.ItemSelectedHasChanged:
            if data:
                self.setBrush(NODE_BRUSH_SELECTED)
            else:
                self.setBrush(NODE_BRUSH_RESTING)
        elif change is wdgt.QGraphicsItem.GraphicsItemChange.ItemPositionHasChanged:
            if self.ii_dialog.isVisible():
                self.ii_dialog.setPos(self.x(), self.y() + NODE_HEIGHT_TOTAL)
            self.position_has_changed = True

        return wdgt.QGraphicsRectItem.itemChange(self, change, data)
