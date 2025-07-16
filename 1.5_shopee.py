try:
    import os
    import sys
    import time
    import json
    import random
    import string
    import requests
    import string
    import base64
    import subprocess
    from time import sleep
    import uuid
    import hashlib
    from colorama import Fore, init
    from collections import defaultdict    
    from datetime import datetime, timedelta
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich import box
    from colorama import init
    from pystyle import Colors, Colorate
except ModuleNotFoundError as e:
    lib = e.name
    print(f"Thiếu thư viện {lib}, đang cài đặt ...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', lib])
        print(f"Đã cài đặt {lib} thành công! ")
        os.system("cls" if os.name == "nt" else "clear")
        os.execl(sys.executable, sys.executable, *sys.argv)
    except subprocess.CalledProcessError:
        print(f"Không thể cài đặt {lib}, thoát tool ...")
        sys.exit(1)

        
        
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
AQUA = "\033[96m"
LIME = "\033[92m"

os.system("cls" if os.name == "nt" else "clear")
# import lại
import string
import requests
import random
from collections import defaultdict    
from datetime import datetime, timedelta
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box
from colorama import init
import cloudscraper
from colorama import Fore, init
from pystyle import Colors, Colorate 

import requests
import random
import string
import hashlib,os

trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam = '\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
AQUA = "\033[96m"
LIME = "\033[92m"
hongnhat = "#FFC0CB"
kt_code = "🌸"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
vua = "\033[1;39m[\033[1;32m ¤ \033[1;39m] \033[32;5;245m\033[1m\033[38;5;39m=> "

import threading
import base64
import os
import time
import re
import json
import random
import requests
import socket
import sys
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box
from colorama import Fore, init
from colorama import init
from pystyle import Colors, Colorate 
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor


RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
AQUA = "\033[96m"
LIME = "\033[92m"

def xoss(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.005)
os.system('cls' if os.name == 'nt' else 'clear')
xoss("\nVui Lòng Chờ... ")
sleep(1.5)
os.system('cls' if os.name == 'nt' else 'clear')
for i in range(1, 101):
  sys.stdout.write(f"\r{BOLD}{LIME}ĐANG LOAD TOOL + GIT +: [{i}% {'█' * (i // 2)}]{RESET}")
  sys.stdout.flush()
  sleep(0.03)  # Điều chỉnh thời gian chờ nếu cần
sleep(1)
import os
os.system("cls" if os.name == "nt" else "clear")
def xoss(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.005)
xoss('\n[●] Đang Load File Cần Thiết... ');time.sleep(0.10)
sleep(1.5)

os.system('cls' if os.name== 'nt' else 'clear')
def Update():
    exit('●] Đang Tiến Hành Vào Tool...... ')

sleep(1)
colors = [
    "\033[1;37m\033[1m",  # Trắng
    "\033[1;32m\033[1m",  # Xanh lá
    "\033[1;34m\033[1m",  # Xanh dương 
    "\033[1m\033[38;5;51m",  # Xanh nhạt
    "\033[1;31m\033[1m\033[1m",  # Đỏ
    "\033[1;30m\033{1m",  # Xám
    "\033[1;33m\033[1m",  # Vàng
    "\033[1;35m\033[1m",  # Tím
    "\033[32;5;245m\033[1m\033[38;5;39m",  # Màu đặc biệt
]

def thanhngang(so):
    for i in range(so):
        print(range+'\033[1;31m-',end ='')
    print('')

def kiem_tra_mang():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
    except OSError:
        print("Mạng không ổn định hoặc bị mất kết nối. Vui lòng kiểm tra lại mạng.")

kiem_tra_mang()

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
\033[1;33m╔═════════════════════════════════════════════════╗
\033[1;33m║                                                 \033[1;33m║
\033[1;33m║  \033[1;39m████████╗██╗  ██╗                              \033[1;33m║
\033[1;33m║  \033[1;39m╚══██╔══╝██║  ██║  \033[1;32m Admin\033[1;37m : \033[1;36mThiệu Hoàng        \033[1;33m║
\033[1;33m║     \033[1;39m██║   ███████║   \033[1;32mNgày\033[1;37m : \033[1;36m{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\033[1;33m ║
\033[1;33m║     \033[1;39m██║   ██╔══██║  \033[1;32m YouTube\033[1;37m : \033[1;36m@thieuhoang75    \033[1;33m║
\033[1;33m║     \033[1;39m██║   ██║  ██║  \033[1;32m Version\033[1;37m : \033[1;36mTool Gộp Vip     \033[1;33m║
\033[1;33m║     \033[1;39m╚═╝   ╚═╝  ╚═╝                              \033[1;33m║
\033[1;33m║      \033[1;32mBox Zalo \033[1;37m: \033[1;36mhttps://zalo.me/g/ahnoav496   \033[1;33m  ║
\033[1;33m╚═════════════════════════════════════════════════╝ 
""")

os.system('cls' if os.name== 'nt' else 'clear')
banner()
sleep(1.2)

    # Nhập auth golike
try:
  Authorization = open("Authorization.txt","x")
  t = open("token.txt","x")
except:
  pass
Authorization = open("Authorization.txt","r")
t = open("token.txt","r")
author = Authorization.read()
token = t.read()
if author == "":
  author = input(Colorate.Diagonal(Colors.red_to_green,"NHẬP AUTHORIZATION GOLIKE : \033[1;33m"))
  token = input(Colorate.Diagonal(Colors.green_to_red,"NHẬP TOKEN (T CỦA GOLIKE): \033[1;33m"))
  Authorization = open("Authorization.txt","w")
  t = open("token.txt","w")
  Authorization.write(author)
  t.write(token)
else:
  print(Colorate.Diagonal(Colors.white_to_black, "=================================================="))
  print(Colorate.Diagonal(Colors.red_to_white, "Nhập [ 1 ] Để Vào Tool TikTok "))
  print(Colorate.Diagonal(Colors.red_to_white, "Nhập [ 2 ] Để Thay Auth Golike Mới "))
  print(Colorate.Diagonal(Colors.white_to_black,"=================================================="))
  
  select = input(f"\033[1;32mNhập số : ")
  kiem_tra_mang()
  if select != "1":
    author = select
  if select == "2":
    for i in range(1, 101):
     sys.stdout.write(f"\r{BOLD}{AQUA} ĐANG TIẾN HÀNH XÓA AUTH CŨ : [{i}% {'║' * (i // 2)}]{RESET}")
     sys.stdout.flush()
     sleep(0.03)  # Điều chỉnh thời gian chờ nếu cần
    os.system('cls' if os.name== 'nt' else 'clear')
    print(banner)
    author = input("\033[1;33mNhập Auth Golike Mới : ")
    token = input("\033[1;32mNhập T Golike Mới : \033[1;33m")
    Authorization = open("Authorization.txt","w")
    t = open("token.txt","w")
    Authorization.write(author)
    t.write(token)
Authorization.close()
t.close()
os.system('cls' if os.name== 'nt' else 'clear')
banner()
print("\033[1;32mDanh Sách Acc Tik Tok Hiện Có ")
print("\033[97m==================================")
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://app.golike.net/account/manager/shopee',
}

scraper = cloudscraper.create_scraper()
def chonacc():
    json_data = {}
    try:
      response = scraper.get(
        'https://gateway.golike.net/api/shopee-account',
    
        headers=headers,
        json=json_data
     ).json()
      return response
    except Exception:
      sys.exit()

def nhannv(account_id):
    try:
        params = {
            'account_id': account_id,
            'data': 'null',
        }
   
        response = scraper.get(
            'https://gateway.golike.net/api/advertising/publishers/shopee/jobs',
            headers=headers,
            params=params,
            json={}
        )
        return response.json()
    except Exception:
      sys.exit()

def hoanthanh(ads_id, account_id):
    try:
        json_data = {
            'ads_id': ads_id,
            'account_id': account_id,
            'async': True,
            'data': None,
        }

        response = scraper.post(
            'https://gateway.golike.net/api/advertising/publishers/shopee/complete-jobs',
            headers=headers,
            json=json_data,
            timeout=6
        )
        return response.json()
    except Exception:
      sys.exit()

def baoloi(ads_id, object_id, account_id, loai):
    try:
        json_data1 = {
            'description': 'Tôi đã làm Job này rồi',
            'users_advertising_id': ads_id,
            'type': 'ads',
            'provider': 'tiktok',
            'fb_id': account_id,
            'error_type': 6,
        }

        scraper.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1)

        json_data2 = {
            'ads_id': ads_id,
            'object_id': object_id,
            'account_id': account_id,
            'type': loai,
        }

        scraper.post(
            'https://gateway.golike.net/api/advertising/publishers/shopee/skip-jobs',
            headers=headers,
            json=json_data2,
        )
    except Exception:
      sys.exit()

# Gọi chọn tài khoản một lần và xử lý lỗi nếu có
chontktiktok = chonacc()

def dsacc():
  if chontktiktok.get("status") != 200:  
    print("\033[1;31mAuthorization hoăc T sai 😂")
    quit()
  for i in range(len(chontktiktok["data"])):
    print(Colorate.Diagonal(Colors.green_to_red,f"[{i+1}] {chontktiktok["data"][i]["shopee_username"]} |  Online"))
dsacc() 
print("\033[97m==================================")
while True:
  try:
    luachon = int(input("\033[1;32mChọn tài khoản bạn muốn chạy : \033[1;33m"))
    while luachon > len((chontktiktok)["data"]):
      luachon = int(input("\033[1;31mAcc Này Không Có Trong Danh Sách Cấu Hình , Nhập Lại : \033[1;33m"))
    account_id = chontktiktok["data"][luachon - 1]["id"]
    break  
  except:
    print("\033[1;31m Sai Định Dạng ") 
while True:
  try:
    os.system('cls' if os.name== 'nt' else 'clear')
    print(banner)
    delay = int(input(f"\033[1;32mDelay thực hiện job  : \033[1;33m"))
    break
  except:
    print("\033[1;31m Sai Định Dạng ")
while True:
  try: 
    os.system('cls' if os.name== 'nt' else 'clear')
    doiacc = int(input(f"\033[1;32mThất bại bao nhiêu lần thì đổi acc tiktok : \033[1;33m"))
    break
  except:
    print("\033[1;31mNhập Vào 1 Số ")  
    
os.system('cls' if os.name== 'nt' else 'clear')
print("\033[1;33mCHỌN JOB ĐỂ LÀM KIẾM TIỀN")
print("")
print("\033[1;36mNhập \033[1;39m[\033[1;36m1\033[1;39m] Thực Hiện NV \033[1;33mFollow  ")
print("\033[1;36mNhập \033[1;39m[\033[1;36m2\033[1;39m] Thực Hiện NV \033[1;31mLike Video Job ")
print("\033[1;36mNhập \033[1;39m[\033[1;36m3\033[1;39m] Thực Hiện Cả 2 NV \033[1;33mFOLLOW + \033[1;31mLIKE  ")

while True:
    try:
        loai_nhiem_vu = int(input("\033[1;32mChọn loại nv cần kiếm tiền : \033[1;33m "))
        if loai_nhiem_vu in [1, 2, 3]:
            break
        else:
            print("\033[1;31mVui lòng chọn số từ 1 đến 3!")
    except:
        print("\033[1;31mSai định dạng! Vui lòng nhập số.")  

os.system('cls' if os.name== 'nt' else 'clear')
x_like, y_like, x_follow, y_follow = None, None, None, None

print("\033[1;36mAUTOCLICK VÀ ADB ")
print("")
print(Colorate.Diagonal(Colors.cyan_to_green,f"Nhập [ 1 ] Để Sử Dụng ADB "))
print(Colorate.Diagonal(Colors.cyan_to_green,f"Nhập [ 2 ] Để Bấm Tay Không Dùng ADB "))

adbyn = input(Colorate.Diagonal(Colors.cyan_to_green,f"Nhập lựa chọn   "))

if adbyn == "1":
    def setup_adb():
      config_file = "adb_config.txt"
      like_coords_file = "toa_do_tim.txt"
      follow_coords_file = "toa_do_follow.txt"

    # Nhập IP và port ADB
      print(Colorate.Diagonal(Colors.blue_to_cyan,"Bạn có thể xem video hướng dẫn kết nối ADB ở trên các video Youtube!!! "))
      ip = input(Colorate.Diagonal(Colors.cyan_to_green,"Nhập IP của thiết bị ví dụ (192.168.1.1): "))
      adb_port = input(Colorate.Diagonal(Colors.cyan_to_green,"Nhập port của thiết bị ví dụ (838699): "))

      # Kiểm tra và đọc tọa độ từ file nếu tồn tại
      x_like, y_like, x_follow, y_follow = None, None, None, None
    
      if os.path.exists(like_coords_file):
           with open(like_coords_file, "r") as f:
              coords = f.read().split("|")
              if len(coords) == 2:
                   x_like, y_like = coords
                   print(Colorate.Diagonal(Colors.cyan_to_green,f"Đã tìm thấy tọa độ nút tim sau : X={x_like}, Y={y_like}"))
    
      if os.path.exists(follow_coords_file):
          with open(follow_coords_file, "r") as f:
               coords = f.read().split("|")
               if len(coords) == 2:
                   x_follow, y_follow = coords
                   print(Colorate.Diagonal(Colors.cyan_to_green,f"Đã tìm thấy tọa độ nút follow sau : X={x_follow}, Y={y_follow}"))
      if not os.path.exists(config_file):
           print(Colorate.Diagonal(Colors.cyan_to_green,"Lần đầu chạy thì nhập mã ghép nối (6 SỐ) và port ghép nối ở Gỡ lỗi Wi-Fi.\033[0m"))
           pair_code = input(Colorate.Diagonal(Colors.cyan_to_green,"Nhập mã ghép nối 6 số ví dụ (322763): \033[1;33m"))
           pair_port = input(Colorate.Diagonal(Colors.cyan_to_green,"Nhập port ghép nối ví dụ (44832): \033[1;33m"))

           with open(config_file, "w") as f:
               f.write(f"{pair_code}|{pair_port}")
      else:
          with open(config_file, "r") as f:
               pair_code, pair_port = [s.strip() for s in f.read().split("|")]
  
      print("\n\033[1;33m Đang ghép nối với thiết bị của bạn...\033[0m")
      os.system(f"adb pair {ip}:{pair_port} {pair_code}")
      time.sleep(2)
  
      print("\033[1;33mĐang kết nối ADB\033[0m")
      os.system(f"adb connect {ip}:{adb_port}")
      time.sleep(2)
  
      devices = os.popen("adb devices").read()
      if ip not in devices:
        print(f"{Fore.RED}Kết nối không thành công do lỗi.Hãy thử lại sau! {Fore.WHITE}")
        exit()
    

       # Yêu cầu nhập tọa độ nếu chưa có
      os.system('cls' if os.name== 'nt' else 'clear')
      print("\033[1;33m NHẬP TỌA ĐỘ ")
      print("")
      if loai_nhiem_vu in [1, 3] and (x_follow is None or y_follow is None):
           x_follow = input("\033[1;32mNhập tọa độ X của nút follow : \033[1;33m ")
           y_follow = input("\033[1;32mNhập tọa độ Y của nút follow : \033[1;33m ")
           with open(follow_coords_file, "w") as f:
               f.write(f"{x_follow}|{y_follow}")
    
      if loai_nhiem_vu in [2, 3] and (x_like is None or y_like is None):
           x_like = input("\033[1;32mNhập tọa độ X của nút tim: \033[1;33m ")
           y_like = input("\033[1;32mNhập tọa độ Y của nút tim: \033[1;33m ")
           with open(like_coords_file, "w") as f:
              f.write(f"{x_like}|{y_like}")

      return x_like, y_like, x_follow, y_follow

# Khi gọi hàm setup_adb()
    x_like, y_like, x_follow, y_follow = setup_adb()
elif adbyn == "2":
    pass
# Thêm phần chọn loại nhiệm vụ sau khi chọn tài khoản và trước khi bắt đầu làm nhiệm vụ
   
dem = 0
tong = 0
checkdoiacc = 0
dsaccloi = []
accloi = ""
os.system('cls' if os.name== 'nt' else 'clear')

banner()
print(" \033[1;31mSTT \033[1;39m║ \033[1;33m THỜI GIAN \033[1;39m ║ \033[1;32mSUCCESS \033[1;39m║ \033[1;34mJOB TYPE \033[1;39m║ \033[1;36mTIỀN LOẠI JOB \033[1;39m║ \033[1;33mTỔNG ")
print("")
while True:
    if checkdoiacc == doiacc:
        dsaccloi.append(chontktiktok["data"][luachon - 1]["nickname"])
        print(f"{Fore.CYAN}══════════════════════════════════════════════════════")
        print(Colorate.Diagonal(Colors.blue_to_cyan," Acc Tiktok bn chọn gặp vấn đề hoặc bị nhả !!!"))
        print(f"{Fore.CYAN}══════════════════════════════════════════════════════")
        dsacc()
        while True:
            try:
                print(f"{Fore.CYAN}════════════════════════════════════════════════════")
                luachon = int(input("\033[1;32mChọn tài khoản : \033[1;33m"))
                while luachon > len((chontktiktok)["data"]):
                    luachon = int(input("\033[1;31m Acc Này Không Có Trong Danh Sách Cấu Hình, Hãy Nhập Lại Acc Khác : \033[1;33m"))
                account_id = chontktiktok["data"][luachon - 1]["id"]
                checkdoiacc = 0
                os.system('cls' if os.name== 'nt' else 'clear')
                for h in banner:
                    print(h,end = "")
                break  
            except:
                print("\033[1;31mSai Định Dạng !!!")
    print('\033[1;35m ĐANG TÌM JOB KIẾM TIỀN  ', end="\r")
    max_retries = 3
    retry_count = 0
    nhanjob = None

    while retry_count < max_retries:
        try:
            nhanjob = nhannv(account_id)
            if nhanjob and nhanjob.get("status") == 200 and nhanjob["data"].get("link") and nhanjob["data"].get("object_id"):
                break
            else:
                retry_count += 1
                time.sleep(2)
        except Exception as e:
            retry_count += 1
            time.sleep(1)

    if not nhanjob or retry_count >= max_retries:
        continue

    ads_id = nhanjob["data"]["id"]
    link = nhanjob["data"]["link"]
    object_id = nhanjob["data"]["object_id"]
    job_type = nhanjob["data"]["type"]

    # Kiểm tra loại nhiệm vụ
    if (loai_nhiem_vu == 1 and job_type != "follow") or \
       (loai_nhiem_vu == 2 and job_type != "like") or \
       (job_type not in ["follow", "like"]):
        baoloi(ads_id, object_id, account_id, job_type)
        continue

    # Mở link và kiểm tra lỗi
    try:
        if adbyn == "1":
            os.system(f'adb shell am start -a android.intent.action.VIEW -d "{link}" > /dev/null 2>&1')
        else:
            #os.system(f"termux-open-url {link}")
            subprocess.run(["termux-open-url", link])
        
        for remaining in range(3, 0, -1):
            time.sleep(1)
        print("\r" + " " * 30 + "\r", end="")

    except Exception as e:
        baoloi(ads_id, object_id, account_id, job_type)
        continue

    # Thực hiện thao tác ADB
    if job_type == "like" and adbyn == "1" and x_like and y_like:
        os.system(f"adb shell input tap {x_like} {y_like}")
    elif job_type == "follow" and adbyn == "1" and x_follow and y_follow:
        os.system(f"adb shell input tap {x_follow} {y_follow}")

    # Đếm ngược delay
    for remaining_time in range(delay, -1, -1):
        color = "\033[1;35m" if remaining_time % 2 == 0 else "\033[1;36m"
        print(f"\r{color} Vương Văn Hoàng [{remaining_time}s]   ", end="")
        time.sleep(1)
    print("\r                          \r", end="") 
    color = "\033[1;35m" if remaining_time % 2 == 0 else "\033[1;33m"
    print(f"{color} Đang Nhận Tiền Lần 1 ... ",end = "\r")

    # Hoàn thành job
    max_attempts = 2
    attempts = 0
    nhantien = None
    while attempts < max_attempts:
        try:
            nhantien = hoanthanh(ads_id, account_id)
            if nhantien and nhantien.get("status") == 200:
                break
        except:
            pass  
        attempts += 1

    if nhantien and nhantien.get("status") == 200:
        dem += 1
        tien = nhantien["data"]["prices"]
        tong += tien
        local_time = time.localtime()
        hour = local_time.tm_hour
        minute = local_time.tm_min
        second = local_time.tm_sec
        h = hour
        m = minute
        s = second
        if hour < 10:
            h = "0" + str(hour)
        if minute < 10:
            m = "0" + str(minute)
        if second < 10:
            s = "0" + str(second)
                                      
        chuoi = (f"\033[1;31m {dem} \033[1;39m║ "
                f"\033[1;33m{h}:{m}:{s} \033[1;39m ║ "
                f"\033[1;32m SUCCESS \033[1;39m║ "
                f"\033[1;34m {job_type} \033[1;39m ║ "
                f"\033[1;36m +{tien} \033[1;39m ║ "
                f"\033[1;33m {tong} vnđ \033[1;39m  ")
                

        print("                                                    ", end="\r")
        print(chuoi)
        time.sleep(0.7)
        checkdoiacc = 0
    else:
        try:
            baoloi(ads_id, object_id, account_id, nhanjob["data"]["type"])
            print("\033[1;35m Bỏ qua job lỗi thành công ", end="\r")
            sleep(1.5)
            checkdoiacc += 1
        except:
            pass
