from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406356643',
        'name': 'Lessyarta Kamali Sopamena Pirade',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
