from django import template
from django.utils.safestring import mark_safe
from listings.choices import ListingStatus
register = template.Library()

@register.simple_tag
def status_indicator(status):
    color_classes = {
        "available": {
            "bg": "bg-green-100 text-green-800",
            "tochka": "bg-green-500",
        },
        "ordered": {
            "bg": "bg-yellow-100 text-yellow-800",
            "tochka": "bg-yellow-500",
        },
        "completed": {
            "bg": "bg-red-100 text-red-800",
            "tochka": "bg-red-500",
        },
    }
    color_kwargs = color_classes.get(status, {
        "bg": "bg-gray-100 text-gray-800",
        "tochka": "bg-gray-500"
    })

    result = f"""
    <span class="inline-flex items-center {color_kwargs['bg']} text-xs font-medium px-2.5 py-0.5 rounded-full">
        <span class="w-2 h-2 me-1 {color_kwargs['tochka']} rounded-full"></span>
        {ListingStatus(status).label}
    </span>
    """
    return mark_safe(result)