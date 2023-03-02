from . import views
from django.urls import path

app_name = 'student'

urlpatterns = [
    path('',views.home, name='home'),
    path('add_student/',views.add_student, name='add_student'),
    path('view_student/',views.view_student, name='view_student'),
    path('update_student/<int:stud_id>',views.update_student, name='update_student'),
    path('delete_student/<int:stud_id>',views.delete_student, name='delete_student'),
]