import os
import json
downstall = ("y"==str(input("Would you like the installer to try and pip install the required packages [y/n]: ")))
if(downstall):
    os.system("pip install sondehub")
    os.system("pip install googlemaps")
    os.system("pip install twilio")
    os.system("pip install slack_sdk")
    os.system("pip install dotenv")

else:
    print("OK")
    print("Packages to install: sondehub, googlemaps, twilio, slack_sdk, dotenv")
if("y"==input("Do you want to updates option file?(If this is your first time say yes) [y/n]: ")):
    distance = int(input("What radius from you do you want to recive sonde notifications(int): "))
    note_alt = int(input("What alt do you want to trigger the notification, look at what alt balloons in your area loose signal and add 500m(int): "))
    msg_type = input("How do you want notifications to be sent. pls type exactly(email or txtmsg): ")
    home_lat = float(input("Latatude of your current location (float): "))
    home_lon = float(input("Longatude of your current location (float):"))
    options = {"distance":distance,"note_alt":note_alt,"msg_type":msg_type,"home_lat":home_lat,"home_lon":home_lon}
    with open("options.json", "w") as outfile:
        json.dump(options, outfile)
else:
    print("ok you can also change stuff by editing the options.json file in a text editor")
if("y" == input("Do you want to updates passwords file?(If this is your first time say yes) [y/n]: ")):
    if("y"==input("Are you using twilio? [y/n]")):
        account_ssid = input("Your twilio account ssid: ")
        auth_token = input("Your twilio auth token: ")
        numFrom = input("Your twilio phone number: ")
        numTo = input("Your phone number: ")
    else:
        print("ok")
        account_ssid = "na"
        auth_token = "na"
        numFrom ="na"
        numTo = "na"
    
    if("y" == input("Do you want to fill out the email information? [y/n]: ")):
        email_sender = input("What gmail will be sending the email (example@example.net): ")
        email_to = input("What email are you sending the notification to?: ")
        email_app_password = input("What is your google application password: ")
    else:
        email_sender = "na"
        email_to = "na"
        email_app_password = "na"
    googlekey = input("What is your google maps api key(Put na if you dont have one): ")
    secure = {"googleKey":googlekey,"account_sid":account_ssid,"auth_token":auth_token,"from#":numFrom,"to#":numTo,"email_sender":email_sender,"email_to":email_to,"email_app_password":email_app_password}
    with open("pass.json", "w") as outfile:
            json.dump(secure, outfile)
    print("Ok cool beans bud")
else:
    print("Ok cool beans bud")
