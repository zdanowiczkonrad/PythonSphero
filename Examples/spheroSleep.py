from sphero import core
s = core.Sphero("/dev/tty.Sphero-OOB-AMP-SPP")
print "Connecting to Sphero..."
s.connect()
s.sleep()
