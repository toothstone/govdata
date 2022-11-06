from django.shortcuts import render


def dashboard(request):
    organizations = [
        {"title": "AA", "datasets": 12}
    ]
    return render(request,
                  'dashboard/dashboard.html',
                  {"organizations": organizations}
                  )
