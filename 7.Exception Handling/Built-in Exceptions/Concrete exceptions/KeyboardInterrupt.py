try:
	print ('Press Return or Ctrl-C:')
	ignored = raw_input()
except (Exception, err):
	print ('Caught exception:', err)
except (KeyboardInterrupt, err):
	print ('Caught KeyboardInterrupt',err)
else:
	print ('No exception')
