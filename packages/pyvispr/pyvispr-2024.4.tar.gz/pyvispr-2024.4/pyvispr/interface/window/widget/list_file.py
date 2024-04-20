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
from pathlib import Path as path_t

from pyvispr.interface.window.widget.list import list_wgt_t


@dtcl.dataclass(slots=True, repr=False, eq=False)
class file_list_wgt_t(list_wgt_t):
    base_folder: path_t | None = None
    recursive_mode: bool = False
    files: dict[str, path_t] = dtcl.field(init=False, default_factory=dict)

    def ActualReload(self) -> None:
        """"""
        if self.base_folder is None:
            self.AddDisabledItem("No Python Files")
            return

        if self.recursive_mode:
            FileIterator = self.base_folder.rglob
        else:
            FileIterator = self.base_folder.glob
        files = tuple(_elm for _elm in FileIterator("*.py") if _elm.is_file())
        if files.__len__() == 0:
            self.AddDisabledItem("No Python Files Found")
            return

        for file_ in files:
            stem = file_.stem
            self.addItem(stem)
            self.files[stem] = file_
