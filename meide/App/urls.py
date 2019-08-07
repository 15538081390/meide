from django.conf.urls import url,include
from App import views

urlpatterns = [

    url(r'^$', views.index, name='index')

]