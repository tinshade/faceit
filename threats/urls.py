from django.urls import path
from django.conf.urls.static import static
from django.conf import settings    
from .views import ThreatActions

urlpatterns=[
    path('', ThreatActions.as_view()),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)