import re
from typing import Dict, Final, Hashable, Iterator, List, Literal, Mapping, Set

from typing_extensions import override

from lazy_type_hint.data_type_tree.data_type_tree import DataTypeTree
from lazy_type_hint.data_type_tree.factory import data_type_tree_factory
from lazy_type_hint.data_type_tree.generic_type.generic_data_type_tree import GenericDataTypeTree
from lazy_type_hint.file_modifiers.yaml_file_modifier import YamlFileModifier


class MappingDataTypeTree(GenericDataTypeTree):
    children: Mapping[Hashable, DataTypeTree]
    hidden_keys_prefix: Final = YamlFileModifier.prefix

    # Iterable-protocol related
    _keys: Iterator[Hashable]

    @override
    def _instantiate_children(self, data: Mapping[Hashable, object]) -> Mapping[Hashable, DataTypeTree]:  # type: ignore
        children: Dict[Hashable, DataTypeTree] = {}

        for key, value in data.items():
            suffix = type(key).__name__ if not isinstance(key, str) else self._to_camel_case(key)
            if isinstance(key, str) and key.startswith(self.hidden_keys_prefix):
                continue
            child = data_type_tree_factory(
                data=value,
                name=f"{self.name}{suffix}",
                imports=self.imports,
                depth=self.depth + 1,
                strategies=self.strategies,
                parent=self,
            )
            if child in children.values():
                self._replace_old_children_by_new_one(child, children)
                children[key] = child
            else:
                children[key] = child
        return children

    def _replace_old_children_by_new_one(self, child: DataTypeTree, children: Dict[Hashable, DataTypeTree]) -> None:
        """
        Replaces old child nodes with a new one in the given dictionary of children.

        Only replaced those children that are equal to the given child. In addition, naming is updated to
        make them match.
        """
        name = f"{self.name}{type(child.data).__name__.capitalize()}"
        modified_name = name
        count = 2
        while modified_name in children.values():
            modified_name = f"{name}{count}"
            count += 1
        child.name = modified_name
        for inserted_key in children:
            if children[inserted_key] == child:
                children[inserted_key] = child

    def _get_str_top_node(self) -> str:
        return self._parse_dict(self.children)

    def _parse_dict(self, children: Mapping[Hashable, DataTypeTree]) -> str:
        """Get a string representation of the dictionary for this same top node.

        Examples:
            - Mapping[str, Union[float, str]]
            - Mapping[str, str]
        """
        container: Literal["dict", "TypedDict", "MappingProxyType", "Mapping"] = (
            "dict" if self.strategies.dict_strategy == "TypedDict" else self.strategies.dict_strategy
        )
        if self.holding_type.__name__ == "mappingproxy":
            container = "MappingProxyType"
            self.imports.add(container)
        else:
            self.imports.add(container)

        keys = self._get_types(iterable=children.keys(), remove_repeated=True)
        keys_str = self._format_types(keys)
        value_types = self.get_type_alias_children()

        container_ = "Dict" if container == "dict" else container
        return f"{self.name} = {container_}[{keys_str}, {value_types}]"

    @staticmethod
    def _to_camel_case(string: str) -> str:
        """Make it camel case and compatible with Python keywords."""
        # Remove any initial number within the string
        match = re.match(r"^\d+", string)
        if match:
            number = match.group()
            string = string[len(number) :]

        new_string = [""] * len(string)
        idx_to_remove: Set[int] = set()
        removed = False
        for idx, char in enumerate(string):
            if not char.isalpha() and not char.isnumeric():
                idx_to_remove.add(idx)
            if idx not in idx_to_remove:
                if removed is True:
                    new_string[idx] = string[idx].upper()
                    removed = False
                else:
                    new_string[idx] = string[idx]
            else:
                removed = True

        try:
            new_string[0] = new_string[0].upper()
        except IndexError:
            return string
        return "".join(new_string)

    @override
    def _get_hash(self) -> Hashable:
        hashes: List[object] = []
        for name, child in self.children.items():
            hashes.append(("mapping", hash(type(name)), child._get_hash()))
        return frozenset(hashes)
