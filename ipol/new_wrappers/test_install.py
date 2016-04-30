import sys
import os

sys.path=[os.path.join(os.path.dirname(__file__),'../..')]+sys.path # make sure the  local version ipol is launched
sys.path.append(os.path.join(os.path.dirname(__file__),'../../ipol'))  # make sure the tools is available to the install script in the new binding folder

from ipol.new_wrappers import _install_all
_install_all()

