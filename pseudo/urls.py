from django.urls import path
from django.conf.urls.static import static
from django.conf import settings    
from .views import Pseudo, PseudoAuth

urlpatterns=[
    path('', Pseudo.as_view()),
    path('auth/', PseudoAuth.as_view()),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)