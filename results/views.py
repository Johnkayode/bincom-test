from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q, Count 
from django.shortcuts import get_object_or_404, render, redirect

from .models import *


def home(request):
    units_results = AnnouncedPuResults.objects.all()
    paginator = Paginator(units_results, 50)
    page = request.GET.get('page')
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
    context = {"results":results}
    return render(request, "index.html", context=context)

def total(request):
    lgas = Lga.objects.all()
    lga_name = request.GET.get('lga_name')
    total = None
    results = None
    if lga_name:
        lga = get_object_or_404(Lga, lga_name=lga_name)
        polling_units = PollingUnit.objects.filter(lga_id=lga.lga_id)
        print(polling_units)
        total = 0
        result_list = []
        for polling_unit in polling_units:
            results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=polling_unit.polling_unit_id)
            unit_total = sum([result.party_score for result in results])
            total+=unit_total
            unit = {}
            unit['polling_unit'] = polling_unit.polling_unit_id
            unit['results'] = results
            result_list.append(unit)
        
    context = {"lgas":lgas, "total":total, "lga_name":lga_name, "result_list":result_list}
    return render(request, "results.html", context)