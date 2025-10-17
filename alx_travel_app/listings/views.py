import requests
from django.conf import settings
from django.http import JsonResponse
from .models import Payment

def initiate_payment(request):
    booking_reference = request.POST.get("booking_reference")
    amount = request.POST.get("amount")
    currency = "ETB"  # or your desired currency
    email = request.POST.get("email")

    # Create Payment record with Pending status
    payment = Payment.objects.create(
        booking_reference=booking_reference,
        amount=amount,
        status="Pending"
    )

    # Chapa API request
    chapa_url = "https://api.chapa.co/v1/transaction/initialize"
    headers = {"Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"}
    payload = {
        "amount": amount,
        "currency": currency,
        "email": email,
        "tx_ref": booking_reference,
        "callback_url": "http://yourdomain.com/verify-payment/"
    }

    response = requests.post(chapa_url, json=payload, headers=headers)
    data = response.json()

    if response.status_code == 200 and data.get("status") == "success":
        payment.transaction_id = data["data"]["id"]
        payment.save()
        return JsonResponse({"payment_url": data["data"]["checkout_url"]})
    else:
        payment.status = "Failed"
        payment.save()
        return JsonResponse({"error": "Payment initiation failed"}, status=400)

