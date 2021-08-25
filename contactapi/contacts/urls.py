from django.urls import path
from .views import ContactList,ContacDetailView


urlpatterns = [
    path('', ContactList.as_view()),
    path('<int:id>', ContacDetailView.as_view()),
]