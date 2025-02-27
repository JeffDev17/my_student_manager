from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import Billing
from .forms import BillingForm

def billing_list(request):
    billings = Billing.objects.all().order_by('-due_date')
    return render(request, 'billing/billing_list.html', {'billings': billings})

def billing_create(request):
    if request.method == "POST":
        form = BillingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cobrança criada com sucesso!")
            return redirect('billing-list')
    else:
        form = BillingForm()
    return render(request, 'billing/billing_form.html', {'form': form})

def billing_update(request, pk):
    billing = get_object_or_404(Billing, pk=pk)
    if request.method == "POST":
        form = BillingForm(request.POST, instance=billing)
        if form.is_valid():
            form.save()
            messages.success(request, "Cobrança atualizada com sucesso!")
            return redirect('billing-list')
    else:
        form = BillingForm(instance=billing)
    return render(request, 'billing/billing_form.html', {'form': form})

def billing_delete(request, pk):
    billing = get_object_or_404(Billing, pk=pk)
    billing.delete()
    messages.success(request, "Cobrança excluída com sucesso!")
    return redirect('billing-list')