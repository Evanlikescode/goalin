from django.shortcuts import render

# Create your views here.

def landing_page(request):

    data = {
        'app_name': 'goalin',
        'creator_name': 'Evan Haryo Widodo',
        'creator_class': 'PBP A'
    }

    return render(request, "landing_page.html", data)
