from django.db.models.aggregates import Sum
from django.shortcuts import render, redirect
from orders.models import Order
from listings.choices import ListingStatus
from listings.models import Listing
from django.views.generic import ListView, DetailView
from customauth.models import BaseSpasiHranaUser, BusinessUser, CustomerUser
from django.db.models import Count, Q
from spasihrana.requests import HttpRequest


# Hrana app views

def index(request):
    if request.user.is_authenticated and request.user.user_type == 'business':
        business_context = BusinessUser.objects.get(user=request.user)
        business_counts = BusinessUser.objects.aggregate(
            active_offers=Count('pk', filter=Q(listing__status='available', user=request.user)),
            total_sales=Count('pk', filter=Q(listing__status='completed', user=request.user)),
            total_revenue=Sum('listing__price', filter=Q(listing__status='completed', user=request.user)))
        return render(request, 'business/main.html', {"business": business_context,
                                          "count": business_counts})
    else:
        counts = BaseSpasiHranaUser.objects.aggregate(
            business=Count('pk', filter=Q(user_type='business')),
            customers=Count('pk', filter=Q(user_type='customer'))
        )
        return render(request, 'landing/main.html',
                  counts)


def faq(request):
    return render(request, 'landing/faq.html')


def business(request):
    return render(request, 'landing/business.html')


def profile(request):
    current_user = request.user
    print(request.user.user_type)
    customer = CustomerUser.objects.get(user=current_user)
    customer_orders = Order.objects.filter(customer=customer).order_by('-created_at')[:5]
    return render(request, 'customer/profile/profile.html', {"customer": customer,
                                                             'orders': customer_orders})


class ListingView(ListView):
    model = Listing
    template_name = 'customer/listings/listings.html'
    context_object_name = 'listings'
    paginate_by = 1

    def get_queryset(self):
        return Listing.objects.filter(status='available').order_by('-created_at')

    def get(self, request: HttpRequest, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()

        if request.htmx:
            print('vliza')
            return render(request, "htmx-partials/listing_partial.html", context)
        else:
            return render(request, self.template_name, context)

class ListingDetailView(DetailView):
    model = Listing
    template_name = 'customer/listings/listingdetail.html'
    context_object_name = 'listing_detail'

    def get_queryset(self):
        return Listing.objects.filter(status=ListingStatus.AVAILABLE)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
