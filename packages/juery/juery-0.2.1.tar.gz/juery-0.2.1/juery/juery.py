from typing import Dict
from .payload import Payload
from .special import Special
import re


def traverse(dictionary: Dict):
    stack = [([], dictionary)]

    while len(stack) > 0:
        rootpath, context = stack.pop()

        def do(key, value):
            path = [*rootpath, str(key)]

            if isinstance(value, dict) or isinstance(value, list):
                stack.append((path, value))  # type: ignore

            return Payload(path=path, key=key, value=value)

        if isinstance(context, dict):
            for key in context:
                yield do(key, context.get(key))

        elif isinstance(context, list):
            for key in range(0, len(context)):
                yield do(key, context[key])

        else:
            break


def juery(dictionary, *keys):
    """
    JSON Query.

    [Syntax]

    ^ = Direct Descendant; ('parent', '^direct_descendant', ...)

    \* = Regular Expression; ('parent', '*hello_.+', ...)
    """
    if dictionary != None:
        for payload in traverse(dictionary):
            if len(keys) > len(payload.path):
                continue

            index = 0

            for i in range(0, len(payload.path)):
                if index >= len(keys):
                    # Comparator terminated before
                    # finishing the path.
                    # Exclude this payload.
                    index = -1
                    break

                special = Special.new(str(keys[index]))
                value = payload.path[i]

                ok = False

                if special.regular_expression:
                    special = re.search(
                        special.value,
                        value,
                        re.I,
                    )
                    ok = special != None

                elif special.value.lower() == value.lower():
                    ok = True

                if ok:
                    index += 1

                elif special.direct_descendant:
                    # Not a direct descendant.
                    index = -1
                    break

            if index == len(keys):
                yield payload


def juery_one(dictionary, *keys, default_value=None):
    if dictionary == None:
        return default_value

    for payload in juery(dictionary, *keys):
        return payload

    return default_value


def juery_one_value(dictionary, *keys, default_value=None):
    if dictionary == None:
        return default_value

    for payload in juery(dictionary, *keys):
        return payload.value

    return default_value
