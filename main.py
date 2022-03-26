import random, vk_api, vk, os
from dotenv import dotenv_values
config_values = dotenv_values(".env")

vk_session = vk_api.VkApi(token=config_values["BOT_TOKEN"])
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
longpoll = VkBotLongPoll(vk_session, config_values["BOT_ID"])

from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType

vk = vk_session.get_api()
Lslongpoll = VkLongPoll(vk_session)
Lsvk = vk_session.get_api()

keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Привет', color=VkKeyboardColor.NEGATIVE)
keyboard.add_button('Клавиатура', color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_location_button()
keyboard.add_line()
keyboard.add_vkpay_button(hash=config_values["VK_PAY_HASH"])

""" 
TODO: джерри укусить
TODO: джерри лизнуть
TODO: джерри отлизать
TODO: джерри поцеловать
TODO: джерри ударить
TODO: джерри задушить
TODO: джерри сделать массаж
TODO: джерри напасть
"""

# *Привет!!!!!
hello_phrases=['Ку', 'Привет', 'Хай', 'Хеллоу']


# *Писька!!!!!
piska_phrases=['Джерри писька']

piska_answers=['Я Джерри! А ты псина!! Не обзывайся!!!!', 'Сам такой >:(', 'Да.', 'Зато большая!']

# *Трахнуть!!!!!
fuck_phrases=['Джерри трахнуть']

fuck_pool=['photo-212141154_457239024', 
'photo-212141154_457239028', 
'photo-212141154_457239029', 
'photo-212141154_457239030', 
'photo-212141154_457239031', 
'photo-212141154_457239032']

fuck_answers=['{}, ты конечно не дракон, но {} хотел(а) бы тебя так же',
'Был произведён акт секса с {}',
'{} был трахнут {}']


# *Обнять!!!!!
hug_phrases=['Джерри обнять']
hug_pool=['photo-212141154_457239042',
'photo-212141154_457239043']

hug_answers=['{} тебя крепко обнял(а) {}',
'{}, {} передаёт тебе, что всё будет хорошо',
'{}, кто грустит тот трансвестит!!',
'{}, тебя любят и ценят!']


# *Спать!!!!!
sleep_phrases=['Споки',
'Сладких снов',
'Спокойной ночи',
'Чпокен нокен']

sleep_pool=['photo-212141154_457239036',
'photo-212141154_457239037',
'photo-212141154_457239038',
'photo-212141154_457239039',
'photo-212141154_457239040',
'photo-212141154_457239041',
'photo-212141154_457239046']

sleep_answers=['Спокен нокен!', 
'Споки ноки', 
'Сладких влажных снов отважных', 
'Ты конечно не луна но на тебя я тоже заглядываюсь по ночам',
'Спокойной ночи, сучки мои)0))']


# *Напасть!!!!!
attack_phrases=['Джерри напасть', 'Джерри атаковать']

attack_pool=['photo-212141154_457239033',
'photo-212141154_457239034',
'photo-212141154_457239035',
'photo-212141154_457239044',
'photo-212141154_457239045',
]

attack_answers=['{} откусил жопу {}',
'{} был укушен {}',
'{} лишился жопы']


# *Душнота!!!!!
stuffy_phrases=['душнит', 'надушнил']
stuffy_pool=['photo-212141154_457239047',
'photo-212141154_457239048',
'photo-212141154_457239049',
'photo-212141154_457239050',
'photo-212141154_457239051']

stuffy_answers=['Ужас, {} надушнил', 
'Мдаааа, {} навалил кринжа', 
'Капец {} навалил', 
'После {} надо открыть форточку']

def form_link(id: int, name: str) -> str:
    return '[id{}|{}]'.format(id, name)

user = vk_session.method("users.get", {"user_ids": 173131506})
fullname = user[0]['first_name'] +  ' ' + user[0]['last_name']

print(fullname)

def menu(event):
    text = '''Привет! Я -- Джерри, Женина псина (собака), и я знаю следующие команды:
    Джерри писька
    Привет
    Джерри трахнуть [кого (чел из чата)]
    Джерри напасть/Джерри атаковать [кого (чел из чата)]
    Джерри обнять [кого (чел из чата)]
    [кто (чел из чата)] душнит/надушнил'''

    vk.messages.send(
                key = (config_values["BOT_KEY"]),
                server = (config_values["SERVER_ADDRESS"]),
                ts=('13'),
                random_id = get_random_id(),
      	        message=text,
    	        chat_id = event.chat_id
                )
    

def callback_to_message(event, callback: str, to: str, of: str, pool: list = None):
    if event.from_chat:
        if pool == None:
            vk.messages.send(
                key = (config_values["BOT_KEY"]),
                server = (config_values["SERVER_ADDRESS"]),
                ts=('13'),
                random_id = get_random_id(),
      	        message=callback,
    	        chat_id = event.chat_id
                )
        elif to == '[id-1|]':
            vk.messages.send(
                key = (config_values["BOT_KEY"]),
                server = (config_values["SERVER_ADDRESS"]),
                ts=('13'),
                random_id = get_random_id(),
      	        message=callback.format("", ""),
                attachment=random.choice(pool),
    	        chat_id = event.chat_id
                )
        else:
            vk.messages.send(
                key = (config_values["BOT_KEY"]),
                server = (config_values["SERVER_ADDRESS"]),
                ts=('13'),
                random_id = get_random_id(),
      	        message=callback.format(of, to),
                attachment=random.choice(pool),
    	        chat_id = event.chat_id
                )


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        # print(event)
        # print(event.message.from_id)
        str_event = event.message.text
        if str_event.find('[id') != -1:
            to_id = int(str_event[str_event.find('[id') + 3:str_event.find('|')])
            of_id = event.message.from_id
            of_name = vk_session.method("users.get", {"user_ids": of_id})[0]['first_name']
            to_name = vk_session.method("users.get", {"user_ids": to_id})[0]['first_name']
        else:
            to_id = of_id = -1
            to_name = of_name = ""
        if any(item in str(event) for item in hello_phrases):
            callback_to_message(event, 'Привет')

        if any(item in str(event) for item in piska_phrases):
            callback_to_message(event, random.choice(piska_answers))

        if any(item in str(event) for item in fuck_phrases):
            callback_to_message(event, random.choice(fuck_answers), form_link(of_id, of_name), form_link(to_id, to_name), pool=fuck_pool)

        if any(item in str(event) for item in hug_phrases):
            callback_to_message(event, random.choice(hug_answers), form_link(of_id, of_name), form_link(to_id, to_name), pool=hug_pool)

        if any(item in str(event) for item in sleep_phrases):
            callback_to_message(event, random.choice(sleep_answers), form_link(of_id, of_name), form_link(to_id, to_name), pool=sleep_pool)

        if any(item in str(event) for item in attack_phrases):
            callback_to_message(event, random.choice(attack_answers), form_link(of_id, of_name), form_link(to_id, to_name), pool=attack_pool)

        if any(item in str(event) for item in stuffy_phrases):
            callback_to_message(event, random.choice(stuffy_answers), form_link(of_id, of_name), form_link(to_id, to_name), pool=stuffy_pool)
        if "Джерри помощь" in str(event):
                menu(event)


# for event in Lslongpoll.listen():
#     if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
#         print("New event!!!")
#         vars1 = ['Привет', 'Ку', 'Хай', 'Хеллоу']
#         if event.text in vars1:
#             if event.from_user:
#                 Lsvk.messages.send(
#                     user_id = event.user_id,
#                     message = 'Привет)',
#                     random_id = get_random_id()
#                     )
#         vars2 = ['Клавиатура', 'клавиатура']
#         if event.text in vars2:
#             if event.from_user:
#                 Lsvk.messages.send(
#                     user_id = event.user_id,
#                     random_id = get_random_id(),
#                     keyboard = keyboard.get_keyboard(),
#                     message = 'Держи'
#                     )

