import os
import constinfo
import os

STATE_NONE = "red"
STATE_NONE2 = '...'

PROXY_LOGIN = "185.146.232.35"
PROXY_CH1 = "185.146.232.35"
PROXY_CH2 = "185.146.232.35"
PROXY_CH3 = "185.146.232.35"
PROXY_CH4 = "185.146.232.35"

TEST_SRV = "168.119.226.104"
LOCAL_SRV = "127.0.0.1"

STATE_DICT = {
	0 : "red",
	1 : "green",
	2 : "yellow",
	3 : "cyan"
}
STATE_TEXT_NONE = "off"

STATE_TEXT_DICT = {
	0 : "OFFLINE",
	1 : "NORM",
	2 : "BUSY",
	3 : "FULL"
}

PROXIES = {
	"LOGIN":	[ PROXY_LOGIN, 11002 ],
	"CH1":		[ PROXY_CH1, 13101 ],
	"CH2":		[ PROXY_CH2, 13201 ],
	"CH3":		[ PROXY_CH3, 13301 ],
	"CH4":		[ PROXY_CH4, 13401 ],
}

if os.path.isfile("gamemaster"):
	constinfo.bIsDEV = True

# Used for server state determination - filled by introLogin.py
SERVER_STATE_TABLE = {}