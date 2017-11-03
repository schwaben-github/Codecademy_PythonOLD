#49. Skipping an iteration
usernames = ['maclover', 'linuxjane', 'windowseightforever', 'osagnostic', 'psychoabracadabra']
for item in usernames:
    if len(item) > 10:
        print ("Too long")
        continue
    else:
        print "Welcome " + item
