from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Record
from .forms import RecordForm


def index(request):
    """Home page of The_counter apps"""
    return render(request, 'the_counter/index.html')


def budget(request):
    """Shows budget parts"""
    income = 0
    expenses = 0
    wishes = 0
    eggs = Record.objects.all()
    for spam in eggs:
        if spam.budget_item == 'income':
            income += spam.money
        elif spam.budget_item == 'expenses':
            expenses += spam.money
        elif spam.budget_item == 'wish_list':
            wishes += spam.money
    context = {'income': income, 'expenses': expenses, 'wishes': wishes}
    return render(request, 'the_counter/budget_parts.html', context)


def income_records(request):
    """List of Income records"""
    records = Record.objects.filter(budget_item='income')
    context = {'records': records}
    return render(request, 'the_counter/income_records.html', context)


def expenses_records(request):
    """List of Expenses records"""
    records = Record.objects.filter(budget_item='expenses')
    context = {'records': records}
    return render(request, 'the_counter/expenses_records.html', context)


def wish_list(request):
    """List of Wish_list records"""
    records = Record.objects.filter(budget_item='wish_list')
    context = {'records': records}
    return render(request, 'the_counter/wish_list.html', context)


def new_record(request):
    """Adding a new record"""
    if request.method != 'POST':
        # Data have not been send, creating empty form
        form = RecordForm()
    else:
        # POST data sent, process data
        form = RecordForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('budget_parts'))

    context = {'form': form}
    return render(request, 'the_counter/new_record.html', context)


def edit_record(request, record_id):
    """Edits an existing record"""
    record = Record.objects.get(id=record_id)

    if request.method != 'POST':
        # Original request; the form is filled with the data of the current record
        form = RecordForm(instance=record)
    else:
        # Sending POST data; process data
        form = RecordForm(instance=record, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('budget_parts'))

    context = {'record': record, 'form': form}
    return render(request, 'the_counter/edit_record.html', context)


def delete_record(request, record_id):
    """Delete record"""
    record = Record.objects.get(id=record_id)
    record.delete()
    return HttpResponseRedirect(reverse('budget_parts'))

