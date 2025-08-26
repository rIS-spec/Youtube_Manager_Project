import json   # Importing the json module to handle JSON data.

# This script is a simple YouTube Manager application that allows users to manage a list of YouTube videos.
# It provides functionalities to load, save, list, add, update, and delete videos.
def load_data():        # This function should load video data from a file or database.
    try:           # Attempt to open the file and load data.
        with open('youtube.tst', 'r') as file:     # Open the file in read mode.
            test = json.load(file)     # Load the JSON data from the file.
            # print(type (test))
            return test
    except FileNotFoundError:       # If the file does not exist, handle the exception.
        return []               # Return an empty list if the file does not exist.    

def save_data_helper(videos):    # This function should save video data to a file or database.
    with open('youtube.tst', 'w') as file:    # Open the file in write mode.
        json.dump(videos, file,)   # Dump the videos list as JSON into the file.This will overwrite the existing file with the new data.

def list_all_videos(videos): # This function lists all videos in the provided list.It prints the video name and duration.
    print("\n")
    print("*" * 70)

    for index, video in enumerate(videos, start=1):  # Start enumeration from 1
        print(f"{index}. {video['name']}, duration: {video['time']}")
        
    print("\n")
    print("*" * 70)


def add_video(videos):   # This function adds a new video to the provided list.
    name = input("Enter video name: ")   
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})  # Append the new video to the list.
    save_data_helper(videos)   # Save the updated list to the file.

def update_video(videos):    # This function updates an existing video in the provided list.
    list_all_videos(videos)
    index = int(input("Enter the index of the video to update: "))  # Get the index of the video to update.
    if 0 < index <= len(videos):  # Check if the index is valid.
        name = input("Enter new video name: ")
        time = input("Enter new video time: ")
        videos[index - 1] = {'name': name, 'time': time}
        save_data_helper(videos)   # Save the updated list to the file.
    else:
        print("Invalid index. Please try again.....")

def delete_video(videos):    # This function deletes a video from the provided list.
    list_all_videos(videos)  # List all videos before deletion.
    index = int(input("Enter the index of the video to delete: "))  # Get the index of the video to delete.
    if 1 <= index <= len(videos):
                         del videos[index-1]
                         save_data_helper(videos)  # Save the updated list to the file.
    else:
         print("Invaalid index please try again.")  # If the index is invalid, print an error message.


# This function deletes a video from the provided list.
def main():       # Main function to run the YouTube Manager application.
    videos = load_data()     # Load existing video data from a file or database.
    while True:          # Main loop to display the menu and handle user choices.
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video")
        print("4. Delete a youtube video")
        print("5. Exit the app ")
        choice = input("Enter your choice: ") 
        print(videos)

        match choice:     # Using match-case to handle user choices.
            case '1':
                list_all_videos(videos)   
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)   
            case '4':
                delete_video(videos)        
            case '5':
                break      
            case _:
                print("Invalid Choice")


if __name__ == "__main__":      # Entry point of the script.
    main()