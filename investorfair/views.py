from django.shortcuts import render

class website:
    def home(request):
    	return render(request, 'site/home.html')

    def attractions(request):
    	return render(request, 'site/attractions.html')

    def visit(request):
    	return render(request, 'site/visit.html')

    def team(request):
    	return render(request, 'site/team.html')

    def faq(request):
    	return render(request, 'site/faq.html')

    def resources(request):
    	return render(request, 'site/resources.html')

class display:
    def overview(request):
        return render(request, 'display/overview.html')

def portal(request):
    return render(request, 'portal.html')

def commercial(request):
    return render(request, 'commercial.html')
