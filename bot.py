print ("VALBOT IS LOADING...")
print()
print("WRITTEN BY FUMS & Pratham")
print()
print()
# https://open.spotify.com/track/152unnv8fuahIUyVnHJutJ?si=oK5FgV8ZQH66chbGCDyl3A
try:
    import pathlib
    import requests
    import webbrowser
    import math
    import keyboard
    import psutil
    import pyautogui
    import pygetwindow as gw
    import os
    import time
    import urllib.request
    import datetime
    import random
    import platform
    import shutil

    from pypresence import Presence
    from PIL import Image
    from pathlib import Path
    from random import randint
    from time import sleep
    from colorama import Fore, Style
    from colorama import init
    from discord_webhook import DiscordWebhook, DiscordEmbed
    from configparser import ConfigParser
except Exception as e: print(e), print("Try to reinstall packages"), input(), quit()


init()  # not a clue what init function its loading but its needed lol

# ---------------------------------------------------------------

start_time = time.time()


pyautogui.FAILSAFE = False

class Bot:
    def __init__(self):

        self.buymenubutton = "b" # what button you use to open the buy menu to choose weapons
        self.xpamount = 0  # how much xp the bot has earned during runtime
        self.restarted = 0  # how many times the bot has restarted during runtime
        self.gamesplayed = 0  # num of games played during runtime
        self.restarttime = time.time() + 3600 # 1 hour after starting bot
        # self.deathmatch_duration = 0
        self.foundwebhook = False

        config = ConfigParser(allow_no_value=True)
        config.read('config.ini')

        if os.path.exists('config.ini'):
            try:
                config = ConfigParser(allow_no_value=True)
                config.read('config.ini')

                self.hookline = config.get('settings', 'webhook')
                self.foundwebhook = True
            except Exception:
                self.foundwebhook = False

        self.versionfix = "Valbot v2.3 " #add two spaces if version number is vx.x and remove spaces if vx.x.x
        self.versionnumber = self.versionfix.replace("Valbot ", "") #add two spaces if version number is vx.x and remove spaces if vx.x.x
        self.versionnumber = self.versionnumber.replace("  ", "") #add two spaces if version number is vx.x and remove spaces if vx.x.x
        self.version = "Valbot " + self.versionnumber  # variable str to change valbot version name in outputs
        
        self.PROCNAME = "VALORANT-Win64-Shipping.exe"
        self.discordbutton = [{"label": "Join Discord", "url": "https://discord.gg/QFC46XKzxU"}]
        self.computer_name = platform.node()

        # Why take from raw GitHub repo? So I can update the bots detection images without having to release an update.
        # Change it manually if you wish by reading the valbotReadMe folder called change_resolution.txt

        # self.cheaterdetected_png = Image.open(requests.get("https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbot_assets_1920_1080/cheated_detected.png", stream=True).raw)
        # self.continueterminated_png = Image.open(requests.get("https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbot_assets_1920_1080/continue_terminated.png", stream=True).raw)
        # self.deathmatch_png = Image.open(requests.get("https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbot_assets_1920_1080/deathmatch.png", stream=True).raw)
        # self.ingame_png = Image.open(requests.get("https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbot_assets_1920_1080/ingame.png", stream=True).raw)
        # self.inqueue_png = Image.open(requests.get("https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbot_assets_1920_1080/inqueue.png", stream=True).raw)
        # self.ondeathmatch_png = Image.open(requests.get("https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbot_assets_1920_1080/ondeathmatch.png", stream=True).raw)
        # self.play_png = Image.open(requests.get("https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbot_assets_1920_1080/play.png", stream=True).raw)
        # self.playagain_png = Image.open(requests.get("https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbot_assets_1920_1080/playagain.png", stream=True).raw)
        # self.start_png = Image.open(requests.get("https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbot_assets_1920_1080/start.png", stream=True).raw)

        picdir = 'assets/1440p'
        self.cheaterdetected_png = "assets/cheated_detected.png"
        self.continueterminated_png = "assets/continue_terminated.png"
        self.deathmatch_png = f"{picdir}/deathmatch.png"
        self.ondeathmatch_png = f"{picdir}/ondeathmatch.png"
        self.ingame_png = f"{picdir}/ingame.png"
        self.inqueue_png = f"{picdir}/inqueue.png"
        self.play_png = f"{picdir}/play.png"
        # self.onplay_png = f"{picdir}/onplay.png"
        self.playagain_png = f"{picdir}/playagain.png"
        self.start_png = f"{picdir}/start.png"
        self.skip_png = f"{picdir}/skip.png"
        self.quit_png = f"{picdir}/quit.png"
        self.exit_png = f"{picdir}/exit.png"
        self.cancel_png = f"{picdir}/cancel.png"
        self.understand_png = f"{picdir}/understand.png"
        
        try:  # if cant connect to discord (if it isnt open for example), bot doesnt crash
            self.RPC = Presence(client_id="772841390467711041")  # discord rpc client id

            try:
                self.RPC.close()
            except Exception:
                pass
            self.RPC.connect()  # connects to rpc


        except Exception:
            pass


        try:
            config = ConfigParser(allow_no_value=True)

            config.read('config.ini')

            self.restarted = config.getint('runtime_values', 'restarted')
            self.timestarted = config.getfloat('runtime_values', 'starttime')
            self.gamesplayed = config.getint('runtime_values', 'gamesplayed')
            self.xpamount = config.getint('runtime_values', 'xpamount')

        except:
            pass
        
    def locateOnScreen(self, file, confidence=.6):
        one = pyautogui.locateOnScreen(file, grayscale=True)
        two = pyautogui.locateOnScreen(file, confidence=confidence, grayscale=True)
        return one, two
    
    def found(self, file, confidence=.6):
        one, two = self.locateOnScreen(file, confidence=confidence)
        return one is not None or two is not None

    def too_long(self, future):
        if time.time() > future:
            # detects possible issue with valorant and restarts the game
            print(Style.RESET_ALL)
            print(Fore.RED + " [!] FOUND A POSSIBLE ERROR WITH VALORANT")
            self.startvalorant()
            return True

    def restartbot(self):  # restarts the bot after 1 hour
        self.titlescreen()
        print(Fore.RED + " [!] BOT IS RESTARTING AFTER 1 HOUR")

        try:
            self.RPC.close()
        except Exception:
            pass
        
        if self.foundwebhook == True:
            try:
                webhook = DiscordWebhook(
                    url=self.hookline,
                    username="Valbot")
                embed = DiscordEmbed(color=0xFF7034, title="Restarting Valbot",
                                     description="Valbot is restarting.\nThis is to prevent crashes.")

                embed.set_author(
                    name=self.version,
                    url="https://github.com/MrFums/Valbot",
                    icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbotlogo_22plusnobg.png",
                )
                textforfooter = "[" + self.computer_name + "] by Fums"
                embed.set_footer(text=textforfooter, icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/fumspfp.png")
                embed.set_timestamp()
                webhook.add_embed(embed)
                webhook.execute()
            except Exception:
                print(Fore.RED + " [!] TRIED TO SEND A WEBHOOK BUT IT IS NOT SETUP")


        time.sleep(1)
        main()
        # os.startfile('restart.py')  # starts the restart script which reopens this script
        # time.sleep(3)
        # quit()  # quits this runtime of the script

    def titlescreen(self):

        os.system('mode con: cols=54 lines=18')
        title = "title " + self.versionfix
        os.system(title)

        print(Fore.YELLOW + """
           ╔╗  ╔╗╔═══╗╔╗   ╔══╗ ╔═══╗╔════╗
           ║╚╗╔╝║║╔═╗║║║   ║╔╗║ ║╔═╗║║╔╗╔╗║
           ╚╗║║╔╝║║ ║║║║   ║╚╝╚╗║║ ║║╚╝║║╚╝
            ║╚╝║ ║╚═╝║║║ ╔╗║╔═╗║║║ ║║  ║║  
            ╚╗╔╝ ║╔═╗║║╚═╝║║╚═╝║║╚═╝║  ║║  
             ╚╝  ╚╝ ╚╝╚═══╝╚═══╝╚═══╝  ╚╝""")

        print(Style.RESET_ALL)
        print(Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " " + self.versionfix + "Fums#0888 & Prathusa#0000")
        print(Style.RESET_ALL)
        print(Style.RESET_ALL)
        print(Style.RESET_ALL + Fore.YELLOW + "——————————————————————————————————————————————————————")
        print(Style.RESET_ALL)
        print(Style.RESET_ALL)
        return
    

    def valorantrunning(self):
        found = False
        print(Fore.YELLOW, "[-] CHECKING IF VALORANT IS RUNNING")
        print(Style.RESET_ALL)
        time.sleep(2)
        

        for proc in psutil.process_iter():
            if proc.name() == "VALORANT-Win64-Shipping.exe":
                found = True
                break

        if not found:
            print(Fore.RED, "[!] VALORANT IS NOT RUNNING")
            print(Style.RESET_ALL)
            self.startvalorant()
        else:
            print(Fore.GREEN, "[√] VALORANT IS RUNNING")
            time.sleep(25)
            #clicks the play button when you are in launcher to fix some peoples launchers
            screenWidth, screenHeight = pyautogui.size()
            pyautogui.click(screenWidth / 2, screenHeight / 2)
            time.sleep(1)
            self.playbutton()

    def startvalorant(self):
        if self.foundwebhook == True:
            try:
                webhook = DiscordWebhook(
                    url=self.hookline,
                    username="Valbot")
                embed = DiscordEmbed(color=0xFF0000, title="Restarting Valorant",
                                     description="Possible error with Valorant.\nValorant will now be relaunched.\nBot will resume as normal.")

                embed.set_author(
                    name=self.version,
                    url="https://github.com/MrFums/Valbot",
                    icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbotlogo_22plusnobg.png",
                )
                textforfooter = "[" + self.computer_name + "] by Fums"
                embed.set_footer(text=textforfooter, icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/fumspfp.png")
                embed.set_timestamp()
                webhook.add_embed(embed)
                webhook.execute()
            except Exception:
                print(Fore.RED + " [!] TRIED TO SEND A WEBHOOK BUT IT IS NOT SETUP")


        for proc in psutil.process_iter():
            try:
                if proc.name().lower() == self.PROCNAME.lower():
                    proc.kill()
                    print(Fore.YELLOW, "[-] KILLING THE VALORANT PROCESS")
                    time.sleep(10)
            except:
                print(Fore.RED, "[!] COULD NOT KILL THE VALORANT PROCESS")

        print(Style.RESET_ALL + Fore.YELLOW, "[-] STARTING VALORANT")
        print(Style.RESET_ALL)
        root = str(pathlib.Path(__file__).parent.absolute())
        fullpath = root + "\Valorant.lnk"
        vallnk = Path(fullpath)
        if vallnk.is_file():
            # file exists
            time.sleep(1)
            os.startfile("Valorant.lnk")

        else:
            print(Style.RESET_ALL, Fore.RED + "[!] COULD NOT FIND A VALORANT SHORTCUT")
            print(Style.RESET_ALL)
        time.sleep(15)
        self.restarted += 1
        #clicks the play button when you are in launcher to fix some peoples launchers
        screenWidth, screenHeight = pyautogui.size()
        pyautogui.click(screenWidth / 2, screenHeight / 2)
        time.sleep(15)
        self.valorantrunning()

    def test_main_screen(self):
        screenWidth, screenHeight = pyautogui.size()
        pyautogui.click(screenWidth, screenHeight)
        mainscreen = self.found(self.exit_png)
        pyautogui.keyDown('esc')
        pyautogui.keyUp('esc')
        return mainscreen

    def playbutton(self):

        now = time.time()

        future = now + 720


        activeactivity = "[" + self.versionnumber + "] - " + "At Menu"

        earned = "{:,}".format(self.xpamount)

        try:

            self.RPC.update(state=("Earned " + earned + " XP"), start=self.timestarted, large_image="valbot22",
                            large_text=self.version, details=activeactivity, buttons = self.discordbutton)

        except Exception:
            pass
        
        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] SEARCHING FOR PLAY BUTTON")
        time.sleep(.5)
        while True:
            if keyboard.is_pressed('f3'):
                self.pause()
            if self.too_long(future):
                break

            print(Style.RESET_ALL)
            print(Fore.YELLOW + " [-] CHECKING FOR ANY PROMPTS")
            self.promptclicker()

            # print(Style.RESET_ALL)
            # print(Fore.YELLOW + " [-] CHECKING TO MAKE SURE ON MAIN SCREEN")
            # if not self.test_main_screen():
            #     self.endofgame()

            play, play2 = self.locateOnScreen(self.play_png)

            if play is not None or play2 is not None:
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] DETECTED PLAY BUTTON")

                if play is not None:
                    time.sleep(1)
                    pyautogui.moveTo(play)
                    pyautogui.moveRel(10, -5, duration=1)  
                    pyautogui.click()
                    time.sleep(2)
                    self.playbuttonclicked()

                if play2 is not None:
                    time.sleep(1)
                    pyautogui.moveTo(play2)
                    pyautogui.moveRel(10, -5, duration=1)  
                    pyautogui.click()
                    time.sleep(2)
                    self.playbuttonclicked()
            else:
                self.endofgame()

    def deathmatchbutton(self):

        print(Style.RESET_ALL)
        print(Fore.YELLOW, "[-] SEARCHING FOR DEATHMATCH BUTTON")

        time.sleep(1)
        now = time.time()

        future = now + 45

        while True:
            if keyboard.is_pressed('f3'):
                self.pause()
            if self.too_long(future):
                break

            deathmatch, deathmatch2 = self.locateOnScreen(self.deathmatch_png)

            if deathmatch is not None or deathmatch2 is not None:
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] DETECTED DEATHMATCH BUTTON")

                if deathmatch is not None:
                    pyautogui.moveTo(deathmatch)
                    pyautogui.click(deathmatch)
                    time.sleep(.5)
                    self.deathmatchbuttonclicked()

                if deathmatch2 is not None:
                    pyautogui.moveTo(deathmatch2)
                    pyautogui.click(deathmatch2)
                    time.sleep(.5)
                    self.deathmatchbuttonclicked()

                time.sleep(5)

    def deathmatchbuttonclicked(self):

        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] DETECTING IF DEATHMATCH IS DETECTED")
        time.sleep(1)
        now = time.time()

        future = now + 120

        while True:
            if keyboard.is_pressed('f3'):
                self.pause()
            if self.too_long(future):
                break
                break

            if self.found(self.ondeathmatch_png, confidence=0.5):
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] DETECTED THAT DEATHMATCH IS SELECTED")
                time.sleep(1)
                self.searchforgame()
            else:
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] DETECTED THAT DEATHMATCH IS NOT SELECTED")
                time.sleep(1)
                self.deathmatchbutton()

    def playbuttonclicked(self):

        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] DETECTING IF PLAY BUTTON IS SELECTED")
        time.sleep(1)
        now = time.time()

        future = now + 120

        while True:
            if keyboard.is_pressed('f3'):
                self.pause()
            if self.too_long(future):
                break
                break

            if self.found(self.start_png, confidence=0.5):
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] DETECTED THAT PLAY BUTTON IS SELECTED")
                time.sleep(1)
                self.deathmatchbutton()
            else:
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] DETECTED THAT PLAY BUTTON IS NOT SELECTED")
                time.sleep(1)
                self.playbutton()

    def firststart(self):

        self.titlescreen()
        foundval = False
        for proc in psutil.process_iter():
            if proc.name() == "VALORANT-Win64-Shipping.exe":
                window = gw.getWindowsWithTitle('Valorant')[0]
                foundval = True
        if not foundval:
            self.startvalorant()

        if not window.isMaximized:
            window.maximize()
            self.firststart()

        print(Style.RESET_ALL)
        print(Style.RESET_ALL)
        for i in range(15, -1, -1):
            print(Fore.RED, Style.BRIGHT + "[!] BOT WILL BEGIN IN", i, "SECONDS                  ", end='\r')
            sleep(1)
        print(Style.RESET_ALL)
        self.playbutton()

    def searchforgame(self):

        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] SEARCHING FOR START BUTTON")

        now = time.time()

        future = now + 240

        while True:
            if keyboard.is_pressed('f3'):
                self.pause()
            if self.too_long(future):
                break

            startbutton, start2 = self.locateOnScreen(self.start_png)
            again, again2 = self.locateOnScreen(self.playagain_png)

            if startbutton is not None or start2 is not None or again is not None or again2 is not None:
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] DETECTED START BUTTON")

                if startbutton is not None:
                    time.sleep(.5)
                    pyautogui.moveTo(startbutton)
                    time.sleep(.3)
                    pyautogui.click(startbutton)
                    self.inqueue()

                if start2 is not None:
                    time.sleep(.5)
                    pyautogui.moveTo(start2)
                    time.sleep(.3)
                    pyautogui.click(start2)
                    self.inqueue()

                if again is not None:
                    time.sleep(.5)
                    pyautogui.moveTo(again2)
                    pyautogui.click(again2)
                    self.inqueue()

                if again2 is not None:
                    time.sleep(.5)
                    pyautogui.moveTo(again2)
                    pyautogui.click(again2)
                    self.inqueue()

    def inqueue(self):

        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] CHECKING IF IN QUEUE")
        now = time.time()
        time.sleep(.2)
        future = now + 240

        while True:
            if keyboard.is_pressed('f3'):
                self.pause()
            if self.too_long(future):
                break
                break

            if self.found(self.inqueue_png):
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] DETECTED IN QUEUE")
                self.waitingforgame()
            else:
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] DETECTED NOT IN QUEUE")
                time.sleep(1)
                self.playbutton()

    def waitingforgame(self):
        time.sleep(1)


        activeactivity = "[" + self.versionnumber + "] - " + "In Queue"

        earned = "{:,}".format(self.xpamount)

        try:

            self.RPC.update(state=("Earned " + earned + " XP"), start=self.timestarted, large_image="valbot22",
                            large_text=self.version, details=activeactivity, buttons = self.discordbutton)

        except Exception:
            pass
        
        print(Style.RESET_ALL)


        print(Fore.YELLOW + " [-] WAITING FOR A GAME")

        now = time.time()

        future = now + 1320  # if not in game after 22 mins, restart valorant as there may be an error. Change this if
        # your servers are bad (in seconds)

        while True:
            if keyboard.is_pressed('f3'):
                self.pause()
            if self.too_long(future):
                break

            if self.found(self.ingame_png, confidence=0.5):
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] DETECTED IN A GAME")

                
                

                activeactivity = "[" + self.versionnumber + "] - " + "In Match"

                earned = "{:,}".format(self.xpamount)


                try:

                    self.RPC.update(state=("Earned " + earned + " XP"), start=self.timestarted, large_image="valbot22",
                                    large_text=self.version, details=activeactivity, buttons = self.discordbutton)

                except Exception:
                    pass
                

                if self.foundwebhook == True:
                    try:
                        webhook = DiscordWebhook(
                            url=self.hookline,
                            username="Valbot")
                        embed = DiscordEmbed(color=0x90ee90, title="Match Found",
                                             description="A match has been found.\nWaiting for the match to end.")
                        embed.set_author(
                            name=self.version,
                            url="https://github.com/MrFums/Valbot",
                            icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbotlogo_22plusnobg.png",
                        )
                        textforfooter = "[" + self.computer_name + "] by Fums"
                        embed.set_footer(text=textforfooter, icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/fumspfp.png")
                        embed.set_timestamp()
                        webhook.add_embed(embed)
                        webhook.execute()
                    except Exception:
                        print(Fore.RED + " [!] TRIED TO SEND A WEBHOOK BUT IT IS NOT SETUP")


                time.sleep(1)
                print(Style.RESET_ALL)
                print(Fore.YELLOW + " [-] WAITING FOR THE GAME TO END")
                time.sleep(15)  # so it doesnt detect the end game screen as soon as it searches
                print(Style.RESET_ALL)
                print(Fore.YELLOW + " [-] TO PAUSE THE BOT HOLD F3")
                print(Fore.YELLOW + " [-] TO RESUME THE BOT HOLD F4")
                # self.deathmatch_duration = time.time() + 780
                self.endofgame()

    def pause(self):
        print(Style.RESET_ALL)
        print(Fore.RED + " [!] PAUSING BOT")
        print(Fore.RED + " [!] HOLD F4 TO RESUME THE BOT")
        pyautogui.keyUp('w')
        pyautogui.keyUp('a')
        pyautogui.keyUp('s')
        pyautogui.keyUp('d')

        while True:
            time.sleep(1)
            try:
                if keyboard.is_pressed('f4'):
                    print(Style.RESET_ALL)
                    print(Fore.GREEN + " [√] RESUMING BOT")
                    print(Fore.GREEN + " [√] TO PAUSE THE BOT AGAIN HOLD F3")
                    break
            except:
                pass

        if self.found(self.play_png, confidence=0.7):
            self.playbutton()
        if self.found(self.inqueue_png):
            self.inqueue()
        if not self.found(self.play_png, confidence=0.7) and not self.found(self.inqueue_png):
            self.antiafk()

    def endofgame(self):

        time.sleep(2)
        deathmatch_duration = time.time() + 780
        while True:
            if keyboard.is_pressed('f3'):
                self.pause()
            if self.too_long(deathmatch_duration):
                break

            if self.found(self.play_png, confidence=0.7):

                activeactivity = "[" + self.versionnumber + "] - " + "At Menu"

                earned = "{:,}".format(self.xpamount)

                try:

                    self.RPC.update(state=("Earned " + earned + " XP"), start=self.timestarted, large_image="valbot22",
                                    large_text=self.version, details=activeactivity, buttons = self.discordbutton)

                except Exception:
                    pass
                
                self.gamesplayed += 1
                self.xpamount += 900

                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] DETECTED AT END GAME SCREEN")

                # time.sleep(2)
                self.promptclicker()
                time.sleep(2)
                self.xpscreen()

            else:
                self.antiafk()


    def xptargethook(self):

        print(Style.RESET_ALL)
        print(Fore.GREEN + " [!] XP TARGET HAS BEEN REACHED")

        if os.path.exists('config.ini'):
            config = ConfigParser(allow_no_value=True)
            config.read('config.ini')
            try:
                config.set('settings', 'xptarget', '0')
                with open('config.ini', 'w+') as configfile:
                    config.write(configfile)

            except:
                
                pass
        if self.foundwebhook == True:
            try:
                desc = "Target of " + str(self.xptarget) + " XP has been reached.\nValbot will resume until stopped."
                webhook = DiscordWebhook(
                    url=self.hookline,
                    username="Valbot")
                embed = DiscordEmbed(color=0x842bd7, title="XP Target Reached",description=desc)

                embed.set_author(
                    name=self.version,
                    url="https://github.com/MrFums/Valbot",
                    icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbotlogo_22plusnobg.png",
                )
                textforfooter = "[" + self.computer_name + "] by Fums"
                embed.set_footer(text=textforfooter, icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/fumspfp.png")
                embed.set_timestamp()
                embed.set_thumbnail(url='https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbotlogo_22plus_curved.png')
                webhook.add_embed(embed)
                webhook.execute()
            except Exception:
                print(Fore.RED + " [!] TRIED TO SEND A WEBHOOK BUT IT IS NOT SETUP")


    def matchlimit(self):

        print(Style.RESET_ALL)
        print(Fore.RED + " [!] XP LIMIT HAS BEEN REACHED")

        if os.path.exists('config.ini'):
            config = ConfigParser(allow_no_value=True)
            config.read('config.ini')
            try:
                config.set('settings', 'matchlimit', '0')
                with open('config.ini', 'w+') as configfile:
                    config.write(configfile)

            except:
                pass
        if self.foundwebhook == True:
            try:
                webhook = DiscordWebhook(
                    url=self.hookline,
                    username="Valbot")
                embed = DiscordEmbed(color=0x842bd7, title="XP Limit Reached",
                                     description="The XP limit has been reached.\nBot has been stopped.")
                embed.set_author(
                    name=self.version,
                    url="https://github.com/MrFums/Valbot",
                    icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbotlogo_22plusnobg.png",
                )
                textforfooter = "[" + self.computer_name + "] by Fums"
                embed.set_footer(text=textforfooter, icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/fumspfp.png")
                embed.set_timestamp()
                embed.set_thumbnail(url='https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbotlogo_22plus_curved.png')
                webhook.add_embed(embed)
                webhook.execute()
            except Exception:
                print(Fore.RED + " [!] TRIED TO SEND A WEBHOOK BUT IT IS NOT SETUP")

        time.sleep(120)
        quit()


    def promptclicker(self):
        skip, skip2 = self.locateOnScreen(self.skip_png)
        quit, quit2 = self.locateOnScreen(self.quit_png)
        cancel, cancel2 = self.locateOnScreen(self.cancel_png)
        understand, understand2 = self.locateOnScreen(self.understand_png)
        if quit is not None or quit2 is not None:
            print(Style.RESET_ALL)
            print(Fore.RED + " [!] DETECTED QUIT BUTTON")

            if quit is not None:
                time.sleep(1)
                pyautogui.moveTo(quit)
                pyautogui.click(quit)
                time.sleep(7)
                self.startvalorant()

            if quit2 is not None:
                time.sleep(1)
                pyautogui.moveTo(quit2)
                pyautogui.click(quit2)
                time.sleep(7)
                self.startvalorant()
            
            print(Style.RESET_ALL)
            print(Fore.GREEN + " [√] RESTARTED VALORANT")

        if skip is not None or skip2 is not None:
            print(Style.RESET_ALL)
            print(Fore.YELLOW + " [-] DETECTED SKIP BUTTON")

            if skip is not None:
                time.sleep(1)
                pyautogui.moveTo(skip)
                pyautogui.click(skip)

            if skip2 is not None:
                time.sleep(1)
                pyautogui.moveTo(skip2)
                pyautogui.click(skip2)
            
            print(Style.RESET_ALL)
            print(Fore.GREEN + " [√] CLICKED SKIP BUTTON")
        
        if cancel is not None or cancel2 is not None:
            print(Style.RESET_ALL)
            print(Fore.YELLOW + " [!] DETECTED CANCEL BUTTON")

            if cancel is not None:
                time.sleep(1)
                pyautogui.moveTo(cancel)
                pyautogui.click(cancel)

            if cancel2 is not None:
                time.sleep(1)
                pyautogui.moveTo(cancel2)
                pyautogui.click(cancel2)
            
            print(Style.RESET_ALL)
            print(Fore.GREEN + " [√] CLICKED CANCEL BUTTON")
        
        if understand is not None or understand2 is not None:
            print(Style.RESET_ALL)
            print(Fore.YELLOW + " [!] DETECTED UNDERSTAND BUTTON")

            if understand is not None:
                time.sleep(1)
                pyautogui.moveTo(understand)
                pyautogui.click(understand)

            if understand2 is not None:
                time.sleep(1)
                pyautogui.moveTo(understand2)
                pyautogui.click(understand2)
            
            print(Style.RESET_ALL)
            print(Fore.GREEN + " [√] CLICKED UNDERSTAND BUTTON")

    def antiafk(self):
        time.sleep(.5)
        n = randint(3, 11)
        a = 0

        cheatercontinue = pyautogui.locateOnScreen(self.continueterminated_png, grayscale=True)
        cheatercontinue1 = pyautogui.locateOnScreen(self.continueterminated_png, grayscale=True)


        weaponselect = [['680','200'],['680','360'],['680','520'],['680','680'],['900','200'],['900','360'],['900','520'],['900','680'],['1180','200'],['1180','360'],['1180','520'],['1180','680']]
        # stinger, spectre, bucky, judge, bulldog, guardian, phantom, vandal, marshal, operator, ares, odin
        #each list entity contains the 1920x1080 res pixel coordinates to a gun in the buy menu. Goes from top to bottom of column then moves to next row
        
        # Convert to any screen coordinates
        screenWidth, screenHeight = pyautogui.size()
        for i in weaponselect:
            weaponselect.append([str(int(i[0])/1920*screenWidth), str(int(i[1])/1080*screenHeight)])
            weaponselect.remove(i)
        
        randomweapon = random.choice(weaponselect)

        pyautogui.keyDown(self.buymenubutton)
        time.sleep(randint(6, 9) / 10)
        pyautogui.keyUp(self.buymenubutton)
        time.sleep(randint(5, 8) / 10)
        pyautogui.moveTo(randomweapon)
        time.sleep(randint(5, 8) / 10)
        pyautogui.moveTo(randomweapon)
        time.sleep(randint(5, 8) / 10)
        pyautogui.click()
        time.sleep(randint(6, 9) / 100)
        pyautogui.keyDown(self.buymenubutton)
        time.sleep(randint(6, 9) / 10)
        pyautogui.keyUp(self.buymenubutton)
        time.sleep(randint(6, 9) / 10)
        
        deathmatch_duration = time.time() + 780
        while a <= n:
            if keyboard.is_pressed('f3'):
                self.pause()
            self.promptclicker()
            if self.found(self.cheaterdetected_png):

                if self.foundwebhook == True:
                    try:
                        webhook = DiscordWebhook(
                            url=self.hookline,
                            username="Valbot")
                        embed = DiscordEmbed(color=0xFF0000, title="Cheater Detected",
                                             description="A cheater was detected in your game.\nMatch has been cancelled.\nRestarting Valorant and resuming.")

                        embed.set_author(
                            name=self.version,
                            url="https://github.com/MrFums/Valbot",
                            icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbotlogo_22plusnobg.png",
                        )
                        textforfooter = "[" + self.computer_name + "] by Fums"
                        embed.set_footer(text=textforfooter, icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/fumspfp.png")
                        embed.set_timestamp()
                        webhook.add_embed(embed)
                        webhook.execute()
                    except Exception:
                        print(Fore.RED + " [!] TRIED TO SEND A WEBHOOK BUT IT IS NOT SETUP")

                print(Style.RESET_ALL)
                print(Fore.RED + " [!] CHEATER DETECTED IN GAME")
                time.sleep(1)
                self.startvalorant()

            a += 1
            n2 = randint(1, 8)

            if self.too_long(deathmatch_duration):
                break

            if n2 == 1:
                pyautogui.keyDown('w')
                sleep(randint(2, 6) / 10)

            if n2 == 2:
                pyautogui.keyUp('w')
                pyautogui.keyDown('d')
                pyautogui.click()

            if n2 == 3:
                pyautogui.keyDown('a')
                sleep(randint(1, 3) / 10)
                pyautogui.keyDown('a')
                pyautogui.click()
                sleep(randint(2, 4) / 10)

            if n2 == 4:
                pyautogui.keyUp('d')
                pyautogui.keyDown('s')
                sleep(randint(2, 5) / 10)

            if n2 == 5:
                pyautogui.keyUp('s')
                sleep(randint(4, 6) / 10)

            if n2 == 6:
                pyautogui.keyDown('w')
                sleep(randint(2, 4) / 10)
                pyautogui.keyUp('w')

            if n2 == 7:
                pyautogui.keyDown('3')
                sleep(randint(2, 4) / 100)
                pyautogui.keyUp('3')
                sleep(randint(20, 40) / 100)
                pyautogui.keyDown('1')
                sleep(randint(2, 4) / 100)
                pyautogui.keyUp('1')
                
            if n2 == 8:
                pyautogui.mouseDown(button='left')
                sleep(randint(2, 4))
                pyautogui.mouseUp(button='left')
                
        self.endofgame()

    def xpscreen(self):

        runtimeraw = time.time() - start_time
        runtimeint = int(runtimeraw)
        runtime = str(datetime.timedelta(seconds=runtimeint))
        
        if os.path.exists('config.ini'):
            try:
                config = ConfigParser(allow_no_value=True)
                config.read('config.ini')

                totalxp = config.getint('lifetime_values', 'totalxpamount')
                totalxp += self.xpamount
                
                totalgamesplayed = config.getint('lifetime_values', 'totalgamesplayed')
                totalgamesplayed += self.gamesplayed
                
                runtimeafterestarts = config.getfloat('lifetime_values', 'totalruntime')
                runtimeafterestarts = int(runtimeraw + runtimeafterestarts)
                totalruntime = str(datetime.timedelta(seconds=runtimeafterestarts))
                
            except Exception:
                pass

        global line
        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] SEARCHING FOR THE XP SCREEN")

        time.sleep(3)

        now = time.time()

        future = now + 600
        while True:
            if keyboard.is_pressed('f3'):
                self.pause()
            if self.too_long(future):
                break
                break

            if self.found(self.play_png):
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] DETECTED THE XP SCREEN")
                time.sleep(2)


                if os.path.exists('config.ini'):

                    config = ConfigParser(allow_no_value=True)
                    config.read('config.ini')

                    config.set('runtime_values', 'restarted', str(self.restarted))
                    config.set('runtime_values', 'gamesplayed', str(self.gamesplayed))
                    config.set('runtime_values', 'xpamount', str(self.xpamount))
                    config.set('runtime_values', 'runtime', str(runtimeint))
                    
                    with open('config.ini', 'w+') as configfile:
                        config.write(configfile)


                

                #exact = start.strftime("%H:%M:%S")
                #dat = start.strftime("%d %h %Y")

                webhookruntime = str(datetime.timedelta(seconds=int(time.time() - self.timestarted)))
                print(Style.RESET_ALL)
                print(Style.RESET_ALL)
                print(
                    Style.RESET_ALL + Fore.YELLOW + "——————————————————————————————————————————————————————")
                print(Style.RESET_ALL)
                print(Fore.YELLOW + " Earned",
                      Style.BRIGHT + Fore.YELLOW + str(self.xpamount) + " XP" + Style.RESET_ALL + Fore.YELLOW,
                      "this session")
                try:
                    print(Fore.YELLOW + " Earned", Style.BRIGHT + Fore.YELLOW + str(totalxp), "XP" + Style.RESET_ALL + Fore.YELLOW,"in total")
                except:
                    pass
                print(Fore.YELLOW + " Bot has been running for",
                      Style.BRIGHT + Fore.YELLOW + str(webhookruntime) + Style.RESET_ALL + Fore.YELLOW)
                #print(Fore.YELLOW + " Bot was started at", Style.BRIGHT + Fore.YELLOW + str(exact),
                  #    Style.RESET_ALL + Fore.YELLOW + "on the" + Style.BRIGHT + Fore.YELLOW,
                 #     dat + Style.RESET_ALL + Fore.YELLOW)
                print(Fore.YELLOW + " Played", Style.BRIGHT + Fore.YELLOW + str(self.gamesplayed), "games" + Style.RESET_ALL + Fore.YELLOW)
                print(" Valorant has been", Style.BRIGHT + Fore.YELLOW + "restarted", self.restarted, "times")
                print(Style.RESET_ALL)
                print(Style.RESET_ALL + Fore.YELLOW + "——————————————————————————————————————————————————————")
                print(Style.RESET_ALL)
                print(Fore.YELLOW + "                     " + self.version)
                print(Style.RESET_ALL)
                print(Style.RESET_ALL)
                time.sleep(1)


                if self.foundwebhook is True:
                    restartstring = (str(self.restarted) + " times")
                    if self.restarted == 0:
                        restartstring = "Not yet restarted"
                    elif self.restarted == 1:
                        restartstring = "1 time"
                    try:
                        webhook = DiscordWebhook(
                            url=self.hookline,
                            username="Valbot")

                        embed = DiscordEmbed(title='Valbot Summary', description='Valbot has completed a match loop!', color=34343)
                        embed.set_author(
                            name=self.version,
                            url="https://github.com/MrFums/Valbot",
                            icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbotlogo_22plusnobg.png",
                        )
                        textforfooter = "[" + self.computer_name + "] by Fums"
                        embed.set_footer(text=textforfooter, icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/fumspfp.png")
                        embed.set_timestamp()
                        embed.set_thumbnail(
                            url='https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbotlogo_22plus_curved.png')

                        embed.add_embed_field(name="XP Earned", value=self.xpamount, inline=False)
                        embed.add_embed_field(name="Games Played", value=self.gamesplayed, inline=False)
                        try:

                            
                            embed.add_embed_field(name="Runtime", value=webhookruntime, inline=False)
                        except:
                            pass
                        try:
                            embed.add_embed_field(name="Total XP Earned", value=totalxp, inline=False)
                            embed.add_embed_field(name="Total Games Played", value=totalgamesplayed, inline=False)

                            embed.add_embed_field(name="Total Runtime", value=totalruntime, inline=False)
                        except:
                            pass
                        
                        timestarted_format = time.strftime('%H:%M:%S, %d %B %Y', time.localtime(self.timestarted))
                        embed.add_embed_field(name="Started At", value=timestarted_format, inline=False)

                        webhook.add_embed(embed)
                        webhook.execute()
                    except:
                        pass

                    #except Exception:
                     #   print(Fore.RED + " [!] TRIED TO SEND A WEBHOOK BUT IT IS NOT SETUP")

                else:
                    print(Style.RESET_ALL)
                    print(Fore.RED + " [!] DISCORD WEBHOOK IS NOT SETUP")

                time.sleep(1)

                if os.path.exists('config.ini'):
                    config = ConfigParser(allow_no_value=True)
                    config.read('config.ini')

                    try:
                        self.xptarget = config.getint('settings', 'xptarget')
                        
                        
                        if self.xpamount >= self.xptarget and self.xptarget != 0:
                            if os.path.exists('config.ini'):

                                config = ConfigParser(allow_no_value=True)
                                config.read('config.ini')

                                config.set('settings', 'xptarget', '0')
                                
                                
                                with open('config.ini', 'w+') as configfile:
                                    config.write(configfile)
                            self.xptargethook()
                        


                    except:
                        pass # could not find xp target in config file

                    


                if os.path.exists('config.ini'):
                    config = ConfigParser(allow_no_value=True)
                    config.read('config.ini')
                    try:
                        matchlimit = config.getint('settings', 'matchlimit')


                        if matchlimit != 0: # check if there is a match limit set
                            matchlimit -= 1 # match limit found so remove 1 from it

                            if matchlimit == 0: # if match limit is now 1, stop bot.
                                self.matchlimit()

                            else: # if match limit continued tell user how many matches left
                                config.set('settings', 'matchlimit', str(matchlimit))

                                with open('config.ini', 'w+') as configfile:
                                    config.write(configfile)

                                print(Style.RESET_ALL)
                                print(Fore.BLUE + Style.BRIGHT, "[√]" + str(matchlimit) + " MATCHES" + Style.RESET_ALL + Fore.YELLOW, "UNTIL LIMIT REACHED")
                        else:
                            print(Style.RESET_ALL)
                            print(Fore.BLUE + Style.BRIGHT,"[√] NO XP LIMIT FOUND")

                    except:
                        pass # could not find xp limit in config file

                if time.time() > self.restarttime:
                    self.titlescreen()
                    self.restartbot()
                time.sleep(5)
                self.playbutton()

def main():
    bot_obj = Bot()
    bot_obj.firststart()
  
if __name__=="__main__":
    main()