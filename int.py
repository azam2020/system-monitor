import psutil

def get_wireless_interface():
    interfaces = psutil.net_if_stats()
    for interface, stats in interfaces.items():
        if stats.isup and 'wireless' in stats and stats.wireless:
            return interface
    return None

if __name__ == '__main__':
    wireless_interface = get_wireless_interface()
    if wireless_interface:
        print(f"The wireless network interface is: {wireless_interface}")
    else:
        print("No wireless network interface found.")
      
