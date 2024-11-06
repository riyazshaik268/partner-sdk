import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.shortcuts import render


latest_data = {}

@csrf_exempt  # Disable CSRF protection for simplicity (not recommended for production)
def account_details(request):
    global latest_data
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            latest_data = data  # Update the latest data

            # Broadcast to WebSocket
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "data_updates",
                {
                    "type": "send_data",
                    "data": latest_data
                }
            )
            return JsonResponse({'status': 'success'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


def get_latest_data(request):
    return JsonResponse(latest_data)


def display_data(request):
    return render(request, 'display_data.html')