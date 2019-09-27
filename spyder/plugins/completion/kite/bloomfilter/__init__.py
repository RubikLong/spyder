# -*- coding: utf-8 -*-

# Copyright © Spyder Project Contributors
# Licensed under the terms of the MIT License
# (see spyder/__init__.py for details)

import os

from spyder.utils.external.pyqt_bloomfilter.pybloom_pyqt import BloomFilter


class KiteBloomFilter:
    """
    KiteBloomFilter managese access to the bloomfilter data, namely
    to tell if Kite would provide completions for a given path.
    """
    _filter = None

    @classmethod
    def is_valid_path(cls, path):
        """
        :param path: string representing a symbol path
        :return: true if the given path is known to kite,
                 i.e. if kite would most likely provide completions
        """
        if cls._filter is None:
            data_path = os.path.join(os.path.dirname(__file__), "kite.bloom")
            cls._filter = BloomFilter.fromfile(data_path)
        return path in cls._filter
