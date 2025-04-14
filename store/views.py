from django.shortcuts import render
from .models import Product

from django.shortcuts import render
from .models import Product

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.contrib import messages

def firstpg(request):
    return render(request, 'store/firstpg.html')

def adminpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Log in the user
            return redirect('home')  # Redirect to the 'home' page
        else:
            return render(request, 'store/adminpage.html', {'error': 'Invalid credentials'})
    return render(request, 'store/adminpage.html')

def user_adminpg(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('user_page')  # Redirect to 'user_page' view
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    
    return render(request, 'store/user_adminpg.html')  # Render the login template

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
import joblib
import pandas as pd

# Load the model at the start
MODEL_PATH = os.path.join('store', 'model', 'heart_disease_model.pkl')
loaded_model_data = joblib.load(MODEL_PATH)

# Extract necessary components
preprocessor = loaded_model_data['preprocessor']
model = loaded_model_data['model']
feature_names = loaded_model_data['feature_names']
disease_labels = loaded_model_data['disease_labels']

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        # Retrieve the data from the form
        try:
            input_data = [
                float(request.POST.get('age', 0)),
                float(request.POST.get('sex', 0)),
                float(request.POST.get('cp', 0)),
                float(request.POST.get('trestbps', 0)),
                float(request.POST.get('chol', 0)),
                float(request.POST.get('thalach', 0)),
                float(request.POST.get('oldpeak', 0)),
                float(request.POST.get('fbs', 0)),
                float(request.POST.get('exang', 0)),
                float(request.POST.get('slope', 0)),
                float(request.POST.get('ca', 0)),
                float(request.POST.get('restecg', 0)),
            ]

            # Define the feature columns
            numeric_features = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
            categorical_features = ['sex', 'cp', 'fbs', 'exang', 'slope', 'ca', 'restecg']
            feature_columns = numeric_features + categorical_features



            # Convert the input into a DataFrame
            input_df = pd.DataFrame([input_data], columns=feature_columns)

            # Make a prediction
            probabilities = model.predict_proba(input_df)

            print(f"Probabilities shape: {probabilities.shape}")
            print(f"Raw probabilities: {probabilities}")

            # Format the response
            results = [
                {
                    'Disease': disease_labels[i],
                    'RiskScore': float(round(float(p) * 100, 2))
                }
                for i, p in enumerate(probabilities[0])
            ]
            results = sorted(results, key=lambda x: x['RiskScore'], reverse=True)
            print(f"Processed Results: {results}")

            # Render the results to an HTML template
            return render(request, 'store/results.html', {'predictions': results})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    # Render the form for GET requests
    return render(request, 'store/upload.html')

def userpg(request):
    phone_number = request.GET.get('phone')
    context = {
        'phone': phone_number
    }
    return render(request, 'store/userpg.html', context)

def user_page(request):
    phone_number = request.GET.get('phone')
    if phone_number:
        # Use the 'heart_data' database to fetch patients
        patients = Patient.objects.using('heart_data').filter(phone=phone_number)
    else:
        patients = []

    context = {
        'page_obj': patients,
        'debug_empty': not patients,
    }
    return render(request, 'store/user_page.html', context)

def user_patientdetail(request, case_no):
    try:
        # Get the most recent patient record if multiple exist
        patient = Patient.objects.filter(case_no=case_no).order_by('-appointment_date').first()
        if patient is None:
            return render(request, 'store/user_patientdetail.html', {
                'error': 'Patient not found',
                'case_no': case_no
            })
        return render(request, 'store/user_patientdetail.html', {'patient': patient})
    except Exception as e:
        return render(request, 'store/user_patientdetail.html', {
            'error': f'Error retrieving patient details: {str(e)}',
            'case_no': case_no
        })
    
def hypertension(request):
    return render(request, 'store/hypertension.html')

def last_consultation(request):
    return render(request, 'store/last-consultation.html')

from django.shortcuts import render

def next_appointment(request):
    # Example data (this should be fetched from your database)
    context = {
        'appointment_date': 'January 10, 2025',
        'appointment_time': '10:30 AM',
        'doctor_name': 'Dr. Jane Smith',
    }
    return render(request, 'store/next_appointment.html', context)

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Patient
from django.core.exceptions import MultipleObjectsReturned

def history_list(request):
    patients = Patient.objects.all().order_by('-appointment_date')
    paginator = Paginator(patients, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'store/history_list.html', {'page_obj': page_obj})

def patient_detail(request, case_no):
    try:
        # Get the most recent patient record if multiple exist
        patient = Patient.objects.filter(case_no=case_no).order_by('-appointment_date').first()
        if patient is None:
            return render(request, 'store/patient_detail.html', {
                'error': 'Patient not found',
                'case_no': case_no
            })
        return render(request, 'store/patient_detail.html', {'patient': patient})
    except Exception as e:
        return render(request, 'store/patient_detail.html', {
            'error': f'Error retrieving patient details: {str(e)}',
            'case_no': case_no
        })
    
# store/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PatientProfileForm

def create_profile(request):
    if request.method == 'POST':
        form = PatientProfileForm(request.POST)
        if form.is_valid():
            # Save the form without committing to the database
            patient_profile = form.save(commit=False)
            # Save the instance to the specified database
            patient_profile.save(using='heart_save_data')
            messages.success(request, 'Patient profile created successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Error creating patient profile.')
    else:
        form = PatientProfileForm()
    return render(request, 'store/create_profile.html', {'form': form})

def dashboard(request):
    return render(request, 'store/dashboard.html')  # Create a dashboard template

# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Doctordb

@csrf_exempt
def authenticate(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            doctor = Doctordb.objects.get(username=username)
            if doctor.password == password:  # In a real application, use hashed passwords
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False})
        except Doctordb.DoesNotExist:
            return JsonResponse({'success': False})

@csrf_exempt
def update_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')

        try:
            doctor = Doctordb.objects.get(email=email)
            doctor.password = new_password  # In a real application, hash the password
            doctor.save()
            return JsonResponse({'success': True})
        except Doctordb.DoesNotExist:
            return JsonResponse({'success': False})

def last_consultation(request):
    return render(request, 'store/last-consultation.html')

def fectors(request):
    return render(request, 'store/fectors.html')

def index(request):
    return render(request, 'store/index.html')

def heart_arrhythmias(request):
    return render(request, 'store/heart_arrhythmias.html')

def cad(request):
    return render(request, 'store/cad.html')

def mayocardial(request):
    return render(request, 'store/mayocardial.html')