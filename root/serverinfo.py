import app

app.ServerName = None

STATE_NONE = '...'
		
STATE_DICT = {
	0 : '....',
	1 : 'NORM',
	2 : 'BUSY',
	3 : 'FULL'	}

SERVER1_CHANNEL_DICT = {
	1:{'key':11,'name':'Channel1','ip':'127.0.0.1','tcp_port':13001,'udp_port':13001,'state':STATE_NONE,},
	2:{'key':12,'name':'Channel2','ip':'127.0.0.1','tcp_port':13002,'udp_port':13002,'state':STATE_NONE,},
	3:{'key':12,'name':'Channel2','ip':'127.0.0.1','tcp_port':13002,'udp_port':13002,'state':STATE_NONE,},
	4:{'key':12,'name':'Channel2','ip':'127.0.0.1','tcp_port':13002,'udp_port':13002,'state':STATE_NONE,},
}

SERVER2_CHANNEL_DICT = {
	1:{'key':21,'name':'Channel1','ip':'159.69.114.21','tcp_port':13001,'udp_port':13001,'state':STATE_NONE,},
	2:{'key':22,'name':'Channel2','ip':'159.69.114.21','tcp_port':13002,'udp_port':13002,'state':STATE_NONE,},
	3:{'key':22,'name':'Channel2','ip':'159.69.114.21','tcp_port':13002,'udp_port':13002,'state':STATE_NONE,},
	4:{'key':22,'name':'Channel2','ip':'159.69.114.21','tcp_port':13002,'udp_port':13002,'state':STATE_NONE,},
}

REGION_NAME_DICT = {
	0 : 'GERMANY',
}

REGION_AUTH_SERVER_DICT = {
	0 : {
		1 : { 'ip':'127.0.0.1', 'port':11002, }, 
		2 : { 'ip':'159.69.114.21', 'port':11002, },
		}	
}

REGION_DICT = {
	0 : {
		1 : { 'name' : 'Windows', 'channel' : SERVER1_CHANNEL_DICT, },
		2 : { 'name' : 'FreeBSD', 'channel' : SERVER2_CHANNEL_DICT, },
		},
}

MARKADDR_DICT = {
	10 : { 'ip' : '127.0.0.1', 'tcp_port' : 13001, 'mark' : '10.tga', 'symbol_path' : '10', },
	20 : { 'ip' : '159.69.114.21', 'tcp_port' : 13001, 'mark' : '10.tga', 'symbol_path' : '10', },
	}

TESTADDR = { 'ip' : '127.0.0.1', 'tcp_port' : 50000, 'udp_port' : 50000, }

#DONE
