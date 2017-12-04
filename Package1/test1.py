import sys
print "Hello world from Test 1"

exit_code = 1
if exit_code != 0:
	print "This shall fail now with exit code ", exit_code

sys.exit(exit_code)
