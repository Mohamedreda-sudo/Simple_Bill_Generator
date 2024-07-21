from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv

from .models import BoughtItem
from .forms import BoughtItemForm

def generate_report(request):
    items = BoughtItem.objects.all()
    form = BoughtItemForm()
    return render(request, 'shopping/report.html', {'items': items, 'form': form})

def add_item(request):
    if request.method == 'POST':
        form = BoughtItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('generate_report')
    else:
        form = BoughtItemForm()
    return render(request, 'shopping/add_item.html', {'form': form})

def export_to_excel(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="bought_items.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Price', 'Bought Date'])

    items = BoughtItem.objects.all()
    for item in items:
        writer.writerow([item.name, item.price, item.bought_date])

    return response
