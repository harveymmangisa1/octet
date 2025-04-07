from django.shortcuts import render
from django.http import JsonResponse
from .models import CyberReport
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Report  # Import your Report model

# Mock database (replace with actual model)
reports = []

@csrf_exempt
def submit_report(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            content = data.get("content", "").strip()
            gender = data.get("gender", "").strip()

            if not content or not gender:
                return JsonResponse({"error": "Content and gender are required"}, status=400)

            report = {"content": content, "gender": gender}
            reports.append(report)  # Simulating database save

            return JsonResponse({"message": "Report submitted successfully!"}, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    
    return JsonResponse({"error": "Invalid request method"}, status=405)

def get_reports(request):
    return JsonResponse({"reports": reports})


def home(request):
    return render(request, 'home.html')

def cybersecurity_page (request):
    return render (request, 'cyber.html')
    
def cyber_bullying_cases(request):
    return render (request, 'cyber.html')
    
def anonymous_report_submit(request):
    return render (request, 'cyber.html')

def all_reports(request):
    return render(request, 'all_reports.html', {'reports': reports})