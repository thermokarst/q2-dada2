# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from ._denoise import denoise_single, denoise_paired
from ._plot import plot_qualities
from ._version import get_versions


__version__ = get_versions()['version']
del get_versions

__all__ = ['denoise_single', 'denoise_paired', 'plot_qualities']
