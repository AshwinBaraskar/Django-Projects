from django.shortcuts import render
from . import forms


def studentregistrationview(request):
    form = forms.StudentRegistration()
    return render(request, 'testapp/register.html', {'form': form})