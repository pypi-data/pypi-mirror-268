"""
The module defines the :py:class:`RustIndex` class which is the base class for the
indices generated for Rust objects. The class is inherited by the specific index
classes for each Rust object type.
"""

from abc import abstractmethod
from collections import defaultdict
from typing import Iterable

# noinspection PyProtectedMember
from sphinx.locale import _  # pylint:disable=protected-access
from sphinx.domains import Index, IndexEntry

from sphinxcontrib_rust.items import RustItem, RustItemType


class RustIndex(Index):
    """Abstract class to implement the various Sphinx indices"""

    @property
    @abstractmethod
    def rust_obj_type(self) -> RustItemType:
        """The Rust object type for the index"""
        raise NotImplementedError

    def generate(
        self, docnames: Iterable[str] | None = None
    ) -> tuple[list[tuple[str, list[IndexEntry]]], bool]:
        """Generate the index content for a list of items of the same type

        Args:
            :items: The items to include in the index.
            :subtype: The sub-entry related type. One of
                0 - A normal entry
                1 - A entry with subtypes.
                2 - A sub-entry

        Returns:
            A list of ``(key, list[IndexEntry])`` tuples that can be used as the
            content for generating the index.
        """
        data: dict[RustItemType, list[RustItem]]

        content = defaultdict(list)
        data = self.domain.data
        for item in data[self.rust_obj_type]:
            if item.docname in (docnames or [item.docname]):
                content[item.dispname[0]].append(
                    (
                        item.dispname,
                        item.entry_type.value,
                        item.docname,
                        item.anchor,
                        item.docname,
                        item.qualifier,
                        item.type_.value,
                    )
                )
        return sorted(content.items()), True


class CrateIndex(RustIndex):
    """Index of the Rust crates in the project"""

    # pylint: disable=too-few-public-methods

    name = "crates"
    localname = _("Rust Crates")
    shortname = _("Crates")

    @property
    def rust_obj_type(self):
        return RustItemType.CRATE


class ModuleIndex(RustIndex):
    """Index of the Rust modules in the project"""

    # pylint: disable=too-few-public-methods

    name = "modules"
    localname = _("Rust Modules")
    shortname = _("Modules")

    @property
    def rust_obj_type(self):
        return RustItemType.MODULE


class StructIndex(RustIndex):
    """Index of the Rust structs in the project"""

    # pylint: disable=too-few-public-methods

    name = "structs"
    localname = _("Rust Structs")
    shortname = _("Structs")

    @property
    def rust_obj_type(self):
        return RustItemType.STRUCT


class TraitIndex(RustIndex):
    """Index of the Rust traits in the project"""

    # pylint: disable=too-few-public-methods

    name = "traits"
    localname = _("Rust Traits")
    shortname = _("Traits")

    @property
    def rust_obj_type(self):
        return RustItemType.TRAIT


class EnumIndex(RustIndex):
    """Index of the Rust enums in the project"""

    # pylint: disable=too-few-public-methods

    name = "enums"
    localname = _("Rust Enums")
    shortname = _("Enums")

    @property
    def rust_obj_type(self):
        return RustItemType.ENUM


class FunctionIndex(RustIndex):
    """Index of the Rust functions in the project"""

    # pylint: disable=too-few-public-methods

    name = "functions"
    localname = _("Rust Functions")
    shortname = _("Functions")

    @property
    def rust_obj_type(self):
        return RustItemType.FUNCTION


class VariableIndex(RustIndex):
    """Index of the Rust variables in the project"""

    # pylint: disable=too-few-public-methods

    name = "variables"
    localname = _("Rust Variables")
    shortname = _("Variables")

    @property
    def rust_obj_type(self):
        return RustItemType.VARIABLE


class TypeIndex(RustIndex):
    """Index of the Rust types in the project"""

    # pylint: disable=too-few-public-methods

    name = "types"
    localname = _("Rust Types")
    shortname = _("Types")

    @property
    def rust_obj_type(self):
        return RustItemType.TYPE
