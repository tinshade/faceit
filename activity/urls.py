from django.urls import path
from django.conf.urls.static import static
from django.conf import settings    
from .views import ActivityActions

urlpatterns=[
    path('', ActivityActions.as_view()),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)