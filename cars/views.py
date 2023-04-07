from django.shortcuts import render

from cars.models import Cars


def car_check(request):
    if request.method == 'POST':
        car_number = request.POST.get('car_number')
        try:
            car = Cars.objects.get(gos_num=car_number)
            return render(request, 'result.html', {'car': car})
        except Cars.DoesNotExist:
            return render(request, 'result.html', {'message': 'Нет данных'})
    else:
        return render(request, 'carcheck.html')
