import requests
import sys
import cmd
import colorama
from colorama import Style, Fore

class RokuRemote(cmd.Cmd):
    prompt = 'rokudigital> '
    intro = "Welcome to the rokudigital CLI. Type 'help' or '?' to list commands.\n"

    def __init__(self, roku_ip):
        super().__init__()
        self.roku_ip = roku_ip
        self.base_url = f'http://{self.roku_ip}:8060'

    def do_launch(self, app_id):
        """Launch an app by its ID. Usage: launch <app_id>"""
        if app_id:
            self.send_command(f'launch/{app_id}')
        else:
            print("Usage: launch <app_id>")

    def do_keypress(self, key):
        """Send a keypress command. Usage: keypress <key>"""
        if key:
            self.send_command(f'keypress/{key}')
        else:
            print("Usage: keypress <key>")

    def do_home(self, arg):
        """Press the Home button"""
        self.send_command('keypress/home')

    def do_up(self, arg):
        """Press the Up button"""
        self.send_command('keypress/up')

    def do_down(self, arg):
        """Press the Down button"""
        self.send_command('keypress/down')

    def do_left(self, arg):
        """Press the Left button"""
        self.send_command('keypress/left')

    def do_right(self, arg):
        """Press the Right button"""
        self.send_command('keypress/right')

    def do_select(self, arg):
        """Press the Select button"""
        self.send_command('keypress/select')

    def do_play(self, arg):
        """Press the Play button"""
        self.send_command('keypress/play')

    def do_pause(self, arg):
        """Press the Pause button"""
        self.send_command('keypress/pause')

    def do_exit(self, arg):
        """Exit the Roku Remote CLI"""
        print("Exiting...")
        return True

    def send_command(self, endpoint):
        try:
            url = f'{self.base_url}/{endpoint}'
            response = requests.post(url)
            if response.status_code == 200:
                print(f'Successfully sent command to {url}')
            else:
                print(f'Failed to send command to {url}. Status code: {response.status_code}')
        except Exception as e:
            print(f'Error sending command: {e}')

banner = f"""{Fore.MAGENTA}{Style.BRIGHT}
               __             ___       _ __        __
   _________  / /____  ______/ (_)___ _(_) /_____ _/ /
  / ___/ __ \/ //_/ / / / __  / / __ `/ / __/ __ `/ / 
 / /  / /_/ / ,< / /_/ / /_/ / / /_/ / / /_/ /_/ / /  
/_/   \____/_/|_|\__,_/\__,_/_/\__, /_/\__/\__,_/_/   
                              /____/                  
                                {Fore.BLUE}>>{Fore.LIGHTMAGENTA_EX} coded by: 0xMxnTy {Fore.BLUE}<<
                                {Fore.BLUE}>>{Fore.LIGHTMAGENTA_EX} version: 1.0 {Fore.BLUE}<<{Fore.MAGENTA}{Style.BRIGHT}
"""

if __name__ == '__main__':
    print(banner)
    roku_ip = input("Enter the Roku IP address: ")
    RokuRemote(roku_ip).cmdloop()
