
# Install Python 3.6, if necessary 
# as specified in https://gist.github.com/niranjv/f80fc1f488afc49845e2ff3d5df7f83b

# Install sqlite, if necessary, to prevent errors while running jupyter notebook
# sudo yum install sqlite-devel

# clone this git repository
git clone https://github.com/niranjv/ml-tools-notes.git
cd ml-tools-notes/
git config --local user.name "<NAME>"
git config --local user.email "<EMAIL>"


# Install virtualenv
python3 -m venv ./venv
source venv/bin/activate


# Install pydata modules
pip install numpy
pip install scipy
pip install pandas

pip install sklearn
pip install patsy
pip install statsmodels

pip install nose

pip install ipython
pip install jupyter

pip install matplotlib
pip install seaborn


# Run `jupyter notebook`
# proceed in notebook

deactivate
