from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.gallery,name='gallery'),
     url(r'^search/', views.search_image, name='search_image'),
    url(r'^image/(?P<category_name>\w+)/(?P<image_id>\d+)',views.picture,name = 'picture')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)