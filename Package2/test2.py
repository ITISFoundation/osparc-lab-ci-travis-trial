import sys
print "Hello world from Test 2"

exit_code = 0
if exit_code != 0:
	print "This shall fail now with exit code ", exit_code
else:
	print "I think, this was a success :)"

sys.exit(exit_code)
