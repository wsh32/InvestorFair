from django.shortcuts import render

from . import connect

class website:
    def home(request):
        if connect.state() == 0:
    	    return render(request, 'site/home.html')
        elif connect.state() == 1:
            return commerciale(request)
        elif connect.state() == 2:
            return blank(request)

    def attractions(request):
        if connect.state() == 0:
    	    return render(request, 'site/attractions.html')
        elif connect.state() == 1:
            return commerciale(request)
        elif connect.state() == 2:
            return blank(request)

    def visit(request):
        if connect.state() == 0:
    	    return render(request, 'site/visit.html')
        elif connect.state() == 1:
            return commerciale(request)
        elif connect.state() == 2:
            return blank(request)

    def team(request):
        if connect.state() == 0:
    	    return render(request, 'site/team.html')
        elif connect.state() == 1:
            return commerciale(request)
        elif connect.state() == 2:
            return blank(request)

    def faq(request):
        if connect.state() == 0:
    	    return render(request, 'site/faq.html')
        elif connect.state() == 1:
            return commerciale(request)
        elif connect.state() == 2:
            return blank(request)

    def resources(request):
        if connect.state() == 0:
    	    return render(request, 'site/resources.html')
        elif connect.state() == 1:
            return commerciale(request)
        elif connect.state() == 2:
            return blank(request)

class display:
    def overview(request):
        if connect.state() == 0:
    	    return render(request, 'display/overview.html')
        elif connect.state() == 1:
            return commerciale(request)
        elif connect.state() == 2:
            return blank(request)

    def attractions(request):
        if connect.state() == 0:
    	    return render(request, 'display/attractions.html')
        elif connect.state() == 1:
            return commerciale(request)
        elif connect.state() == 2:
            return blank(request)

    def finance(request):
        if connect.state() == 0:
    	    return render(request, 'display/finance.html')
        elif connect.state() == 1:
            return commerciale(request)
        elif connect.state() == 2:
            return blank(request)

def commercial(request):
    if connect.state() == 0:
        return render(request, 'commercial.html')
    elif connect.state() == 1:
        return commerciale(request)
    elif connect.state() == 2:
        return blank(request)

def portal(request):
    return render(request, 'portal.html')

def admin(request):
    return render(request, 'admin.html')

def commerciale(request):
    return render(request, 'commerciale.html')

def blank(request):
    return render(request, 'blank.html')
