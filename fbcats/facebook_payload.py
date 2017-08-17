import json

def payload_response_txt(uid,msg):
    payload=dict(recipient=dict(id=uid),message=dict(text=msg))
    return json.dumps(payload)

def payload_response_image(uid,url):
    payload=dict(recipient=dict(id=uid),message=dict(attachment=dict(type="image",payload=dict(url=url))))
    return json.dumps(payload)

def payload_response_quick(uid,):
    payload=dict(recipient=dict(id=uid),message=dict(text="Chon mau sac",quick_replies=[dict(content_type="text",title="RED",payload="Chon mau do"),dict(content_type="text",title="BLUE",payload="Chon mau xanh")]))
    return json.dumps(payload)

