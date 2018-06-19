from django.shortcuts import render
from django.http import HttpResponse
from homevalue.forms import ValueForm
from homevalue.models import Homeinfo

import sys, requests


# Create your views here.
def index(request):


    if request.method == 'POST':
        search = ValueForm(request.POST)
        if search.is_valid():
            #find = Homeinfo.objects.get(title__regex=r''+)
            #print(search.cleaned_data["addy"])
            test = Homeinfo.objects.all().filter(address__contains=search.cleaned_data["addy"])
            return render(request, "resultsTest.html", {'results': test})
    else:
        search = ValueForm()

    return render(request, "test.html", {'form': search})
    #return HttpResponse('HELLO FROM HOMEVALUE')

def singleView(request, id):
    aTest = Homeinfo.objects.get(id=id)

    # Might not need this
    # https://stackoverflow.com/questions/25888396/how-to-get-latitude-longitude-with-python
    addyPlus = aTest.address.replace(" ", "+")
    print(addyPlus,file=sys.stderr)


    return render(request, "singleHome.html", {'house': aTest})
    #return HttpResponse("Test")