"""
Module initialisation for GemPy
Created on 21/10/2016

@author: Miguel de la Varga
"""
import sys
import os

import warnings

try:
    import faulthandler
    faulthandler.enable()
except Exception as e:  # pragma: no cover
    warnings.warn('Unable to enable faulthandler:\n%s' % str(e))


PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

# =================== Core ===================
from .core.model import Project, ImplicitCoKriging
from .core.data import AdditionalData, Options, KrigingParameters
from .core.data_modules.stack import Faults, Series
from .core.structure import Structure

from .core.grid import Grid
from .core.surfaces import Surfaces
from .core.data_modules.scaling_system import ScalingSystem
from .core.data_modules.orientations import Orientations
from .core.data_modules.surface_points import SurfacePoints
from .core.solution import Solution

# =================== API ===================
from .gempy_api import *
from .api_modules.getters import *
from .api_modules.setters import *
from .api_modules.io import *

# =================== Addons ===================
from .addons.gempy_to_rexfile import geomodel_to_rex

# =================== Plotting ===================
import gempy_legacy.plot.plot_api as plot
from .plot.plot_api import plot_2d, plot_3d
from .plot import _plot as _plot

# Assert at least pyton 3.10
assert sys.version_info[0] >= 3 and sys.version_info[1] >= 10, "GemPy requires Python 3.10 or higher"

__version__ = '2.3.2'

if __name__ == '__main__':
    pass
