from django.urls import path
from robots.views import robot_create_post_view

app_name='robots'

urlpatterns = [
    path('api/create_robot/', robot_create_post_view, name='robot_create'),
]
