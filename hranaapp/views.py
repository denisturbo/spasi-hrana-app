from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from listings.models import Listing
from django.views.generic import ListView, DetailView
from customauth.models import BaseSpasiHranaUser, BusinessUser, CustomerUser
from django.db.models import Count, Q
from spasihrana.requests import HttpRequest


# Hrana app views

def index(request):
    counts = BaseSpasiHranaUser.objects.aggregate(
        business=Count('pk', filter=Q(user_type='business')),
        customers=Count('pk', filter=Q(user_type='customer'))
    )
    if request.user.is_authenticated and request.user.user_type == 'customer':
        return render(request, 'landing/main.html',
                      counts)  # shte bude smeneno.. unauth i auth kato customer pokazva edno i sushto
    if request.user.is_authenticated and request.user.user_type == 'business':
        business_context = BusinessUser.objects.get(user=request.user)
        return render(request, 'business/main.html', {"business": business_context})
    else:
        return render(request, 'landing/main.html', counts)


def faq(request):
    return render(request, 'landing/faq.html')


def business(request):
    return render(request, 'landing/business.html')


def profile(request):
    current_user = request.user
    print(request.user.user_type)
    customer = CustomerUser.objects.get(user=current_user)
    return render(request, 'customer/profile/profile.html', {'current_user': current_user,
                                                             "customer": customer})


class ListingView(ListView):
    model = Listing
    template_name = 'customer/listings/listings.html'
    context_object_name = 'listings'
    paginate_by = 10

    def get_queryset(self):
        return Listing.objects.all()

    def get(self, request: HttpRequest, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()

        if request.htmx:
            print('vliza')
            return TemplateResponse(request, "htmx-partials/listing_partial.html", context)
        else:
            return TemplateResponse(request, self.template_name, context)

class ListingDetailView(DetailView):
    model = Listing
    template_name = 'customer/listings/listingdetail.html'
    context_object_name = 'listing_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = Listing.objects.get(id=self.kwargs['pk'])
        return context
