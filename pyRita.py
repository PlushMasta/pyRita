import os
import sys

import SaintRitaShield

if __name__ == '__main__':
    if len(sys.argv) > 2:
        shieldUp = SaintRitaShield.ShieldUp(sys.argv[1], sys.argv[2])
    else:
        print("execute with params: python %s PathToDir fileExtension" % os.path.basename(__file__))
