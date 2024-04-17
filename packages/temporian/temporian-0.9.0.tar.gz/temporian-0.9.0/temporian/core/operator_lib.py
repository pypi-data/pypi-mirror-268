# Copyright 2021 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Registering mechanism for operator classes."""

from typing import Any, Dict, Type

from temporian.core.operators.base import Operator

_OPERATORS = {}


def register_operator(operator_class: Type[Operator]):
    """Registers an operator."""

    op_key = operator_class.operator_key()
    if op_key in _OPERATORS:
        raise ValueError("Operator already registered")
    _OPERATORS[op_key] = operator_class


def get_operator_class(key: str):
    """Gets an operator class from a registered key."""

    if key not in _OPERATORS:
        raise ValueError(
            f"Unknown operator '{key}'. "
            f"Available operators are: {list(_OPERATORS.keys())}."
        )
    return _OPERATORS[key]


def registered_operators() -> Dict[str, Any]:
    """Lists the registered operators."""

    return _OPERATORS


def _unregister_operator(operator_class: Type[Operator]):
    """(For test operators purposes only) Unregisters an operator."""
    op_key = operator_class.operator_key()
    if op_key in _OPERATORS:
        _OPERATORS.pop(op_key)
