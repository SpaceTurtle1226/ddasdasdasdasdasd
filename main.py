import tkinter as tk
import os

# Create the main window
root = tk.Tk()
root.title("Roblox Style Start Screen")
root.geometry("800x600")

# Load the background image (using PIL since Tkinter can't handle large images)
background_path = "images/start screen/poblox.png"  # Modify this path as needed
if not os.path.exists(background_path):
    raise FileNotFoundError(f"{background_path} not found.")

# Load the background image as PhotoImage
background_image = tk.PhotoImage(file=background_path)

# Create a canvas to hold the background and other elements
canvas = tk.Canvas(root, highlightthickness=0)
canvas.pack(fill="both", expand=True)


# Function to update the background image when the window is resized
def update_background_image(event=None):
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    # Clear the canvas and redraw the background image
    canvas.delete("all")  # Clear the canvas
    resized_image = background_image.subsample(max(1, original_width // window_width),
                                               max(1, original_height // window_height))
    canvas.create_image(0, 0, anchor="nw", image=resized_image)

    # Reposition the start button to the center of the window
    canvas.coords(start_button_window, window_width // 2, window_height // 2)


# Set original dimensions for resizing purposes
original_width = background_image.width()
original_height = background_image.height()

# Set the initial background on the canvas
canvas.create_image(0, 0, anchor="nw", image=background_image)

# Load the character image using PhotoImage
character_path = "images/character.png"  # Modify this path as needed
if not os.path.exists(character_path):
    raise FileNotFoundError(f"{character_path} not found.")

# Load the character image as a PhotoImage
character_photo = tk.PhotoImage(file=character_path)  # Using Tkinter's PhotoImage
character_x = root.winfo_width() // 2
character_y = root.winfo_height() // 2
character = canvas.create_image(character_x, character_y, image=character_photo)


# Function to move the character based on key presses
def move_character(event):
    global character_x, character_y
    if event.keysym == 'W':  # Move up
        character_y -= 10
    elif event.keysym == 'S':  # Move down
        character_y += 10
    elif event.keysym == 'A':  # Move left
        character_x -= 10
    elif event.keysym == 'D':  # Move right
        character_x += 10

    # Update character position on canvas
    canvas.coords(character, character_x, character_y)


# Function to start the game (removes start button and enables character movement)
def start_game():
    canvas.delete(start_button_window)  # Remove start button
    # Change the background to white
    canvas.delete("all")  # Clear the canvas
    canvas.create_rectangle(0, 0, 800, 600, fill="white", outline="")  # Create a white rectangle for the background
    canvas.create_text(400, 50, text="게임 시작!", font=("Arial", 24), fill="Black")

    # Reset character position to center of the new window size
    global character_x, character_y
    character_x = root.winfo_width() // 2
    character_y = root.winfo_height() // 2
    canvas.create_image(character_x, character_y, image=character_photo)  # Re-add character image

    root.bind("<KeyPress>", move_character)  # Enable character movement


# Create the start button
start_button = tk.Button(root, text="START", font=("Arial", 24), bg="yellow", command=start_game)
start_button_window = canvas.create_window(400, 300, anchor="center", window=start_button)

# Update background image when the window is resized
root.bind("<Configure>", update_background_image)

# Start the main loop
root.mainloop()
