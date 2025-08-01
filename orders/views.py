from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View, ListView, UpdateView

from hranaapp.mixins import CreatedUpdatedAtMixin
from listings.choices import ListingStatus
from listings.models import Listing
from orders.models import Order
from spasihrana.requests import HttpRequest


# Create your views here.
class CreateOrder(LoginRequiredMixin, CreatedUpdatedAtMixin, View):

    def post(self, request, *args, **kwargs):
        listing = get_object_or_404(Listing, pk=kwargs['pk'])
        customer = self.request.user.customeruser
        has_order = Order.objects.filter(customer=customer,listing__status=ListingStatus.ORDERED).first()

        if has_order:
            return render(request, 'htmx-partials/error_partial.html', {
                'listing': listing,
                'customer': customer,
                'has_order': has_order
            })

        order = Order.objects.create(
            listing=listing,
            customer=customer,
            business=listing.connection,
        )

        listing.status = ListingStatus.ORDERED
        listing.save()

        return render(request, 'htmx-partials/confirmed_list_partial.html', {
            'order': order,
            'listing': listing,
        })

class OrdersTableList(PermissionRequiredMixin, ListView):
    permission_required = ('customauth.can_create_listing')
    paginate_by = 10
    model = Order
    template_name = 'business/orders/data-table.html'

    def get_queryset(self):
        return Order.objects.filter(business=self.request.user.businessuser, listing__status='ordered')

    def get(self, request: HttpRequest, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()

        if request.htmx:
            print('vliza')
            return render(request, "htmx-partials/order_table_partial.html", context)
        else:
            return render(request, self.template_name, context)


class CompleteOrder(PermissionRequiredMixin, UpdateView):
    permission_required = ('customauth.can_create_listing')
    model = Order
    success_url = reverse_lazy('orders:table')

    def post(self, request: HttpRequest, *args, **kwargs):
        self.object = self.get_object()

        if request.htmx:
            current_page = request.GET.get('page', 1)
            print(self.object.listing.status, "IMA LI NQKOI")
            self.object.listing.status = ListingStatus.COMPLETED
            self.object.listing.save()
            print(self.object.listing.status, "IMA LI NQKOI")

            queryset = Order.objects.filter(business=self.request.user.businessuser, listing__status='ordered')
            paginate_by = 10
            paginator = Paginator(queryset, paginate_by)
            page_obj = paginator.get_page(current_page)

            context = {
                'object_list': page_obj.object_list,
                'page_obj': page_obj,
                'is_paginated': page_obj.has_other_pages(),
                'paginator': paginator,
                }
            return render(request, 'htmx-partials/order_table_partial.html', context)
        return super().post(request, *args, **kwargs)