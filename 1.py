import tkinter as tk
import random

# Define ASCII art for the headline
ASCII_ART = """



______                  _____                          
|  _  \                |_   _|                         
| | | |___  __ _ _ __    | | __ _ _ __ ___   __ _ _ __ 
| | | / _ \/ _` | '__|   | |/ _` | '_ ` _ \ / _` | '__|
| |/ /  __/ (_| | |      | | (_| | | | | | | (_| | |   
|___/ \___|\__,_|_|      \_/\__,_|_| |_| |_|\__,_|_|   
                                                        
                                                                     
"""

class RainSimulator:
    def __init__(self, canvas, width, height, char_size=10):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.char_size = char_size  # Smaller characters
        self.characters = ['0', '1']
        self.drops = []
        self.is_rain_enabled = True

        # Initialize raindrops
        self.initialize_drops()

    def initialize_drops(self):
        for x in range(0, self.width, self.char_size):
            drop = {
                'x': x,
                'y': random.randint(-self.height, 0),
                'char': random.choice(self.characters)
            }
            self.drops.append(drop)

    def update_rain(self):
        if not self.is_rain_enabled:
            return

        # Clear the canvas with the 'rain' tag to prevent artifacts
        self.canvas.delete("rain")

        # Update and draw each raindrop
        for drop in self.drops:
            drop['y'] += self.char_size
            if drop['y'] > self.height:
                drop['y'] = random.randint(-self.char_size, 0)
                drop['char'] = random.choice(self.characters)

            self.canvas.create_text(drop['x'] + self.char_size / 2, drop['y'] + self.char_size / 2, text=drop['char'],
                                    fill='green', font=('Courier', self.char_size), tags="rain")

        self.canvas.after(30, self.update_rain)  # Faster updates

    def reset(self):
        self.is_rain_enabled = True
        self.drops = []
        self.initialize_drops()
        self.update_rain()


class RainSimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary Rain Simulator")

        # Create a canvas for the rain effect
        self.canvas = tk.Canvas(root, bg='black', width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Create simulator instance
        self.simulator = RainSimulator(self.canvas, 800, 600, char_size=10)  # Smaller characters for rain

        # Create a frame for the ASCII headline and set its background color to black
        self.headline_frame = tk.Frame(root, bg='black', bd=0)
        self.headline_frame.place(relx=0.5, rely=0.1, anchor='center')  # Position the headline at the top

        # Create a label for the ASCII headline
        self.headline_label = tk.Label(self.headline_frame, text=ASCII_ART, font=("Courier", 12), bg='black', fg='lime',
                                       justify="center", anchor='center', padx=10, pady=10)
        self.headline_label.pack()

        # Create a frame for the congratulations message and set its background color to black
        self.message_frame = tk.Frame(root, bg='black', bd=0)
        self.message_frame.place(relx=0.5, rely=0.6, anchor='center')  # Center the frame in the middle of the window

        # Create a label for the congratulations message
        self.message_label = tk.Label(self.message_frame, text="", font=("Courier", 14), bg='black', fg='lime',
                                      wraplength=780, justify="center")
        self.message_label.pack(padx=20, pady=20)  # Add padding around the text for better readability

        # Create a frame for buttons and set its background color to black
        self.button_frame = tk.Frame(root, bg='black')
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Create buttons inside the black frame
        self.start_button = tk.Button(self.button_frame, text="Start Simulation", command=self.start_simulation,
                                      bg='black', fg='white')
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.reset_button = tk.Button(self.button_frame, text="Reset", command=self.reset_simulation, bg='black',
                                      fg='white')
        self.reset_button.pack(side=tk.RIGHT, padx=10, pady=10)

        # Set the congratulations message with hearts and emojis
        self.message = ("🎉🎓 Thank you for an amazing Python course! 🎓🎉\n\n"
                        "❤️ Your patience and care made all the difference. ❤️\n"
                        "🌟 From explaining the basics to helping debug our code, 🌟\n"
                        "you were always there with a smile and encouragement. 😊\n\n"
                        "🚀 Your dedication turned Python from a mystery into something 🚀\n"
                        "We truly enjoy. You've made learning fun and accessible, 🎓\n"
                        "and We'll always be grateful for your support. 🙏\n\n"
                        "Thanks for everything! 🌈")
        # Initialize animation index
        self.animation_index = 0

    def start_simulation(self):
        # Start the rain and message animation
        if not self.simulator.is_rain_enabled:
            self.simulator.reset()
        else:
            self.simulator.update_rain()

        self.animate_message()

    def reset_simulation(self):
        self.simulator.reset()
        self.animation_index = 0
        self.message_label.config(text="")

    def animate_message(self):
        """Animate the message character by character."""
        if self.animation_index < len(self.message):
            current_text = self.message[:self.animation_index + 1]
            self.message_label.config(text=current_text)
            self.animation_index += 1
            self.root.after(50, self.animate_message)  # Faster message animation

# Create the main window and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = RainSimulatorApp(root)
    root.mainloop()
