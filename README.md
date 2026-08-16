# Restaurant Management System

A robust, full-featured Restaurant Management System backend built with Django and Django REST Framework. This API powers restaurant operations including user authentication, order processing, and table booking.

## Features

- **Authentication**: JWT-based authentication system.
- **Order Management**: Handle customer orders seamlessly.
- **Booking Management**: Table reservation system.
- **CORS Configured**: Ready for frontend integration.

## Tech Stack

- Python 3
- Django & Django REST Framework
- SQLite (Local) / PostgreSQL (Production ready via `dj-database-url`)
- Gunicorn & WhiteNoise (Production serving)

## Local Setup

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd restaurent_management/config
```

### 2. Set up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Variables
Copy the example environment file and update it with your settings:
```bash
cp .env.example .env
```

### 5. Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Run Development Server
```bash
python manage.py runserver
```

## Deployment Ready

This project is configured for easy deployment on platforms like Heroku or Render.

- **Procfile** included for standard WSGI deployment.
- **WhiteNoise** configured for static file serving.
- **python-dotenv** & **dj-database-url** for dynamic environment configuration.

## License

MIT
