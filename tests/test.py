import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from export import export_user_suite

# export_user_suite("suite", "EN")
export_user_suite("suite", "JP")