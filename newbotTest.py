# -*- coding: utf-8 -*-
import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,random

cl = LINETCR.LINE()
cl.login(token = "Em8E2LSbEzJK5IaXM9rd.9iHYe2N0JDi7v/ZccJo5Fq.7rDN8vYLYqAZWPNK6quWFvYZZnpxKLrxObu4W33fVzQ=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token = "EndEzUOOyuVBATfnqa74.bOTjwJ4IY6/M4ng+aUJmLa.MV9+3p3YkaU/utEtkeRnkY+K81Oy2xIh6lPLSntuidA=")
ki.loginResult()

kk = kc = cl

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""
"""
KAC=[cl,ki,kk,kc]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
OOO = []
Bots=[mid,Amid]
lucky = ["大吉","吉","凶","大凶"]
admin=["uf488721369f48dd23b57ecc20a33b97d","u54993d23db22d0787d7e58417578e635","u7d8710559bda136ae7030477f83069df","u6a71cd21be3446e85a70e964c6478a06"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':False,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me",
    "lang":"JP",
    "MMM":"未設定",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
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
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                cl.acceptGroupInvitation(op.param1)
                cl.sendText(op.param1,"九条拡散機械 降临です\n" + str(wait["MMM"]))
            else:
                pass
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
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
        if op.type == 25:
            msg = op.message
            if "Share:" in msg.text:
                midd = msg.text.replace("Share:","")
                try:
                    wait["MMM"] = midd
                    cl.sendText(msg.to,"增加完成")
                except:
                    pass
            elif "查看擴散" in msg.text:
                cl.sendText(msg.to,"現在訊息:\n" + str(wait["MMM"]))
                pass
            elif "擴散中" in msg.text:
                gid = cl.getGroupIdsJoined()
                for i in gid:
                  cl.sendText(i,str(wait["MMM"]))
            elif msg.text in ["Sp","Speed","speed"]:
                if msg.from_ in admin:
                  start = time.time()
                  cl.sendText(msg.to, "Progress...")
                  elapsed_time = time.time() - start
                  cl.sendText(msg.to, "%sseconds" % (elapsed_time))
            elif "Mid @" in msg.text:
                if msg.from_ in admin:
                  _name = msg.text.replace("Mid @","")
                  _nametarget = _name.rstrip(' ')
                  gs = cl.getGroup(msg.to)
                  for g in gs.members:
                      if _nametarget == g.displayName:
                          cl.sendText(msg.to, g.mid)
                      else:
                          pass
            elif "運勢" in msg.text:
                if msg.from_ in admin:
                  try:
                      ss =random.choice(lucky)
                      cl.sendText(msg.to,ss)
                  except:
                      pass
            elif msg.text in ["高調進入","高調加入"]:
                if msg.from_ in admin:
                    G = ki.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    print "EXECUTED -- SUMMON BOT"
                    Ticket = ki.reissueGroupTicket(msg.to)
                    cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = ki.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
            elif msg.text in ["星星進入","星星加入"]:
                if msg.from_ in admin:
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    print "EXECUTED -- SUMMON BOT"
                    Ticket = cl.reissueGroupTicket(msg.to)
                    ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
        if op.type == 26:
            msg = op.message
            if msg.text is None:
                return
            elif msg.text in ["高調進入","高調加入"]:
                if msg.from_ in admin:
                    G = ki.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    print "EXECUTED -- SUMMON BOT"
                    Ticket = ki.reissueGroupTicket(msg.to)
                    cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = ki.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
            elif msg.text in ["星星進入","星星加入"]:
                if msg.from_ in admin:
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    print "EXECUTED -- SUMMON BOT"
                    Ticket = cl.reissueGroupTicket(msg.to)
                    ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
            elif "運勢" in msg.text:
                if msg.from_ in admin:
                  try:
                      ss =random.choice(lucky)
                      cl.sendText(msg.to,ss)
                  except:
                      pass
            elif "Share:" in msg.text:
                if msg.from_ in admin:
                  midd = msg.text.replace("Share:","")
                  try:
                      wait["MMM"] = midd
                      cl.sendText(msg.to,"增加完成")
                  except:
                      pass
            elif "查看擴散" in msg.text:
                if msg.from_ in admin:
                  cl.sendText(msg.to,"現在訊息:\n" + str(wait["MMM"]))
                  pass
            elif "擴散中" in msg.text:
                if msg.from_ in admin:
                  gid = cl.getGroupIdsJoined()
                  for i in gid:
                    cl.sendText(i,str(wait["MMM"]))
            elif "Mid @" in msg.text:
                if msg.from_ in admin:
                  _name = msg.text.replace("Mid @","")
                  _nametarget = _name.rstrip(' ')
                  gs = cl.getGroup(msg.to)
                  for g in gs.members:
                      if _nametarget == g.displayName:
                          cl.sendText(msg.to, g.mid)
                      else:
                          pass
#-----------------------------------------------
            elif msg.text in ["Sp","Speed","speed"]:
                if msg.from_ in admin:
                  start = time.time()
                  cl.sendText(msg.to, "Progress...")
                  elapsed_time = time.time() - start
                  cl.sendText(msg.to, "%sseconds" % (elapsed_time))

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

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
