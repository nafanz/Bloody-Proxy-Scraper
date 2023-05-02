import os
import time
import AutoUpdate

from antiskid import AntiSkid
from pystyle import Write, Colors

CurrentVersion = "2.0.7"

# Clean and Pause variables
def cls():
    os.system('cls')

def pause():
    os.system('pause >nul')

# Updaters
def MainUpdater():
    AutoUpdate.set_url("https://github.com/NoobToolzz/Bloody-Proxy-Scraper/blob/main/data/version.txt")
    AutoUpdate.set_download_link("https://raw.githubusercontent.com/NoobToolzz/Bloody-Proxy-Scraper/main/Bloody%20Proxy%20Scraper%20V2.py")
    AutoUpdate.set_current_version(CurrentVersion)

    if not AutoUpdate.is_up_to_date():
        AutoUpdate.download("Bloody Proxy Scraper V2.py")

def CommonUpdater():
    AutoUpdate.set_url("https://github.com/NoobToolzz/Bloody-Proxy-Scraper/blob/main/data/version.txt")
    AutoUpdate.set_download_link("https://raw.githubusercontent.com/NoobToolzz/Bloody-Proxy-Scraper/main/data/plugins/common.py")
    AutoUpdate.set_current_version(CurrentVersion)

    if not AutoUpdate.is_up_to_date():
        AutoUpdate.download("common.py")

    os.remove("data/plugins/common.py")
    os.rename("common.py", "data/plugins/common.py")

def SkidUpdater():
    AutoUpdate.set_url("https://github.com/NoobToolzz/Bloody-Proxy-Scraper/blob/main/data/version.txt")
    AutoUpdate.set_download_link("https://raw.githubusercontent.com/NoobToolzz/Bloody-Proxy-Scraper/main/data/plugins/antiskid.py")
    AutoUpdate.set_current_version(CurrentVersion)

    if not AutoUpdate.is_up_to_date():
        AutoUpdate.download("antiskid.py")

    # directory = os.getcwd()
    os.remove("data/plugins/antiskid.py")
    os.rename("antiskid.py", "data/plugins/antiskid.py")

# Check if version.txt exists because you don't need it, it's needed for updating
def VersionFileRemover():
    versionfile = "data/version.txt"
    if os.path.isfile(versionfile):
        Write.Print("Detected version.txt, deleting (not needed on local pc)\n", Colors.red_to_yellow, interval=0)
        time.sleep(2)
        os.remove(versionfile)
        Write.Print("Deleted version.txt\n", Colors.green_to_blue, interval=0)
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        pass
