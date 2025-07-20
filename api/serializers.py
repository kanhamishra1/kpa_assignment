from rest_framework import serializers
from .models import (
    BogieChecksheetForm,
    BogieDetails,
    BogieChecksheet,
    BmbcChecksheet,
    WheelSpecificationForm
)

# ========== Sub-Serializers for Nested Form ==========

class BogieDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BogieDetails
        exclude = ['form']

class BogieChecksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BogieChecksheet
        exclude = ['form']

class BmbcChecksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BmbcChecksheet
        exclude = ['form']

# ========== Main BogieChecksheetForm Serializer (POST) ==========

class BogieChecksheetFormSerializer(serializers.ModelSerializer):
    bogieDetails = BogieDetailsSerializer()
    bogieChecksheet = BogieChecksheetSerializer()
    bmbcChecksheet = BmbcChecksheetSerializer()

    class Meta:
        model = BogieChecksheetForm
        fields = [
            'form_number',
            'inspection_by',
            'inspection_date',
            'bogieDetails',
            'bogieChecksheet',
            'bmbcChecksheet',
        ]

    def create(self, validated_data):
        bogie_details_data = validated_data.pop('bogieDetails')
        bogie_checksheet_data = validated_data.pop('bogieChecksheet')
        bmbc_checksheet_data = validated_data.pop('bmbcChecksheet')

        form = BogieChecksheetForm.objects.create(**validated_data)

        BogieDetails.objects.create(form=form, **bogie_details_data)
        BogieChecksheet.objects.create(form=form, **bogie_checksheet_data)
        BmbcChecksheet.objects.create(form=form, **bmbc_checksheet_data)

        return form

# ========== WheelSpecificationForm Serializer (GET) ==========

class WheelSpecificationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelSpecificationForm
        fields = '__all__'
