from django.urls import path
from .views import Ask

urlpatterns = [
    path('', Ask.as_view())
]