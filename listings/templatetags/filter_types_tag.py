from django import template
register = template.Library()

@register.inclusion_tag('components/partials/list_types.html')
def filter_types_tag(listings, title):
    return {'listings': listings,
            'title': title}