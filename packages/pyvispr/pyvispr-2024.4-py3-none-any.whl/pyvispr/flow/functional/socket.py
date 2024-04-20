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

from pyvispr.runtime.socket import VALUE_NOT_SET


@dtcl.dataclass(slots=True, repr=False, eq=False)
class _base_t:
    value: h.Any = VALUE_NOT_SET

    @property
    def has_value(self) -> bool:
        """"""
        return self.value is not VALUE_NOT_SET

    def Invalidate(self) -> None:
        """"""
        self.value = VALUE_NOT_SET


@dtcl.dataclass(slots=True, repr=False, eq=False)
class input_t(_base_t):
    """
    Used only for script output (no need to save).
    """

    is_linked: bool = False
    source_output_name: str | None = None

    def Connect(self, output_unique_name: str, output_value: h.Any, /) -> None:
        """"""
        self.is_linked = True
        self.source_output_name = output_unique_name
        self.value = output_value

    def Disconnect(self) -> None:
        """"""
        self.is_linked = False
        self.source_output_name = None
        self.value = VALUE_NOT_SET


output_t = _base_t
