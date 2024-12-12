from functions import validatemenu
from mafileFunctions import *
import os

os.makedirs("temp", exist_ok=True)

while 1:
    print("""Mafile sorter by Marmarmeanic
1 - create ASF configs (Fill MasterTradeToken, MasterSteamid in config and accounts.txt)
2 - convert MaFiles to name.maFile
3 - convert Mafiles to steamid.maFile
4 - export data from mafiles (login:steamid) to use it in tables
5 - clear temp folder""")
    user_input = input()
    if not validatemenu(user_input): continue

    if user_input == "1":
        create_configs()

