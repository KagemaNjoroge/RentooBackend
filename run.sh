# activate venv
echo "Checking..."
python ./manage.py check
echo "Testing..."
python ./manage.py test
echo "Running..."
python ./manage.py runserver