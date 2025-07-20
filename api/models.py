

from django.db import models


# 1. POST /api/forms/bogie-checksheet


class BogieChecksheetForm(models.Model):
    form_number = models.CharField(max_length=100, unique=True)
    inspection_by = models.CharField(max_length=100)
    inspection_date = models.DateField()

    def __str__(self):
        return self.form_number

class BogieDetails(models.Model):
    form = models.OneToOneField(BogieChecksheetForm, on_delete=models.CASCADE, related_name='bogie_details')
    bogie_no = models.CharField(max_length=100)
    date_of_ioh = models.DateField()
    deficit_components = models.TextField()
    incoming_div_and_date = models.CharField(max_length=100)
    maker_year_built = models.CharField(max_length=100)

class BogieChecksheet(models.Model):
    form = models.OneToOneField(BogieChecksheetForm, on_delete=models.CASCADE, related_name='bogie_checksheet')
    axle_guide = models.CharField(max_length=100)
    bogie_frame_condition = models.CharField(max_length=100)
    bolster = models.CharField(max_length=100)
    bolster_suspension_bracket = models.CharField(max_length=100)
    lower_spring_seat = models.CharField(max_length=100)

class BmbcChecksheet(models.Model):
    form = models.OneToOneField(BogieChecksheetForm, on_delete=models.CASCADE, related_name='bmbc_checksheet')
    adjusting_tube = models.CharField(max_length=100)
    cylinder_body = models.CharField(max_length=100)
    piston_trunnion = models.CharField(max_length=100)
    plunger_spring = models.CharField(max_length=100)



# 2. GET /api/forms/wheel-specifications


class WheelSpecificationForm(models.Model):
    form_number = models.CharField(max_length=100)
    submitted_by = models.CharField(max_length=100)
    submitted_date = models.DateField()

    condemning_dia = models.CharField(max_length=100)
    last_shop_issue_size = models.CharField(max_length=100)
    tread_diameter_new = models.CharField(max_length=100)
    wheel_gauge = models.CharField(max_length=100)

    def __str__(self):
        return self.form_number
