# (C) Copyright 2023 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import logging
import re

LOG = logging.getLogger(__name__)


class Remapping:
    def __init__(self, remapping):
        self.remapping = {}

        for k, v in remapping.items():
            m = re.split(r"\{([^}]*)\}", v)
            self.remapping[k] = m

    def __call__(self, func):
        if self.remapping is None or not self.remapping:
            return func

        class CustomJoiner:
            def format_name(self, x, **kwargs):
                return func(x, **kwargs)

            def format_string(self, x):
                return str(x)

            def join(self, args):
                return "".join(str(x) for x in args)

        joiner = CustomJoiner()

        def wrapped(name, **kwargs):
            return self.substitute(name, joiner, **kwargs)

        return wrapped

    def substitute(self, name, joiner, **kwargs):
        if name in self.remapping:
            lst = []
            for i, bit in enumerate(self.remapping[name]):
                if i % 2:
                    p = joiner.format_name(bit, **kwargs)
                    if p is not None:
                        lst.append(p)
                    else:
                        lst = lst[:-1]
                else:
                    lst.append(joiner.format_string(bit))
            return joiner.join(lst)
        return joiner.format_name(name, **kwargs)

    def as_dict(self):
        return self.remapping


def build_remapping(mapping):
    if mapping is None:
        return Remapping({})

    if isinstance(mapping, dict):
        return Remapping(mapping)

    return mapping


def normalize_order_by(*args, **kwargs):
    _kwargs = {}
    for a in args:
        if a is None:
            continue
        if isinstance(a, dict):
            _kwargs.update(a)
            continue
        if isinstance(a, str):
            _kwargs[a] = "ascending"
            continue
        if isinstance(a, (list, tuple)):
            if not all(isinstance(k, str) for k in a):
                _kwargs.update(normalize_order_by(*a))
            else:
                for k in a:
                    _kwargs[k] = "ascending"
            continue

        raise ValueError(f"Unsupported argument {a} of type {type(a)}")

    _kwargs.update(kwargs)

    for k, v in _kwargs.items():
        if not (
            v is None
            or callable(v)
            or isinstance(v, (list, tuple, set))
            or v in ["ascending", "descending"]
        ):
            raise ValueError(f"Unsupported order: {v} of type {type(v)} for key {k}")

    return _kwargs
