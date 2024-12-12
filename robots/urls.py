from django.urls import path
from robots import views

app_name='robots'

urlpatterns = [
    path('api/create_robot/', views.robot_create_post_view, name='robot_create'),
path('robot-report/', views.robot_report_view, name='robot_report'),
path('robot-report/generate', views.generate_excel_report, name='robot_report_generate'),
]
