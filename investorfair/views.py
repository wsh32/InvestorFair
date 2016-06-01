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
        elif connect.state() == 3:
            return rickroll(request)
        elif connect.state() == 4:
            return justdoit(request)
        elif connect.state() == 5:
            return darude(request)

    def attractions(request):
        if connect.state() == 0:
    	    return render(request, 'site/attractions.html')
        elif connect.state() == 1:
            return commerciale(request)
        elif connect.state() == 2:
            return blank(request)
        elif connect.state() == 3:
            return rickroll(request)
        elif connect.state() == 4:
            return justdoit(request)
        elif connect.state() == 5:
            return darude(request)

    def visit(request):
        if connect.state() == 0:
    	    return render(request, 'site/visit.html')
        elif connect.state() == 1:
            return commerciale(request)
        elif connect.state() == 2:
            return blank(request)
        elif connect.state() == 3:
            return rickroll(request)
        elif connect.state() == 4:
            return justdoit(request)
        elif connect.state() == 5:
            return darude(request)

    def team(request):
        if connect.state() == 0:
    	    return render(request, 'site/team.html')
        elif connect.state() == 1:
            return commerciale(request)
        elif connect.state() == 2:
            return blank(request)
        elif connect.state() == 3:
            return rickroll(request)
        elif connect.state() == 4:
            return justdoit(request)
        elif connect.state() == 5:
            return darude(request)

    def faq(request):
        if connect.state() == 0:
    	    return render(request, 'site/faq.html')
        elif connect.state() == 1:
            return commerciale(request)
        elif connect.state() == 2:
            return blank(request)
        elif connect.state() == 3:
            return rickroll(request)
        elif connect.state() == 4:
            return justdoit(request)
        elif connect.state() == 5:
            return darude(request)

    def resources(request):
        if connect.state() == 0:
    	    return render(request, 'site/resources.html')
        elif connect.state() == 1:
            return commerciale(request)
        elif connect.state() == 2:
            return blank(request)
        elif connect.state() == 3:
            return rickroll(request)
        elif connect.state() == 4:
            return justdoit(request)
        elif connect.state() == 5:
            return darude(request)

class display:
    def cover(request):
        if connect.state() == 0:
    	    return render(request, 'display/cover.html')
        elif connect.state() == 1:
            return commerciale(request)
        elif connect.state() == 2:
            return blank(request)
        elif connect.state() == 3:
            return rickroll(request)
        elif connect.state() == 4:
            return justdoit(request)
        elif connect.state() == 5:
            return darude(request)

    def overview(request):
        if connect.state() == 0:
    	    return render(request, 'display/overview.html')
        elif connect.state() == 1:
            return commerciale(request)
        elif connect.state() == 2:
            return blank(request)
        elif connect.state() == 3:
            return rickroll(request)
        elif connect.state() == 4:
            return justdoit(request)
        elif connect.state() == 5:
            return darude(request)

    def attractions(request):
        if connect.state() == 0:
    	    return render(request, 'display/attractions.html')
        elif connect.state() == 1:
            return commerciale(request)
        elif connect.state() == 2:
            return blank(request)
        elif connect.state() == 3:
            return rickroll(request)
        elif connect.state() == 4:
            return justdoit(request)
        elif connect.state() == 5:
            return darude(request)

    def finance(request):
        if connect.state() == 0:
    	    return render(request, 'display/finance.html')
        elif connect.state() == 1:
            return commerciale(request)
        elif connect.state() == 2:
            return blank(request)
        elif connect.state() == 3:
            return rickroll(request)
        elif connect.state() == 4:
            return justdoit(request)
        elif connect.state() == 5:
            return darude(request)

def commercial(request):
    if connect.state() == 0:
        return render(request, 'commercial.html')
    elif connect.state() == 1:
        return commerciale(request)
    elif connect.state() == 2:
        return blank(request)
    elif connect.state() == 3:
        return rickroll(request)
    elif connect.state() == 4:
        return justdoit(request)
    elif connect.state() == 5:
        return darude(request)

def portal(request):
    if connect.state() == 0:
        return render(request, 'portal.html')
    elif connect.state() == 1:
        return commerciale(request)
    elif connect.state() == 2:
        return blank(request)
    elif connect.state() == 3:
        return rickroll(request)
    elif connect.state() == 4:
        return justdoit(request)
    elif connect.state() == 5:
        return darude(request)

def admin(request):
    return render(request, 'admin.html')

def commerciale(request):
    return render(request, 'commerciale.html')

def blank(request):
    return render(request, 'blank.html')

def rickroll(request):
    return render(request, 'rickroll.html')

def justdoit(request):
    return render(request, 'justdoit.html')

def darude(request):
    return render(request, 'darude.html')
