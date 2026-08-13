import sondehub
import math
import json
import Notification

import landingGuess
import time
import sys

# import numpy as np
# Loads in the options file
options = open("options.json")
options = json.load(options)
# Sets the lat and lon from options
B = options["home_lat"]
A = options["home_lon"]

print("Sonde Alert online")
print("Current location: " + str(B) + " ," + str(A))
"""
def calc_angle(a,b,c,d):
    angle =  (((d-b)/(abs(d-b)))*(180*((math.acos((((math.sqrt((d-b)**2)+(c-a)**2))**2+(10**2)-(math.sqrt((d-b)**2+(c-a+10)**2))**2)/(20*((math.sqrt((d-b)**2)+(c-a)**2)))))/math.pi)))
    return angle
#Idealy this would give you asumuth and elivation at some point
"""


# This calculates the distance between 2 sets of cordinites and ruturns it in miles, not sure how accurate this is everware else in the world...
def calc_distance(a, b, c, d):
    i = B - d
    j = A - c
    distance = math.sqrt(i**2 + j**2)
    distance = distance * 54.6
    return distance


# The on msg runs everytime balloon data comes in from sonde hub
def on_message(message):
    # C and D are the position lat and lon of the balloon
    C = float((message["position"]).split(",")[1])
    D = float((message["position"]).split(",")[0])

    balloon_alt = message["alt"]  # Gets the balloons current alt
    dist = calc_distance(A, B, C, D)
    # print(dist)

    if 1 < options["distance"] and int(balloon_alt) < options["note_alt"]:
        print(message)
        try:
            balloon_frequ = message["frequency"]
        except:
            balloon_frequ = "Unknown"
        try:
            balloon_type = message["type"]
        except:
            balloon_type = "Unknown"
        print(round(dist))
        guess_landing = landingGuess.glanding(message)
        print(guess_landing)
        # timeToBalloon = maper.time_to_destination(
        #     str(B) + "," + str(A), str(guess_landing[0]) + "," + str(guess_landing[1])
        # )
        if options["msg_type"] == "txtmsg":
            # for texting the user
            Notification.text_me(
                "There is a balloon("
                + balloon_type
                + ") @ "
                + str(D)
                + ","
                + str(C)
                + " At alt:"
                + str(balloon_alt)
                + ". On:"
                + str(balloon_frequ)
                + "MHZ. ETA:"
                # + str(timeToBalloon)
                + " Predicted landing: "
                + str(guess_landing[1])
                + " ,"
                + str(guess_landing[0])
            )
        elif options["msg_type"] == "email":
            # For emailing the user
            Notification.email_me(
                "Balloon alert",
                "There is a balloon("
                + balloon_type
                + ") @ "
                + str(D)
                + ","
                + str(C)
                + " At alt:"
                + str(balloon_alt)
                + ". On:"
                + str(balloon_frequ)
                + "MHZ. ETA:"
                # + str(timeToBalloon)
                + " Predicted landing: "
                + str(guess_landing[1])
                + " ,"
                + str(guess_landing[0]),
            )
        elif options["msg_type"] == "slack":
            # for sending slack message
            Notification.slack_everyone(
                "C08101JEU94",
                "TEST Baloon alert \n There is a balloon("
                + balloon_type
                + ") @ "
                + str(D)
                + ","
                + str(C)
                + " At alt:"
                + str(balloon_alt)
                + ". On:"
                + str(balloon_frequ)
                + "MHZ. ETA:"
                # + str(timeToBalloon)
                + " Predicted landing: "
                + str(guess_landing[1])
                + " ,"
                + str(guess_landing[0]),
            )
        else:
            # If some setting is wrong it will default to print
            print(
                "There is a balloon("
                + balloon_type
                + ") @ "
                + str(D)
                + ","
                + str(C)
                + " At alt:"
                + str(balloon_alt)
                + ". On:"
                + str(balloon_frequ)
                + "MHZ. ETA:"
                # + str(timeToBalloon)
                + " Predicted landing: "
                + str(guess_landing[1])
                + " ,"
                + str(guess_landing[0])
            )
        print("Sent msg\nsleeping till next balloon window")
        time.sleep(36000)

    else:
        pass


test = sondehub.Stream(on_message=on_message)
# print(test)
# on_message(test)
animation = "|/-\\"
idx = 0
while 1:
    print(animation[idx % len(animation)], end="\r")
    idx += 1
    time.sleep(0.2)
