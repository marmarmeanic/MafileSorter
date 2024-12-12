from functions import validatemenu

while 1:
    print("""Mafile sorter by Marmarmeanic
1 - create ASF configs (Fill trade_token in cfg and accounts.txt)
2 - convert MaFiles to name.maFile
3 - convert Mafiles to steamid.maFile
4 - export data from mafiles (login:steamid) to use it in tables""")
    user_input = input()
    if not validatemenu(user_input): continue

