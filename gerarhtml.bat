

coverage run manage.py test
coverage html

start http://localhost:8000/
cd htmlcov
python -m http.server
cd ..