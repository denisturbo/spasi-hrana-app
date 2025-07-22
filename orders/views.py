from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from hranaapp.mixins import CreatedUpdatedAtMixin
from listings.models import Listing
from orders.models import Order


# Create your views here.
class CreateOrder(LoginRequiredMixin, CreatedUpdatedAtMixin, View):

    def post(self, request, *args, **kwargs):
        listing = get_object_or_404(Listing, pk=kwargs['pk'])

        order = Order.objects.create(
            listing=listing,
            customer=self.request.user.customeruser,
            business=listing.connection,
        )

        listing.status = 'ordered'
        listing.save()

        return render(request, 'htmx-partials/confirmed_list_partial.html', {
            'order': order,
            'listing': listing,
        })


