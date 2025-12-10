import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN}👋🎉 welcome to sentient spy🎉{Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA}PLS ENTER NAME: {Style.RESET_ALL}").strip()
if not user_name:
    user_name = "STUPID AHH IDIOT"

ch = []
print(f"{Fore.GREEN}HALLO {user_name}")
print(f"{Fore.CYAN} TYPE SENTINCE AND I OBEZERVE AND TELL MOOD")
bob = Fore.YELLOW
jim = Fore.CYAN
print(f"Type{bob} 'reset' {jim},{bob} 'history'{jim}, {bob} or 'exit'{jim}, to quit{Style.RESET_ALL}")


while True:
    ui = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()
    if not ui:
        print(f"{Fore.RED}PLS ENTER TEXT.{Style.RESET_ALL}")
        continue
    if ui.lower() == "exit":
        print(f"\n{Fore.BLUE} GET OUT😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤😤{Style.RESET_ALL}")
        break
    elif ui.lower() == "reset":
        ch.clear()
        print(f"\n{Fore.BLUE} GET OUT, WE ARE SENDING THESE FILES ONLINE🧌🧌🧌🧌🧌🧌🧌🧌{Style.RESET_ALL}")
        continue
    elif ui.lower() == "history":
        if not ch:
            print(f"{bob} SOLD IT ALL ONLINE{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}📜 Conversation History:{Style.RESET_ALL}")

            for idx, (text, polarity, sentiment_type) in enumerate(ch, start=1):


                if sentiment_type == "Positive":

                    color = Fore.GREEN

                    emoji = "😊"

                elif sentiment_type == "Negative":

                    color = Fore.RED

                    emoji = "😳"

                else:

                    color = Fore.YELLOW

                    emoji = "😐"

                print(f"{idx}. {color}{emoji} {text} "f"(Polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}")
        continue

    polarity = TextBlob(ui).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"

        color = Fore.GREEN

        emoji = "😊"
    elif polarity < -0.25:
        
        sentiment_type == "Negative"

        color = Fore.RED

        emoji = "😭"
    else:
        sentiment_type = "neutral"
        color = Fore.YELLOW

        emoji = "😐"

    ch.append((ui,polarity, sentiment_type))
    print(f"{color}{emoji}{sentiment_type} sentiment detected"
          f"(polarity: {polarity: .2f}){Style.RESET_ALL}")

