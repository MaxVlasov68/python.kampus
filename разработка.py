import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType
from vk_api.keyboard import VkKeyboard
from vk_api.keyboard import VkKeyboardColor
import random




TOKEN = "b1eb6e18f00883f160735fdba030821f3620db744e876b83e6df741bcdd13432d8ae232caf856efb79c19"
vk_session = vk_api.VkApi(token=TOKEN)

vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, "187554026")

def f():
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:                  
            if event.obj.text != '':
                if event.from_user:
                    c = event.obj.text
                    a=['1','2','3']
                    if (c != 0) and (c != ''):
                            b=random.choice(a)
                            if  b == c :
                                return 'WIN'
                            elif b != c:
                                return'Game Over'
                    reply="спасибо за игру"
                                  


for event in longpoll.listen(): #Проверка действий
    print(event)
    if event.type == VkBotEventType.MESSAGE_NEW:                  
        if event.obj.text != '':
            if event.from_user:
                text= event.obj.text
                if text ==  "Привет":
                    reply= "Ты используешь Bot_Friend)"
                elif (text=="Как дела?") or (text=="Как у тебя дела?") or (text=="Как настроение?"):
                    reply = "У меня все хорошо, как ты? <3 <3 <3"
                elif (text=="У меня все хорошо")or (text=="У меня все отлично") or (text=="У меня все плохо")or (text=="отлично")or (text=="хорошо")or (text=="плохо")or (text=="нормально"):
                    reply ="мне нужно писать более полезный код"
                elif text ==  "Начать":
                    reply= "Привет)"
                elif text =="Играть":
                    reply = "Введите число от 1 до 3"
                    f()
                elif text == "Я не играю":
                    reply ="Ладно, напиши в другое время, когда захочешь поиграть) <3 "               
                        
                else:
                    reply="Bot_Friend не знает таких команд((("                
        if event.from_user:
            vk.messages.send(
            user_id=event.obj.from_id,
            random_id=get_random_id(),
            message=reply)
