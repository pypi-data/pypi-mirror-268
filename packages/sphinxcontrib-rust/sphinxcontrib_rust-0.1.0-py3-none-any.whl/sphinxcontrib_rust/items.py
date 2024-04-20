"""
This module provides an enum for the various object types for the Rust domain.
The enum makes it easier to manage all the different object types. The module also
provides a data class :py:class:`RustObj` that encapsulates the details of each object.
"""

from dataclasses import dataclass
from enum import Enum, IntEnum
from typing import Iterator, Sequence
from sphinx.domains import ObjType

# noinspection PyProtectedMember
from sphinx.locale import _  # pylint:disable=protected-access


class RustItemType(Enum):
    """The various Rust objects"""

    # XXX: Python 3.11 has StrEnum that can be used here
    #      but that would limit the Python version supported.
    #      Once older versions are EOL, this can be used.

    CRATE = "crate"
    ENUM = "enum"
    FUNCTION = "function"
    IMPL = "impl"
    MACRO = "macro"
    MODULE = "module"
    STRUCT = "struct"
    TRAIT = "trait"
    TYPE = "type"
    VARIABLE = "variable"

    @classmethod
    def from_str(cls, value: str) -> "RustItemType":
        """Get the enum corresponding to the string value"""
        if value in ("fn", "func"):
            return RustItemType.FUNCTION
        if value == "var":
            return RustItemType.VARIABLE
        for e in RustItemType:
            if e.value == value:
                return e
        raise ValueError(f"{value} is not a known RustObjType value")

    def get_roles(self) -> Sequence[str]:
        """Get the Sphinx roles that can reference the object type"""
        return [
            self.value,
            *(
                {
                    RustItemType.FUNCTION: ["func", "fn"],
                    RustItemType.VARIABLE: ["var"],
                }.get(self, [])
            ),
        ]

    @staticmethod
    def iter_roles() -> Iterator[tuple[str, str]]:
        """Iterate over (type, role) tuples across all types"""
        for typ in RustItemType:
            for role in typ.get_roles():
                yield typ, role

    def get_sphinx_obj_type(self) -> ObjType:
        """Get the Sphinx ``ObjType`` instance for the object type"""
        return ObjType(_(self.value), *self.get_roles())

    @property
    def display_name(self) -> str:
        """Return the string to display for the item type.

        Returns ``fn`` for the ``FUNCTION`` item type and the value
        for all other item types.
        """
        return "fn" if self == RustItemType.FUNCTION else self.value


class SphinxIndexEntryType(IntEnum):
    """Various index types implemented by Sphinx

    See Also:
        https://www.sphinx-doc.org/en/master/extdev/domainapi.html#sphinx.domains.Index.generate
    """

    NORMAL = 0
    WITH_SUB_ENTRIES = 1
    SUB_ENTRY = 2


@dataclass(frozen=True)
class RustItem:
    """A dataclass for holding the details of a Sphinx object for Rust domain

    Attributes:
        :name: The name of the object.
        :dispname: The name of the object used in directives and references.
        :type_: The object type.
        :docname: The document the object is defined in. This is the generated
            reStructured Text document, not the source code.
        :qualifier: Qualifier for the description.
        :anchor: Anchor for the entry within the docname.
        :priority: The search priority for the object.
        :entry_type: The Sphinx index entry type for the object.
    """

    # pylint: disable=too-many-instance-attributes

    name: str
    dispname: str
    type_: RustItemType
    docname: str
    qualifier: str = ""
    anchor: str = ""
    priority: int = 0
    entry_type: SphinxIndexEntryType = SphinxIndexEntryType.NORMAL
