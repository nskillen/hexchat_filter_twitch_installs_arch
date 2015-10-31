__module_name__ = 'TwitchInstalls Filter'
__module_version__ = '1.0'
__module_description__ = 'Filters commands for Twitch Installs Arch Linux stream'

import hexchat

CHANNEL = '#twitchinstallsarchlinux'
BOTNAME = 'twitchinstallsarchlinux'
COMMANDS = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","w","W","x","X","y","Y","z","Z","0","1","2","3","4","5","6","7","8","9","!","at","#","$","%","^","&","*","(",")","-","_","'","\"","dot",":",";","=",">","<","`","~","slash","?","backslash","[","]","{","}","escape","backspace","enter","space","tab","up","down","left","right","f1","f2","f3","f4","f5","f6","f7","f8","f9","alt-f1","alt-f2","alt-f3","alt-f4","alt-f5","alt-f6","alt-f7","alt-f8","alt-f9","ctrl-a","ctrl-b","ctrl-c","ctrl-d","ctrl-e","ctrl-f","ctrl-g","ctrl-h","ctrl-i","ctrl-j","ctrl-k","ctrl-l","ctrl-m","ctrl-n","ctrl-o","ctrl-p","ctrl-q","ctrl-r","ctrl-s","ctrl-t","ctrl-u","ctrl-v","ctrl-w","ctrl-x","ctrl-y","ctrl-z","nop","system_reset","boot_cd","boot_drive","yes"]
FAKE_COMMANDS = ["minus","dash"]

def is_command(msg):
	return msg in COMMANDS or msg in FAKE_COMMANDS

def on_message(word, word_eol, userdata):
	"""Strip out commands being sent to the VM
	"""
	if hexchat.get_info('channel').startswith(CHANNEL) and is_command(word[1]):
		return hexchat.EAT_ALL
	elif hexchat.get_info('channel').startswith(CHANNEL) and word[0] == BOTNAME:
		print('\002\00304%s' % word[1])
		return hexchat.EAT_ALL
	
	return hexchat.EAT_NONE

hexchat.hook_print('CHannel Message', on_message)
print("%s loaded successfully" % __module_name__)