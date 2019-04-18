from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
import logging
import copy
import cv2, os
import numpy as np
from keras.models import model_from_json
import tensorflow as tf

label_dictionary = {0: 'Early Blight', 1: 'Healthy', 2: 'Late Blight'}

json_file = open('model/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights("model/model.h5")

graph = tf.get_default_graph()

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def start_handler(bot, update):
    bot.send_message(update.message.chat_id, text='Upload the image of Infected Area.')

def photo_handler(bot, update):
    if update.message.photo != []:
        upd = copy.deepcopy(update.to_dict())
        user_id = update.message.from_user.id
        f_name = update.message.from_user.first_name
        l_name = update.message.from_user.last_name
        content['user_id'] = user_id
        if l_name is None:
            content['name'] = f_name
        else:
            content['name'] = f_name + ' ' + l_name
        content['file_info'] = update.message.photo[-1].get_file()['file_path']
        image = update.message.photo[-1].get_file().download('./temp/' + str(update.message.chat_id) + '.jpg')
    
    img_path = './temp/' + str(update.message.chat_id) + '.jpg'
    img = cv2.imread(img_path)
    output = cv2.resize(img, (256, 256)).copy()
    img = cv2.resize(img, (128, 128))
    img = img / 255
    with graph.as_default():
        proba = model.predict(img.reshape(-1, 128, 128, 3))
    
    idx = np.argmax(proba)

    res = label_dictionary[idx]
    cc = str(np.max(proba) * 100)[:5]

    bot.send_message(chat_id=update.message.chat_id, text="{} Detected with Confidence {}".format(res, cc))

def main():
    TOKEN = open('key.txt').read()
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    ## Adding Command Handler and Message Handler
    start_cmd_handler = CommandHandler('start', start_handler)
    photo_msg_handler = MessageHandler(Filters.photo, photo_handler)
    dp.add_handler(start_cmd_handler)
    dp.add_handler(photo_msg_handler)

    # log all errors
    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()



if __name__ == "__main__":
    main()