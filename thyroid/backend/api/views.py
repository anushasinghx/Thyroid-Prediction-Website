import joblib
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from sklearn.preprocessing import StandardScaler

# Load the model and scaler
model_path = 'D:/thyroidweb/thyroid/backend/thyroid_model_core.pkl'
model = joblib.load(model_path)

# Assuming scaler was saved similarly; if not, initialize it as per training configuration
scaler_path = 'D:/thyroidweb/thyroid/backend/thyroid_scaler.pkl'
scaler = joblib.load(scaler_path)

# Define mappings for categorical fields
gender_map = {"M": 1, "F": 0}
smoking_map = {"Yes": 1, "No": 0}
thyroid_function_map = {"Euthyroid": 0, "Hypothyroid": 1, "Hyperthyroid": 2}
physical_exam_map = {"Single": 0, "Multinodular": 1}
adenopathy_map = {"Yes": 1, "No": 0}
pathology_map = {"Micropapillary": 0, "Other": 1}
focality_map = {"Uni-Focal": 0, "Multi-Focal": 1}
risk_map = {"Low": 0, "Intermediate": 1, "High": 2}
response_map = {"Excellent": 0, "Indeterminate": 1}

# Mappings for T, N, M, and Stage fields based on dataset
t_map = {"T1a": 1.1, "T1b": 1.2, "T2": 2, "T3a": 3.1, "T3b": 3.2, "T4a": 4.1, "T4b": 4.2}
n_map = {"N0": 0, "N1a": 1.1, "N1b": 1.2}
m_map = {"M0": 0, "M1": 1}
stage_map = {"I": 1, "II": 2, "III": 3, "IVA": 4.1, "IVB": 4.2}

@csrf_exempt
def thyroid_test_results(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received data:", data)  # Debugging step

            # Convert input data using mappings
            input_features = [
                data.get('age', 0),
                gender_map.get(data.get('gender', "M")),
                smoking_map.get(data.get('smoking', "No")),
                smoking_map.get(data.get('hx_smoking', "No")),
                smoking_map.get(data.get('hx_radiotherapy', "No")),
                thyroid_function_map.get(data.get('thyroid_function', "Euthyroid")),
                physical_exam_map.get(data.get('physical_exam', "Single")),
                adenopathy_map.get(data.get('adenopathy', "No")),
                pathology_map.get(data.get('pathology', "Micropapillary")),
                focality_map.get(data.get('focality', "Uni-Focal")),
                risk_map.get(data.get('risk', "Low")),
                t_map.get(data.get('t', "T1a")),       # Convert T field
                n_map.get(data.get('n', "N0")),       # Convert N field
                m_map.get(data.get('m', "M0")),       # Convert M field
                stage_map.get(data.get('stage', "I")),  # Convert Stage field
                response_map.get(data.get('response', "Excellent"))
            ]
            print("Input features:", input_features)  # Debugging step

            # Convert to numpy array and standardize it
            input_array = np.array([input_features])
            input_array_scaled = scaler.transform(input_array)
            print("Input array for model after scaling:", input_array_scaled)  # Debugging step

            # Make the prediction using the loaded model
            prediction = model.predict(input_array_scaled)
            print("Prediction result:", prediction)  # Debugging step

            # Send a JSON response with the prediction result
            return JsonResponse({'result': "Thyroid condition detected." if prediction[0] == 1 else "Your results indicate no presence of thyroid disease."})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        except KeyError as ke:
            return JsonResponse({'error': f'Missing key: {str(ke)}'}, status=400)
        except Exception as e:
            print("Unexpected error:", e)  # Additional debugging for any other error
            return JsonResponse({'error': f'Prediction error: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

# Test endpoint for connectivity
@csrf_exempt
def test_view(request):
    if request.method == 'POST':
        return JsonResponse({'message': 'POST request received at /test'})
    return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
