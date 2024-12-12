import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError

from .models import Robot
from .validators import validate_robot_data

@csrf_exempt
def robot_create_post_view(request):
    if request.method == 'POST':
        if not request.body:
            return JsonResponse({"error": "No data provided"}, status=400)
        try:
            data = json.loads(request.body)
            validated_data = validate_robot_data(data)
            robot = Robot.objects.create(**validated_data)
            return JsonResponse({"message": "Robot created successfully", "robot_id": robot.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

        except ValidationError as e:
            return JsonResponse({"error": str(e)}, status=400)

        except Exception as e:
            return JsonResponse({"error": f"Unexpected error: {str(e)}"}, status=500)

