
from django.contrib import admin
from .models import (
    WheelSpecificationForm,
    BogieChecksheetForm,
    BogieDetails,
    BogieChecksheet,
    BmbcChecksheet
)

admin.site.register(WheelSpecificationForm)
admin.site.register(BogieChecksheetForm)
admin.site.register(BogieDetails)
admin.site.register(BogieChecksheet)
admin.site.register(BmbcChecksheet)
