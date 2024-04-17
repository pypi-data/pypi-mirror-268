
import os
import time
import os
import zipfile
import shutil
import subprocess
try:
    from illusioncolor import *
    from illusionanime import *
    import requests
    import shutil
except ImportError:
    _ = os.system('pip install requests illusionanime illusioncolor' if os.name == 'nt' else 'pip3 install requests illusionanime illusioncolor')
import requests
from illusioncolor import *
from illusionanime import *

logo=f"""{Plum1}
  _________              __  .__  _____                 ____ ___      .__                 __    
 /   _____/_____   _____/  |_|__|/ ____\__.__.         |    |   \____ |  |   ____   ____ |  | __
 \_____  \\\\____ \ /  _ \   __\  \   __<   |  |  ______ |    |   /    \|  |  /  _ \_/ ___\|  |/ /
 /        \  |_> >  <_> )  | |  ||  |  \___  | /_____/ |    |  /   |  \  |_(  <_> )  \___|    < 
/_______  /   __/ \____/|__| |__||__|  / ____|         |______/|___|  /____/\____/ \___  >__|_ \\
        \/|__|                         \/                           \/                 \/     \/
        
"""

logoss=f"""
  _________              __  .__  _____                 ____ ___      .__                 __    
 /   _____/_____   _____/  |_|__|/ ____\__.__.         |    |   \____ |  |   ____   ____ |  | __
 \_____  \\\\____ \ /  _ \   __\  \   __<   |  |  ______ |    |   /    \|  |  /  _ \_/ ___\|  |/ /
 /        \  |_> >  <_> )  | |  ||  |  \___  | /_____/ |    |  /   |  \  |_(  <_> )  \___|    < 
/_______  /   __/ \____/|__| |__||__|  / ____|         |______/|___|  /____/\____/ \___  >__|_ \\
        \/|__|                         \/                           \/                 \/     \/
                                    {Yellow} >> {Red}Team Illusion {Yellow}<<
"""




class install:
    def installer():
        ps_command = 'iwr -useb https://raw.githubusercontent.com/spicetify/spicetify-cli/master/install.ps1 | iex'
        subprocess.run(["powershell", "-Command", ps_command], check=True)
        
        spicetify_path = shutil.which('spicetify')
        if spicetify_path is None:
            url = 'https://raw.githubusercontent.com/spicetify/spicetify-cli/master/install.ps1'
            response = requests.get(url)
            with open('install.ps1', 'w') as file:
                file.write(response.text)
            os.system('powershell.exe -ExecutionPolicy ByPass -File install.ps1')

        spice_user_data_path = subprocess.check_output(['spicetify', 'path', 'userdata']).decode().strip()
        if not os.path.isdir(spice_user_data_path):
            spice_user_data_path = os.path.join(os.getenv('APPDATA'), 'spicetify')
        market_app_path = os.path.join(spice_user_data_path, 'CustomApps', 'marketplace')
        market_theme_path = os.path.join(spice_user_data_path, 'Themes', 'marketplace')

        shutil.rmtree(market_app_path, ignore_errors=True)
        shutil.rmtree(market_theme_path, ignore_errors=True)
        os.makedirs(market_app_path, exist_ok=True)
        os.makedirs(market_theme_path, exist_ok=True)


        url = 'https://github.com/spicetify/spicetify-marketplace/releases/latest/download/spicetify-marketplace.zip'
        response = requests.get(url)
        with open(os.path.join(market_app_path, 'marketplace.zip'), 'wb') as file:
            file.write(response.content)
        with zipfile.ZipFile(os.path.join(market_app_path, 'marketplace.zip'), 'r') as zip_ref:
            zip_ref.extractall(market_app_path)

        os.system('spicetify config custom_apps spicetify-marketplace- -q')
        os.system('spicetify config custom_apps marketplace')
        os.system('spicetify config inject_css 1 replace_colors 1')
        url = 'https://raw.githubusercontent.com/spicetify/spicetify-marketplace/main/resources/color.ini'
        response = requests.get(url)
        with open(os.path.join(market_theme_path, 'color.ini'), 'w') as file:
            file.write(response.text)
        os.system('spicetify backup')
        os.system('spicetify apply')

        
        

class animate:
    def checkreq():
        os.system('cls')
        print(f"{Yellow}{logoss}")
        print(f"{Red}》{Green}Check Requirement{White}.")
        time.sleep(0.8)
        os.system('cls')
        print(f"{Blue}{logoss}")
        print(f"{Red}》{Green}Check Requirement{White}..")
        time.sleep(0.8)
        os.system('cls')
        print(f"{Purple}{logoss}")
        print(f"{Red}》{Green}Check Requirement{White}...")
        time.sleep(0.8)
        
    def unlucking():
        os.system('cls')
        print(f"{Yellow}{logoss}")
        print(f"{Red}》{Green}Unlucking The Prumium.{White}.")
        time.sleep(0.8)
        os.system('cls')
        print(f"{Blue}{logoss}")
        print(f"{Red}》{Green}Unlucking The Prumium{White}..")
        time.sleep(0.8)
        os.system('cls')
        print(f"{Purple}{logoss}")
        print(f"{Red}》{Green}Unlucking The Prumium{White}...")
        time.sleep(0.8)
        

class main:
    def unluck():
        os.system("cls")
        writewayy(f"{Purple}{logoss}")
        animate.unlucking()
        install.installer()
        os.system("cls")
        writewayy(logo,0.01)
        print(f"{Yellow}[ {Green}✓ {Yellow}]{White} Premium Unlucked..! Open Spotify and Get the extensions from marketplace..")
        
    def is_spotify_installed():
        appdata_path = os.getenv('LOCALAPPDATA')
        spotify_path = os.path.join(appdata_path, 'Spotify')
        return os.path.exists(spotify_path)

    def start():
        os.system("cls")
        writewayy(logo,0.01)
        animate.checkreq()
        if main.is_spotify_installed()==True:
            os.system('cls')
            print(f"{Green}{logoss}")
            ask=input(f"{Red}》{Yellow}Have you installed Spotify from given url [Y/N]{White}: ").strip()
            if ask=="Y" or ask=="y":
                main.unluck()
            else:
                os.system('cls')
                print(f"{Red}{logoss}")
                print(f"{Yellow}[ {Red}x {Yellow}] {White}Please Uninstall The Spotify..!\n{Yellow}[ {Green}✓ {Yellow}]{White} Download from {Red}: {Green}https://download.scdn.co/SpotifySetup.exe")
        else:
            os.system("cls")
            print(f"{Red}{logoss}")
            print(f"[ {Green}! {Yellow}]{White} Download from {Red}: {Green}https://download.scdn.co/SpotifySetup.exe\n{Yellow}[ {Green}✓ {Yellow}]{White} After Installing Run this program again...")
            
        
        
if __name__=="__main__":
    try:
        main.start()
    except:
        pass