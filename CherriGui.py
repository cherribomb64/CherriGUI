import pyfiglet
from colorama import Fore, Style
import os
import subprocess
import time
from datetime import datetime
import random

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
    "Why was the math lecture so long? The professor kept going off on a tangent.",
    "Why did the chicken join a band? Because it had the drumsticks!",
    "What do you call fake spaghetti? An impasta!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "Why don’t some couples go to the gym? Because some relationships don’t work out.",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "What do you call cheese that isn't yours? Nacho cheese!",
    "Why don't programmers like nature? It has too many bugs.",
    "Why did the computer show up at work late? It had a hard drive.",
    "Why was the cell phone wearing glasses? Because it lost its contacts.",
    "Why did the coffee file a police report? It got mugged.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "Why can't your nose be 12 inches long? Because then it would be a foot.",
    "Why was the stadium so cool? It was filled with fans.",
    "What do you call an alligator in a vest? An investigator.",
    "Why did the cookie go to the doctor? Because it felt crummy.",
    "Why was the computer cold? It left its Windows open.",
    "Why did the scarecrow become a successful neurosurgeon? Because he was outstanding in his field and had a brain.",
    "What do you call a snowman with a six-pack? An abdominal snowman.",
    "Why don't eggs tell jokes? Because they'd crack each other up.",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
    "Why are ghosts bad liars? Because they are too transparent.",
    "Why did the stadium get hot after the game? Because all the fans left.",
    "What do you call a belt made out of watches? A waist of time.",
    "Why was the math book unhappy? It had too many problems.",
    "Why do bees have sticky hair? Because they use honeycombs.",
    "Why did the robot go on a diet? It had too many bytes.",
    "Why do seagulls fly over the sea? Because if they flew over the bay, they’d be bagels.",
    "Why was the broom late? It swept in.",
    "Why did the chicken cross the playground? To get to the other slide.",
    "Why did the orange stop? It ran out of juice.",
    "Why don’t oysters donate to charity? Because they are shellfish.",
    "Why was the math book sad? Because it had too many problems.",
    "Why did the scarecrow get promoted? Because he was outstanding in his field!",
    "Why did the frog take the bus to work today? His car got toad.",
    "Why did the cookie cry? Because his mom was a wafer too long.",
    "Why did the chicken go to the séance? To get to the other side.",
    "Why did the melon jump into the lake? Because it wanted to be a watermelon.",
    "What do you call a sleeping bull? A bulldozer.",
    "Why did the pony get sent to his room? He wouldn’t stop horsing around.",
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why do cows have hooves instead of feet? Because they lactose.",
    "Why was the math lecture so long? The professor kept going off on a tangent.",
    "What did the grape do when he got stepped on? Nothing but let out a little wine!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What do you get when you cross a snowman and a vampire? Frostbite.",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "What do you call a fake noodle? An impasta.",
    "Why did the chicken go to the seance? To get to the other side.",
    "Why did the computer keep sneezing? It had a virus!",
    "Why did the duck get arrested? For using foul language.",
    "Why do fish live in salt water? Because pepper makes them sneeze.",
    "Why did the bicycle fall over? Because it was two tired!",
    "What do you call an elephant that doesn’t matter? An irrelephant.",
    "Why did the cow jump over the moon? Because the farmer had cold hands.",
    "Why did the chicken join a band? Because it had the drumsticks!",
    "Why are ghosts bad liars? Because you can see right through them!",
    "Why did the scarecrow get promoted? Because he was outstanding in his field!",
    "Why did the chicken cross the road? To get to the other side!",
    "What do you call cheese that isn't yours? Nacho cheese!",
    "Why did the tomato blush? Because it saw the salad dressing!",
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "Why don’t some couples go to the gym? Because some relationships don’t work out.",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why did the skeleton go to the party alone? Because he had no body to go with.",
    "Why did the math book look so sad? Because it had too many problems.",
    "Why did the golfer bring extra pants? In case he got a hole in one.",
    "What do you call a fish with no eyes? Fsh.",
    "Why did the chicken sit on a clock? She wanted to lay time eggs.",
    "Why did the robot go on a diet? Because it had too many bytes.",
    "Why did the cookie go to the hospital? Because he felt crummy.",
    "Why was the computer cold? It left its Windows open.",
    "Why did the chicken cross the playground? To get to the other slide.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why did the math teacher break up with the calculator? She felt he was something she could always count on.",
    "What do you call a dinosaur with an extensive vocabulary? A thesaurus.",
    "Why don’t some couples go to the gym? Because some relationships don’t work out.",
    "Why did the coffee file a police report? It got mugged.",
    "Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25.",
    "Why did the chicken cross the road? To get to the other side!",
    "Why did the duck get arrested? For using foul language."
]

    print(f"{Fore.LIGHTRED_EX}{random.choice(jokes)}{Style.RESET_ALL}")

ascii_banner = pyfiglet.figlet_format("CHERRIgui", font="slant")
salmon_red = Fore.LIGHTRED_EX

clear_and_show_banner()

while True:
    try:
        cmd = input(f"{Fore.LIGHTRED_EX}Ɛ> {Style.RESET_ALL}").strip()

        if cmd.lower() == "cherri kill":
            print(f"{Fore.LIGHTRED_EX}Exiting CHERRI...{Style.RESET_ALL}")
            break
        elif cmd.lower() == "cherri clear":
            clear_and_show_banner()
        elif cmd.lower() == "cherri cls":
            clear_and_show_banner()
        elif cmd.lower() == "time":
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
                time.sleep(2)
            except FileNotFoundError:
                print(f"{Fore.RED}Directory not found: {path}{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        elif cmd == "":
            continue
        else:
            subprocess.run(cmd, shell=True)
    except KeyboardInterrupt:
        print("\nUse 'exit' to quit.")
    except Exception as e:
        print(f"Error: {e}")


# Aww, look at you! You've reached the bottom of the code! Im proud of you. - cherri