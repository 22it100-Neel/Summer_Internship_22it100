
from django.urls import path,include

from buy import views
from .views import first,second

urlpatterns = [
   path('',views.first,name='first'),
   path('second/',second,name='second'),

]