import vk_api
import time
from vk_api.longpoll import VkLongPoll, VkEventType , VkPeerFlag
vkc= vk_api.VkApi(token="9207d0e06c5b6cc2f515b356a5792cae46fba6b9de75959e7d31103c296afe52b1194c7704394d6a5c700")
vk = vkc.get_api()
longpoll = VkLongPoll(vkc)
def sendmess(id,text):
  vkc.method('messages.send',{'user_id':id,'message':text,'random_id':0})
def sendmess2(id2,text):
  vkc.method('messages.send',{'chat_id':id2,'message':text,'random_id':0})
fdd=0
def startanim(kdd,usid):
  print(usid)
  vkc.method('messages.edit',{'peer_id':usid,'message_id':kdd,'message':"Ой",'random_id':0})
  time.sleep(2)
  vkc.method('messages.edit',{'peer_id':usid,'message_id':kdd,'message':"[marysiiiioo|Машуля]",'random_id':0})
  time.sleep(2)
  vkc.method('messages.edit',{'peer_id':usid,'message_id':kdd,'message':"Люблю",'random_id':0})
  time.sleep(2)
  vkc.method('messages.edit',{'peer_id':usid,'message_id':kdd,'message':"тебя",'random_id':0})
  time.sleep(2)
  vkc.method('messages.edit',{'peer_id':usid,'message_id':kdd,'message':"солнце",'random_id':0})
  time.sleep(2)
  vkc.method('messages.edit',{'peer_id':usid,'message_id':kdd,'message':"хых",'attachment':"photo211977236_457244672",'random_id':0})
  time.sleep(2)
def deadcode():
	sendmess2(142,"++++++ [marysiiiioo|Машуля]")
	sendmess2(142,"++++++ [xxxxlonerxxxx|Илья]")
	sendmess2(142,"++++++ [kaspesky|Каспейский]")
	sendmess2(142,"++++++ [alexanderastro|Сашуля]")
	sendmess2(142,"++++++ [matveyio|Мотвей]")
	sendmess2(142,"++++++ [anechka_carter|Анечка]")
	sendmess2(142,"++++++ [tulskiy71ru|никитка]")
	sendmess2(142,"++++++ [firraa|Настюшка]")
	sendmess2(142,"++++++ [11denis11|Дениска]")
	sendmess2(142,"++++++ [fackk_yoou|Назарчик]")
	sendmess2(142,"++++++ [cuhan|Чечен]")
	sendmess2(142,"++++++ [andrey_1sever|Андрейка]")
	sendmess2(142,"++++++ [kotelnikov|Гейкакойта]")
	
while True:
    try:
      deadcode()
      time.sleep(86400)
    except Exception as error:
        print(error)
