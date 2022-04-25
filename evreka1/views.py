from django.shortcuts import render
import datetime
from .models import NavigationRecord, Vehicle


def getVehicleThatSendNavigationDataInFourtyEightHours(request):
    dataInfourtyeighthours = NavigationRecord.objects.filter( datetime__gte = datetime.datetime.now()-datetime.timedelta(days=2))
    a = 5

    result = []
    for datum in dataInfourtyeighthours:
        return_json = {}
        return_json["latitude"] = datum.latitude
        return_json["longitude"] = datum.longitude
        return_json["vehicle_plate"] = datum.vehicle.plate
        return_json["datetime"] = datum.datetime
        result.append(return_json)


    result = list(dataInfourtyeighthours.values())

    return render(request, "home.html", ({'result': result}))