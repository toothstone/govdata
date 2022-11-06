from django.shortcuts import render

from ckanapi import RemoteCKAN

def dashboard(request):
    govdata = RemoteCKAN("https://www.govdata.de/ckan/")
    organizations = govdata.action.organization_list(all_fields=True)
    return render(request,
                  'dashboard/dashboard.html',
                  {"organizations": organizations}
                  )
