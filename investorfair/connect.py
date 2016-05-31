import json
from django.http import HttpResponse

class connect:
    states = [0,1,2]
    state = 0

    '''
    State 0: Normal
    State 1: Commercial
    State 2: Blank
    '''

def state():
    return connect.state

def get_state(request):
    response = {'state': connect.state}
    return HttpResponse(json.dumps(response), content_type="application/json")

def set_state(request):
    if (request.method != 'POST') or not ('state' in request.POST):
        return HttpResponse()

    try:
        s = int(request.POST['state'])
    except:
        return HttpResponse()

    if not s in connect.states:
        return HttpResponse()

    connect.state = s

    response = {'success': True}
    return HttpResponse(json.dumps(response), content_type="application/json")
