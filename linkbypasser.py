import requests
import shodan
import os
import platform
from datetime import date
from colorama import Fore, Back, Style
import json
import time
import socket
import re
import io
import tarfile
V_API = "8c2337b2f7536099da76ed1ee9e20b537ca1a9cc80a5e4e146908b6b5f9a648b"
S_API = "7LlJsHMKaLqNk0lG3NitI7CNWgdKvr4Q"
banner = """
 __       __  _______       _______    ______    ______   ________ 
/  \     /  |/       \     /       \  /      \  /      \ /        |
$$  \   /$$ |$$$$$$$  |    $$$$$$$  |/$$$$$$  |/$$$$$$  |$$$$$$$$/ 
$$$  \ /$$$ |$$ |__$$ |    $$ |__$$ |$$ |  $$ |$$ |  $$ |   $$ |   
$$$$  /$$$$ |$$    $$<     $$    $$< $$ |  $$ |$$ |  $$ |   $$ |   
$$ $$ $$/$$ |$$$$$$$  |    $$$$$$$  |$$ |  $$ |$$ |  $$ |   $$ |   
$$ |$$$/ $$ |$$ |  $$ | __ $$ |  $$ |$$ \__$$ |$$ \__$$ |   $$ |   
$$ | $/  $$ |$$ |  $$ |/  |$$ |  $$ |$$    $$/ $$    $$/    $$ |   
$$/      $$/ $$/   $$/ $$/ $$/   $$/  $$$$$$/   $$$$$$/     $$/    
"""
def windowsScan(url):
    api = shodan.Shodan(S_API)
    print("")
    print(Fore.RED + "Url Will Be Worked With : "  + Style.RESET_ALL + url + Style.RESET_ALL)
    url_fix = url.replace("https://", "")
    url_fix2 = url_fix.replace("http://", "")
    url_fix_end = url_fix2.replace("/", "") 
    try : 
        search = socket.gethostbyname(url_fix_end)
    except:
        print("")
        print("Error [Socket] No Internet Connection Or FireWall Blocked The Request . ")
    time.sleep(1)
    os.system("cls")
    print(Fore.GREEN + "Shodan Search Started . . . " + Style.RESET_ALL )
    results = api.search(search)
    print("")
    print( Fore.RED +'Results found: {}'.format(results['total']) + Style.RESET_ALL )
    for result in results['matches']:
            print(Fore.RED + 'IP: {}'.format(result['ip_str']))
            print(result['data'])
            print('')
    print(Fore.GREEN + "Finshed . . . " + Style.RESET_ALL )
    print("")
    input("Press Enter To Complete..")
    os.system("cls")
    print(f"{Fore.RED} Starting Virus Total ... {Style.RESET_ALL}")
    time.sleep(1)
    os.system("cls")
    url = 'https://www.virustotal.com/vtapi/v2/url/scan'
    params = {'apikey': V_API, 'url':url}
    response = requests.post(url, data=params)
    print (json.dumps(response.json(), indent=4, sort_keys=True))
    print("")
    input("Press Enter To Complete..")
    os.system("cls")
    print(Fore.GREEN  + "getting info ...." + Style.RESET_ALL)
    url_V = 'https://www.virustotal.com/vtapi/v2/domain/report'
    params = {'apikey':V_API,'domain':url_fix_end}
    response = requests.get(url_V, params=params)
    print (json.dumps(response.json(), indent=4, sort_keys=True))
    #rint(response.json())
    #com = input(Fore.RED + "Do You Want To Scan it With VirusTotal ? Y/N : "+ Style.RESET_ALL )

def LinuxScan(url):
    api = shodan.Shodan(S_API)
    print("")
    print(Fore.RED + "Url Will Be Worked With : "  + Style.RESET_ALL + url + Style.RESET_ALL)
    url_fix = url.replace("https://", "")
    url_fix2 = url_fix.replace("http://", "")
    url_fix_end = url_fix2.replace("/", "") 
    try : 
        search = socket.gethostbyname(url_fix_end)
    except:
        print("")
        print("Error [Socket] No Internet Connection Or FireWall Blocked The Request . ")
    time.sleep(1)
    os.system("clear")
    print(Fore.GREEN + "Shodan Search Started . . . " + Style.RESET_ALL )
    results = api.search(search)
    print("")
    print( Fore.RED +'Results found: {}'.format(results['total']) + Style.RESET_ALL )
    for result in results['matches']:
            print(Fore.RED + 'IP: {}'.format(result['ip_str']))
            print(result['data'])
            print('')
    print(Fore.GREEN + "Finshed . . . " + Style.RESET_ALL )
    print("")
    input("Press Enter To Complete..")
    os.system("clear")
    print(f"{Fore.RED} Starting Virus Total ... {Style.RESET_ALL}")
    time.sleep(1)
    os.system("clear")
    url = 'https://www.virustotal.com/vtapi/v2/url/scan'
    params = {'apikey': V_API, 'url':url}
    response = requests.post(url, data=params)
    print (json.dumps(response.json(), indent=4, sort_keys=True))
    print("")
    input("Press Enter To Complete..")
    os.system("clear")
    print(Fore.GREEN  + "getting info ...." + Style.RESET_ALL)
    url_V = 'https://www.virustotal.com/vtapi/v2/domain/report'
    params = {'apikey':V_API,'domain':url_fix_end}
    response = requests.get(url_V, params=params)
    print (json.dumps(response.json(), indent=4, sort_keys=True))
    #rint(response.json())
    #com = input(Fore.RED + "Do You Want To Scan it With VirusTotal ? Y/N : "+ Style.RESET_ALL )
def Linux():
    print("")
    url = input(f" {Fore.RED}Enter Url Here : {Style.RESET_ALL} ")
    r = requests.get(url) 
    print(Fore.GREEN + "[*] Url Bypassed successfully : " + Style.RESET_ALL + Fore.WHITE +  r.url + Style.RESET_ALL)
    url_Linux = r.url
    LinuxScan(url_Linux)
def windows():
    print("")
    url = input(f" {Fore.RED}Enter Url Here : {Style.RESET_ALL} ")
    r = requests.get(url) 
    print(Fore.GREEN + "[*] Url Bypassed successfully : " + Style.RESET_ALL + Fore.WHITE +  r.url + Style.RESET_ALL)
    Url_Windows = r.url
    windowsScan(Url_Windows)
def startt():
    system = os.name
    if (system == "nt"):
        os.system("cls")
        today = date.today()
        date_time =  today.strftime("%B %d, %Y")
        print(f"{Fore.GREEN}Started On {date_time} {Style.RESET_ALL}")
        time.sleep(1)
        os.system("cls")
        time.sleep(0.50)
        info = f"{Fore.RED} System : {platform.system()} {Style.RESET_ALL} {Fore.GREEN} \n Realese : {platform.release()} {Style.RESET_ALL} {Fore.RED}  \n Machine : {platform.machine()} {Style.RESET_ALL} {Fore.GREEN} \n Processor : {platform.processor()} {Style.RESET_ALL}"
        print(Fore.RED  + " [*] Windows System Detected " + Style.RESET_ALL)
        time.sleep(0.70)
        print(Fore.GREEN + " [*] Starting Windows Function" + Style.RESET_ALL)
        time.sleep(0.70)
        os.system("cls")
        print(f"{Fore.RED} {banner} {Style.RESET_ALL}")
        print(Fore.WHITE + " \n [*] Started On : " + Style.RESET_ALL)
        print(info)
        windows()
    else :
        today = date.today()
        date_time =  today.strftime("%B %d, %Y")
        os.system("clear")
        print(f"{Fore.GREEN}Started On {date_time} {Style.RESET_ALL}")
        time.sleep(1)
        info = f"{Fore.RED} System : {platform.system()} {Style.RESET_ALL} {Fore.GREEN} \n Realese : {platform.release()} {Style.RESET_ALL} {Fore.RED}  \n Machine : {platform.machine()} {Style.RESET_ALL} {Fore.GREEN} \n Processor : {platform.processor()} {Style.RESET_ALL}"
        print(Fore.RED  + " [*] Linux System Detected " + Style.RESET_ALL)
        time.sleep(0.70)
        print(Fore.GREEN + " [*] Starting Linux Function" + Style.RESET_ALL)
        time.sleep(0.50)
        print(Fore.WHITE + " \n [*] Started On : " + Style.RESET_ALL)
        print(info)








startt()