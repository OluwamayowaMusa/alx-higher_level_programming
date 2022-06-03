#!/usr/bin/python3
import sys

argc = len(sys.argv) - 1  # Arguments count
if (argc == 0):
    print("{} arguments.".format(argc))
else:
    if (argc == 1):
        print("{} argument:".format(argc))
    else:
        print("{} argumemts:".format(argc))
    for i in range(1, argc + 1):
        print("{}: {}".format(i, sys.argv[i]))
