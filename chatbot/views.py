from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def chatbot_view(request):
    """Chatbot interface view"""
    return render(request, 'chatbot/chat.html')

@csrf_exempt
def chat_api(request):
    """API endpoint for chatbot responses"""
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '')
        
        # Simple response logic (to be enhanced with AI later)
        response = get_bot_response(user_message)
        
        return JsonResponse({
            'response': response,
            'success': True
        })
    
    return JsonResponse({'error': 'Invalid request'}, status=400)


def get_bot_response(message):
    """Generate bot response based on user message"""
    message_lower = message.lower()
    
    # Simple keyword-based responses
    if 'mygap' in message_lower or 'certification' in message_lower:
        return "MyGAP (Malaysian Good Agricultural Practices) is a certification scheme. Visit the Department of Agriculture website for more information on how to apply."
    
    elif 'price' in message_lower or 'cost' in message_lower:
        return "Prices vary depending on the product and seller. You can browse our marketplace to compare prices from different sellers."
    
    elif 'farming' in message_lower or 'tips' in message_lower:
        return "For farming tips, I recommend visiting our Courses section where experts share valuable agricultural knowledge."
    
    elif 'aquaculture' in message_lower or 'fish' in message_lower:
        return "We have a dedicated Aquaculture section with various fish species and aquaculture equipment. Check out our listings!"
    
    elif 'hello' in message_lower or 'hi' in message_lower:
        return "Hello! I'm Agrohub Assistant powered by Magna Cita AI. How can I help you today? Ask me about farming tips, MyGAP certification, or product recommendations!"
    
    else:
        return "I'm here to help! You can ask me about farming tips, MyGAP certification, product listings, or navigate through our marketplace. What would you like to know?"
