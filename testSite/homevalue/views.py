from django.shortcuts import render
from django.http import HttpResponse
from homevalue.forms import ValueForm, valAutoForm, valAuto
<<<<<<< HEAD
from homevalue.models import Homeinfo,Listing
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.shortcuts import render

import json
from dal import autocomplete
=======
from homevalue.models import Homeinfo
from django.views import generic
from django.urls import reverse, reverse_lazy

import json
from dal import autocomplete

>>>>>>> 1942034eb499aadce85ca5008d37798bca61bf91
import sys, requests


# Create your views here.

<<<<<<< HEAD
# Auto Compelete
=======
# Auto Compelete 
>>>>>>> 1942034eb499aadce85ca5008d37798bca61bf91
# Base on: https://django-autocomplete-light.readthedocs.io/en/3.1.3/tutorial.html
# class homeAutoComplete(autocomplete.Select2QuerySetView):
#     template_name = 'autoComplete.html'
#     form_class = valAuto
#     def get_queryset(self):
#         qs = Homeinfo.objects.all().order_by('id')
#         if self.q:
#             qs = qs.filter(address__istartswith=self.q)
#         return qs

# Another Test
# Failed but keeping for the week of torment it gave me
# class homeAutoComplete(generic.UpdateView):
#     model = Homeinfo
#     form_class = valAuto
#     template_name = 'get_addy.html'
#     success_url = reverse_lazy("homeAutoComplete")

#     # def form_valid(self, form):
#     #     return super().form_valid(form)

#     def get_object(self):
#         return Homeinfo.objects.first()

def get_addy(request):
    print('TEST')
    print(request)
    if request.is_ajax():
        q = request.GET.get('term', '')

        print(q)
        address = Homeinfo.objects.filter(address__icontains = q)[:20]
        results = []
        for addy in address:
            addy_json = {}
            addy_json = addy.address
            addy_json = addy.id
            addy_json = addy.estimate
            results.append(addy_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

<<<<<<< HEAD
def indexAuto(request):

=======

def indexAuto(request):
>>>>>>> 1942034eb499aadce85ca5008d37798bca61bf91
    if request.method == 'POST':
        search = ValueForm(request.POST)
        #search = valAutoForm(request.POST)
        if search.is_valid():
            #find = Homeinfo.objects.get(title__regex=r''+)
            print(search.cleaned_data["addy"])
            hope = search.cleaned_data["addy"].split(',')
            final = ""
            more = str(hope[0])
            sleep = more.split(' ')

            # Our Database doesn't exactly match up with google
<<<<<<< HEAD
            # So we have to cut some of the data off
=======
            # So we have to cut some of the data off 
>>>>>>> 1942034eb499aadce85ca5008d37798bca61bf91
            # Needs to be tested more but i think it works?
            if(sleep[-1] == 'Avenue'):
                for part in sleep:
                    final += str(part) + " "
            elif(sleep[-1] == 'Street'):
                for part in sleep:
                    final += str(part) + " "
            else:
                sleep.pop(-1)
                for part in sleep:
                    final += str(part) + " "

            #print(final)

            test = Homeinfo.objects.all().filter(address__contains=final)

            # If somehow there is a longer list
            if(len(test) > 1):
                return render(request, "resultsTest.html", {'results': test})
            else:
                return render(request, "singleHome.html", {'house': test[0]})
    else:
        search = ValueForm()

<<<<<<< HEAD
    context = {
        'form': search
    }
    return render(request, "autoaddress.html", context)
=======
    return render(request, "autoaddress.html", {'form': search})
>>>>>>> 1942034eb499aadce85ca5008d37798bca61bf91

def speakAgent(request):
    return render(request, "speak-with-agent.html")


def listWith(request):
    return render(request, "list-with-us.html")


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


<<<<<<< HEAD
# Single home info
=======
# Single home info 
>>>>>>> 1942034eb499aadce85ca5008d37798bca61bf91
def singleView(request, id):
    aTest = Homeinfo.objects.get(id=id)

    # Might not need this
    # https://stackoverflow.com/questions/25888396/how-to-get-latitude-longitude-with-python
    addyPlus = aTest.address.replace(" ", "+")
    print(addyPlus,file=sys.stderr)


    return render(request, "singleHome.html", {'house': aTest})
<<<<<<< HEAD
    #return HttpResponse("Test")
=======
    #return HttpResponse("Test")
>>>>>>> 1942034eb499aadce85ca5008d37798bca61bf91
