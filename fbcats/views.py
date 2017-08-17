# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json,requests,time
from django.http import HttpResponse
from facebook_payload import payload_response_quick
from models import NguoiDung
from begin import Begin
from theface import TheFace

@csrf_exempt
def webhook(request):
    if request.method == 'GET':
        if request.GET['hub.verify_token'] == "299198611092012":
            return HttpResponse(request.GET['hub.challenge'])
        else :
            return HttpResponse('Error, invalid token')
    elif request.method == 'POST':
        incomming_mesage = json.loads(request.body.decode('utf-8'))
        for entry in incomming_mesage['entry']:
            for message in entry['messaging']:
                uid= message['sender']['id']
                msg= message['message']['text']
                if NguoiDung.objects.filter(uid=uid):
                    nguoidung=list(NguoiDung.objects.filter(uid=uid).values())[0]
                    topic=nguoidung['topic']
                    status=nguoidung['status']
                else:
                    nguoidung=NguoiDung(uid=uid,lastcontact=time.ctime(),topic="begin",status="0")
                    nguoidung.save()
                    topic="begin"
                    status=0

                cautraloi=xuly_msg(uid,msg,topic,status)
                post_facebook_message(cautraloi)
        return HttpResponse()

def post_facebook_message(payload):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAYehmpLlIABADMZCePBzCgYMZCwhxtpNDT7fiXHZBEkgpEHNH3RqbmEaIDn9pFJHdbwy92k7lZCINHoamEGB3O3VDP8BQuIyggjaOJ8Xre7g6PURP5ZBDishQ1y5jWKKRBriEXUexPnN0OdnHpUUHWoLmjSt9zQQepG1wsk7lwZDZD'
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=payload)
    print payload

def xuly_msg(uid,msg,topic,status):
    if topic == "begin":
        phanhoi = Begin(uid,msg,status).respond()
    elif topic == "theface":
        phanhoi = TheFace(uid, msg, status).respond()

    nguoidung = NguoiDung.objects.filter(uid=uid)[0]
    nguoidung.status = phanhoi['status']
    # print phanhoi['topic']
    nguoidung.topic = phanhoi['topic']
    nguoidung.save()
    return phanhoi['phanhoi']

