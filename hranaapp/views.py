from django.shortcuts import render
from business.models import Listing
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from customauth.models import BaseSpasiHranaUser
from django.db.models import Count, Q

#Hrana app views 

def index(request):
    counts = BaseSpasiHranaUser.objects.aggregate(
        business=Count('pk', filter=Q(user_type='business')),
        customers=Count('pk', filter=Q(user_type='customer'))
    )
    return render(request, 'landing/main.html', counts)
def faq(request):
    return render(request, 'faq/faq.html')

def baba(request):
    return render(request, 'errors/404.html')

def business(request):
    return render(request, 'business/business.html')


class ListingView(LoginRequiredMixin, ListView):
    model = Listing
    template_name = 'listings/listings.html'
    context_object_name = 'listings'

    def get_queryset(self):
        return Listing.objects.all()

class ListingDetailView(LoginRequiredMixin, DetailView):
    model = Listing
    template_name = 'listings/listingdetail.html'
    context_object_name = 'listing_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = Listing.objects.get(id=self.kwargs['pk'])
        return context


        