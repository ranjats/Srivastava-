from django.http import HttpResponse
from django.shortcuts import render
# This is for when we pass r parameter of render

# def index(request):
#     params = {'name':'Ranjat', 'Designation':'SE'}
#     return render(request, 'index.html', params)

# This is the for request on index

# def index(request):
#     return HttpResponse('''<h1> This is the first Page </h1> <a href="http://127.0.0.1:8000/"> Django Tutorial</a>''')

# this is the for Homapage style


def index(request):

    print(request.GET.get('Text', 'default'))
    return render(request, 'index.html')


def about(request):
    return HttpResponse("this is for About Page <a href='/'> back</a>")

#
# def back(request):
#     return HttpResponse('''<h1> This is the Second page  </h1> <a href="http://127.0.0.1:8000/"> Django Tutorial</a>''')

def back(request):
    djtext=  request.POST.get('Text', 'default')
    backremove = request.POST.get('backremove', 'off')
    caseU = request.POST.get('caseU', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    if backremove == "on":

        puncuation = '''!()-[]{};:'"\,<>./'''
        analyzed = ""
        for char in djtext:
            if char not in puncuation:
                analyzed = analyzed + char
        param = {'purpose': 'Remove the Puncuaion', 'check_value': analyzed}
        djtext = analyzed
        #return render(request, 'secondPage.html', param)

    if caseU == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        param = {'purpose': 'Convert into upperCase ', 'check_value': analyzed}
        djtext = analyzed

        #return render(request, 'secondPage.html', param)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != '\r':
                analyzed = analyzed + char
            else:
                print("no")
        param = {'purpose': 'remove New line', 'check_value': analyzed}

    if backremove != "on" and caseU != "on" and newlineremover != "on":
        param1 = {'result': 'Please select any operation'}
        return render(request, 'error.html', param1)

    return render(request, 'secondPage.html', param)


def website(request):
    return HttpResponse(''' <h1> FaceBook </h1><a href="https://www.facebook.com/">Click</a>
    <h1>Gmail</h1><a href="https://ww.gmail.com">Click ME!</a>
    <h1>Code with Herry</h1><a href="https://www.codewithherry.com">Click Me2!</a>''')


