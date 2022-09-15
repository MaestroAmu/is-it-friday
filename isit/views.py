from django.shortcuts import render

import datetime
# Create your views here.
def index(request):
    return render(request, 'isit/index.html', {
        'friday': datetime.datetime.now().weekday()
    })
