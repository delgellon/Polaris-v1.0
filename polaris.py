from email import message
from colorama import Fore, Back, Style
from selenium import webdriver
from mailtm import Email
from win10toast import ToastNotifier
import subprocess
import socket
import time
import os

subprocess.call('cls', shell=True)

print("""
    ____        __           _         
   / __ \____  / /___ ______(_)____    
  / /_/ / __ \/ / __ `/ ___/ / ___/  Dev by  
 / ____/ /_/ / / /_/ / /  / (__  )    Ell0n#0070
/_/    \____/_/\__,_/_/  /_/____/  Fuck that fucking license !
                   version 1.0

 [*] Create unlimited shodan accounts with Polaris :)

 [1] Generate
""")

def PolarisMenu():

    selection=int (input(" --> "))
    if selection==1:
        polaris_registration()
    else:
        print("")
        print("[!] This choice does not exist !")

def polaris_registration():

    print("")
    username_registration_username = input(" Username : ")
    username_registration_password = input(" Password : ")
    username_registration_password_verif = input(" Retype Password : ")

    logins_informations = open("logins.txt", "w+")
    logins_informations.write(f'Username : {username_registration_username} Password : {username_registration_password}')
    logins_informations.close()

    listener = message

    def account_creation_choice():

        selection=int (input(" --> "))
        if selection==1:
            listener(message)
        else:
            print("")
            print(" [!] The account has not been created")

    def listener(message):
        print("\n[+] Subject: " + message['subject'])
        print("[+] Content: " + message['text'] if message['text'] else message['html'])

    test = Email()

    test.register()
    print("\n[+] Email Adress: " + str(test.address))

    test.start(listener, interval=1)
    print("\n[%] Waiting for verification mail...")

    driver_shodan_registration = webdriver.Chrome(executable_path="chromedriver.exe")
    driver_shodan_registration.get("https://account.shodan.io/register")

    shodan_registration_username = driver_shodan_registration.find_element_by_id("username")
    shodan_registration_username.send_keys(username_registration_username) 

    shodan_registration_password = driver_shodan_registration.find_element_by_id("password")
    shodan_registration_password.send_keys(username_registration_password) 

    shodan_registration_password_confirm = driver_shodan_registration.find_element_by_id("password_confirm")
    shodan_registration_password_confirm.send_keys(username_registration_password_verif)

    shodan_registration_password_confirm2 = driver_shodan_registration.find_element_by_id("email")
    shodan_registration_password_confirm2.send_keys(test.address)

    shodan_registration_button = driver_shodan_registration.find_element_by_class_name("button-primary")
    shodan_registration_button.click()

    driver_shodan_registration.get("https://account.shodan.io/login")

    shodan_registration_username2 = driver_shodan_registration.find_element_by_id("username")
    shodan_registration_username2.send_keys(username_registration_username)

    shodan_registration_password2 = driver_shodan_registration.find_element_by_id("password")
    shodan_registration_password2.send_keys(username_registration_password)

    toaster = ToastNotifier()
    toaster.show_toast("Polaris",
                   "Don't forget to activate your account before trying to login !",
                   duration=10)

    time.sleep(999999999999)

PolarisMenu()
