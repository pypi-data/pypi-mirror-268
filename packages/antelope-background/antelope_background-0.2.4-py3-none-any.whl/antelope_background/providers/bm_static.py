"""
LcArchive subclass that supports rich background computations by providing a FlatBackground implementation.
"""

import os
import time
from abc import ABC

from antelope_core.archives import LcArchive, InterfaceError
from ..background.flat_background import FlatBackground, SUPPORTED_FILETYPES, ORDERING_SUFFIX
from ..background.implementation import TarjanBackgroundImplementation, TarjanConfigureImplementation
from .check_terms import termination_test


def _ref(obj):
    if hasattr(obj, 'external_ref'):
        return obj.external_ref
    return str(obj)


class TarjanBackground(LcArchive, ABC):

    def __init__(self, source, save_after=False, **kwargs):
        self._save_after = save_after
        self._prefer = dict()
        if source.endswith(ORDERING_SUFFIX):
            source = source[:-len(ORDERING_SUFFIX)]  # prevent us from trying to instantiate from the ordering file

        filetype = os.path.splitext(source)[1]
        if filetype not in SUPPORTED_FILETYPES:
            raise ValueError('Unsupported filetype %s' % filetype)

        '''
        if not source.endswith(self._filetype):
            source += self._filetype
        '''

        super(TarjanBackground, self).__init__(source, **kwargs)

        if os.path.exists(source):  # flat background already stored
            self._flat = FlatBackground.from_file(source)
        else:
            self._flat = None

    def prefer(self, flow, process):
        self._prefer[flow] = process

    def test_archive(self, query, strict=True):
        return termination_test(query, self._prefer, strict=strict)

    def make_interface(self, iface, privacy=None):
        if iface == 'background':
            return TarjanBackgroundImplementation(self)
        elif iface == 'configure':
            return TarjanConfigureImplementation(self)
        else:
            raise InterfaceError(iface)

    def create_flat_background(self, index, save_after=None, prefer=None, **kwargs):
        """
        Create an ordered background, save it, and instantiate it as a flat background
        :param index: index interface to use for the engine
        :param save_after: trigger save-after (note: does not override init value)
        :return:
        """
        if self._flat is None:
            if prefer is None:
                prefer = self._prefer
            print('Creating flat background')
            start = time.time()
            self._flat = FlatBackground.from_index(index, prefer=prefer, **kwargs)
            self._add_name(index.origin, self.source, rewrite=True)
            print('Completed in %.3g sec' % (time.time() - start))
            if save_after or self._save_after:
                self.write_to_file()  # otherwise, the user / catalog must explicitly request it
        return self._flat

    def reset(self):
        self._flat = None

    def write_to_file(self, filename=None, gzip=False, complete=True, **kwargs):
        if filename is None:
            filename = self.source
        self._flat.write_to_file(filename, complete=complete, **kwargs)
