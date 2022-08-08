from CARA import random_responses
import os
import json
import random
import re
import requests
from pprint import pprint
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import generic
from django.http.response import HttpResponse
# Create your views here.
test = {
         'class': [""" Class is canceled, Class will be continued from 27th July.""",
                    ],
         'exam':    ["""Your exam(semester final) will start from 24th August 2022 GLHF.""",
                    ],
         'result':   ["""The result is not published yet """],
         'eee': ["""Here's the link to the notes of EEE2187: https://drive.google.com/drive/folders/19nLQQakI3MJOLdNb9JlVUaIOFDFgcthu?usp=sharing """],
         'cse': ["""Here's the link to the notes of CSE2187: https://drive.google.com/drive/folders/19nLQQakI3MJOLdNb9JlVUaIOFDFgcthu?usp=sharing """],
         'help': ["""Type the name of the courses to get notes\nType 'notice' to get recent notices\nType 'ca' to get contact details of course advisors\nType 'courses' to know the names of the courses of this semester"""],
         'courses': ["""EEE2187\nCSE2187\nMath2127\nHum2127\nME2155"""],
         'hello': ["""Hello, How can I help you?"""],
         'ca': ["""Zinat Tasneem\nAssistant Professor\nDept. of Mechatronics Engineering,\nRajshahi University of Engineering & Technology,\nRajshahi-6204.\nMd. Faisal Rahman Badal\nLecturer\nDept. of Mechatronics Engineering,\nRajshahi University of Engineering & Technology,\nRajshahi-6204"""],
         'ct': [""" Hum 2127 ct will be held on 26th of July""",
                    ],

         }

def post_facebook_message(fbid, recevied_message):
    # Remove all punctuations, lower case the text and split it based on space
    tokens = re.sub(r"[^a-zA-Z0-9\s]",' ',recevied_message).lower().split()
    test_text = ''
    for token in tokens:    
        if token in test:
            test_text = random.choice(test[token])
            break
    if not test_text:
        test_text = "I didn't understand! Type help to know more."    
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAIfrbRUABoBANqfQRYeP97oJOgUZAqdgSHvlAoZBVe8YxSgXqRB09rvKdTiiCY7RfvL7IN0vYXpiEjcTDzmIhAZBWwwBbXR27ry6WHZBT1vvuBGHO9qtMWfPNvqohxDM1A4xA73QfYZBUZBtqJF36Xv9kEi4ZAZCaXvayjA1TtZBY3GT9iI9CCO6' 
    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":test_text}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    pprint(status.json())

    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAIfrbRUABoBANqfQRYeP97oJOgUZAqdgSHvlAoZBVe8YxSgXqRB09rvKdTiiCY7RfvL7IN0vYXpiEjcTDzmIhAZBWwwBbXR27ry6WHZBT1vvuBGHO9qtMWfPNvqohxDM1A4xA73QfYZBUZBtqJF36Xv9kEi4ZAZCaXvayjA1TtZBY3GT9iI9CCO6'
    response_msg = json.dumps(
        {"recipient": {"id": fbid}, "message": {"text": recevied_message}})
    status = requests.post(post_message_url, headers={
                           "Content-Type": "application/json"}, data=response_msg)
    pprint(status.json())


class YoMamaBotView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == '1234':
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        # Post function to handle Facebook messages
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Converts the text payload into a python dictionary
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        # Facebook recommends going through every entry since they might send
        # multiple messages in a single call during high load
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    # Print the message to the terminal
                    
                    # Assuming the sender only sends text. Non-text messages like stickers, audio, pictures
                    # are sent as attachments and must be handled accordingly. 
                    post_facebook_message(message['sender']['id'], message['message']['text'])
              
                    
        return HttpResponse()
