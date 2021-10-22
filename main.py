import os.path
import os
import shutil

if __name__ == '__main__':

    # Get osu installation directory
    while True:
        print("Enter OSU Installation Path (DO NOT USE BACKSLASH). For example: 'C:/User/OSU/'  ")
        root_dir = input((">>> "))
        if os.path.isdir(root_dir):
            print("[SUCCESS]    Installation directory found")
        else:
            print("[FAILURE]    Installation directory not found. Please try again")
            continue

        # Check if this is THE osu directory or not.
        if os.path.isfile(root_dir+'osu!.exe'):
            print("[SUCESS]     Osu executable found.")
        else:
            print("[WARN]   Osu executable cannot be found in this directory. Be VERY SURE THAT THIS IS THE CORRECT DIRECTORY")  


        # Search for the songs folder
        songs_path = root_dir+'Songs/'
        if os.path.dir(songs_path):
            print("[SUCESS]     Beatmapsets folder found.")
            break
        else:
            print("[FAILURE]    Could not find the songs folder, enter the directory properly")
            continue
    
    beatmap_count = len(os.listdir(songs_path))
    if beatmap_count == 0:
        print("[FAILURE] No beatmaps were found. Exiting")
        exit()
    print(f"{beatmap_count} beatmaps found in the directory.")
    
    #Get the backgrounds
    print("\n","\n","Since mappers use both JPGs as well as PNGs for their backgrounds, both of the image types will be required. Make sure the name of both the images are what you specified")
    print("Enter the filename of the image (excluding the extension): ")
    image_name = input(">>> ")
    while True:
        print("Enter the path of the PNG Image (For example: C:/Users/John/Pictures/wally.png)")
        png_path = input(">>> ") 
        if os.path.isfile(png_path):
            print("[SUCESS]     Image Found.")
            break
        else:
            print("[SUCESS]     Image Not Found.")
    
    while True:
        print("Enter the path of the jpg Image (For example: C:/Users/John/Pictures/wally.jpg)")
        jpg_path = input(">>> ") 
        if os.path.isfile(jpg_path):
            print("[SUCESS]     Image Found.")
            break
        else:
            print("[FAILURE]     Image Not Found.")
    
    #List all the beatmaps folders
    for song in os.listdir(songs_path):
        #Get all the files in each beatmap folder
        for file in os.listdir(os.path.join(songs_path,song)):
            #If the selected file is a png image
            if ".png" in file:
                #Store the image name
                old_image_name = str(file)
                #Rename the old background
                os.replace(file,"osureplace.png")
                #Copy the new background
                shutil.copy(png_path, song)
                # Rename the new background
                os.replace(song+f'{image_name}.png',old_image_name)
            elif ".jpg" in file:
                image_name = str(file)
                os.replace(file,"osureplace.jpg")
                shutil.copy(jpg_path, song)
        

    
    

        
    
    


            
