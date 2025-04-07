from django.contrib import admin
from django.urls import path, include
from main.views import (
    cybersecurity_page,
    cyber_bullying_cases,
    anonymous_report_submit
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Cybersecurity pages
    path('cybersecurity/', cybersecurity_page, name='cybersecurity'),
    path('cyber-bullying-cases/', cyber_bullying_cases, name='cyber_bullying_cases'),
    path('report-submit/', anonymous_report_submit, name='report_submit'),
    
    # Main app routes
    path('', include('main.urls')),
]