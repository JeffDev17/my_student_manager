from django import template
from django.utils import timezone
from datetime import datetime

register = template.Library()

@register.filter
def filter_by_status(billings, status):
    return [billing for billing in billings if billing.status == status]

@register.filter
def days_overdue(date):
    today = timezone.now().date()
    delta = today - date
    return delta.days