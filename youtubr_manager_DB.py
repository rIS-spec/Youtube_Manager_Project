import sqlite3  # Import the sqlite3 module to interact with SQLite databases.

conn = sqlite3.connect('youtubr_manager.db')  # Connect to the SQLite database (or create it if it doesn't exist).
# This line connects to a SQLite database named 'youtubr_videos.db'. If the database does not exist, it will be created.

cursor = conn.cursor() # Create a cursor object to interact with the database.

# This line creates a cursor object that allows you to execute SQL commands and queries on the database.
cursor.execute('''  
    CREATE TABLE IF NOT EXISTS videos(  
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    ) 
''') # Create a table named 'videos' if it does not already exist. The table has three columns: id, name, and time.

def list_videos():
    cursor.execute("SELECT * FROM videos") # Execute a query to select all videos from the videos table.
    print("\n")
    print("*" * 70)
    for row in cursor.fetchall(): # Fetch all rows from the videos table.
        print(row) 
    print("\n")
    print("*" * 70)    

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))  # Insert a new video into the videos table.
    conn.commit()  # Commit the changes to the database.

def update_video(video_ID, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_ID))  # Update an existing video in the videos table.
    conn.commit()  # Commit the changes to the database.

def delete_video(video_ID):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_ID,))  # Delete a video from the videos table based on its ID.
    conn.commit()  # Commit the changes to the database.


def main():  # Main function to run the YouTube Manager application.
    while True: # Main loop to display the menu and handle user choices.
        print("\n Youtube Manager app with DB ")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video")
        print("4. Delete a youtube video")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")

        if choice == '1': # List all videos
            list_videos()
        elif choice == '2':  # Add a new video
            name = input("Enter video name: ")  
            time = input("Enter video time: ")
            add_video(name, time) 
        elif choice == '3':  # Update an existing video
            video_ID = input("Enter video ID to update: ")
            name = input("Enter video name: ")  
            time = input("Enter video time: ")
            add_video(name, time)  
            update_video(video_ID, name, time)  
        elif choice == '4':   # Delete a video
            video_ID = input("Enter video ID to Delete: ")
            delete_video(video_ID)   
        elif choice == '5':   # Exit the application
            break
        else:  # If the user enters an invalid choice
            print("Invalid choice, please try again.")        

    conn.close()  # Close the database connection when done.


if __name__ =="__main__":
    main()