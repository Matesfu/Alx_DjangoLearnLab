# Social Media API

A professional and robust RESTful API built with Django and Django REST Framework, designed to power modern social media applications. This project focuses on secure user authentication, interactive content sharing, and scalable architecture.

## 🚀 Features

### User Accounts & Authentication
- **Custom User Model**: Enhanced user profiles with bio, profile pictures, and follower/following relationships.
- **Token-based Authentication**: Secure user registration and login using Django REST Framework's `TokenAuthentication`.
- **Profile Management**: Detailed user profiles with follower and following counts.

### Posts & Interactions
- **Post Management**: Create, read, update, and delete posts with ease.
- **Comment System**: Interactive commenting on posts with nested visibility.
- **Custom Permissions**: Secure access control ensuring only owners can modify their content (`IsOwnerOrReadOnly`).
- **Advanced Filtering**: Full-text search on post titles and content.
- **Smart Pagination**: Paginated results for improved performance and user experience.

## 🛠️ Technology Stack

- **Framework**: [Django](https://www.djangoproject.com/)
- **Toolkit**: [Django REST Framework](https://www.django-rest-framework.org/)
- **Filtering**: [django-filter](https://django-filter.readthedocs.io/)
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
python manage.py makemigrations accounts posts
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

### Posts App (`/api/`)

| Endpoint | Method | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `posts/` | GET/POST | List all posts (paginated/searchable) or create a new post. | Yes |
| `posts/{id}/` | GET/PUT/PATCH/DELETE | Retrieve, update, or delete a specific post (owner only). | Yes |
| `comments/` | GET/POST | List all comments or create a new comment. | Yes |
| `comments/{id}/` | GET/PUT/PATCH/DELETE | Retrieve, update, or delete a specific comment (owner only). | Yes |

## 🧪 Testing

To run the automated tests, execute the following command:
```bash
python manage.py test accounts posts
```

---
*Built as part of the ALX Backend curriculum.*
