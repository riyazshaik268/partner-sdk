import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.shortcuts import render

import requests
from myapp import llm

latest_data = {}

@csrf_exempt  # Disable CSRF protection for simplicity (not recommended for production)
def account_details(request):
    global latest_data
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            latest_data = data  # Update the latest data

            print(f"api receive data: {data}")
            # Broadcast to WebSocket
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "data_updates",
                {
                    "type": "send_data",
                    "data": latest_data
                }
            )
            return JsonResponse({'status': data})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


# Display form on GET request
def submit_partner_data(request):
    if request.method == 'GET':
        return render(request, 'toast.html')
    elif request.method == 'POST':
        # Extract data from form
        partner_data = request.POST.get('partnerData', '')

        response = llm.process(json.loads(partner_data))
        requests.post(url="http://localhost:8001/api/account_details/",
                      data=json.dumps({"data": response}))
        message = "Data submitted successfully!"
        message_type = "success"
        # Process or save the data as needed
        # Here, we'll assume you want to send it to /partner_data endpoint
        return render(request, 'toast.html', {'message': message, 'message_type': message_type})


def get_latest_data(request):
    return JsonResponse(latest_data)


def display_data(request):
    return render(request, 'display_data.html')