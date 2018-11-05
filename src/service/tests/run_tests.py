# --------------------------------------------------------------------------------------------------------------------
# <copyright file="run_tests.py" company="Microsoft">
#   2018 William M Mortl
# </copyright>
# --------------------------------------------------------------------------------------------------------------------
import errno
import os
import subprocess
import sys

if __name__ == '__main__':

    # list of all files
    fileList = os.listdir()

    # loop through subdirectories, and look for and then execute tests
    for directory, subdirectories, fileList in os.walk("."):
        for fileName in fileList:
            if (fileName.startswith("test_")):
                print("Running test: " + fileName + "...")
                if (subprocess.call(["python3", fileName]) != 0):
                    print("ERROR in unit test: " + fileName, sys.stderr)
                    sys.exit(errno.ENOTRECOVERABLE)
                else:
                    print("Ok")