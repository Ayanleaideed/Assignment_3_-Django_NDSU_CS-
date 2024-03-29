from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Course
from .utils import dataset_to_hashmap
from datetime import datetime
import time


# Create your views here.
def courses_view(request):
  # call the process function
  courses = dataset_to_hashmap(Course)
  return render(request, 'course_view.html', {'courses': courses})


# Function to view more details about a Course
def course_detail(request, pk):
    try:
        start_time = time.time()  # Start time before retrieving course details
        # Retrieve the course with the specified pk
        courses = dataset_to_hashmap(Course, pk=pk, OneRecord=True)
        # Calculate the time taken
        end_time = time.time()
        duration = end_time - start_time
        # Display a success message with the course details and time taken
        messages.success(request, f'Course Details Was Requested Successfully. Time taken: {duration:.4f} Milliseconds/Seconds.')
        return render(request, 'course_detail.html', {'courses': courses})
    except Course.DoesNotExist:
        # Display a message if the course does not exist
        messages.error(request, f'No course found with ID: {pk}')
        return render(request, 'course_detail.html')



#Function to create new course
def create_course(request):
    if request.method == 'POST':
        course_code = request.POST.get('course_code', 'N/A')
        title = request.POST.get('title', 'Title')
        description = request.POST.get('description', None)
        credits = request.POST.get('credits', 3)
        instructor = request.POST.get('instructor', 'N/A')
        start_date_str = request.POST.get('start_date', '2024-09-01')
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        prerequisites = request.POST.get('prerequisites', '')

        # Create the new course object
        new_course = Course.objects.create(
            course_code=course_code,
            title=title,
            description=description,
            credits=credits,
            instructor=instructor,
            start_date=start_date,
            prerequisites=prerequisites
        )
        # save the object
        new_course.save()
        messages.success(request, 'Course created successfully')
        # Redirect the user to course_views page
        return redirect('courses_view')

    # Handle GET request if needed
    return render(request, 'create_course.html')


def edit_course(request, pk):
    try:
        # Retrieve the course with the specified pk
        course = Course.objects.get(pk=pk)

        if request.method == 'POST':
            # Update the course with the data submitted in the form
            course.title = request.POST.get('title', '')
            course.course_code = request.POST.get('course_code', 'N/A')
            course.description = request.POST.get('description', '')
            course.credits = int(request.POST.get('credits', ''))
            course.instructor = request.POST.get('instructor', '')
            course.start_date = request.POST.get('start_date', '')
            course.prerequisites = request.POST.get('prerequisites', '')
            course.save()
            messages.success(request, f'Course "{course.title}" has been successfully updated.')
            return redirect('courses_view')
        else:
            # Create a dictionary to store course details
            course_details = {
                'id': course.id,
                "course_code": course.course_code,
                'Title': course.title,
                'Description': course.description,
                'Credits': course.credits,
                'Instructor': course.instructor,
                'StartDate': course.start_date,
                'Prerequisites': course.prerequisites,
            }

        # Render the template with the course details
        return render(request, 'edit_course.html', {'course': course, 'course_details': course_details})

    except Course.DoesNotExist:
        messages.error(request, f"Course with ID {course_detail.get('Title')} does not exist.")
        return redirect('courses_view')



if __name__ == '__main__':
  debug=True
