from django.urls import path
from .views import CreateStudentView, IndexView, StudentDelete , StudentEdit , StudentStatus

urlpatterns = [
    path('', CreateStudentView.as_view(), name="home-view"),
    path('delete/<int:pk>', StudentDelete.as_view(), name="student-delete"),
    path('edit/<int:pk>', StudentEdit.as_view(), name="student-edit"),
    path('status/<int:pk>', StudentStatus.as_view(), name="student-status"),
    path('success', IndexView.as_view(), name="success")
]
