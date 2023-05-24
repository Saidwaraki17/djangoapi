# two types views
# function type
# object type
# request is the common argument
from django.http import HttpResponse,JsonResponse

# this is method for small data
def home_page(request):
    print("Home Page is requested")
    days = [
        'Monday',
        'Tueday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday',
    ]
    #return HttpResponse("<h1>This is the requested Home Page!!<h1>")
    return JsonResponse(days, safe= False)



