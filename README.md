This is a sample app, i built for my learning
# Flask Student Management App

A modular Flask web application for student management, featuring:
- User login/logout
- Flash messaging
- File upload
- Contact form (with WTForms)
- SQLAlchemy database (SQLite)
- Modern AJAX demo
- Docker support

## Project Structure
```
project/
├── app/                # (if modularized)
├── templates/
├── static/
├── main.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

## Local Setup
1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
2. **Run the app:**
   ```sh
   python main.py
   ```
3. **Visit:**
   - Home: http://localhost:5000/
   - AJAX Demo: http://localhost:5000/ajax-demo

## Docker Usage
1. **Build the image:**
   ```sh
   docker build -t flaskapp:v1 .
   ```
2. **Run the container:**
   ```sh
   docker run -p 5000:5000 flaskapp:v1
   ```
3. **Visit:**
   - http://localhost:5000/

## Configuration
- All configuration is in `main.py` (or `config.py` if refactored).
- Update mail, secret key, and database URI as needed.

## Features
- Modular Flask routes
- WTForms for form validation
- SQLAlchemy ORM
- Flash messages
- File upload
- Flask-Mail integration
- Modern AJAX with fetch
- Dockerized for easy deployment

## Notes
- For production, use a production-ready WSGI server (e.g., gunicorn).
- Update secrets and credentials before deploying.

---

Feel free to extend this app with more features or blueprints as needed!
