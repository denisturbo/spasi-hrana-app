from django.shortcuts import render, redirect
from listings.models import Listing
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from customauth.models import BaseSpasiHranaUser, BusinessUser, CustomerUser
from django.db.models import Count, Q
from django.contrib.auth.decorators import permission_required

#Hrana app views 

def index(request):
    counts = BaseSpasiHranaUser.objects.aggregate(
        business=Count('pk', filter=Q(user_type='business')),
        customers=Count('pk', filter=Q(user_type='customer'))
    )
    if request.user.is_authenticated and request.user.user_type == 'customer':
        return render(request, 'landing/main.html', counts) # shte bude smeneno.. unauth i auth kato customer pokazva edno i sushto
    if request.user.is_authenticated and request.user.user_type == 'business':
        business_context = BusinessUser.objects.get(user=request.user)
        return render(request, 'business/main.html', {"business": business_context})
    else:
        return render(request, 'landing/main.html', counts)
    
    
def faq(request):
    return render(request, 'landing/faq.html')

def business(request):
    return render(request, 'landing/business.html')    


def profile(request): # Profile View for both types.. Business & Customer. Renders different based on Role
    current_user = request.user
    print(request.user.user_type)
    customer = CustomerUser.objects.get(user=current_user)
    return render(request, 'profile/profile.html', {'current_user': current_user,
                                                    "customer": customer})


class ListingView(LoginRequiredMixin, ListView):
    model = Listing
    template_name = 'customer/listings/listings.html'
    context_object_name = 'listings'

    def get_queryset(self):
        return Listing.objects.all()

class ListingDetailView(LoginRequiredMixin, DetailView):
    model = Listing
    template_name = 'customer/listings/listingdetail.html'
    context_object_name = 'listing_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = Listing.objects.get(id=self.kwargs['pk'])
        return context


        