from .views import get_data,post_data,TheModelView,newdata
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('getdata/', csrf_exempt(get_data)),
    path('postdata/',csrf_exempt(post_data)),
    path('newdata/',csrf_exempt(TheModelView)),
    path('data/',csrf_exempt(newdata)),
    ]
