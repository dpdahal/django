from django.urls import path, include
from rest_framework import routers

from .views import *

app_name = 'newsapi'

router = routers.DefaultRouter()
router.register('', NewsApiDetails)

urlpatterns = [
    path('', include(router.urls))

]