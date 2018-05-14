from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def keyboard(request):

        return JsonResponse(
        {
            'type': 'buttons',
            'buttons': ["python", "django", "worldcup"]
            
        }
    )

@csrf_exempt

def message(request):
    
    json_str = (request.body).decode('utf-8')
    received_json = json.loads(json_str)
    content_name = received_json['content']
    
    if content_name == 'python':
        return JsonResponse(
        {
                'message': {
                    'text': "let's start python with codecademy https://www.codecademy.com/tracks/python"
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ["python", "django", "worldcup"]
                }
            }
        )
    
    elif content_name == 'django':
        return JsonResponse(
        {
                'message': {
                    'text': "django is interesting with djangogirls https://tutorial.djangogirls.org/ko/"
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ["python", "django", "worldcup"]
                }
            }
        )
    
    elif content_name == 'worldcup':
        return JsonResponse(
        {
                'message': {
                    'text': "2018 Russia Worldcup coming soon with Naver \n http://sports.news.naver.com/wfootball/index.nhn"
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ["python", "django", "worldcup"]
                }
            }
        )

    