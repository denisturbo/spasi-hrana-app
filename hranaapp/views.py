from django.db.models.aggregates import Sum
from django.shortcuts import render
from orders.models import Order
from customauth.models import BaseSpasiHranaUser, BusinessUser, CustomerUser
from django.db.models import Count, Q


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