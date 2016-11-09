
sudo pip install virtualenv

mkdir python
cd python/
virtualenv venv

source venv/bin/activate

pip install numpy scipy sympy pandas nose ipython jupyter matplotlib seaborn
pip install sklearn

# jupyter notebook
# proceed in notebook

deactivate

# See also venv/bin/frameworkpython
# to make matplotlib work from Terminal in virtualenv
