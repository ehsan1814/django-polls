from django.urls import path
from django.conf.urls import url
 
from . import views

app_name = 'polls' #if we have more than one application it help to distinguish

urlpatterns = [
   path('' , views.index , name = 'index'),
   path('<int:pk>/' , views.detail , name='detail'),
   path('<int:pk>/results/' , views.results , name='results'),
   path('<int:question_id>/vote/' , views.vote , name='vote'),
   ]