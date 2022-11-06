import json

from django.shortcuts import render

from ckanapi import RemoteCKAN


def dashboard(request):
    govdata = RemoteCKAN("https://www.govdata.de/ckan/")
    organizations = govdata.action.organization_list(all_fields=True)
    with open('govdata/dashboard/departments.json') as departments_json:
        departments = json.load(departments_json)["departments"]
    ministries = []
    for ministry in departments:
        try:
            datasets = next(filter(lambda x: x['title'] == ministry["name"],
                                   organizations))["package_count"]
        except StopIteration:
            datasets = 0
        for sub_deps in ministry.get("subordinates", []):
            try:
                datasets += \
                next(filter(lambda x: x['title'] == sub_deps["name"],
                            organizations))["package_count"]
            except StopIteration:
                pass
        ministries.append({"name": ministry["name"], "datasets": datasets})
    return render(request,
                  'dashboard/dashboard.html',
                  {"ministries": sorted(ministries, key=lambda x: x["datasets"],
                                        reverse=True)}
                  )
