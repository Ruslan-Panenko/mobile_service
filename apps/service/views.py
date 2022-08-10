from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from apps.service.forms import CreateTask, CreateInvoice
from apps.service.models import Phone, Invoice


@login_required
def home(request):
    user = request.user
    if user.is_master:
        tasks = Phone.objects.all().order_by('id')
    else:
        tasks = Phone.objects.filter(user_id=user.id).order_by('id')
    data = {
        'user': user,
        'tasks': tasks,
    }
    return render(request, 'home.html', data)


@login_required
def create_task(request):
    if request.method == 'POST':
        form = CreateTask(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Phone.objects.create(brand=cd['brand'], problem=cd['problem'],
                                 status=Phone.CD ,user_id=request.user)
            return redirect('homepage')
        else:
            return HttpResponse('Invalid data')
    else:
        form = CreateTask()
    return render(request, 'create_task.html', {'form': form})


@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        task = Phone.objects.filter(id=task_id).first()
        status_choices = Phone.status_choices
        invoices = Invoice.objects.filter(phone_id=task_id)
        return render(request, 'task_detail.html', {'task': task,
                                                    'status_choices': status_choices,
                                                    'invoices': invoices,
                                                    })
    else:
        Phone.objects.filter(id=task_id).update(brand=request.POST['brand'],
                                                problem=request.POST['problem'],
                                                status=request.POST['status'])
        return redirect('homepage')


@login_required
def task_delete(request, task_id):
    user = request.user
    if user == Phone.objects.filter(id=task_id).first().user_id or user.is_master:
        Phone.objects.filter(id=task_id).delete()
        return redirect('homepage')

    else: return HttpResponse('It is not your task')


@login_required
def create_invoice(request, task_id):
    if request.user.is_master:
        if request.method == 'POST':
            form = CreateInvoice(request.POST)
            if form.is_valid():
                cd = form.cleaned_data

                Invoice.objects.create(description=cd['description'],
                                       price=cd['price'],
                                       phone_id_id=task_id,
                                       )
                return redirect('homepage')
        else:
            form = CreateInvoice()
        return render(request, 'create_invoice.html', {'form': form})

    else: return HttpResponse('unavailable action')