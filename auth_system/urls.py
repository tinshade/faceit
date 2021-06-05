from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),
    path('inquiry/', include('inquiry.urls'), name="inquiry"),
    path('accounts/', include('accounts.urls'), name="accounts"),
    path('pseudo/', include('pseudo.urls'), name="pseudo"),
    path('devices/', include('clientdev.urls'), name="devices"),
    path('filez/', include('filez.urls'), name="filez"),
    path('threats/', include('threats.urls'), name="threats"),
    path('activity/', include('activity.urls'), name="activity"),
    path('', TemplateView.as_view(template_name="index.html"))
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

#urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]