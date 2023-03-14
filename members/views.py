from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Member
from.forms import memberform
# Create your views here.


def index(request): 
    return render(request, 'members/index.html', {
        'members': Member.objects.all() 
    })

def view_member(request, id): 
    member = Member.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))


def add(request): 
    if request.method == 'POST': 
        form = memberform(request.POST)
        if form.is_valid(): 
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_phone_number = form.cleaned_data['phone_number']
            new_hop = form.cleaned_data['hop']
            new_date_joined = form.cleaned_data['date_joined']
            new_occupation = form.cleaned_data['occupation']
            new_extra_notes = form.cleaned_data['extra_notes']

            new_member = Member(
                first_name = new_first_name,
                last_name = new_last_name,
                email = new_email,
                phone_number = new_phone_number,
                hop = new_hop,
                date_joined = new_date_joined,
                occupation = new_occupation,
                extra_notes = new_extra_notes
            )

            new_member.save()
            return render(request, 'members/add.html', {
                'form': memberform(), 
                'success': True
            })  
    else: 
        return render(request, 'members/add.html', {
            'form': memberform(), 
        })



def edit(request, id):
    if request.method == 'POST': 
        member = Member.objects.get(pk=id)
        form = memberform(request.POST,instance=member)
        if form.is_valid():
            form.save()
            return render(request, 'members/edit.html', {
                'form': form, 
                'success' : True
            })
    else: 
        member = Member.objects.get(pk=id)
        form = memberform(instance=member)
    return render(request, 'members/edit.html', {
        'form': form
    })

def delete(request, id ): 
    if request.method == 'POST': 
        member = Member.objects.get(pk=id)
        member.delete()
    return HttpResponseRedirect(reverse('index'))
    