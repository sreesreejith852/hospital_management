from django.db import models

class Patient(models.Model):
    patient_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=255)
    medical_history = models.TextField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    appointment_id = models.CharField(max_length=10, unique=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason_for_visit = models.TextField()

    def __str__(self):
        return self.appointment_id