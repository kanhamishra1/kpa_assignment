from django.urls import path
from .views import BogieChecksheetCreateView
from .views import WheelSpecificationListView

urlpatterns = [
    path('forms/bogie-checksheet', BogieChecksheetCreateView.as_view(), name='bogie-checksheet-create'),
    path('forms/wheel-specifications', WheelSpecificationListView.as_view(), name='wheel-specification-list'),
]
