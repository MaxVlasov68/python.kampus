import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType
import random



TOKEN = "b1eb6e18f00883f160735fdba030821f3620db744e876b83e6df741bcdd13432d8ae232caf856efb79c19"
vk_session = vk_api.VkApi(token=TOKEN)


vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, "187554026")

filename="keyboard.json"
file = open(filename, "r", encoding="UTF-8")
main_keyboard=file.read()
# game_keyboard = open(filename, "r", encoding="UTF-8")
gameStarted = False
keyboard = main_keyboard
# keyboard = game_keyboard

def f(text):
    a=['1','2','3']
    if (text != 0) and (text != ''):
            b=random.choice(a)
            if  b == text :
                return 'WIN'
            elif b != text:
                return 'Game Over'
    s =  "спасибо за игру"

    return s
  
for event in longpoll.listen(): #Проверка действий
    print(event)
    if event.type == VkBotEventType.MESSAGE_NEW:          
        if event.obj.text != '':
            if event.from_user:
                text = event.obj.text
                if gameStarted:
                        reply = f(text)
                        gameStarted = False
                else:
                    if text ==  "Привет":
                        reply= "Привет,ты используешь Bot_Friend (≧ω≦) )"
                    elif (text=="Как дела?") or (text=="Как у тебя дела?") or (text=="Как настроение?"):
                        reply = "У меня все хорошо, как ты? <3 <3 <3 "
                    elif (text=="У меня все хорошо")or (text=="У меня все отлично") or (text=="У меня все плохо")or (text=="отлично")or (text=="хорошо")or (text=="плохо")or (text=="нормально"):
                        reply ="Здорово!  (≧ω≦) )"
                    elif text ==  "Начать":
                        reply= "Привет)"
                    elif text == "Где самые лучшие ребята?":
                        reply="В КамПусе <3 "
                    elif text== "Я освоил python ?":
                        reply = "Мой друг, ты освоил часть учебного материала, но тебе ещё нужно развиваться"
                    elif text == "Играть":
                        gameStarted = True
                        reply = 'введи число от 1 до 3'
                    elif text == "Я не играю":
                        reply ="Ладно, напиши в другое время, когда захочешь поиграть) <3 "
                    elif text == "Помощь":
                        reply="""--Привет
--Как дела?
--У меня все хорошо
--Начать
--Где самые лучшие ребята ?
--Я освоил python ?
--Играть
--Я не играю"""
                                
                    else:
                        reply="Bot_Friend не знает таких команд((("                
        if event.from_user:
            vk.messages.send(
            user_id=event.obj.from_id,
            random_id=get_random_id(),
            message=reply,
            keyboard=keyboard)
