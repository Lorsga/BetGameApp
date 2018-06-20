import telepot
import time
from firebase import firebase
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

def on_chat_message(pureMsg):
    content_type, chat_type, chat_id = telepot.glance(pureMsg)
    message = pureMsg['text']
    username = pureMsg['from']['username']
    if(message == '/start') :
        startMessage(username,chat_id)
        


def startMessage(username,chat_id) :
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Partecipa al torneo', callback_data='tournaments')],
            ])
    betGameBot.sendMessage(chat_id, 'Benvenuto in BetGameSoccer %s ! Partecipa subito al torneo !'%username, reply_markup=keyboard)
   
def messageButton(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)
    if query_data == 'tournaments' :
        tournamentList(from_id)
        

def tournamentList(from_id) :
    betGameBot.sendMessage(from_id,'Seleziona uno dei tornei!')

TOKEN = '567521864:AAEjrVpBEKkfTv--V39gdg9X3NIITqVMmXw'
betGameBot = telepot.Bot(TOKEN)
MessageLoop(betGameBot, {'chat': on_chat_message,
                        'callback_query': messageButton}).run_as_thread()

print('Listening...')

while 1:
    time.sleep(10)
