from telegram.ext import Updater,CommandHandler



def start(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text = "Testing")

def startBot():
    #우선 처음에 Updater 객체를 생성해 주어야 한다. 이 객체에는 토큰이 위치해야한다
    updater = Updater(token = '', use_context=True)
    dispatcher = updater.dispatcher
    #커맨드를 저장해보자. 목표는 start라는 함수를 /start command를 받을떄 마다 실행하는 것이다
    #이를 하기 위해서는 CommandHandler를 사용하여야 한다.
    start_handler = CommandHandler('start',start)
    
    # CommandHandler : 텔레그램 커맨드를 handling하기 위한 클래스이다.https://python-telegram-bot.readthedocs.io/en/latest/telegram.ext.commandhandler.html
    dispatcher.add_handler(start_handler)
    #dispatcher에 핸들러 추가
    updater.start_polling()
    #start bot https://python-telegram-bot.readthedocs.io/en/latest/telegram.ext.updater.html#telegram.ext.updater.Updater.start_polling
    
    

if __name__=="__main__":
    startBot()
