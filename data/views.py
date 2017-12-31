from django.shortcuts import render
from .models import Data
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def station_list(request):
    all_station = Data.objects.all()
    paginator = Paginator(all_station, 10)

    page_num = request.GET.get('page')
    try:
        stations = paginator.page(page_num)
    except PageNotAnInteger:
        stations = paginator.page(1)
    except EmptyPage:
        stations = paginator.page(paginator.num_pages)

    context = {
        'stations': stations,
    }
    return render(request, 'data/station_list.html', context)
