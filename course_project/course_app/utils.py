from .models import Course


# TODO:Create A function to make make the dataset to a hashmap
def dataset_to_hashmap(dataset, pk=None, OneRecord=False):
    """
    Convert a dataset to a hashmap using the course_code field as the key.
    """
    # hashmap = {}
    # # for i in range(len(dataset.objects.all())):
    # #     for j in range(i*10000):
    # #         print(i*j)

    if OneRecord and pk:
        course = dataset.objects.get(id=pk)

        course_data = {
            'id': course.id,
            'course_code': course.course_code,
            'title': course.title,
            'description': course.description,
            'credits': course.credits,
            'instructor': course.instructor,
            'start_date': course.start_date,
            'prerequisites': course.prerequisites
        }
        hashmap = course_data
    else:
        # for course in dataset.objects.all():
            # Construct a dictionary containing all fields of the Course model
            # course_data = {
            #     'course_code': course.course_code,
            #     'title': course.title,
            #     'description': course.description,
            #     'credits': course.credits,
            #     'instructor': course.instructor,
            #     'start_date': course.start_date,
            #     'prerequisites': course.prerequisites
            # }
            # Use course_code as the key in the hashmap
            course_data = dataset.objects.all()
            # hashmap = course_data
            # hashmap['id'] = course_data.id

    return course_data
