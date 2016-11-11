
# To install & upgrade pip
# Install pip: https://pip.pypa.io/en/stable/installing/
# Upgrade pip: pip install --upgrade pip

sudo pip install virtualenv

mkdir python
cd python/
virtualenv venv

# ----------

# now add a file called venv/bin/frameworkpython to make matplotlib work from Terminal in virtualenv:
# for more info, see http://matplotlib.org/faq/virtualenv_faq.html#pythonhome-script

# #!/bin/bash

# # what real Python executable to use
# PYVER=2.7
# PATHTOPYTHON=/usr/bin/
# PYTHON=${PATHTOPYTHON}python${PYVER}

# # find the root of the virtualenv, it should be the parent of the dir this script is in
# ENV=`$PYTHON -c "import os; print(os.path.abspath(os.path.join(os.path.dirname(\"$0\"), '..')))"`

# # now run Python with the virtualenv set as Python's HOME
# export PYTHONHOME=$ENV
# exec $PYTHON "$@"

# ----------

source venv/bin/activate

pip install numpy scipy sympy pandas nose ipython jupyter matplotlib seaborn
pip install sklearn

# jupyter notebook
# proceed in notebook

deactivate
