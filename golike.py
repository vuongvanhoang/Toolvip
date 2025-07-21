import subprocess
import sys
required_packages = {
    "requests": "requests",
    "pystyle": "pystyle",
    "colorama": "colorama",
    "rich": "rich",
    "bs4": "beautifulsoup4",
    "cloudscraper": "cloudscraper"
}
missing = False
for module_name, pip_name in required_packages.items():
    try:
        __import__(module_name)
    except ImportError:
        print(f"Đang cài đặt thư viện thiếu: {pip_name} ...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])
            missing = True
        except Exception as e:
            print(f"Cài thư viện {pip_name} thất bại: {e}")
            missing = True
if missing:
    print("\nĐã cài đặt thư viện cần thiết.")
    print("Vui lòng **chạy lại tool**.")
    sys.exit()
import os
import sys
import json
import base64
import uuid
import time
import socket
import random
import string
from datetime import datetime, timedelta
from random import randint
from time import sleep, strftime
import requests
import cloudscraper
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
from pystyle import Write, Colors
from rich.console import Console
from rich.text import Text
init(autoreset=True)
os.system('cls' if os.name=='nt' else 'clear')
red = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
cam = "\033[38;5;208m"
tim = "\033[1;35m"
lam = "\033[1;36m"
trang = "\033[1;37m"
listck = []
listjob = []
import socket
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
banner()
console = Console()
def get_shortened_link_yeumoney(url):
    token = "47afc4032f15cbfd8c7a5b4bd2e32b2b60bc2eed25afc54b8580f2ccec7c61d6"  # Thay bằng token của bạn
    api_url = f"https://yeumoney.com/QL_api.php?token={token}&format=text&url={url}"
    try:
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            return response.text.strip()  # Lấy link rút gọn
        else:
            return "Lỗi khi kết nối API!"
    except Exception as e:
        return f"Lỗi Mạng"
# Hàm tạo key ngẫu nhiên
def generate_random_key(length=8):
    """Tạo chuỗi ngẫu nhiên với chữ cái + số."""
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=length))
def generate_key(is_admin=False):
    """Tạo key, admin key không hết hạn."""
    if is_admin:
        return "vuongvanhoang"  # Key admin không có ngày hết hạn
    else:
        return f"vuongvanhoang-{generate_random_key(10)}"  # Key user
# Hàm lưu key vào file (chỉ lưu 1 key)
def save_key_to_file(key):
    """Lưu key vào file, ghi đè để chỉ lưu 1 key."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Thời gian lưu key
    with open("key.txt", "w") as f:  # Dùng mode "w" để ghi đè
        f.write(f"{key} | {timestamp}\n")
# Hàm kiểm tra và xóa key nếu đã qua 00:00
def clean_expired_key():
    """Xóa key nếu đã qua 00:00 của ngày hôm sau."""
    if not os.path.exists("key.txt"):
        return    
    updated_lines = []
    current_time = datetime.now()
    current_date = current_time.date()  # Ngày hiện tại    
    with open("key.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            try:
                key, timestamp = line.strip().split(" | ")
                key_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                key_date = key_time.date()  # Ngày tạo key
                # Nếu key không phải admin và đã qua ngày mới (00:00), bỏ qua
                if not key.startswith("vuongvanhoang") and key_date == current_date:
                    updated_lines.append(line)
                elif key.startswith("vuongvanhoang"):  # Giữ lại key admin
                    updated_lines.append(line)
            except:
                continue    
    # Ghi lại key còn hiệu lực (nếu không còn key nào thì file sẽ trống)
    with open("key.txt", "w") as f:
        f.writelines(updated_lines)
# Hàm kiểm tra key hợp lệ
def is_valid_key(key, expected_key):
    """Kiểm tra key có hợp lệ không."""
    clean_expired_key()  # Dọn dẹp key hết hạn trước    
    if key == "vuongvanhoang":
        return True  # Key admin hợp lệ mọi lúc
    elif key == expected_key:  # So sánh với key đã tạo
        return True
    return False
# Hàm kiểm tra key đã lưu và còn hạn không
def check_stored_key():
    """Kiểm tra xem có key nào còn hạn trong file không, trả về key nếu hợp lệ."""
    clean_expired_key()  # Dọn dẹp key hết hạn trước    
    if not os.path.exists("key.txt"):
        return None, None    
    current_time = datetime.now()
    current_date = current_time.date()  # Ngày hiện tại
    with open("key.txt", "r") as f:
        for line in f:
            try:
                stored_key, timestamp = line.split(" | ")
                stored_key = stored_key.strip()
                key_time = datetime.strptime(timestamp.strip(), "%Y-%m-%d %H:%M:%S")
                key_date = key_time.date()  # Ngày tạo key
                if stored_key == "vuongvanhoang":
                    return stored_key, stored_key  # Key admin luôn hợp lệ
                elif stored_key.startswith("vuongvanhoang-"):
                    if key_date == current_date:  # Key chỉ hợp lệ trong cùng ngày
                        return stored_key, stored_key
            except:
                continue
    return None, None
# ======= Chạy Tool =======
try:
    admin_key = "vuongvanhoang"    
    # Kiểm tra xem có key nào còn hạn trong file không
    stored_key, user_key = check_stored_key()    
    # Nếu không có key còn hạn, tạo key mới và yêu cầu người dùng vượt link
    if not stored_key:
        user_key = generate_key(is_admin=False)
        # Tạo link YeuMoney chứa key
        link_can_rut = f"https://flowing-silo-450510-e1.web.app/key/?ma={user_key}"  # Thay bằng URL mới của bạn
        short_link = get_shortened_link_yeumoney(link_can_rut)
        console.print(f"[bold red][bold yellow]LINK[/bold yellow] [bold white]|[/bold white][bold magenta]VƯỢT LINK ĐỂ LẤY KEY[/bold magenta][/bold red][bold green]: {short_link}[/bold green]")        
        while True:
            nhap_key = console.input("[bold blue][[bold red]NHẬP KEY[bold blue]][/bold blue][bold yellow]==>> [/bold yellow]").strip()           
            if is_valid_key(nhap_key, user_key):
                # Lưu key vừa nhập thành công vào file (ghi đè key cũ)
                save_key_to_file(nhap_key)
                print("\nKey hợp lệ! Đang vào Tool...", end="\r")
                time.sleep(3)  # Chờ 3 giây trước khi vào tool
                print("\033[F\033[K" * 3, end="")  # Xóa 3 dòng vừa in
                break  
            else:
                print("\nKey không hợp lệ. Vui lòng vượt link để lấy key!", end="\r")
                time.sleep(2)
                print("\033[F\033[K" * 2, end="")  # Xóa 2 dòng vừa in
    else:
        # Nếu có key còn hạn, hiển thị link YeuMoney nhưng không yêu cầu nhập lại
        link_can_rut = f"https://flowing-silo-450510-e1.web.app/key/?ma={user_key}"
        short_link = get_shortened_link_yeumoney(link_can_rut)
        console.print(f"[bold green]Key [bold blue]{stored_key}[bold green] còn hạn. Đang vào Tool...[/bold green]")
        time.sleep(2)  # Chờ 3 giây trước khi vào tool
        print("\033[F\033[K" * 4, end="")
except Exception as e:
    console.print(f"[bold red]ErrolKey: {e}[/bold red]")
    
    
import requests    
import os,sys
from time import sleep, strftime
from datetime import datetime
from pystyle import Colors, Colorate   
from rich.console import Console
def kiem_tra_mang():	
 red = "\033[1;31m"
 luc = "\033[1;32m"
 vang = "\033[1;33m"
 cam = "\033[38;5;208m"
 tim = "\033[1;35m"
 lam = "\033[1;36m"
 trang = "\033[1;37m"
os.system('cls' if os.name == 'nt' else 'clear')
banner()
print (Colorate.Diagonal(Colors.blue_to_white, "┌──────────────────────┐"))
print (Colorate.Diagonal(Colors.blue_to_white, "║     Tool Golike      ║"))
print (Colorate.Diagonal(Colors.blue_to_white, "└──────────────────────┘"))
print(                    f" \033[1;37m=> \033[1;32mNhập \033[1;39m[\033[1;33m1\033[1;39m]\033[1;32m Tool Golike TikTok ") 
print(                    f" \033[1;37m=> \033[1;32mNhập \033[1;39m[\033[1;33m2\033[1;39m]\033[1;32m Tool Golike Tiktok Lọc Job 42₫") 
print(                    f" \033[1;37m=> \033[1;32mNhập \033[1;39m[\033[1;33m3\033[1;39m]\033[1;32m Tool Golike LinkedIn") 
print(                    f" \033[1;37m=> \033[1;32mNhập \033[1;39m[\033[1;33m4\033[1;39m]\033[1;32m Tool Golike SnapChat ") 
print(                    f" \033[1;37m=> \033[1;32mNhập \033[1;39m[\033[1;33m5\033[1;39m]\033[1;32m Tool Golike Twitter") 
print(                    f" \033[1;37m=> \033[1;32mNhập \033[1;39m[\033[1;33m6\033[1;39m]\033[1;32m Tool Golike Pinterest") 
print(                    f" \033[1;37m=> \033[1;32mNhập \033[1;39m[\033[1;33m7\033[1;39m]\033[1;32m Tool Golike Shopee") 
print(                    f" \033[1;37m=> \033[1;32mNhập \033[1;39m[\033[1;33m8\033[1;39m]\033[1;32m Tool Golike Threads") 
print(                    f" \033[1;37m=> \033[1;32mNhập \033[1;39m[\033[1;33m9\033[1;39m]\033[1;32m Tool Golike Instagram") 
print (Colorate.Diagonal(Colors.blue_to_white, "┌──────────────────────┐"))
print (Colorate.Diagonal(Colors.blue_to_white, "║     Tool Cày Xu      ║"))
print (Colorate.Diagonal(Colors.blue_to_white, "└──────────────────────┘"))
print(                    f" \033[1;37m=> \033[1;32mNhập \033[1;39m[\033[1;33m10\033[1;39m]\033[1;32m Tool Trao Đổi Sub Tiktok") 
print(                    f" \033[1;37m=> \033[1;32mNhập \033[1;39m[\033[1;33m11\033[1;39m]\033[1;32m Tool Trao Đổi Sub Instagram") 
print(                    f" \033[1;37m=> \033[1;32mNhập \033[1;39m[\033[1;33m12\033[1;39m]\033[1;32m Tool Trao Đổi Sub Facebook") 
print(                    f" \033[1;37m=> \033[1;32mNhập \033[1;39m[\033[1;33m13\033[1;39m]\033[1;32m Tool Tương Tác Chéo Facebook") 
print (Colorate.Diagonal(Colors.blue_to_white, "┌──────────────────────┐"))
print (Colorate.Diagonal(Colors.blue_to_white, "║    Tool Profile      ║"))
print (Colorate.Diagonal(Colors.blue_to_white, "└──────────────────────┘"))
print(                    f" \033[1;37m=> \033[1;32mNhập \033[1;39m[\033[1;33m14\033[1;39m]\033[1;32m Tool Buff Share Ảo Cookie") 
print(                    f" \033[1;37m=> \033[1;32mNhập \033[1;39m[\033[1;33m15\033[1;39m]\033[1;32m Tool Get Token Facebook 16 Loại") 
print(                    f" \033[1;37m=> \033[1;32mNhập \033[1;39m[\033[1;33m16\033[1;39m]\033[1;32m Tool Lấy ID Bài Viết, ID Facebook") 
print(                    f" \033[1;37m=> \033[1;32mNhập \033[1;39m[\033[1;33m17\033[1;39m]\033[1;32m Tool Get Cookie Facebook Bằng TK MK") 
print(                    f" \033[1;37m=> \033[1;32mNhập \033[1;39m[\033[1;33m18\033[1;39m]\033[1;32m Tool Spam Tin Nhắn, War Messenger") 
print (Colorate.Diagonal(Colors.blue_to_white, "┌──────────────────────┐"))
print (Colorate.Diagonal(Colors.blue_to_white, "║    Tool Tiện Ích     ║"))
print (Colorate.Diagonal(Colors.blue_to_white, "└──────────────────────┘"))
print(                    f" \033[1;37m=> \033[1;32mNhập \033[1;39m[\033[1;33m19\033[1;39m]\033[1;32m Tool Doss Web + Doss IP") 
print(                    f" \033[1;37m=> \033[1;32mNhập \033[1;39m[\033[1;33m20\033[1;39m]\033[1;32m Tool Get Proxy") 
print(                    f" \033[1;37m=> \033[1;32mNhập \033[1;39m[\033[1;33m21\033[1;39m]\033[1;32m Tool Lọc Proxy") 
print(                    f" \033[1;37m=> \033[1;32mNhập \033[1;39m[\033[1;33m22\033[1;39m]\033[1;32m Tool Scan Mail Ảo Lấy Mã") 
print(                    f" \033[1;37m=> \033[1;32mNhập \033[1;39m[\033[1;33m23\033[1;39m]\033[1;32m Tool Spam SĐT")
print(                    f" \033[1;37m=> \033[1;32mNhập \033[1;39m[\033[1;33m24\033[1;39m]\033[1;32m Tool Buff Tiktok [PC]")
print(                    f" \033[1;37m=> \033[1;32mNhập \033[1;39m[\033[1;33m25\033[1;39m]\033[1;32m Tool Tool Reg Nick FB")  
print(f"\033[1;37m---------------------------------------------------  ")
chon = input(" \033[1;37m=> \033[1;32mNhập Tool Mà Bạn Muốn Chạy :\033[1;37m ")    
kiem_tra_mang()
if chon == "1":
            try:               
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/vuongvanhoang/Toolvip/refs/heads/main/1.py').text
              exec(code, globals())
            except:
              sys.exit()  
if chon == "2":
            try:               
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/vuongvanhoang/Toolvip/refs/heads/main/2.py').text
              exec(code, globals())
            except:
              sys.exit()  
if chon == "3":
            try:               
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/vuongvanhoang/Toolvip/refs/heads/main/3.py').text
              exec(code, globals())
            except:
              sys.exit()          
if chon == "4":
            try:               
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/vuongvanhoang/Toolvip/refs/heads/main/4.py').text
              exec(code, globals())
            except:
              sys.exit()          
if chon == "5":
            try:               
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/vuongvanhoang/Toolvip/refs/heads/main/5.py').text
              exec(code, globals())
            except:
              sys.exit()       
if chon == "6":
            try:               
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/vuongvanhoang/Toolvip/refs/heads/main/6.py').text
              exec(code, globals())
            except:
              sys.exit()              
if chon == "7":
            try:               
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/vuongvanhoang/Toolvip/refs/heads/main/7.py').text
              exec(code, globals())
            except:
              sys.exit()  
if chon == "8":
            try:               
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/vuongvanhoang/Toolvip/refs/heads/main/8.py').text
              exec(code, globals())
            except:
              sys.exit()  
if chon == "9":
            try:               
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/vuongvanhoang/Toolvip/refs/heads/main/9.py').text
              exec(code, globals())
            except:
              sys.exit()                   
if chon == "10":
            try:               
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/vuongvanhoang/Toolvip/refs/heads/main/10.py').text
              exec(code, globals())
            except:
              sys.exit()  
if chon == "11":
            try:               
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/vuongvanhoang/Toolvip/refs/heads/main/11.py').text
              exec(code, globals())
            except:
              sys.exit()       
if chon == "12":
            try:               
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/vuongvanhoang/Toolvip/refs/heads/main/12.py').text
              exec(code, globals())
            except:
              sys.exit()              
if chon == "13":
            try:               
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/vuongvanhoang/Toolvip/refs/heads/main/13.py').text
              exec(code, globals())
            except:
              sys.exit()         
if chon == "14":
            try:               
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/vuongvanhoang/Toolvip/refs/heads/main/14.py').text
              exec(code, globals())
            except:
              sys.exit()            
if chon == "15":
            try:               
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/vuongvanhoang/Toolvip/refs/heads/main/15.py').text
              exec(code, globals())
            except:
              sys.exit()         
if chon == "16":
            try:               
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/vuongvanhoang/Toolvip/refs/heads/main/16.py').text
              exec(code, globals())
            except:
              sys.exit()        
if chon == "17":
            try:               
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/vuongvanhoang/Toolvip/refs/heads/main/17.py').text
              exec(code, globals())
            except:
              sys.exit()              
if chon == "18":
            try:               
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/vuongvanhoang/Toolvip/refs/heads/main/18.py').text
              exec(code, globals())
            except:
              sys.exit()              
if chon == "19":
            try:               
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/vuongvanhoang/Toolvip/refs/heads/main/19.py').text
              exec(code, globals())
            except:
              sys.exit()              
if chon == "20":
            try:               
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/vuongvanhoang/Toolvip/refs/heads/main/20.py').text
              exec(code, globals())
            except:
              sys.exit()              
if chon == "21":
            try:               
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/vuongvanhoang/Toolvip/refs/heads/main/21.py').text
              exec(code, globals())
            except:
              sys.exit()              
if chon == "22":
            try:               
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/vuongvanhoang/Toolvip/refs/heads/main/22.py').text
              exec(code, globals())
            except:
              sys.exit()              
if chon == "23":
            try:               
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/vuongvanhoang/Toolvip/refs/heads/main/23.py').text
              exec(code, globals())
            except:
              sys.exit()            
if chon == "24":
            try:               
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/vuongvanhoang/Toolvip/refs/heads/main/24.py').text
              exec(code, globals())
            except:
              sys.exit()             
if chon == "25":
            try:               
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/vuongvanhoang/Toolvip/refs/heads/main/25.py').text
              exec(code, globals())
            except:
              sys.exit()                                                 