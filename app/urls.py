from .views import *
from .models import *
from django.urls import path
urlpatterns = [
    path("", StudentCreate.as_view()),
    path("StudentList/", StudentList.as_view()),
    path("StudentView/<int:pk>/", StudentView.as_view()),
    path("StudentUpdate/<int:pk>/", StudentUpdate.as_view()),
    path("StudentDestroy/<int:pk>/", StudentDestroy.as_view()),
]
