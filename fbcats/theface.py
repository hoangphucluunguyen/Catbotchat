from facebook_payload import payload_response_txt
class TheFace():
    def __init__(self,uid,msg,status):
        self.uid=uid
        self.msg=msg
        self.status=status

    def respond(self):
        kq={}
        kq['topic']='theface'
        kq['status']=self.status+1
        kq['phanhoi']=payload_response_txt(self.uid,"Ban chon chuong trinh thefae {}".format(self.msg))
        return kq
