from django.urls import path
from .views import StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView

urlpatterns = [
    path('', StudentListView.as_view(), name='student_list'),
    path('add/', StudentCreateView.as_view(), name='add_student'),
    path('edit/<int:pk>/', StudentUpdateView.as_view(), name='edit_student'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete_student'),
]
