from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
import stripe

from .models import Item


def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    stripe.api_key = "sk_test_51MdvCXAVBPAmsMEl0TZBCziPyiEucass5rVNL8qR23xqfQH4qeJoOqAMEW0EJP53o0jt2CIhLL1zJbPR7psdDTR100SAQKmcgz"
    session_id = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "usd",
                "unit_amount": int(item.price * 100),
                "product_data": {
                    "name": item.name,
                    "description": item.description,
                },
            },
            "quantity": 1,
        }],
        mode="payment",
        success_url=request.build_absolute_uri(reverse("success")),
        cancel_url=request.build_absolute_uri(reverse("cancel")),
    ).id
    context = {
        "item": item,
        "session_id": session_id,
    }
    return render(request, "item_detail.html", context)


def buy_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    stripe.api_key = "sk_test_51MdvCXAVBPAmsMEl0TZBCziPyiEucass5rVNL8qR23xqfQH4qeJoOqAMEW0EJP53o0jt2CIhLL1zJbPR7psdDTR100SAQKmcgz"
    session_id = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "usd",
                "unit_amount": int(item.price * 100),
                "product_data": {
                    "name": item.name,
                    "description": item.description,
                },
            },
            "quantity": 1,
        }],
        mode="payment",
        success_url=request.build_absolute_uri(reverse("success")),
        cancel_url=request.build_absolute_uri(reverse("cancel")),
    ).id
    return JsonResponse({"session_id": session_id})




def success_view(request):
    return render(request, 'success.html')


def cancel_view(request):
    return render(request, 'cancel.html')
