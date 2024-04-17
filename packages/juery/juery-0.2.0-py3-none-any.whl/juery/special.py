from typing import Any, List, NamedTuple


class Special(NamedTuple):
    direct_descendant: bool
    regular_expression: bool
    value: str

    @staticmethod
    def new(value: str):
        direct_descendant = False
        regular_expression = False

        for _ in range(2):
            if value.startswith("^"):
                direct_descendant = True

            elif value.startswith("*"):
                regular_expression = True

            else:
                break

            value = value[1:]

        return Special(
            direct_descendant=direct_descendant,
            regular_expression=regular_expression,
            value=value,
        )
