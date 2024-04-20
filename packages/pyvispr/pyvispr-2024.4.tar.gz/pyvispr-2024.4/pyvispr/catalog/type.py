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

from pyvispr.config.path import CATALOG_FOLDER
from pyvispr.flow.descriptive.node import node_t


@dtcl.dataclass(slots=True, repr=False, eq=False)
class catalog_t(list[node_t]):
    def __post_init__(self) -> None:
        """"""
        self.extend(map(node_t.NewForPath, CATALOG_FOLDER.rglob("*.py")))

    @property
    def node_names(self) -> tuple[str, ...]:
        return tuple(_elm.name for _elm in self)

    def NodeDescription(self, node_name: str, /) -> node_t:
        """"""
        for node in self:
            if node.name == node_name:
                return node

        raise ValueError(f"No node with name: {node_name}")
