from facebook_payload import payload_response_txt
class Begin():
    def __init__(self,uid,msg,status):
        self.uid=uid
        self.msg=msg
        self.status=status

    def respond(self):
        kq={}
        if self.msg=="The Face":
            kq['topic']="theface"
        elif self.msg=="VoiceKid":
            kq['topic'] = "TheFace"
        else:
            kq['topic']='begin'

        kq['status']=self.status+1
        kq['phanhoi']=payload_response_txt(self.uid,"Ban chon {}".format(self.msg))
        return kq
