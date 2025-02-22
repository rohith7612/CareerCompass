from django.shortcuts import render

# Create your views here.
import openai
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import io
import sys

from django.conf import settings

# Configure the OpenAI API key
openai.api_key = settings.OPENAI_API_KEY

def codesavant(request):
    return render(request, 'code_assistant/codesavant.html')

@csrf_exempt
def run_code(request):
    """
    Naive approach to execute Python code. 
    Not safe for production. 
    """
    if request.method == 'POST':
        code = request.POST.get('code', '')
        
        # Redirect stdout to capture code output
        old_stdout = sys.stdout
        redirected_output = io.StringIO()
        sys.stdout = redirected_output
        
        try:
            exec(code, {})
            output = redirected_output.getvalue()
        except Exception as e:
            output = str(e)
        finally:
            sys.stdout = old_stdout
        
        return JsonResponse({'output': output})
    return JsonResponse({'error': 'Invalid request method'}, status=400)
@csrf_exempt
def assistant_feedback(request):
    if request.method == 'POST':
        user_code = request.POST.get('code', '')
        instruction = (
            "You are an AI assistant that validates Python code. "
            "If the submitted code is correct, appreciate the candidate with an encouraging message. "
            "If errors are found, provide a detailed analysis and corrections. "
            "Your response must strictly adhere to the following exact format:\n"
            "Error identified: {error}\n"
            "corrected code: {correct code}\n"
            "Level of code: {level of the corrected code}\n"
            "Resources: {resources}\n"
            "Feedback: {feedback}"
        )

        if not user_code.strip():
            return JsonResponse({'error': 'No code provided'}, status=400)

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": instruction},
                    {"role": "user", "content": f"Analyze the following code:\n{user_code}"}
                ],
                max_tokens=500,
                temperature=0.7
            )

            assistant_message = response['choices'][0]['message']['content']
            return JsonResponse({'assistant_response': assistant_message})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)