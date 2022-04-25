from django.urls import path

from . import views

urlpatterns = [
    path('', views.getVehicleThatSendNavigationDataInFourtyEightHours, name='home') #home page


]