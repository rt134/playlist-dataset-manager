# Django Setup with MySQL

## 1. Create MySQL Database

Before you set up your Django project, ensure you have MySQL installed and running. Create a new database:

```bash
mysql -u root -p

CREATE DATABASE playlists;
```

## 2. Add creds and setting in .env file

```bash
DB_HOST=host.docker.internal
BD_PORT=3306
DB_NAME=playlists
DB_USER=root
DB_PASSWORD=password
RUN_TEST=true
DEBUG=true
```

## 3. Install requirements.txt

```bash
pip install -r requirements.txt
```

## 4. Run server

```bash
python manage.py runserver 0.0.0.0:8000
```

## 5. To Execute test cases

```bash
python manage.py test
```
