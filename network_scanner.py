import scapy.all as scapy
import optparse
from datetime import datetime
import os
import sys
import ipaddress

class Style:
    CYAN = '\033[36m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    RED = '\033[31m'
    BOLD = '\033[1m'
    REVERSE = '\033[7m'
    RESET = '\033[0m'

def show_banner():
    banner = f"""{Style.CYAN}{Style.BOLD}
███╗   ██╗███████╗████████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗
████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝
██╔██╗ ██║█████╗     ██║   ██║ █╗ ██║██║   ██║██████╔╝█████╔╝ 
██║╚██╗██║██╔══╝     ██║   ██║███╗██║██║   ██║██╔══██╗██╔═██╗ 
██║ ╚████║███████╗   ██║   ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗
╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
    {Style.REVERSE}           NETWORK SCANNER | v1.0             {Style.RESET}{Style.CYAN}{Style.BOLD}
    {Style.REVERSE} GitHub: https://github.com/UZinfosec404      {Style.RESET}
    """
    print(banner)

def get_time():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--ip_address", dest="ip", help="Target IP/Subnet (e.g. 192.168.1.0/24)")
    (options, arguments) = parser.parse_args()

    if not options.ip:
        parser.error(f"{Style.RED}IP manzil ko'rsatilmadi. --help ni ko'ring.{Style.RESET}")

    try:
        ipaddress.ip_network(options.ip, strict=False)
    except ValueError:
        parser.error(f"{Style.RED}IP format xato. Misol: 192.168.1.0/24{Style.RESET}")

    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    try:
        
        answered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]
    except Exception as e:
        print(f"{Style.RED}Skanerlashda xatolik: {e}{Style.RESET}")
        return []

    clients_list = [] 
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def print_result(results):
    print(f"\n{Style.GREEN}{Style.BOLD}{'IP Address':<20} {'MAC Address':<20}")
    print("-" * 45 + f"{Style.RESET}")
    for client in results:
        
        print(f"{client['ip']:<20} {client['mac']:<20}")
    
    if not results:
        print(f"{Style.YELLOW}Hech qanday faol qurilma topilmadi.{Style.RESET}")
    print("\n")

def write_log(results):
    try:
        with open("network_scanner.log", "a", encoding="utf-8") as f:
            f.write(f"{'═'*30} {get_time()} {'═'*30}\n")
            if not results:
                f.write("No active hosts found.\n")
            else:
                for host in results:
                    f.write(f"IP: {host['ip']:<15} | MAC: {host['mac']}\n")
            f.write("\n")
    except Exception as e:
        print(f"Log yozishda xato: {e}")

if __name__ == "__main__":
 
    if os.geteuid() != 0:
        print(f"{Style.RED}[-] ROOT huquqi talab qilinadi (sudo ishlating).{Style.RESET}")
        sys.exit()

    show_banner()
    options = get_arguments()
    scan_result = scan(options.ip)
    print_result(scan_result)
    write_log(scan_result)