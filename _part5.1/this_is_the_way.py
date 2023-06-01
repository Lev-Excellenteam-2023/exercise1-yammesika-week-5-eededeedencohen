#==================
# זו הדרך - 5.1
#==================
import os

FOLDER_PATH = os.getcwd() +'/images'

# ----------------------------------------------------
# get_files get path of a folder and return list
# of all files name in the folder that contain "deep"
# ----------------------------------------------------
import os
def get_files(folder_path):
    files = os.listdir(folder_path)
    return [file for file in files if "deep" in file]


#----------------
# Main function
#----------------
def main():
    print(get_files(FOLDER_PATH))

if __name__ == "__main__":
    print(os.getcwd())
    main()