from django.conf.urls import url

#file has been created
from .import views

urlpatterns = [
    url(r'^(?P<question_id>[0-9]+)/$' ,views.detail , name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$',views.results , name = 'results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote  , name = 'vote'),
  #  url(r'^home',views.home, name= 'home'),
   # url(r'^fpage/',views.fpage, name = 'fpage')
]