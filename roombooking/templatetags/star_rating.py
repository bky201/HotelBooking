from django import template

register = template.Library()

@register.filter(name='stars')
def stars(value):
    full_stars = int(value)
    empty_stars = 5 - full_stars
    star_html = '<span class="star star-full">★</span>' * full_stars
    star_html += '<span class="star star-empty">☆</span>' * empty_stars
    return star_html