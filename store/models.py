from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200, default='General')
    email_id = models.EmailField(max_length=254, null=True, blank=True)  # Keep null=True for now
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.title

from django.db import models
import joblib
import os
from django.conf import settings

class HeartDiseaseModel:
    def __init__(self):
        model_path = os.path.join(settings.BASE_DIR, 'predictor', 'model', 'heart_disease_model.pkl')
        self.model = joblib.load(model_path)

    def predict(self, input_data):
        probabilities = self.model.predict_proba([input_data])
        return probabilities


class Patient(models.Model):
    case_no = models.CharField(max_length=100)
    appointment_date = models.DateField()
    patient_name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    trestbps = models.IntegerField()
    chol = models.IntegerField()
    thalach = models.IntegerField()
    fbs = models.IntegerField()
    restecg = models.IntegerField()
    cp = models.IntegerField()
    exang = models.IntegerField()
    oldpeak = models.FloatField()
    slope = models.IntegerField()
    ca = models.IntegerField()
    diseases = models.TextField()
    risk_score = models.IntegerField()
    doctor_notes = models.TextField()

    class Meta:
        db_table = 'patientdata'
        app_label = 'store'

    def __str__(self):
        return f"{self.case_no} - {self.patient_name}"
    


# store/models.py

from django.db import models

class PatientProfile(models.Model):
    case_no = models.CharField(max_length=255)
    appointment_date = models.DateField()
    patient_name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.CharField(
        max_length=10,
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female')
        ]
    )
    trestbps = models.IntegerField()
    chol = models.IntegerField()
    thalach = models.IntegerField()
    fbs = models.CharField(
        max_length=3,
        choices=[
            ('Yes', 'Yes'),
            ('No', 'No')
        ]
    )
    restecg = models.CharField(
        max_length=50,
        choices=[
            ('Normal', 'Normal'),
            ('ST-T Wave Abnormality', 'ST-T Wave Abnormality'),
            ('Left Ventricular Hypertrophy', 'Left Ventricular Hypertrophy')
        ]
    )
    cp = models.CharField(
        max_length=50,
        choices=[
            ('Typical Angina', 'Typical Angina'),
            ('Atypical Angina', 'Atypical Angina'),
            ('Non-anginal Pain', 'Non-anginal Pain'),
            ('Asymptomatic', 'Asymptomatic')
        ]
    )
    exang = models.CharField(
        max_length=3,
        choices=[
            ('Yes', 'Yes'),
            ('No', 'No')
        ]
    )
    oldpeak = models.DecimalField(max_digits=3, decimal_places=1)
    slope = models.CharField(
        max_length=20,
        choices=[
            ('Upsloping', 'Upsloping'),
            ('Flat', 'Flat'),
            ('Downsloping', 'Downsloping')
        ]
    )
    ca = models.IntegerField()
    diseases = models.CharField(max_length=255, blank=True, null=True)
    risk_score = models.CharField(max_length=255, blank=True, null=True)
    doctor_notes = models.TextField(blank=True, null=True)
    #created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'patientdata'
        app_label = 'store'

    def __str__(self):
        return self.patient_name
    
# models.py
from django.db import models

class PatientDetail(models.Model):
    case_no = models.AutoField(primary_key=True)
    appointment_date = models.DateField()
    patient_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10, unique=True)
    risk_score = models.IntegerField()

    class Meta:
        db_table = 'patientdata'
        app_label = 'store'

    def __str__(self):
        return self.patient_name
    
# models.py
from django.db import models

class Doctordb(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)  # Note: In a real application, use Django's built-in user model or hash passwords
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
    
