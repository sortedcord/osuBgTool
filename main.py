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
    #Check for dependencies
    try:
        import cv2
    except ImportError:
        debug('e', 'OpenCV not found, trying to install it automatically')
        try:
            os.system("pip install opencv-python")
            time.sleep(2)
        except:
            debug('e','Could not install OpenCV. Try doing so manually.')
            exit()
        debug('s', 'OpenCV installed successfully. Try running the script again.')
        time.sleep(1)
        exit()

    # Get osu installation directory
    while True:
        time.sleep(1)
        nl()
        debug('i',"Enter OSU Installation Path (DO NOT USE BACKSLASH). For example: 'C:/User/OSU/'")
        root_dir = input((">>> "))
        # root_dir ='C:/Root/'

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
    debug('i','Since mappers use both JPGs as well as PNGs for their backgrounds, both of the image types will be required. Make sure both have the same file names')
    

    time.sleep(1.5)
    nl()
    while True:
        print("Enter the path of the PNG Image (For example: C:/Users/John/Pictures/wally.png)")
        png_path = input(">>> ")
        # png_path = 'C:/Root/wall.png' 
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
        jpg_path = input(">>> ") 
        # jpg_path = 'C:/Root/wall.jpg'
        nl()
        time.sleep(1.5)
        if os.path.isfile(jpg_path):
            print("[SUCESS]     Image Found.")
            break
        else:
            print("[FAILURE]     Image Not Found.")
    
    time.sleep(1.5)
    png_image_name = os.path.basename(png_path.replace('\\',os.sep))
    debug('i',f'PNG Image name set as {png_image_name}')
    time.sleep(0.7)
    jpg_image_name = os.path.basename(jpg_path.replace('\\',os.sep))
    debug('i',f'JPG Image name set as {jpg_image_name}')
    
    

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
                # print(file)
                
                
                # Fixed Issue #1: Skip beatmap skin elements
                img = cv2.imread(file_location)
  
                # fetching the dimensions
                wid = img.shape[1]
                hgt = img.shape[0]

                if wid < 600 or hgt < 600:
                    continue

                #Store the image name
                old_image_name = str(file)
                # print(old_image_name)
                
                
                #Rename the old background
                os.replace(file_location,os.path.join(song_location,f'osureplace{ext}'))


                #Copy the new background
                if ext == '.png':shutil.copy(png_path,song_location)
                else: shutil.copy(jpg_path,song_location)

                # Rename the new background
                if ext == '.png':
                    os.replace(os.path.join(song_location,png_image_name),os.path.join(song_location, old_image_name))
                else:
                    os.replace(os.path.join(song_location,jpg_image_name),os.path.join(song_location, old_image_name))
            
                debug('s',f'Replaced background for {song}')
                time.sleep(0.1)
                
                # debug('e',f'Could not replace background for {song}. Moving on to the next map')
                # time.sleep(0.1)
                    
            else:
                continue




        
    
    


            
