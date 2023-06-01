#===================
# לחששנית - 5.3
#===================
import os
import re # regular expressions

LOGO_PATH = os.getcwd() + '/resources/logo.jpg'
TXT_LOGO_PATH = os.getcwd() + '/resources/txtLogo.txt' # temporary txt file 

#-------------------------------------------------------
# regular expression pattern that match all the strings
# that contains 5 or more lowcase letters and ends with "!"
#-------------------------------------------------------
pattern = re.compile(r'[a-z]{5,}!')


#-------------------------------------------------------
# Convert bytes to string Function: 
# steps:
# 1. write the bytes to txt file
# 2. read the txt file to a string - type is str
#-------------------------------------------------------
def convertBytesToString(bytes):
    with open(TXT_LOGO_PATH, 'w') as f2:
        f2.write(str(bytes)) # write the bytes to txt file
    with open(TXT_LOGO_PATH, 'r') as file:
        bytes_type_str = file.read() # read the txt file to a string - type is str
    return bytes_type_str


def GeneratorSecretMasage():
    #loop of read the image/logo.jpg file in binary mode - 20 next bytes and save it in a temp variable
    with open(LOGO_PATH, 'rb') as file:  
        while True:
            nextBytes = file.read(20) # read 20 next bytes - type is bytes
            # break when get to the end of the jpg file
            if len(nextBytes) == 0:
                break
            str_NextBytes = convertBytesToString(nextBytes) # convert the bytes to string
            matches = pattern.finditer(str_NextBytes) # find all the matches in the str_NextBytes 
            for match in matches:
                yield match.group() # yield the matches


#----------------
# Main function
#----------------
def main():
    # create a generator object
    secret_msg_iter = GeneratorSecretMasage()

    # print the secret message
    print("The secret message is: ")
    for msg in secret_msg_iter:
        print(msg)

    # delete the temporary txt file
    if os.path.exists(TXT_LOGO_PATH):
        os.remove(TXT_LOGO_PATH)

if __name__ == "__main__":
    main()

