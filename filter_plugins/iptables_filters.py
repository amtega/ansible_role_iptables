# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from datetime import datetime
from random import randint, seed


def iptables_attrs_subset(d, attributes, ignore_missing=False):
    """Extract a list of attributes from a dict.

    Args:
        d: dict to get the attributes subset.
        attributes (list): name of the attributes to extract.
        ignore_missing (bool): ignore missing attributes.

    Returns:
        dict: containing only the specified attributes.
    """
    subset = dict()
    for attribute in attributes:
        if attribute in d:
            subset[attribute] = d[attribute]
        elif not ignore_missing:
            raise AttributeError("Attribute '%s' not found" % attribute)

    return subset


def iptables_unique(dicts, attributes, ignore_missing=False):
    """Return unique dicts considering only a set of attributes.

    Args:
        dicts (list of dicts): dicts to get the uniques.
        attributes (list): name of the attributes to consider.
        ignore_missing (bool): ignore missing attributes.

    Returns:
        list of dicts: dicts containing only the unique ones.
    """
    unique_subsets = []
    result = []
    for d in dicts:
        subset = iptables_attrs_subset(d, attributes, ignore_missing)

        if subset not in unique_subsets:
            unique_subsets.append(subset)
            result.append(d)

    return result


class FilterModule(object):
    """Ansible iptables filters."""

    def filters(self):
        return {
            'iptables_unique': iptables_unique
        }
