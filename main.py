from threading import Semaphore, Thread
from os       import system
import requests, json, string, random, sys
from colorama import Fore, init

init(autoreset=True)

semaphore = Semaphore(300)
found = 0 
failed = 0

ascii_art = r"""
    ____  __                 __        __  _           
   / __ \/ /___ ___  _______/ /_____ _/ /_(_)___  ____ 
  / /_/ / / __ `/ / / / ___/ __/ __ `/ __/ / __ \/ __ \
 / ____/ / /_/ / /_/ (__  ) /_/ /_/ / /_/ / /_/ / / / /
/_/   /_/\__,_/\__, /____/\__/\__,_/\__/_/\____/_/ /_/ 
              /____/                                   
"""
def unsave():
    semaphore.acquire()
    global found, failed
    while True:
        try:
            first_letter = random.choice(string.ascii_lowercase)
            rest_of_username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
            new_username = first_letter + rest_of_username

            url = "https://accounts.api.playstation.com/api/v1/accounts/onlineIds"
            
            headers = {
                "Content-Type": "application/json; charset=UTF-8",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
            }

            data = {
                "onlineId": new_username,
                "reserveIfAvailable": False
            }

            
            response = requests.post(url, headers=headers, data=json.dumps(data))

            if response.text == "{}":
                found += 1
                system(f'title Playstation Username Checker ^| Available {found} ^| Not Available {failed}')
                sys.stdout.write("\r[" + Fore.GREEN + "+" + Fore.RESET + "]" + f" {new_username} Available" + Fore.GREEN)
                with open("x.txt", "a") as file:
                    file.write(new_username + "\n")
            else: 
                failed += 1
                system(f'title Playstation Username Checker ^| Available {found} ^| Not Available {failed}')
                sys.stdout.write("\r[" + Fore.RED + "-" + Fore.RESET + "]" + f" {new_username} Not Available" + Fore.GREEN)
                continue
        except:
            continue
            
        semaphore.release()



if __name__ == '__main__':
    system('cls')
    print(Fore.GREEN + ascii_art)
    Thread(target=unsave).start()