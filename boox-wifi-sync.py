#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import argparse
import os
# you can add more than one ips! for use ip still use a Python list e.g.
# IPS = ['192.168.1.10']
IPS = ['192.168.1.10', "192.168.0.52"]
# path to your ffs_batch
FFS_BATCH = "/Users/magnus/Documents/note.ffs_batch"
MNT_PATH  = "/Users/magnus/mnt/note/"
def get_parser():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-v", "--verbose",
                        action="store_true", help="be verbose")
    return parser

def is_ok(hostname):
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        print(hostname, 'is up!')
        return True
    else:
        print(hostname, 'is down!')
        return False


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    os.system('cd ')        
    hostnames = IPS
    for h in hostnames:
        if is_ok(h):
            os.system('diskutil unmount /Users/magnus/mnt/note/')
            cmd = "echo 'ssh' | sshfs -o password_stdin -o allow_other,default_permissions -p 2222 ssh@" + h + ":/storage/emulated/0 " + MNT_PATH
            print(cmd)
            os.system(cmd)
            # Documents/
            cmd = "open -a FreeFileSync " + FFS_BATCH
            os.system(cmd)  #"open -a FreeFileSync")# ~/Documents/NovaX.ffs_batch")
            import time
            # time.sleep(60)
            break
