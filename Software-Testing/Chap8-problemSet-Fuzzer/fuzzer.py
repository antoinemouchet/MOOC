import math
import random
import subprocess
import os
import time
import platform
import ctypes

# Get time when program started
actualTime = time.localtime()

# Create a string containing info on time at which program started
timeStringPath = ("%d-%d-%d-%dh%dmin%dsec" % (actualTime[2], actualTime[1], actualTime[0],\
    actualTime[3], actualTime[4], actualTime[5]))

# Get a random number and use it as seed
seed = random.randint(1, 100000000000)
random.seed(seed)

# Initialize directories
initialDir = "C:/Users/Antoine/Pictures/Fuzzer/Initial"
fuzzedDir = "C:/Users/Antoine/Pictures/Fuzzer/Fuzzed"
logDir = "C:/Users/Antoine/Pictures/Fuzzer/Logs"

# Define dico with paths of program
appsPath = {"WMP": "C:/Program Files (x86)/Windows Media Player/wmplayer.exe",
            "VLC": "D:/VLC/vlc.exe",
            "MPCHC": "C:/Program Files/MPC-HC/mpc-hc64.exe"}

# Define chosen app
chosenApp = "MPCHC"

# Create directory for fuzzed files
fuzzedFilesDir = "/".join([fuzzedDir, timeStringPath])
os.mkdir(fuzzedFilesDir)

# Generate name of logfile
logFileName = ("log-%s.txt" % timeStringPath)

# Generate log file path
logFilePath = "/".join([logDir, logFileName])

# Open log file in write mode or append ath the end if already exists
log = open(logFilePath, 'a')

# Get system info
sysInfo = platform.uname()
nbCPU = os.cpu_count()

# Change for clarity
if chosenApp == "WMP":
    chosenAppName = "Windows Media Player"
else:
    chosenAppName = chosenApp

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
 ----\n" % (time.asctime(actualTime), chosenAppName, seed, sysInfo[0], sysInfo[3], sysInfo[4], sysInfo[5], nbCPU))

# Write platform info into log file
log.write(platformInfo)

# Dict for sleeping times following file format
sleepingTime = {'png': 4,
                'jpg': 4,
                'mp3': 7,
                'mp4': 7}

# Define nb of tests to do
nbTest = 100

# Initialize nb of crash at 0
nbCrash = 0

# Initialize corruption factor
corruptFactor = 500

for testID in range(nbTest):

    # Define list of types availables
    typeList = ['png', 'jpg', 'mp3', 'mp4']

    # Choose a random type
    randType = random.choice(typeList)

    # Get directory path of type chosen
    directory = "/".join([initialDir, randType])

    # Choose a random file from chosen type
    fileName = random.choice(os.listdir(directory))

    # Get path of file
    filePath = "/".join([directory, fileName])

    # Open chosen file
    fileRead = open(filePath,'rb')

    # Read file as binary
    fileAsBytes = bytearray(fileRead.read())

    # Close file
    fileRead.close()

    # CORRUPT FILE
    # Get random number of bytes to corrupt
    # Choose a random number which gets smaller as the denominator gets bigger.
    NbCorrupt = random.randrange(math.ceil(len(fileAsBytes)/corruptFactor))
    
    # Loop until we corrupted chosen amount of bytes
    for byte in range(NbCorrupt):

        # Get a random byte
        rbyte = random.randrange(256)

        # Get a random index for bytes
        randIndex = random.randrange(len(fileAsBytes))

        # Change byte by random byte at position wanted
        fileAsBytes[randIndex] = rbyte

    # STORE FUZZED FILE     
    # Generate path of fuzzed file
    fuzzedFilePath  = "/".join([fuzzedFilesDir, fileName])

    # Open fuzzed file
    fuzzedFile = open(fuzzedFilePath, 'wb')
    
    # Write corrupted bytes into file
    fuzzedFile.write(fileAsBytes)

    # Close fuzzed file
    fuzzedFile.close()

    # Add more info into logging file
    logSentence = ("Test number: %d\tType chosen: %s\tFile changed: %s\tNb of bytes changed: %d" %\
     # Test id, type chose, file chosen, amount of bytes corrupted.
     (testID, randType, fileName, NbCorrupt))

    # TESTING APP WITH FUZZED FILE
    # Launch app with file specified
    appli = subprocess.Popen([appsPath[chosenApp], fuzzedFilePath])

    # Sleep depends of the file type
    time.sleep(sleepingTime[randType])

    # Get status of application
    status = appli.poll()
    
    # No crash
    if status == None:

        # Kill app and go to next line in log
        appli.terminate()

    # Crashed
    else:
        errorCode = ctypes.c_int32(appli.returncode).value

        # Make sure it was a crash (return code should be negative if crashed)
        if errorCode != 0:

            # Increase nb of crash by 1
            nbCrash += 1
            # Add log about what happened
            logSentence += ("\tError code: %d" % (errorCode))

    logSentence += "\n"

    # Write log for the file
    log.write(logSentence)

# Write last sentence of file
log.write("\nProgram ended on: %s. It found: %d bug.\n" % (time.asctime(), nbCrash))

# Close log file
log.close()
