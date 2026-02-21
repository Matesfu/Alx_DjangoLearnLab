# Social Media API

A professional and robust RESTful API built with Django and Django REST Framework, designed to power modern social media applications. This project focuses on secure user authentication, interactive content sharing, real-time engagement, and scalable architecture.

## 🚀 Features

### User Accounts & Social Networking
- **Custom User Model**: Enhanced user profiles with bio, profile pictures, and intuitive follow/unfollow relationships.
- **Following System**: Connect with other users through a robust following/followers mechanism.
- **Token-based Authentication**: Secure user registration and login using Django REST Framework's `TokenAuthentication`.
- **Profile Management**: Detailed user profiles with real-time follower and following counts.

### Posts & Interactions
- **Post Management**: Create, read, update, and delete posts with ease.
- **Personalized Feed**: A dedicated activity feed showing the latest posts from users you follow.
- **Like/Unlike System**: Interactive content engagement with built-in duplicate prevention.
- **Comment System**: Interactive commenting on posts with nested visibility.
- **Custom Permissions**: Secure access control ensuring only owners can modify their content (`IsOwnerOrReadOnly`).
- **Advanced Filtering**: Full-text search on post titles and content.
- **Smart Pagination**: Paginated results for improved performance and user experience.

### Real-time Engagement
- **Notification System**: Instant notifications for social actions like follows, likes, and comments.
- **Notification Center**: A dedicated endpoint for users to keep track of their interactions.

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
python manage.py makemigrations accounts posts notifications
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
| `follow/<int:user_id>/` | POST | Follow a specific user. | Yes |
| `unfollow/<int:user_id>/` | POST | Unfollow a specific user. | Yes |

### Posts App (`/api/`)

| Endpoint | Method | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `posts/` | GET/POST | List all posts (paginated/searchable) or create a new post. | Yes |
| `posts/{id}/` | GET/PUT/PATCH/DELETE | Retrieve, update, or delete a specific post (owner only). | Yes |
| `posts/{id}/like/` | POST | Like a specific post. | Yes |
| `posts/{id}/unlike/` | POST | Unlike a specific post. | Yes |
| `feed/` | GET | View a personalized activity feed from followed users. | Yes |
| `comments/` | GET/POST | List all comments or create a new comment. | Yes |
| `comments/{id}/` | GET/PUT/PATCH/DELETE | Retrieve, update, or delete a specific comment (owner only). | Yes |

### Notifications App (`/api/`)

| Endpoint | Method | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `notifications/` | GET | Retrieve a list of notifications for the authenticated user. | Yes |

## 🚀 Deployment

This project is configured for deployment on platforms like Heroku, AWS, or DigitalOcean.

### Production Environment Variables
Create a `.env` file in the root directory and configure the following:
- `DEBUG`: Set to `False`.
- `SECRET_KEY`: A secure random string.
- `ALLOWED_HOSTS`: A comma-separated list of your production domains.
- `DATABASE_URL`: Your production database connection string (e.g., PostgreSQL).

### Static Files
The project uses **WhiteNoise** to serve static files efficiently in production. Run the following before deploying:
```bash
python manage.py collectstatic
```

### Web Server
**Gunicorn** is included as the production WSGI server. The `Procfile` is already configured for easy deployment.

## 🧪 Testing

To run the automated tests, execute the following command:
```bash
python manage.py test accounts posts notifications
```

---

