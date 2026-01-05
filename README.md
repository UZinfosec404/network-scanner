# Network Scanner (Linux)
![Banner](banner.png)

Bu loyiha Python va Scapy kutubxonasi yordamida yozilgan **oddiy tarmoq skaneri** hisoblanadi.  
Dastur ARP so‘rovlari orqali lokal tarmoqdagi qurilmalarni aniqlaydi va ularning **IP** hamda **MAC address**larini ko‘rsatadi.

⚠️ Ushbu dastur **faqat Linux operatsion tizimi** uchun mo‘ljallangan.

---

## Imkoniyatlari
- Lokal tarmoqni ARP orqali skanerlash
- IP va MAC manzillarni aniqlash
- Terminalda rangli chiqish
- Natijalarni log faylga yozish

---

## Talablar
- Linux OS
- Python 3
- Root huquqi (sudo)
- Scapy kutubxonasi

---

## O‘rnatish

```bash
git clone https://github.com/USERNAME/network-scanner.git
```
```
cd network-scanner 
```
```
pip3 install scapy 
```
## Ishga tushirish
```
sudo python3 scanner.py -i 192.168.1.0/24 
```
## Natija

Topilgan qurilmalar terminalda ko‘rsatiladi

Natijalar network_scanner.log fayliga quyidagicha yoziladi
```
══════════════════════════════ 05-01-2026 15:06:21 ══════════════════════════════
IP: 10.236.108.8    | MAC: e6:3d:4b:d0:47:56
IP: 10.236.108.146  | MAC: 08:00:27:83:9c:44
IP: 10.236.108.201  | MAC: 70:68:71:f2:58:36

══════════════════════════════ 05-01-2026 15:06:26 ══════════════════════════════
No active hosts found.

══════════════════════════════ 05-01-2026 15:06:41 ══════════════════════════════
IP: 10.236.108.8    | MAC: e6:3d:4b:d0:47:56
IP: 10.236.108.146  | MAC: 08:00:27:83:9c:44
IP: 10.236.108.201  | MAC: 70:68:71:f2:58:36

══════════════════════════════ 05-01-2026 15:22:18 ══════════════════════════════
IP: 10.236.108.8    | MAC: e6:3d:4b:d0:47:56
IP: 10.236.108.201  | MAC: 70:68:71:f2:58:36
```
