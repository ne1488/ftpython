import telebot
from ftplib import FTP
import os.path
import time
from telebot import types

bot = telebot.TeleBot("1187555043:AAGxpyNUhS8219-vNlRUE5Ltcdk2Nbd7FYA")

ids = {"777127781", "1475685625", "1416723532"}

while True:
    ftp = FTP('f30-preview.awardspace.net')  
    ftp.login('4204404_sdf123','SiXKzh5Zn3ZD')

    filew = open("files.txt", 'r')
    ftpcount = len(ftp.nlst()) - 2
    filecount = len(filew.readlines())
    print("ftp coll: " + str(ftpcount) + "\tfile coll:" + str(filecount))
    if(ftpcount > filecount):
        print(str(len(ftp.nlst()) - 3) + " = " + str(filecount))
        for idss in ids:
            print("try send to" + idss)
            bot.send_message(idss, "卐Обнаружен новый лог卐")
        
    filew.close()
    fileq = open("files.txt", 'w')
    fileq.write("")
    fileq.close()
    filem = open("files.txt", 'a')
    for file in ftp.nlst():
        if file == "." or file == "..":
            continue
        filem.write(file+"\r")
    filem.close()
    ftp.close()
    print("good")
    time.sleep(300)
bot.polling(none_stop=True)
