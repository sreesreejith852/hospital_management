from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from management.views import PatientViewSet, AppointmentViewSet, upload_data
from management.views import patients_view, list_patients

router = DefaultRouter()  

router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('api/', include('management.urls')),
    # path('api/patients/', list_patients),
    path('api/upload/', upload_data),
    path('patients/', patients_view),
    path('create_patient/', list_patients, name='patients_view')
]
