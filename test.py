import os.path
import os
import shutil
import time

def debug(type, message):
    if type == 'w':
        print(f"[WARN]    ",message)
    elif type == 's':
        print(f"[SUCESS]    ",message)
    elif type == 'e':
        print(f"[ERROR]    ",message)
    elif type == 'i':
        print(f"[INFO]    ",message)

def nl(x=1):
    for i in range(x):print()

if __name__ == '__main__':

    # Get osu installation directory
    while True:
        time.sleep(1)
        nl()
        debug('i',"Enter OSU Installation Path (DO NOT USE BACKSLASH). For example: 'C:/User/OSU/'")
        # root_dir = input((">>> "))
        root_dir ='C:/Osu/'

        # Format the path
        if root_dir[-1] != '/':
            root_dir+= "/"

        time.sleep(1.5)
        nl()
        if os.path.isdir(root_dir):
            debug('s','Installation directory found')
        else:
            debug('e','Installation directory not found. Please try again.')
            continue

        time.sleep(1.5)
        # Check if this is THE osu directory or not.
        if os.path.isfile(root_dir+'osu!.exe'):
            debug('s','Osu executable found.')
        else:
            debug('w','Osu executable cannot be found in this directory. Be VERY SURE THAT THIS IS THE CORRECT DIRECTORY')  

        time.sleep(1.5)
        # Search for the songs folder
        songs_path = root_dir+'Songs/'
        if os.path.isdir(songs_path):
            debug('s','Beatmapsets folder found.')
            break
        else:
            debug('e','Could not find the songs folder, enter the directory properly')
            continue
    time.sleep(1.5)
    beatmap_count = len(os.listdir(songs_path))
    if beatmap_count == 0:
        debug('e','No beatmaps were found. Exiting')
        exit()
    debug('i',f'{beatmap_count} beatmaps found in the directory.')

    nl()
    #Get the backgrounds
    debug('i','Since mappers use both JPGs as well as PNGs for their backgrounds, both of the image types will be required.')
    nl(2)
    time.sleep(1.5)
    debug('i','Enter the filename of the image (excluding the extension): ')
    # image_name = input(">>> ")
    image_name= 'wall'

    time.sleep(1.5)
    nl()
    while True:
        print("Enter the path of the PNG Image (For example: C:/Users/John/Pictures/wally.png)")
        # png_path = input(">>> ")
        png_path = 'C:/Root/wall.png' 
        nl()
        time.sleep(1.5)
        if os.path.isfile(png_path):
            print("[SUCESS]     Image Found.")
            break
        else:
            print("[SUCESS]     Image Not Found.")
    
    time.sleep(1.5)
    nl()
    while True:
        print("Enter the path of the jpg Image (For example: C:/Users/John/Pictures/wally.jpg)")
        # jpg_path = input(">>> ") 
        jpg_path = 'C:/Root/wall.jpg'
        nl()
        time.sleep(1.5)
        if os.path.isfile(jpg_path):
            print("[SUCESS]     Image Found.")
            break
        else:
            print("[FAILURE]     Image Not Found.")

    #List all the beatmaps folders
    for song in os.listdir(songs_path):
        song_location = os.path.join(songs_path, song)
        #Get all the files in each beatmap folder
        for file in os.listdir(os.path.join(songs_path,song)):
            file_location = os.path.join(song_location,file)
            if ".png" in file or ".jpg" in file:
                if ".png" in file:
                    ext = ".png"
                else:
                    ext = ".jpg"

                #Store the image name
                old_image_name = str(file)
                # print(old_image_name)
                

                #Rename the old background
                os.replace(file_location,os.path.join(song_location,f'osureplace{ext}'))


                #Copy the new background
                shutil.copy(png_path,song_location)

                # Rename the new background
                os.replace(os.path.join(song_location,f'{image_name}.png'),os.path.join(song_location, old_image_name))



        
    
    


            
