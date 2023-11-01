from django.urls import path
from .views import HomeView, AboutView, GeneratorView
from django.conf.urls.static import static
from django.conf import settings
from django.views import View
from . import views

#app_name = 'blog'
urlpatterns =[
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('generator/', GeneratorView.as_view(), name='generator'),
    #path('', views.BlogListView.as_view(), name='blog_home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)