from django.http import HttpResponse
from rnk.forms import LinkForm
from django.shortcuts import render
from rnk.classifier import callit
from rq import Queue

#import gc

def index(request):
    return render(request, 'test.html')

def result(request):

    link = "No Link"
    #cls = ""
    #prb = 0.0
    if request.method == "POST":
        #Get the posted form
        MyLinkForm = LinkForm(data=request.POST)
        #print("errors=")
        #print(MyLinkForm.errors)
        if MyLinkForm.is_valid():
            #print("Form is Valid")
            link = MyLinkForm.cleaned_data['link']

            cls, prb = callit(link)

        else:
            MyLinkForm = LinkForm()
            print("Form Not Valid")

    #print("Before delete views")
    #print(dir())
    #print("Local files")
    #print(locals())
    #for name in dir():
    #    if name!='link' and name!='cls' and name!='prb' and not name.startswith('__'):
    #        del locals()[name]

    #print("After delete views")
    #print(dir())
    #gc.collect()

    return render(request, 'test1.html', {"link" : link,
                                          "cls": cls,
                                          "prb": prb})
