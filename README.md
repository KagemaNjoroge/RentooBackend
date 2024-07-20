# RentooPMS

This repository contains the source code for RentooPMS, a Property Management System, backend API.

Tech Stack:

- Django
- Django Rest Framework
- PostgreSQL
- Firebase

The client is built using Flutter and can be found [here](https://github.com/KagemaNjoroge/RentooClient).

## Installation

1. Clone the repository

```bash
git clone https://github.com/KagemaNjoroge/RentooBackend.git && cd RentooBackend
```

2. Create a virtual environment

(a) Unix

```bash
python3 -m venv venv && source venv/bin/activate
```

(b) Windows

```bash
python -m venv venv && venv\Scripts\activate
```

3. Install the dependencies

```bash
pip install -r requirements.txt
```

4. Run database migrations

```bash
python manage.py migrate
```

5. Create a superuser

```bash
python manage.py createsuperuser
```

6. Run the development server

```bash
python manage.py runserver
```

7. Browse API docs at `http://localhost:8000/swagger/`
8. Play around with the API

## License

This project is licensed under the MIT License.

Brought to you with :heart: by [Kagema Njoroge](https://njoroge.tomorrow.co.ke)
