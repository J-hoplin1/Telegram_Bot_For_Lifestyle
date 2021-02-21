'''
이번에는 커맨드가 아닌 메세지에 반응하는 커맨드를 만들어보자 

사실 이부분은 안쓸꺼같긴한데
https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot
'''
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters

def echo(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    
# 매개변수를 받는 부분
def caps(update, context):
    # print(context.args) #arguments를 리스트로 반환 매개변수가 없으면 telegram.error.BadRequest: Message text is empty 를 보낸다
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

def startBot():
    updater = Updater(token = '', use_context=True)
    dispatcher = updater.dispatcher
    echoHandelr = MessageHandler(Filters.text & (~Filters.command), echo) # MessageHandler()의 첫번쨰 매개변수는 필터이다.
    caps_handler = CommandHandler('caps', caps)
    dispatcher.add_handler(caps_handler)
    dispatcher.add_handler(echoHandelr)
    updater.start_polling()
    
if __name__=="__main__":
    startBot()
