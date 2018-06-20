from django.shortcuts import render
from django.http import HttpResponse
from homevalue.forms import ValueForm, valAutoForm
from homevalue.models import Homeinfo
from django.views import generic
from django.urls import reverse, reverse_lazy

from dal import autocomplete

import sys, requests


# Create your views here.

# Auto Compelete 
# Base on: https://django-autocomplete-light.readthedocs.io/en/3.1.3/tutorial.html
# class homeAutoComplete(autocomplete.Select2QuerySetView):
#     template_name = 'autoComplete.html'
#     def get_queryset(self):
#         qs = Homeinfo.objects.all().order_by('id')
#         if self.q:
#             qs = qs.filter(address__istartswith=self.q)
#         return qs

# Another Test
class homeAutoComplete(generic.UpdateView):
    model = Homeinfo
    form_class = valAutoForm
    template_name = 'autoComplete.html'
    success_url = reverse_lazy("homeAutoComplete")

    def get_object(self):
        return Homeinfo.objects.first()




# No autocomplete
def index(request):
    if request.method == 'POST':
        search = ValueForm(request.POST)
        #search = valAutoForm(request.POST)
        if search.is_valid():
            #find = Homeinfo.objects.get(title__regex=r''+)
            #print(search.cleaned_data["addy"])
            test = Homeinfo.objects.all().filter(address__contains=search.cleaned_data["addy"])
            return render(request, "resultsTest.html", {'results': test})
    else:
        search = ValueForm()

    return render(request, "test.html", {'form': search})
    #return HttpResponse('HELLO FROM HOMEVALUE')


# Single home info 
def singleView(request, id):
    aTest = Homeinfo.objects.get(id=id)

    # Might not need this
    # https://stackoverflow.com/questions/25888396/how-to-get-latitude-longitude-with-python
    addyPlus = aTest.address.replace(" ", "+")
    print(addyPlus,file=sys.stderr)


    return render(request, "singleHome.html", {'house': aTest})
    #return HttpResponse("Test")