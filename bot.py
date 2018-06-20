# -*- coding: utf-8 -*-
from linepy import *
from datetime import datetime
from time import sleep
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse, timeit
#登入
cl = LINE("Eu1NLO7arDSKlcfZ08p3.CJJqcfAXdwYNnFnJQs+SOW.Yb2vfresfgakL8nzhgl7F9/XnAHpmO4HGLWuHZ0GIBw=")
print ("Auth Token : " + str(cl.authToken))
oepoll = OEPoll(cl)
clMID,mbt = cl.profile.mid,cl.mbmmbmb()
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
}
setTime = {}
setTime = wait2['setTime']
wait = {
    'admin': {}
    }
readOpen = codecs.open("read.json","r","utf-8")
setbot = codecs.open("setting.json","r","utf-8")
groupset = codecs.open("groupset.json","r","utf-8")
pgroup = json.load(groupset)
read = json.load(readOpen)
setmain = json.load(setbot)
msg_dict = {}
bl = [""]
#reread=False
mbc=b'\xe6\x84\x9b\xe6\x84\x9b'
def backupData():
    try:
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = setmain
        f = codecs.open('setting.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = pgroup
        f = codecs.open('groupset.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def logError(text):
    cl.log("[ ERROR ] " + str(text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def sendMention(to, mid, firstmessage='', lastmessage=''):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        client.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)

def mentionSiders(to, firstmessage, lastmessage):
    try:
        mid = []
        if read["ROM"][to] == {} and read["readMember"] != {}:
            for ar in read["readMember"][to]:
                mid.append(ar)
        elif read["ROM"][to] == {} and read["readMember"][to] == {}:
            pass
        else:
            for ars in read["readMember"][to]:
                if ars not in read["ROM"][to]:
                    mid.append(ars)
        arrData = ""
        textx = str(firstmessage)
        arr = []
        if mid != []:
            for i in mid:
                textx += str("\n? ")
                mention = "@x "
                slen = str(len(textx))
                elen = str(len(textx) + len(mention) - 1)
                arrData = {'S':slen, 'E':elen, 'M':i}
                arr.append(arrData)
                textx += mention
            textx += str(lastmessage)
            client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        else:
            textx += str(lastmessage)
            client.sendMessage(to, textx)
    except:
        try:
            ret_ = str(firstmessage)
            sider = {}
            sider["name"] = ""
            if read["ROM"][to] == {} and read["readMember"][to] != {}:
                for ar in read["readMember"][to]:
                    contact = client.getContact(ar)
                    sider["name"] += "\n? {}".format(str(contact.displayName))
            elif read["ROM"][to] == {} and read["readMember"][to] == {}:
                pass
            else:
                for ars in read["readMember"][to]:
                    if ars not in read["ROM"][to]:
                        contact = client.getContact(ars)
                        sider["name"] += "\n? {}".format(str(contact.displayName))
            ret_ += str(sider["name"])
            ret_ += str(lastmessage)
            client.sendMessage(to, str(ret_))
        except Exception as error:
            logError(error)

def mentionMembers(to, mid):
    try:
        group = client.getGroup(to)
        mids = [mem.mid for mem in group.members]
        jml = len(mids)
        arrData = ""
        if mid[0] == mids[0]:
            textx = "???[ Mention {} User ]\n".format(str(jml))
        else:
            textx = ""
        arr = []
        for i in mid:
            no = mids.index(i) + 1
            textx += "? {}. ".format(str(no))
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
        if no == jml:
            textx += "???[ Success ]"
        client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        client.sendMessage(to, "[ INFO ] Error :\n" + str(error))        
def helpmessage():
    helpMessage = """
╔══════════════
╠════指令表════
╠ me
╠ 發送指令者友資
╠ mid
╠ 發送指令者MID
╠ op:(mid)
╠ 新增使用權限
╠ opd:(mid)
╠ 移除使用權限
╠ Speed
╠ 查看機器速度
╠ Set
╠ 查看設定
╠ Reread On/Off
╠ 收回功能 開啟/關閉
╠ welcome:On/Off
╠ 歡迎通知 開啟/關閉
╠ Protect:On/Off
╠ 群組保護 開啟/關閉
╠ groupname:On/Off
╠ 群名保護 開啟/關閉
╠ groupurl:On/Off
╠ 群組網址保護 開啟/關閉
╠ 進入通知:On/Off
╠ 進入提醒 開啟/關閉
╠ Delread
╠ 刪除已讀點
╠ Setread
╠ 設定已讀點
╠ Lookread
╠ 查詢已讀點
╠ Tagall
╠ 標註全部人
╠ 踢@
╠ 將標記人踢除
╠ 來回@
╠ 將標記人踢除並邀請
╚══════════════
"""
    return helpMessage
def lineBot(op):
    
    try:
        if op.type == 0:
            return
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            if msg.toType == 0:
                if msg._from != cl.profile.mid:
                    to = msg._from
                else:
                    to = msg.to
            else:
                to = msg.to
            if msg.contentType == 0:
                if text is None:
                    return
                if text.lower() == 'help':
                  if msg._from in setmain["adminlsit"]:    
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                elif text.lower() == 'me':
                    cl.sendContact(to,str(msg._from))
                    cl.sendMessage(to,str(msg._from))
                elif text.lower() == 'mid':
                    cl.sendMessage(to,str(msg._from))
                elif 'adminlist' in msg.text:
                    if msg._from in setmain["adminlsit"]:
                        if setmain["adminlsit"] == []:
                            cl.sendMessage(to,"無權限者")
                        else:
                            cl.sendMessage(to,"權限名單:")
                            mc = ""
                            for mi_d in setmain["adminlsit"]:
                                mc += ">>" +cl.getContact(mi_d).displayName + "\n"
                            cl.sendMessage(to,mc)
                elif 'op:' in msg.text:
                  if msg._from in setmain["adminlsit"]:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                           try:
                               setmain["adminlsit"][target] = True
                               backupData()
                               cl.sendMessage(to,"已給權限")
                           except:
                               cl.sendMessage(to,"錯誤")
                elif 'opd:' in msg.text:
                  if msg._from in setmain["adminlsit"]:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                           try:
                               del setmain["adminlsit"][target]
                               backupData()
                               cl.sendMessage(to,"已刪權限")
                           except:
                               cl.sendMessage(to,"錯誤")
                elif msg.text in ["SR","Setread"]:
                    cl.sendMessage(to, "設置已讀點")
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(datetime.now(),"%H:%M")
                elif msg.text in ["DR","Delread"]:
                    cl.sendMessage(to, "刪除已讀點")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                        del wait2['setTime'][msg.to]
                    except:
                        pass
                elif msg.text in ["LR","Lookread"]:
                    if msg.to in wait2['readPoint']:
                        cl.sendMessage(to, "||已讀的人||%s\n[%s]" % (wait2['readMember'][msg.to],setTime[msg.to]))
                    else:
                        cl.sendMessage(to, "請輸入SR設置已讀點")
                elif text.lower() == 'speed':
                  if msg._from in setmain["adminlsit"]:
                    str1 = str(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
                    start = time.time()
                    cl.sendMessage(to,'測試中～')
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,'處理速度\n' + str1 + '秒\n指令反應\n' + format(str(elapsed_time)) + '秒')
                elif text.lower() == 'set':
                  if msg._from in setmain["adminlsit"]:
                    a = ""
                    if setmain["reread"] == True: a+= "收回功能開啟 ✅\n"
                    else: a += "收回功能關閉 ❌\n"
                    if setmain["welcome"] == True: a+= "離開功能開啟 ✅\n"
                    else: a += "離開功能關閉 ❌\n"
                    if setmain["welcome"] == True: a+= "歡迎功能開啟 ✅\n"
                    else: a += "歡迎功能關閉 ❌\n"
                    if to in pgroup["protect"]: a+= "群組保護開啟 ✅\n"
                    else: a += "群組保護關閉 ❌\n"
                    if to in pgroup["groupname"]: a+= "群名保護開啟 ✅\n"
                    else: a += "群名保護關閉 ❌\n"
                    if to in pgroup["groupurl"]: a+= "網址保護開啟 ✅"
                    else: a += "網址保護關閉 ❌"
                    cl.sendMessage(to, str(a))
                elif text.lower() == 'reread on':
                  if msg._from in setmain["adminlsit"]:
                    setmain["reread"] = True
                    backupData()
                    cl.sendMessage(to, "收回功能開啟 ✅")
                elif text.lower() == 'reread off':
                  if msg._from in setmain["adminlsit"]:  
                    setmain["reread"] = False
                    backupData()
                    cl.sendMessage(to, "收回功能關閉 ❌")
                elif text.lower() == mbc.decode('utf-8'):
                    cl.sendMessage(to,mbt.decode('utf-8'))
                elif text.lower() == 'tagall':
                  if msg._from in setmain["adminlsit"]:
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//100
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*100 : (a+1)*100]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Fuck \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        cl.sendMessage(to, "成功標記 {} 位成員".format(str(len(nama))))
                elif "踢 " in text.lower():
                  if msg._from in setmain["adminlsit"]:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(to,[target])
                        except:
                            pass
                elif "來回 " in text.lower():
                  if msg._from in setmain["adminlsit"]:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.findAndAddContactsByMid(target)
                            cl.kickoutFromGroup(to,[target])
                            cl.inviteIntoGroup(to,[target])
                        except:
                            pass
                elif "邀請 " in text.lower():
                  if msg._from in setmain["adminlsit"]:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.findAndAddContactsByMid(target)
                            cl.inviteIntoGroup(to,[target])
                        except:
                            pass
                elif text.lower() == '進入通知:on':
                  if msg._from in setmain["adminlsit"]:
                    try:
                        pgroup["MemberJoinGroup"] = True
                        backupData()
                        cl.sendMessage(to,"已開啟")
                    except:
                        pass
                elif text.lower() == '進入通知:off':
                  if msg._from in setmain["adminlsit"]:
                    try:
                        pgroup["MemberJoinGroup"] = False
                        backupData()
                        cl.sendMessage(to,"已關閉")
                    except:
                        pass
                elif text.lower() == 'protect:on':
                  if msg._from in setmain["adminlsit"]:
                    try:
                        pgroup["protect"][to] = True
                        backupData()
                        cl.sendMessage(to,"已開啟保護")
                    except:
                        pass    
                elif text.lower() == 'protect:off':
                  if msg._from in setmain["adminlsit"]:
                    try:
                        del pgroup["protect"][to]
                        backupData()
                        cl.sendMessage(to,"已關閉保護")
                    except:
                        pass
                elif text.lower() == 'groupname:on':
                  if msg._from in setmain["adminlsit"]:
                    try:
                        pgroup["groupname"][to] = True
                        pgroup["group_name"][to] = cl.getGroup(to).name
                        backupData()
                        cl.sendMessage(to,"已開啟保護")
                    except:
                        pass    
                elif text.lower() == 'groupname:off':
                  if msg._from in setmain["adminlsit"]:
                    try:
                        del pgroup["groupname"][to]
                        backupData()
                        cl.sendMessage(to,"已關閉保護")
                    except:
                        pass
                elif text.lower() == 'groupnurl:on':
                  if msg._from in setmain["adminlsit"]:
                    try:
                        pgroup["groupurl"][to] = True
                        backupData()
                        cl.sendMessage(to,"已開啟保護")
                    except:
                        pass    
                elif text.lower() == 'groupurl:off':
                  if msg._from in setmain["adminlsit"]:
                    try:
                        del pgroup["groupurl"][to]
                        backupData()
                        cl.sendMessage(to,"已關閉保護")
                    except:
                        pass
                elif text.lower() == 'leavemessage:on':
                  if msg._from in setmain["adminlsit"]:
                    try:
                        setmain["leavemessage"] = True
                        backupData()
                        cl.sendMessage(to,"已開啟")
                    except:
                        pass    
                elif text.lower() == 'leavemessage:off':
                  if msg._from in setmain["adminlsit"]:
                    try:
                        setmain["leavemessage"] = False
                        backupData()
                        cl.sendMessage(to,"已關閉")
                    except:
                        pass
                elif text.lower() == 'welcome:on':
                  if msg._from in setmain["adminlsit"]:
                    try:
                        setmain["welcome"] = True
                        backupData()
                        cl.sendMessage(to,"已開啟")
                    except:
                        pass    
                elif text.lower() == 'welcome:off':
                  if msg._from in setmain["adminlsit"]:
                    try:
                        setmain["welcome"] = False
                        backupData()
                        cl.sendMessage(to,"已關閉")
                    except:
                        pass    
        if op.type == 13:
            if pgroup["MemberJoinGroup"] == True:
                try:
                    cl.sendMessage(op.param1,"有人邀請成員")
                except:
                    pass
        if op.type == 11:
            if op.param3 == '4':
                if op.param1 in pgroup["groupurl"]:
                    if op.param2 not in setmain["adminlsit"]:
                        group = cl.getGroup(op.param1)
                        if group.preventedJoinByTicket == False:
                            group.preventedJoinByTicket = True
                            cl.updateGroup(group)
                            cl.sendMessage(op.param1,"網址開啟\n更改者為:")
                            cl.sendContact(op.param1,op.param2)
                    else:
                        cl.sendMessage(op.param1,"網址開啟\n更改者為:")
                        cl.sendContact(op.param1,op.param2)
        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in pgroup["groupname"]:
                    if op.param2 not in setmain["adminlsit"]:
                        try:
                            cl.sendMessage(op.param1,"群名更改\n更改者為:")
                            cl.sendContact(op.param1,op.param2)
                            G = cl.getGroup(op.param1)
                            G.name = pgroup["group_name"][op.param1]
                            cl.updateGroup(G)
                            cl.sendMessage(op.param1,"已改回")
                        except:
                            pass
            else:
                if op.param3 == '1':
                    cl.sendMessage(op.param1,"群名更改\n更改者為:")
                    cl.sendContact(op.param1,op.param2)
                else:
                    pass
        if op.type == 19:
            msg = op.message
            chiya = []
            chiya.append(op.param2)
            chiya.append(op.param3)
            cmem = cl.getContacts(chiya)
            zx = ""
            zxc = ""
            zx2 = []
            xpesan ='通知:'
            for x in range(len(cmem)):
                xname = str(cmem[x].displayName)
                pesan = ''
                pesan2 = pesan+"@x →"
                xlen = str(len(zxc)+len(xpesan))
                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                zx2.append(zx)
                zxc += pesan2
            text = xpesan + zxc + "踢出群組"
            try:
                cl.sendMessage(op.param1, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
            except:
                cl.sendMessage(op.param1,"Notified kick out from group")
            if op.param1 in pgroup["protect"]:
                  if  op.param2  in setmain["adminlsit"] and op.param3 not in setmain["adminlsit"]:
                    pass  
                    
                  elif op.param2 not in setmain["adminlsit"] and op.param3  in setmain["adminlsit"]:
                    try:                        
                          cl.kickoutFromGroup(op.param1,[op.param2])
                          cl.findAndAddContactsByMid(op.param3)
                          cl.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        pass
            else:
                pass        
        if op.type == 15:
            print ("MEMBER LEAVE TO GROUP")
            try: 
                if setmain["leavemessage"] == True:
                    
                    ginfo = cl.getGroup(op.param1)
                    contact = cl.getContact(op.param2)
                    image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
                    #cl.sendImageWithURL(op.param1,image)
                    cl.sendContact(op.param1,str(op.param2))
                    cl.sendMessage(op.param1,"慢走不送\n " + cl.getContact(op.param2).displayName + " 離開了群組(´･ω･`)")
                    #cl.sendMessage(op.paraml, "慢走不送 @wanping 離開了群組(´･ω･`)" , contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
            except:
                cl.sendMessage(op.param1,"ERROR")
                
        if op.type == 17:
            
          #  ginfo = str(cl.getGroup(op.param1).name)
            try:
                if setmain["welcome"] == True:
                    strt = int(3)
                    akh = int(3)
                    akh = akh + 8
                    aa = """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(op.param2)+"},"""
                    aa = (aa[:int(len(aa)-1)])
                    cl.sendMessage(op.param1, "歡迎 @wanping 加入了群組(´･ω･`)" , contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
            except Exception as e:
                print(str(e))
        if op.type == 26:
            try:
                msg = op.message
                if setmain["reread"] == True:
                    if msg.toType == 2:
                        if msg.toType == 0:
                            cl.log("[%s]"%(msg._from)+msg.text)
                        else:
                            cl.log("[%s]"%(msg.to)+msg.text)
                        if msg.contentType == 0:
                            msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 65:
            print ("[ 65 ] REREAD")
            try:
                at = op.param1
                msg_id = op.param2
                if setmain["reread"] == True:
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"] not in bl:
                            timeNow = datetime.now()
                            timE = datetime.strftime(timeNow,"(%y-%m-%d %H:%M:%S)")
                            try:
                                strt = int(3)
                                akh = int(3)
                                akh = akh + 8
                                aa = """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(msg_dict[msg_id]["from"])+"},"""
                                aa = (aa[:int(len(aa)-1)])
                                
                                cl.sendMessage(at, "收回訊息者 @wanping ", contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                            except Exception as e:
                                print(str(e))
                           
                            cl.sendMessage(at,"[收回訊息者]\n%s\n[訊息內容]\n%s"%(cl.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"]))
                            cl.sendMessage(at,"/n發送時間/n"+strftime("%y-%m-%d %H:%M:%S")+"/n收回時間/n"+timE)
                            
                        del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print (e)
        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n[※]" + Name
                        wait2['ROM'][op.param1][op.param2] = "[※]" + Name
                        print (time.time() + name)
                else:
                    pass
            except:
                pass
    except Exception as error:
        logError(error)
#==============================================================================#
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
