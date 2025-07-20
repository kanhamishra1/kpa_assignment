from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import BogieChecksheetForm, WheelSpecificationForm
from .serializers import (
    BogieChecksheetFormSerializer,
    WheelSpecificationFormSerializer
)

# ===============================
# 1. POST /api/forms/bogie-checksheet
# ===============================

class BogieChecksheetCreateView(APIView):
    def post(self, request):
        serializer = BogieChecksheetFormSerializer(data=request.data)
        if serializer.is_valid():
            form = serializer.save()
            return Response({
                "data": {
                    "formNumber": form.form_number,
                    "inspectionBy": form.inspection_by,
                    "inspectionDate": form.inspection_date.strftime("%Y-%m-%d"),
                    "status": "Saved"
                },
                "message": "Bogie checksheet submitted successfully.",
                "success": True
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ===============================
# 2. GET /api/forms/wheel-specifications
# ===============================

class WheelSpecificationListView(generics.ListAPIView):
    queryset = WheelSpecificationForm.objects.all()
    serializer_class = WheelSpecificationFormSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['form_number', 'submitted_by', 'submitted_date']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        results = []

        for spec in queryset:
            results.append({
                "fields": {
                    "condemningDia": spec.condemning_dia,
                    "lastShopIssueSize": spec.last_shop_issue_size,
                    "treadDiameterNew": spec.tread_diameter_new,
                    "wheelGauge": spec.wheel_gauge,
                },
                "formNumber": spec.form_number,
                "submittedBy": spec.submitted_by,
                "submittedDate": spec.submitted_date.strftime("%Y-%m-%d")
            })

        return Response({
            "data": results,
            "message": "Filtered wheel specification forms fetched successfully.",
            "success": True
        }, status=status.HTTP_200_OK)

