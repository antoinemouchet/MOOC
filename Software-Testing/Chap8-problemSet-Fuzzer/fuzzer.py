import random
import subprocess
import os
import time
import platform

# All images and mp4 are from pixabay (https://pixabay.com/)
# All wav and mp3 files are music from Vexento (youtube: https://www.youtube.com/user/Vexento/)

# -- SET UP --

# Get time when program started
actualTime = time.localtime()

# Create a string containing info on time at which program started
timeStringPath = ("%d-%d-%d-%dh%dmin%dsec" % (actualTime[2], actualTime[1], actualTime[0],\
    actualTime[3], actualTime[4], actualTime[5]))

# Get a random number and use it as seed
seed = random.randint(1, 100000000000)
# Change seed here to remake another test
random.seed(seed)

# -- DIRECTORY SETUP --
actualDir = os.getcwd()
initialDir = "%s\\Chap8-problemSet-Fuzzer\\Fuzzer\\Initial" % actualDir
fuzzedDir = "%s\\Chap8-problemSet-Fuzzer\\Fuzzer\\Fuzzed" % actualDir
logDir = "%s\\Chap8-problemSet-Fuzzer\\Fuzzer\\Logs" % actualDir

# Create directory for fuzzed files
fuzzedFilesDir = "\\".join([fuzzedDir, timeStringPath])
os.mkdir(fuzzedFilesDir)
# ---------------------

# -- DEFINE TEST VALUES --
# Define chosen app
chosenApp = "WMP"

# Define nb of tests to do
nbTest = 50

# Initialize corruption factor
corruptFactor = 100

# Dict with path of each program that can be tested
appsPath = {"WMP": "C:/Program Files (x86)/Windows Media Player/wmplayer.exe",
            "VLC": "D:/VLC/vlc.exe",
            "MPCHC": "C:/Program Files/MPC-HC/mpc-hc64.exe"}
# ------------------------

# -- PERMANENT VALUES --
# Initialize nb of crash at 0
nbCrash = 0

# Define initial fuzzed file name
basicFuzzedPath = "TestedFile"

# Size of fuzzed files directory
fuzzedDirSize = 0

# Define list of types availables
typeList = ['png', 'jpg', 'mp3', 'mp4', 'wav']

# Dict for sleeping times following file format
sleepingTime = {'png': 2,
                'jpg': 2,
                'mp3': 3,
                'mp4': 3,
                'wav': 3}
# ----------------------

# -- CREATION AND INITIALISATION OF LOG FILE --

# Change for clarity
if chosenApp == "WMP":
    chosenAppName = "Windows Media Player"
elif chosenApp == "MPCHC":
    chosenAppName = "Media Player Classic"
else:
    chosenAppName = chosenApp

# Generate name of logfile
logFileName = ("log-%s.txt" % timeStringPath)

# Generate log file path
logFilePath = "\\".join([logDir, logFileName])

# Get system info
sysInfo = platform.uname()

# Open log file in write mode or append at the end if already exists
log = open(logFilePath, 'a')

# Define string for system and fuzzing info.
platformInfo = ("Fuzzing started on: %s\nApp tested: %s\nSeed used: %d\n\n\
 SYSTEM INFO\n\
 -----------\n\
 System: %s\n\
 Version: %s\n\
 Machine: %s\n\
 Processor: %s\n\
 Total amount of cores: %d\n\n\
 LOGS\n\
 ----\n" % (time.asctime(actualTime), chosenAppName, seed, sysInfo[0], sysInfo[3], sysInfo[4], sysInfo[5], os.cpu_count()))

# Write platform info into log file
log.write(platformInfo)
# Close log file
log.close()
# -- END OF SETUP --

# -- START TESTING --
# Code adapted from Charlie's Miller "Babysitting an army of monkeys"

for testID in range(nbTest):
    # Open log file and append at the end
    log = open(logFilePath, 'a')

    # Choose a random type
    randType = random.choice(typeList)

    # Get directory path of type chosen
    directory = "\\".join([initialDir, randType])

    # Choose a random file from chosen type
    fileName = random.choice(os.listdir(directory))

    # Get path of file
    filePath = "\\".join([directory, fileName])

    # Open chosen file
    fileRead = open(filePath,'rb')

    # Read file as binary
    fileAsBytes = bytearray(fileRead.read())

    # Get size of array
    fileSize = len(fileAsBytes)

    # Get 10 percent of file size
    tenPercentFile = (10 * fileSize) // 100

    # Close file
    fileRead.close()

    # -- CORRUPT FILE -- 
    # Get random number of bytes to corrupt
    # Choose a random number in a range that gets smaller as the corrupt factor gets bigger.
    # Corrupt at least one
    NbCorrupt = (random.randrange(fileSize//corruptFactor)) + 1
    
    # Loop until we corrupted chosen amount of bytes
    for byte in range(NbCorrupt):

        # Get a random byte
        rbyte = random.randrange(256)

        # ---- TEST EXTREME CASES ----
        # Force random bytes on the start for 25% of test
        if testID < (25 * nbTest / 100):
            # Get a random index for bytes
            randIndex = random.randrange(0, tenPercentFile)
        
        # Force random bytes at the end for 10% of test
        elif testID > (90 * nbTest / 100):
           randIndex = random.randrange((fileSize - tenPercentFile), fileSize)
        
        # Force random bytes in the middle for 15% of test
        elif (testID > (25 * nbTest / 100) and testID < (40 * nbTest / 100)):
            randIndex = random.randrange(((fileSize//2)- tenPercentFile), ((fileSize//2) + tenPercentFile))

        # Random bytes anywhere
        else:
            randIndex = random.randrange(fileSize)

        # ---- END OF RANDOM GENERATING ----

        # Change byte by random byte at position wanted
        fileAsBytes[randIndex] = rbyte
    # -- END OF CORRUPTION --

    # -- STORE FUZZED FILE --
    # Generate path of fuzzed file
    corruptedFileName = basicFuzzedPath + ("%d.%s" % (testID + 1, fileName.split(".")[1]))
    fuzzedFilePath  = "\\".join([fuzzedFilesDir, corruptedFileName])

    # Open fuzzed file
    fuzzedFile = open(fuzzedFilePath, 'wb')

    # Write corrupted bytes into file
    fuzzedFile.write(fileAsBytes)

    # Close fuzzed file
    fuzzedFile.close()
    # -- FUZZED FILE STORED --

    # Add more info into logging file
    logSentence = ("Test number: %d\tType chosen: %s\tFile changed: %s\t" %\
     # Test id, type chose, file chosen
     (testID + 1, randType, fileName))

    # Clarity in log files
    if len(fileName) <= 17:
        logSentence += "\t"

    # Add number of bytes corrupted
    logSentence += "Nb of bytes changed: %d" % NbCorrupt

    # -- TESTING APP WITH FUZZED FILE --
    # Launch app with file specified
    appli = subprocess.Popen([appsPath[chosenApp], fuzzedFilePath])

    # Sleep depends of the file type
    time.sleep(sleepingTime[randType])

    # -- CHECK STATUS OF APP --
    status = appli.poll()
    # No crash
    if status == None:
        # Kill app and go to next line in log
        appli.terminate()

    # Crashed
    else:
        # Get return code of appli
        errorCode = appli.returncode

        # Make sure it was a crash (return code should be negative if crashed)
        if errorCode != 0:
            # Increase nb of crash by 1
            nbCrash += 1
            # Add log about what happened
            logSentence += ("\tError code: %d" % (errorCode))

    # -- END OF STATUS CHECK --
    # -- END OF TESTING WITH THIS FILE --

    # -- LOG WRITING --
    logSentence += "\n"
    # Write log for the file
    log.write(logSentence)
    # Close log file after each file
    log.close()
    # -----------------

    # -- SIZE OF FUZZED FILES DIRECTORY --
    # Increase size of directory by the size of the file
    fuzzedDirSize += os.path.getsize(fuzzedFilePath)
    # Check if size of dir is more than 1GB
    if (fuzzedDirSize / (1024**3)) > 1:
        # Delete all files in dir
        for fileToDel in os.listdir(fuzzedFilesDir):
            os.unlink("\\".join([fuzzedFilesDir, fileToDel]))
        
        # Reset size of directory now that it is empty
        fuzzedDirSize = 0
    # ------------------------------------

# Open log file in append mode
log = open(logFilePath, 'a')

# Write last sentence of file
log.write("\nProgram ended on: %s. It found: %d bug.\n" % (time.asctime(), nbCrash))

# Close log file
log.close()
