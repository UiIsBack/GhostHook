
import os
os.system(f'cls & mode 85,20 & title GhostHook! - Version 1.4!')
from json import loads, dumps
from threading import Thread
from time import sleep
from sys import argv
import pystyle
from pystyle import *
import time
import requests
from colorama import Fore
import threading
import sys


def main():
    image = """

                                        ,%@&(                                      
                                    @@@@@@@@@@@@@%                                 
                                .@@@@@@@@@@@@@@@@@(                               
                                @@@@@@@@@@@@@@@@@@@#                              
                                (@@@@@&  @@@@  @@@@@@.                             
                                @@@@&   @@@*   @@@@@(        @@@@@@@@             
                    ,  /         ,@@@. *@@@@@*  @@@@@&      @@@@@ @@/ @&           
                @@@@@@@@@       /@@@@@@@@@@@@@@@@@@@@     &@&  @* @@  #%          
            @@ @@.&@@(@@@@    (@@@@@@#    ,.@@@@@@@@@   &@@(  %   @              
            @ ,@/ @*    &@@@@@@@@@@@, @@@@% ((@@@@@@@@@@@@      /&               
                #(  &@#  &@@@@@@@@@@@&@@@@@@@@# @@@@@@@@@@,                       
                        &@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@                       
                        &@@@@@@@@@@@@@@@@@@@@@#&@@@@@@@@@@@                      
                        &. /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                     
                        @  /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,/                     
                        , #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ //                    
                        ,  (,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                       
                            @*@@@@@@@@@@@@@@@@@@@@@@@@@@@@                       
                            @ @@@@@@@@@@@@@@@@@@@@@@@@@@@@                       
                            @ @ @@@@@@@@@@@@@@@@@@@@@@@@@%                       
                            ,(#  * *@#@@@@@@@@@@@@@@@@@@ & @                        
                                    @%@@@@@@@@@@@@@@@@@/ ..                         
                                    @@@@@@@@@@@@@@@@@@#                             
                                    *.@@@@@@@@@@@@@@@&,                             
                                    #%@@/ @@@@@@@@ @                              
                                    %.*@  *@@@@@@@ (                              
                                    (  @   @@@@@@                                 
                                        @   &@@@@@                                 
                                        @   @@@.@                                  
                                            #@*                                     
                                        /@*                                      
                                        &@  
    """

    Anime.Fade(Center.Center(image), Colors.purple_to_blue, Colorate.Vertical, interval=0.025, enter=True)

    print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(image)))


    name = """



    d888b  db   db  .d88b.  .d8888. d888888b db   db  .d88b.   .d88b.  db   dD 
    88' Y8b 88   88 .8P  Y8. 88'  YP `~~88~~' 88   88 .8P  Y8. .8P  Y8. 88 ,8P' 
    88      88ooo88 88    88 `8bo.      88    88ooo88 88    88 88    88 88,8P   
    88  ooo 88~~~88 88    88   `Y8b.    88    88~~~88 88    88 88    88 88`8b   
    88. ~8~ 88   88 `8b  d8' db   8D    88    88   88 `8b  d8' `8b  d8' 88 `88. 
    Y888P  YP   YP  `Y88P'  `8888Y'    YP    YP   YP  `Y88P'   `Y88P'  YP   YD  


    https://sexism.cc                                               Version 1.4


    ─═══════════════════════════════════☆☆═══════════════════════════════════─
                    loading ghosthook || webhook spammer                
    ─═══════════════════════════════════☆☆═══════════════════════════════════─

    """

    #wow


    Anime.Fade(Center.Center(name), Colors.purple_to_blue, Colorate.Vertical, interval=0.025, enter=True)

    print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(name)))


    webhook_url = Write.Input("webhook>", Colors.purple_to_blue, interval=0.008)  



    r = requests.get(webhook_url)

    if r.status_code == 200:
            print(f"{Fore.GREEN}Webhook working{Fore.RESET}")
            time.sleep(1)
    
            
    else:
            print(f"{Fore.RED}[404] Webhook Invalid{Fore.RESET}")
            os.system('pause >null') # or break()

    Write.Print('1. Webhook Deleter 2. Webhook Spammer\n', Colors.purple, interval=0)

    def deelhook():
        #deletes webhook
        result = requests.request(method="DELETE", url=webhook_url)

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(f"{Fore.RED}[{Fore.GREEN}!{Fore.RED}]{Fore.GREEN} " + str(err))
        else:
            Write.Print(f" Webhook successfully deleted\n  [{result.status_code}]", Colors.red, interval=0)
            time.sleep(3)

    def hooks():
        msg = Write.Input(f"message-> ", Colors.purple_to_blue, interval=0.008)

        namehook = Write.Input(f"webhook name-> ", Colors.blue_to_purple, interval=0.008)

        theard = int(Write.Input(f"amount of messages-> ", Colors.blue_to_cyan))

        discordavurl = Write.Input(f"Enter Avatar Url leave blank for default [>]", Colors.cyan_to_blue, interval= 0.008)

        footer = Write.Input(f"Embed Footer [>]", Colors.cyan_to_blue, interval= 0.008)

        maincon = Write.Input(f"embed content [>]", Colors.cyan_to_blue, interval= 0.008)

        embedauth = Write.Input(f"embed author [>]", Colors.cyan_to_blue, interval= 0.008 )

        Write.Print('spam starting...\n', Colors.green, interval=0)

        time.sleep(2)

        

        embeds = []
        embed = {
                        "color": 12208895,
                        "fields": [
                            {
                                "name": "**Nice Webhook**",
                                "value": f'{maincon}',
                                "inline": True
                            },
                        ],
                        "author": {
                            "name": f"{embedauth}",
                            "icon_url": discordavurl
                        },
                        "footer": {
                        "text": f"{footer}"
                        }
                    }
        embeds.append(embed)

        #setting up
        os.system('cls')
        os.system('cls')
        defaulthookname = 'ui!'
        defaultmessage = 'c '
        defaultav = 'https://www.kindpng.com/picc/m/103-1038268_not-scary-cartoon-ghost-hd-png-download.png'

        if discordavurl == '': 
            discordavurl = defaultav
            print(" ")

            hookname = namehook

        data = {
                "content": msg,
                "embeds": embeds,
                "username": namehook,
                "avatar_url": discordavurl
            }






        webhook = webhook_url
        
        for x in range(theard):
            response = requests.post(url=webhook, json=data)
            try:
                    if response.status_code == 204 or response.status_code == 200:
                        Write.Print(f"Message sent\n", Colors.green_to_cyan, interval= 0)
                    elif response.status_code == 429:
                        Write.Print(f"Rate limited ({response.json()['retry_after']}ms)\n", Colors.red_to_yellow, interval= 0)
                        time.sleep(response.json()["retry_after"] / 1000)
                    elif response.status_code == 404:
                        Write.Print(f"Webhook Deleted)\n", Colors.red_to_black, interval= 0)
                        time.sleep(3)
                        break
                    else:
                        Write.Print(f"Error : {response.status_code}!\n", Colors.red_to_green, interval= 0)
                        time.sleep(.01)
                        break
            except KeyboardInterrupt:
                    break
        Write.Print("Spam Ended", Colors.blue, interval=0.08)
        time.sleep(0.75)

        print(" ")
        print(" ")
        os.system('cls')

        hookname = namehook

        if hookname == '': 
                hookname = defaulthookname
                print(" ")
                print(f'you enterd nothing name set to {defaulthookname}')

        print(" ")
        message = msg
        if message == '': 
                message = defaultmessage
                print(" ")
                print(f'you entered nothing msg set to {defaultmessage}')

        try:
                print(" ")
                threads = theard
                if threads < 1: 
                    print(" ")
                    print(f"you didn't set any threads threads set to 1")
                    threads = 1

        except ValueError:
                threads = 1
                print(" ")
                print(f'Invalid threads / Setting to 1.')

        print(" ")







    gh = input(f"{Fore.RED}[+]{Fore.RESET}{Fore.MAGENTA}")




    if gh == '1':
        deelhook()
        main()
    elif gh == '2':
        hooks()
        main()
    else:
        Write.Print(f"enter either 1 or 2! not {gh}", Colors.red, interval=0)
        time.sleep(3)
        main()

main()



