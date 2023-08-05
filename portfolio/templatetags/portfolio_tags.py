from django import template
from portfolio.models import *

register = template.Library()


# @register.simple_tag()
# def get_photos_from_one_theme(theme_slug=None):
#     return Files.objects.filter(theme__slug=theme_slug)


