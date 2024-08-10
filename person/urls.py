from django.urls import path
from .views import PersonView

urlpatterns = [
    path('person/', PersonView.as_view()),
    path('person/<int:pk>/', PersonView.as_view())
]