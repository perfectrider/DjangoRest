Hello friends! This is my django rest test learning project.

The project describes a car ordering system.

---

To launch the project, for Linux OS:

1. Create virtual enviroment:

python -m venv djangoenv

2. To activate the virtual environment with the command:

source djangoenv/bin/activate 

3. The next step to install the dependencies from the requirements.txt file. To do this, you need to run the command:

pip install -r DRF/requirements.txt

4. Apply all migrations:

python3 DRF/manage.py migrate

5. To run the local server and test the project, you need run command:

python3 DRF/manage.py runserver
