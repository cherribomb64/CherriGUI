import pyfiglet
from colorama import Fore, Style
import os
import subprocess
import time
from datetime import datetime
import random
import sys

def clear_and_show_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(salmon_red + ascii_banner + Style.RESET_ALL)
    print(salmon_red + "by cherribomb64 :3" + Style.RESET_ALL)
    print()

def tell_joke():
    jokes = [
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "I told my computer I needed a break, and it said 'No problem — I'll go to sleep.'",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the math book look sad? Because it had too many problems.",
    ]
    print(f"{Fore.LIGHTRED_EX}{random.choice(jokes)}{Style.RESET_ALL}")

ascii_banner = pyfiglet.figlet_format("CHERRIgui", font="slant")
salmon_red = Fore.LIGHTRED_EX

clear_and_show_banner()

while True:
    try:
        # Use Fore.LIGHTRED_EX for both prompt and typed input
        sys.stdout.write(f"{Fore.LIGHTRED_EX}Ɛ> ")
        sys.stdout.flush()
        cmd = input().strip()

        if cmd.lower() == "cherri kill":
            print(f"{Fore.LIGHTRED_EX}Exiting CherriGui...{Style.RESET_ALL}")
            break
        elif cmd.lower() in ("cherri clear", "cherri cls"):
            clear_and_show_banner()
        elif cmd.lower() == "cherri time":
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"{Fore.LIGHTRED_EX}Current Time: {current_time}{Style.RESET_ALL}")
        elif cmd.lower() == "cherri joke":
            tell_joke()
        elif cmd.startswith("cd "):
            path = cmd[3:].strip().strip('"')
            try:
                os.chdir(path)
                print(f'{Fore.LIGHTRED_EX}changed directory to "{os.getcwd()}"!{Style.RESET_ALL}')
                time.sleep(1)
            except FileNotFoundError:
                print(f"{Fore.RED}Directory not found: {path}{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        elif cmd.startswith("ps:"):  # Run PowerShell command
            powershell_cmd = cmd[3:].strip()
            subprocess.run(["powershell", "-Command", powershell_cmd], shell=True)
        elif cmd == "":
            continue
        elif cmd.lower() == "cherri help":
            print("\nTutorial\n\nCherri Commands\ncherri help: pulls up this menu.\ncherri kill: exits the program.\ncherri joke: tells a random joke.\ncherri clear: cleans up the gui. (you can also use cls)\n\nPowershell\nuse ps: as a prefix to use powershell.\n")
        else:
            subprocess.run(cmd, shell=True)
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Use 'cherri kill' to quit.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

