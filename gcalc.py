from ldtp import *
from ldtputils import *


try:
	wait (2)
	click ("frmCalculator", "btnNumeric8")
	click ("frmCalculator", "btnMultiply")
	click ("frmCalculator", "btnNumeric6")
	click ("frmCalculator", "btnCalculateresult")
except LdtpExecutionError, msg:
	raise
