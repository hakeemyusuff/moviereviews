# MovieReviews
This is a project I built along with the book "Django4 for the impatients" the MovieReviews is a Django-based web application that allows users to review movies. Users can create, update, and delete their reviews, as well as view reviews from other users.

## Features

- User authentication and authorization
- Create, update, and delete movie reviews
- View reviews from other users
- Search and filter reviews

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/moviereviews.git
    cd moviereviews
    ```

2. Install `pipenv` if you haven't already:
    ```sh
    pip install pipenv
    ```

3. Install dependencies:
    ```sh
    pipenv install --dev
    ```

4. Activate the virtual environment:
    ```sh
    pipenv shell
    ```

5. Run migrations:
    ```sh
    python manage.py migrate
    ```

6. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

7. Run the development server:
    ```sh
    python manage.py runserver
    ```

8. Open your web browser and go to `http://127.0.0.1:8000/` to access the application.

## Usage

- Register for an account or log in if you already have one.
- Create a new movie review by navigating to the "Add Review" page.
- Update or delete your reviews by navigating to the review detail page.
- View reviews from other users on the homepage.
- Use the search bar to find specific movies.

## Project Structure

- `moviereviews/`: Main project directory
- `account/`: Django app for handling authentication
- `news/`: Django app for handling news update

## What I Learned

- **Django Models**: How to define and interact with models.
- **Django Forms**: Handling forms, form validation, and saving form data.
- **Authentication**: Implementing user authentication with Django’s built-in tools.
- **CRUD Operations**: Creating, reading, updating, and deleting records in the database.
- **Search Functionality**: Implementing search functionality to filter database records.
- **Template Rendering**: Using Django’s templating system to dynamically render HTML pages.
- **Decorator Usage**: Utilizing Django decorators like `@login_required` to protect views.
- **Error Handling**: Implementing error handling in forms and views.
- **Static and Media Files**: Managing static and media files in a Django project.
