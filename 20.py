import requests
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from datetime import datetime, timedelta
from colorama import Fore, Style
import os
# Danh sách các nguồn proxy
raw_proxy_sites = [
    "https://api.proxyscrape.com/?request=displayproxies&proxytype=http",
    "https://api.openproxylist.xyz/http.txt",
    "https://openproxylist.xyz/http.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://www.proxy-list.download/api/v1/get?type=http",
    "https://www.proxy-list.download/api/v1/get?type=https",
    "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt",
    "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt",
    "https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt",
]

proxies = []
os.system('clear')
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
# Tải proxy từ các nguồn
print("\033[1;32m[+] Đang tải proxy từ các nguồn...")
for site in raw_proxy_sites:
    try:
        response = requests.get(site, timeout=10)
        response.raise_for_status()
        for line in response.text.splitlines():
            line = line.strip()
            if ':' in line:
                proxies.append(line)
    except requests.RequestException as e:
        print(f"[-] Không thể tải proxy từ {site}: {e}")

print(f"[+] Đã thu thập {len(proxies)} proxy. Đang kiểm tra proxy live...")

# Tạo session dùng lại kết nối
session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=200, pool_maxsize=200)
session.mount('http://', adapter)
session.mount('https://', adapter)

# Khóa để tránh ghi file cùng lúc gây lỗi
file_lock = Lock()

# Hàm kiểm tra proxy
def is_proxy_live(proxy):
    try:
        test_url = 'https://api64.ipify.org?format=json'
        response = session.get(test_url, proxies={
            'http': f'http://{proxy}',
            'https': f'http://{proxy}',
        }, timeout=3)
        if response.ok:
            print(f"[LIVE] {proxy}")
            with file_lock:
                with open('proxy.txt', 'a') as f:
                    f.write(proxy + '\n')
    except:
        pass

# Dùng đa luồng để kiểm tra proxy
with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(is_proxy_live, proxies)

print("[+] Kiểm tra hoàn tất. Proxy live đã được lưu vào proxy.txt")
