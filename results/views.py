from datetime import datetime
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q, Count 
from django.shortcuts import get_object_or_404, render, redirect

from .models import *



def home(request):
    lgas = [lga.lga_id for lga in Lga.objects.filter(state_id=25)]
    units = PollingUnit.objects.filter(lga_id__in=lgas)
    units_results = []
    for unit in units:
        unit_name = unit.polling_unit_name
        results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=unit.polling_unit_id)
        units_results.append({"unit":unit_name, "results":results})
    paginator = Paginator(units_results, 10)
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
    result_list = []
    if lga_name:
        lga = get_object_or_404(Lga, lga_name=lga_name)
        polling_units = PollingUnit.objects.filter(lga_id=lga.lga_id)
    
        total = 0
        
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


def create(request):
    parties = Party.objects.all()
    polling_units = PollingUnit.objects.all()
    context = {"parties":parties, "polling_units":polling_units}

    if request.method == 'POST':
        name = request.POST['name']
        polling_unit_id = request.POST["polling_unit_id"]
        party = request.POST["party"]
        score = request.POST["party_score"]
        ip = request.POST["ip"]

        result = AnnouncedPuResults.objects.create(
            polling_unit_uniqueid = polling_unit_id,
            party_abbreviation = party,
            party_score = score,
            entered_by_user = name,
            date_entered = datetime.now(),
            user_ip_address = ip
        )

        result.save()
        return redirect('create')
    

    
    return render(request, "create.html", context)