activate_this = '/var/www/firstapp/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, "/var/www/firstapp")
from helloworld import app as application
