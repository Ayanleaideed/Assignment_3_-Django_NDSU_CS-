# Assignment_3_-Django_NDSU_CS-

# Course Project

## Description
This Django project displays a web page with a list of courses fetched from the SQLite database. Each course is displayed on its card with a "Read More" link displayed as a button. When the user clicks on this button, they are navigated to a different view which displays additional information about the course using Bootstrap Cards.

## Requirements
1. The project should have a Django app called `courses`.
2. Create a Model called `Course` in the `courses` app with the following attributes:
   - Course id
   - Course title
   - Course description
   - Credits
   - Instructor
   - Start Date
3. Apply migrations to translate the model to a database in SQLite.
4. Using the admin interface, create at least 5 different course objects.
5. Define two views in the `courses` app:
   - `courses_view` that displays all the courses ordered by course title in `index.html`.
   - `course_detail` that displays additional details of the course in `course_detail.html`.
     - The `course_detail` view function will take two arguments: `request` and `pk`, where `pk` is the primary key of the course.

## Usage
1. Install Django and other dependencies:

pip install -r requirements.txt


2. Apply migrations:
  .python manage.py makemigrations
  .python manage.py migrate

3. Create superuser for admin access:
  .python manage.py createsuperuser

4. Run the development server:
  .python manage.py runserver


5. Navigate to the admin interface (`/admin`) to create course objects.

6. Access the courses at the following URLs:
- All courses: `/courses/`
- Course details: `/courses/<course_id>/`

## Screenshots


## Credits
This project was created by [Ayanle].
