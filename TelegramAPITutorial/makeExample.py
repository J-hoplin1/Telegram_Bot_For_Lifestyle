import logging
from telegram.ext import Updater,CommandHandler
from commandEngine.covid19 import start

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)    

class botCommandManager(object):
    def __init__(self,updater,dispatcher):
        self.updater = updater
        self.dispatcher = dispatcher
        test1Handler = CommandHandler('test1',self.test1)
        dispatcher.add_handler(test1Handler)
        covid19Handler = CommandHandler('covidkr',self.covid19)
        dispatcher.add_handler(covid19Handler)
        
    def test1(self,update,context):
        context.bot.send_message(chat_id=update.effective_chat.id,text = "Testing")
    
    def covid19(self,update,context):
        value = start()
        updated = f'Recent Updated in {value[0]}\n'
        newPatient = f'Today new Patinet : {value[1]}\n'
        totalPatient = f'Total Covid-19 Korea Patients : {value[2]}\n'
        treatMentCompleted = f'Treatment Completed : {value[3]}\n'
        underTreatment = f'Undertreatment : {value[4]}\n'
        totaldeath = f'Total Death : {value[5]}'
        textPar = updated + newPatient + totalPatient + treatMentCompleted + underTreatment + totaldeath
        context.bot.send_message(chat_id = update.effective_chat.id,text=textPar)
    
    def stream(self):
        self.updater.start_polling()
        self.updater.idle()

def startBotProcess():
    updater = Updater(token = '', use_context=True)
    dispatcher = updater.dispatcher
    bot = botCommandManager(updater,dispatcher)
    bot.stream()
    
if __name__=="__main__":
    startBotProcess()
