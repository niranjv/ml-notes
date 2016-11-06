
sudo pip install virtualenv

cd sklearn/
virtualenv venv

source venv/bin/activate

pip install numpy scipy matplotlib ipython jupyter pandas sympy nose
pip install sklearn

# jupyter notebook
# proceed in notebook

deactivate

# See also venv/bin/frameworkpython
# to make matplotlib work from Terminal in virtualenv
