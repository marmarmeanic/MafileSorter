import json

baseconfig = {
  "AcceptGifts": True,
  "BotBehaviour": 32,
  "Enabled": True,
  "FarmingOrders": [9],
  "SteamLogin": "login",
  "SteamPassword": "password",
  "SteamTradeToken": "SteamTradeToken",
  "SteamUserPermissions": {},
  "TradingPreferences": 1
}
config = json.loads(open('config.json').read())
