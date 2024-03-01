from django.urls import path
from . import views

urlpatterns = [
  path('', views.courses_view, name='courses_view'),
  path('<int:pk>', views.course_detail, name='course_detail'),
  path('create_course', views.create_course, name='create_course'),
  path('edit_course/<int:pk>/', views.edit_course, name='edit_course'),

]
