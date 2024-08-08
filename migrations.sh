# activate venv
echo "Running makemigrations"
python ./manage.py makemigrations
echo "Migrating"
python ./manage.py migrate