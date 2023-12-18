from django.urls import path
from django.http import JsonResponse
import joblib
import numpy as np
import pandas as pd
from rest_framework.decorators import api_view

@api_view(["POST"])
def approvereject(request):
    try:
        mdl = joblib.load("E:\Data science\Projects\Bank Loan Approval\loan_model.pkl")
        mydata = request.data
        unit = np.array(list(mydata.values()))
        unit = unit.reshape(1, -1)
        scalers = joblib.load("E:\Data science\Projects\Bank Loan Approval\scalers.pkl")
        X = scalers.transform(unit)
        y_pred = mdl.predict(X)
        y_pred = (y_pred > 0.5)
        status = 'Approved' if y_pred else 'Rejected'
        return JsonResponse({'status': status})
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)

urlpatterns = [
    path('approvereject/', approvereject, name='approvereject'),
    # Add other URL patterns as needed
]
