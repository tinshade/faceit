from django.urls import path
from django.conf.urls.static import static
from django.conf import settings    
from .views import Profile, Generate, VerifyPassword

urlpatterns=[
    path('profile/', Profile.as_view(), name="profile"),
    path('generate/', Generate.as_view(), name="generate"),
    path('verify/', VerifyPassword.as_view(), name="verify"),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)