import sys, os

def change_path(path):
	try: os.chdir(path)
	except:
		if os.path.exists(path): print('Unknown error. Cannot proceed.')
		else: print('Path does not exist.')

def check_dir():
	return os.path.abspath('')

def print_dir():
	d = os.path.split(check_dir())
	print('Parent  Directory : %s' % d[0])
	print('Current Directory : %s' % d[1])

def init(path):
	path = os.path.abspath(path)
	return change_path(path)

FNS = {
		'$init' : init,
		'changedir': change_path,
		'checkdir-' : check_dir,
		'printdir': print_dir
		}

def cmd():
	if '$init' in FNS: FNS['$init']
	while True:
		cmdline = input('FileMan >>> ').split(maxsplit=1)
		if cmdline[0].lower() in ['exit', 'quit']: sys.exit(0)
		if cmdline[0] in FNS:
			if cmdline[0][0] == '$':
				print('You do not have permission to use this function.')
			else:
				try: r = FNS[cmdline[0]](*cmdline[1:])
				except:
					print("Unknown error. Cannot proceed.")
					continue
				if cmdline[0][-1] == '-': print(r)
		else: print('Command not found.')

if __name__ == '__main__':
	cmd()
