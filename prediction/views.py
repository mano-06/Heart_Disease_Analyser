from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import joblib

model = joblib.load('./model.joblib')

def plans(request):
    return render(request,'prediction/plans.html')

def home(request):
    
    return render(request, 'prediction/home.html')
    

def index(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Age = float(request.POST.get('num1'))
        Sex = int(request.POST.get('sex'))
        ChestPainType = int(request.POST.get('chestPainType'))
        RestingBP = float(request.POST.get('num4'))
        Cholesterol = float(request.POST.get('num5'))
        FastingBS = int(request.POST.get('fastingBs'))
        RestingECG = int(request.POST.get('restingECG'))
        MaxHR = float(request.POST.get('num8'))
        ExerciseAngina = int(request.POST.get('exerciseAngina'))
        OldPeak = float(request.POST.get('num10'))
        STSlope = int(request.POST.get('stslope'))

        input_data = np.array([[Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, OldPeak, STSlope]])

        prediction = model.predict(input_data)[0]

        return render(request, 'prediction/result.html', {'prediction': prediction, 'name': Name})

    return render(request, 'prediction/index.html')
