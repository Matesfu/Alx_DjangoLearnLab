# Social Media API

A professional and robust RESTful API built with Django and Django REST Framework, designed to power modern social media applications. This project focuses on secure user authentication, profile management, and scalable architecture.

## 🚀 Features

- **Custom User Model**: Enhanced user profiles with bio, profile pictures, and follower/following relationships.
- **Token-based Authentication**: Secure user registration and login using Django REST Framework's `TokenAuthentication`.
- **Profile Management**: Detailed user profiles with follower and following counts.
- **RESTful API**: Clean and well-structured API endpoints for user-related operations.
- **Scalable Architecture**: Built with modularity and scalability in mind.

## 🛠️ Technology Stack

- **Framework**: [Django](https://www.djangoproject.com/)
- **Toolkit**: [Django REST Framework](https://www.django-rest-framework.org/)
- **Database**: SQLite (Development)
- **Language**: Python

## 📥 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Matesfu/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/social_media_api
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install django djangorestframework django-filter
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Start the development server
```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

## 📡 API Endpoints

### Accounts App (`/api/`)

| Endpoint | Method | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `register/` | POST | Register a new user and receive a token. | No |
| `login/` | POST | Login with credentials and receive a token. | No |
| `profile/` | GET/PATCH | Retrieve or update the authenticated user's profile. | Yes |

## 🧪 Testing

To run the automated tests, execute the following command:
```bash
python manage.py test accounts
```


