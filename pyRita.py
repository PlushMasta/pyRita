import os
import sys

from SaintRitaShield import ShieldUp

if __name__ == '__main__':
    if len(sys.argv) > 1:
        shieldUp = ShieldUp(sys.argv[1])
    else:
        print "execute with param: %s PathToDir" % os.path.basename(__file__)

