from django.conf import settings
from django import template
from datetime import datetime
# Depending on your django version, `reverse` and `NoReverseMatch` has been moved.
# From django 2.0 they've been moved to `django.urls`
from fish.models import Fish

try:
    from django.urls import reverse, NoReverseMatch
except ImportError:
    from django.core.urlresolvers import reverse, NoReverseMatch

register = template.Library()

# From django 1.9 `assignment_tag` is deprecated in favour of `simple_tag`
try:
    simple_tag = register.simple_tag
except AttributeError:
    simple_tag = register.assignment_tag

MAX_LENGTH_BOOTSTRAP_COLUMN = 12


@register.simple_tag(takes_context=True)
def fetch_setting(context, key):
    try:
        request = context.get('request')
        obj = Fish.objects.get(id=key)
        return obj.name
    except Fish.DoesNotExist:
        return ''
