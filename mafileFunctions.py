import json
import os
from os.path import abspath

from cfg import baseconfig, config
import random

def create_configs():
    dir = f'./temp/configs-{str(random.randint(1000000, 99999999))}'
    os.mkdir(dir)

    accounts = []
    with open('accounts.txt') as f:
        for line in f:
            stripped_line = line.strip()
            if stripped_line:
                accounts.append(
                    {
                        "login": stripped_line.split(':')[0],
                        "password": stripped_line.split(':')[1]
                    }
                )

    for account in accounts:
        account_config = baseconfig
        account_config['SteamLogin'] = account['login']
        account_config['SteamPassword'] = account['password']
        account_config['SteamTradeToken'] = config['MasterTradeToken']
        account_config['SteamUserPermissions'] = {str(config['MasterSteamid']): 3}
        with open(f'{dir}/{account["login"]}.json', 'w') as f:
            f.write(json.dumps(account_config))
    normilized_dir = dir.replace('./', '\\').replace('/', '\\')

    os.system(rf'explorer.exe "{os.path.dirname(os.path.abspath(__file__))}{normilized_dir}"')
    print(rf'explorer.exe {os.path.dirname(os.path.abspath(__file__))}{normilized_dir}')

def rename_mafiles(ren_type):
    dir = f'./temp/rename-{str(random.randint(1000000, 99999999))}'
    os.mkdir(dir)
    #if ren_type == 'toid':

