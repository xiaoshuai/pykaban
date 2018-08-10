python setup.py sdist build
python setup.py sdist upload
python setup.py bdist_wheel --universal
python setup.py sdist upload
python setup.py bdist_wheel upload
rm -rf pykaban.egg-info dist build