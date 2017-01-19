
# Installpip, virtualenv
wget https://bootstrap.pypa.io/get-pip.py # Install pip
sudo python get-pip.py
pip install --upgrade pip # Upgrade pip
sudo pip install virtualenv

mkdir ml-tools-notes
cd ml-tools-notes/

# Create virtualenv for pydata
virtualenv venv
source venv/bin/activate

# Install pydata modules
pip install numpy
pip install scipy
pip install sympy
pip install pandas

pip install sklearn
pip install patsy
pip install statsmodels

pip install nose

pip install ipython
pip install jupyter

pip install matplotlib
pip install seaborn


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

git init
git remote add origin https://github.com/niranjv/ml-tools-notes.git
git remote -v # verify remote
git fetch --all --prune

git config --local user.name "<NAME>"
git config --local user.email "<EMAIL>"

# jupyter notebook
# proceed in notebook

deactivate
