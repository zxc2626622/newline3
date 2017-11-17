# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob

cl = LINETCR.LINE()
cl.login(token="EmuRJMvgdXsFbHsIDUQe.ZQs77UR8dD0/ViI2S3UVFG.XtVAWhYQ4uipk0/HLubMw6Mtk/yPlsDq9z9XL3vkArU=")
cl.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""====[Help]====\n輸入-->[#Check2]設定讀取點\n輸入-->[#See2]查看已讀\n[以上注意事項]\n .如果發現已讀數跟實際出來的人數不一樣請重新[#check2]\n輸入-->[#Invite2:MID]可以邀請MID\n[以上注意事項]\n1.是用mid邀請如果要拿去好友的Mid,請丟出友資即會顯示,把那串mid放在 : 後面即可邀請\n輸入-->[#Me2 @]此功能需要標註 獲得標註人的友資\n輸入-->[#Mid2 @]此功能需要標註 獲得標註人的MID\n[以上兩個標註注意事項]\n1.開頭都要大寫其餘小寫\n2.輸入完#Mid2 #Me2 後要空一格\n輸入-->[#Yid]可獲取自己MID\n輸入-->[#Ginfo2]可查看群組資料\n輸入-->[#Cancel2]可以取消邀請\n輸入-->[#Bye2]機器離開群組\n====[功能有待增加]====\n====[重要 此為很重要一定要看!!]====\n1.不要私訊傳指令\n2.不要過度猛玩怕壞掉\n3.如果進群之後,輸入指令沒有用,請邀請官方翻譯機進來群組,發幾次指令之後在退翻譯機\n4.如果早上發現機器沒回應,不是壞掉而是關閉機器\n製作者:\nhttp://line.me/ti/p/~fang_xin\n\nhttp://line.me/ti/p/~.90.11.24.\n\n\n如果機器沒有動作\n請把下面這隻邀進群組\nhttp://line.me/ti/p/~@zdb7366g"""
KAC=[cl]
mid = cl.getProfile().mid

Bots=[mid]
admin=["ucd9332352d3460cbca62f39047a990fe","u7d8710559bda136ae7030477f83069df","ucea4bbeeeafc0ddd3ebc88b6b37baf7e"]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"",
    "lang":"JP",
    "comment":"====[已讀機]====\nhttp://line.me/ti/p/~fang_xin\nAuto like By fung xin 放芯",
    "commentOn":True,
    "likeOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":True
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


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
                    cl.sendText(op.param1,helpMessage)
                    c = Message(to=op.param1, from_=None, text=None, contentType=13)
                    c.contentMetadata={'mid':'u219cfb34db6d3dc96a35023a74579bc0'}
                    cl.sendMessage(c)
                    cl.sendText(op.param1,"如果進群無動作請邀↑↑這隻")
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (helpMessage in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,helpMessage)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message
            if "AGc2 " in msg.text:
              if msg.from_ in admin:
                bctxt = msg.text.replace("AGc2 ","")
                gid = cl.getGroupIdsJoined()
                for i in gid:
                  cl.sendText(i,(bctxt))
            elif "AGbye2" in msg.text:
              if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                for i in gid:
                  cl.leaveGroup(i)
            elif msg.text in ["Join on","Auto join:on"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已開啟")
                    else:
                        cl.sendText(msg.to,"完成")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已開啟")
                    else:
                        cl.sendText(msg.to,"完成")
            elif msg.text in ["Join off","Auto join:off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已關閉")
                    else:
                        cl.sendText(msg.to,"完成")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已關閉")
                    else:
                        cl.sendText(msg.to,"完成")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已開啟")
                    else:
                        cl.sendText(msg.to,"完成")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"完成")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已關閉")
                    else:
                        cl.sendText(msg.to,"完成")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"完成")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["#help","#Help","help","Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif "Invite:" in msg.text:
                midd = msg.text.replace("Invite:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["cancel","Cancel"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"沒有邀請")
                        else:
                            cl.sendText(msg.to,"沒有邀請")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["ginfo","Ginfo"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "關閉中"
                        else:
                            u = "開啟中"
                        cl.sendText(msg.to,"[群組名稱]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[群創者]\n" + gCreator + "\n[群組圖片]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n成員:" + str(len(ginfo.members)) + "\n邀請中人數:" + sinvitee + "\n網址:" + u)
                    else:
                        cl.sendText(msg.to,"[群組名稱]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[群創者]\n" + gCreator + "\n[群組圖片]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["check","Check"]:
                cl.sendText(msg.to, "[輸入See查看已讀(｀・ω・´)]")
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
	            pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                wait2['ROM'][msg.to] = {}
                print wait2
            elif msg.text in ["see","See"]:
		  if msg.to in wait2['readPoint']:
	            if wait2["ROM"][msg.to].items() == []:
	              chiya = ""
	            else:
	              chiya = ""
	              for rom in wait2["ROM"][msg.to].items():
	                print rom
	                chiya += rom[1] + "\n"

	            cl.sendText(msg.to, "↓↓↓↓↓↓↓↓↓↓已讀的人↓↓↓↓↓↓↓↓↓↓%s"  % (wait2['readMember'][msg.to]))
	          else:
	            cl.sendText(msg.to, "[請先輸入Check讀取已讀點]")
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

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[名稱]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[個性簽名]:\n" + contact.statusMessage + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[主頁照片網址]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[名稱]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[個性簽名]:\n" + contact.statusMessage + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[主頁照片網址]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["#help2","#Help2"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)

            elif "#Invite2:" in msg.text:
                midd = msg.text.replace("#Invite2:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["#cancel2","#Cancel2"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"沒有邀請")
                        else:
                            cl.sendText(msg.to,"沒有邀請")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["#ginfo2","#Ginfo2"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "關閉中"
                        else:
                            u = "開啟中"
                        cl.sendText(msg.to,"[群組名稱]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[群創者]\n" + gCreator + "\n[群組圖片]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n成員:" + str(len(ginfo.members)) + "\n邀請中人數:" + sinvitee + "\n網址:" + u)
                    else:
                        cl.sendText(msg.to,"[群組名稱]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[群創者]\n" + gCreator + "\n[群組圖片]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["#Yid","#yid"]:
                cl.sendText(msg.to,msg.from_)
            elif "#Mid2 @" in msg.text:
                _name = msg.text.replace("#Mid2 @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
            elif "#Me2 @" in msg.text:
                msg.contentType = 13
                _name = msg.text.replace("#Me2 @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        msg.contentMetadata = {'mid': g.mid}
                        cl.sendMessage(msg)
                    else:
                        pass
            elif msg.text in ["#check2","#Check2"]:
                cl.sendText(msg.to, "[輸入#See2查看已讀(｀・ω・´)]")
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
	            pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                wait2['ROM'][msg.to] = {}
                print wait2
            elif msg.text in ["#see2","#See2"]:
		  if msg.to in wait2['readPoint']:
	            if wait2["ROM"][msg.to].items() == []:
	              chiya = ""
	            else:
	              chiya = ""
	              for rom in wait2["ROM"][msg.to].items():
	                print rom
	                chiya += rom[1] + "\n"

	            cl.sendText(msg.to, "↓↓↓↓↓↓↓↓↓↓已讀的人↓↓↓↓↓↓↓↓↓↓%s"  % (wait2['readMember'][msg.to]))
	          else:
	            cl.sendText(msg.to, "[請先輸入#Check2讀取已讀點]")
            elif msg.text in ["#Cancelall"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                    print "SUKSES -- SEND CANCELALL"
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"全部邀請已清除")
                else:
                    cl.sendText(msg.to,"錯誤")
            elif msg.text in ["#所有數量"]:
                gid = cl.getGroupIdsJoined()
                fid =  cl.getAllContactIds()
                Iid =  cl.getGroupIdsInvited()
                if Iid is None:
                    Iid = "0"
                else:
                    Iid = cl.getGroupIdsInvited()
                cl.sendText(msg.to,"群組:" + str(len(gid)) + "\n群組邀請中:" + str(len(Iid)) + "\n好友:" + str(len(fid)))
#-----------------------------------------------
#-----------------------------------------------
            elif msg.text in ["#Bye2","#bye2"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)
                    except:
                        pass
#----------------------------------------------------------------------------------
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n☑" + Name
                        wait2['ROM'][op.param1][op.param2] = "☑" + Name
                else:
                    cl.sendText
            except:
                  pass              
#-----------------------------------------------------
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
def autoSta():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()

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
