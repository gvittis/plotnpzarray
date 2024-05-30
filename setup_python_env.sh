python3 -m venv yourpythonenv
. yourpythonenv/bin/activate
export PYTHONPATH=/pathtoyourpythonenv/yourpythonenv/bin/python3.9:/pathtoyourpythonenv/yourpythonenv/lib/python3.9/site-packages:$PYTHONPATH
pip install --upgrade pip
pip install pandas
pip install dash
pip install kaleido
pip install -U scikit-image
