from ldtp import *
from ldtputils import *

try:
	wait (3)
	click ("*gedit*", "btnNew")
	wait (2)
	click ("*gedit*", "btnOpen")
	waittillguiexist ("dlgOpenFiles")
	click ("dlgOpenFiles", "tbtnroot")
	wait (5)
	click ("dlgOpenFiles", "btnCancel")
	waittillguinotexist ("dlgOpenFiles")
except LdtpExecutionError, msg:
	raise
