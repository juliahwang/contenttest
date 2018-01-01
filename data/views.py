from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Data
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def station_list(request):
    """
    모든 역정보에 대한 리스트를 제공한다.
    리스트는 10개 단위로 페이지네이션 하였다.
    """
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


def station_detail(request, station_id):
    """
    역명을 클릭하면 해당 역에 대한 정보를 넘겨준다
    """
    station_id = Data.objects.filter(station_id=station_id)
    station = get_object_or_404(Data, pk=station_id)
    context = {
        'station': station,
    }
    return render(request, 'data/station_detail.html', context)


def test_detail(request, station_id):
    station = get_object_or_404(Data, station_id=station_id)
    js_data = station.get_selected_data()
    print(js_data)
    data_set = list()
    for key, value in js_data.items():
        data_set.append({"label": key, "value": value})
    return JsonResponse(data_set, safe=False)
