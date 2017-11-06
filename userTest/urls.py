from django.conf.urls import url
from .views import index , strTest , getNameTest

urlpatterns = [
    url(r'^index/', index),
    url(r'^(\d+)/(\d+)/$',strTest),
    url(r'getNameTest/(?P<date>\d{4})/', getNameTest),
]