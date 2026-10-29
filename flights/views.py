from django.shortcuts import render
from .models import Flight, Passenger


def index(request):
    flights = (
        Flight.objects
        .select_related("origin", "destination")
        .prefetch_related("passengers")
        .order_by("id")
    )

    return render(
        request,
        "flights/index.html",
        {"flights": flights},
    )


def passengers(request):
    passengers = (
        Passenger.objects
        .prefetch_related("flights__origin", "flights__destination")
        .order_by("name")
    )

    return render(
        request,
        "flights/passengers.html",
        {"passengers": passengers},
    )
