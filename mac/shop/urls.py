from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),             # inspection done
    path("about/", views.about, name="about"),        # inspection done
    path("contact/", views.contact, name="contact"),      # inspection done
    path("tracker/", views.tracker, name="tracker"),
    path("search/", views.search, name="search"),        # inspection done
    path("products/<int:myid>", views.prodview, name="prodview"),    # inspection done
    path("checkout/", views.checkout, name="checkout")                   # inspection done
]