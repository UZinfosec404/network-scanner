# Network Scanner (Linux)

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
cd network-scanner ```
```
```
pip3 install scapy ```
```
sudo python3 scanner.py -i 192.168.1.0/24 ```
