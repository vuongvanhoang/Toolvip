
import os, sys, time, json, requests, threading
from datetime import datetime
from time import sleep
from rich.console import Console
from rich.table import Table
import cloudscraper

try:
    from pystyle import Colors, Colorate
except:
    os.system("pip install pystyle")
    from pystyle import Colors, Colorate

author = open("Authorization.txt").read().strip()
token = open("token.txt").read().strip()

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10)',
    'Referer': 'https://app.golike.net/account/manager/twitter',
}

scraper = cloudscraper.create_scraper()

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

def chonacc():
    try:
        res = scraper.get('https://gateway.golike.net/api/twitter-account', headers=headers)
        return res.json()
    except:
        return {"status": 403}

def nhannv(account_id):
    try:
        params = {'account_id': account_id, 'data': 'null'}
        res = scraper.get('https://gateway.golike.net/api/advertising/publishers/twitter/jobs',
                          headers=headers, params=params)
        return res.json()
    except:
        return None

def hoanthanh(ads_id, account_id):
    try:
        json_data = {
            'ads_id': ads_id,
            'account_id': account_id,
            'async': True,
            'data': None
        }
        res = scraper.post('https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs',
                           headers=headers, json=json_data, timeout=6)
        return res.json()
    except:
        return None

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
        scraper.post('https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs',
                     headers=headers, json=json_data2)
    except:
        pass

def chay_job_tung_acc(acc, delay):
    account_id = acc['id']
    screen_name = acc['screen_name']
    ads_ids_done = set()  # Dùng để lọc job trùng
    dem = 0
    tong = 0
    console = Console()
    while True:
        try:
            nhanjob = nhannv(account_id)
            if not nhanjob or nhanjob.get("status") != 200 or not nhanjob["data"].get("link"):
                print(f"[{screen_name}] Không có job, đang đợi...")
                time.sleep(3)
                continue

            ads_id = nhanjob["data"]["id"]
            if ads_id in ads_ids_done:
                continue
            ads_ids_done.add(ads_id)

            if nhanjob["data"]["type"] != "follow":
                baoloi(ads_id, nhanjob["data"]["object_id"], account_id, nhanjob["data"]["type"])
                continue

            for i in range(delay, 0, -1):
                print(f"[{screen_name}] Đợi {i}s để làm job...", end="")
                time.sleep(1)

            nhantien = hoanthanh(ads_id, account_id)
            if nhantien and nhantien.get("status") == 200:
                tien = nhantien["data"]["prices"]
                tong += tien
                dem += 1
                thoigian = time.strftime("%H:%M:%S", time.localtime())

                table = Table(show_header=True, header_style="bold magenta")
                table.add_column("STT", justify="center", style="bold yellow")
                table.add_column("Tài khoản", style="cyan")
                table.add_column("Thời gian", justify="center", style="green")
                table.add_column("Nhận được", style="bold green")
                table.add_column("Tổng xu", style="bold white")

                table.add_row(
                    str(dem),
                    screen_name,
                    thoigian,
                    f"+{tien}đ",
                    f"{tong}đ"
                )

                console.print(table)
                sleep(0.5)

            else:
                baoloi(ads_id, nhanjob["data"]["object_id"], account_id, nhanjob["data"]["type"])
                print(f"[{screen_name}]Job lỗi, đã bỏ qua.")
                time.sleep(1.5)

        except Exception as e:
            print(f"[{screen_name}] Lỗi: {e}")
            time.sleep(2)

def main():
    banner()
    dsacc = chonacc()
    if dsacc.get("status") != 200:
        print("Sai Authorization hoặc Token Golike!")
        return
    print("Danh sách tài khoản:")
    for i, acc in enumerate(dsacc["data"], 1):
        print(f"[{i}] {acc['screen_name']}")
    while True:
        try:
            print("Gợi ý: Delay nên là 60s (ban ngày) hoặc 120s (ban đêm)")
            delay = int(input("Nhập delay giữa các job (s): "))
            break
        except:
            print("Sai định dạng!")
    print("Bắt đầu chạy toàn bộ tài khoản...\n")
    threads = []
    for acc in dsacc["data"]:
        t = threading.Thread(target=chay_job_tung_acc, args=(acc, delay))
        t.start()
        threads.append(t)
        time.sleep(1)
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
