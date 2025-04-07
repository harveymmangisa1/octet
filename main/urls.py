from django.urls import path
from .views import home, get_reports, submit_report, all_reports # Import submit_report

urlpatterns = [
    path('', home, name='home'),
    path('api/reports/', get_reports, name='get_reports'),
    path('api/submit-report/', submit_report, name='submit_report'),  # Add this line
    path('all-reports/', all_reports, name='all_reports'),  # New URL for all reports
]
