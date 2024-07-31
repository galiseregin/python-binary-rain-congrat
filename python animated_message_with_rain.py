import tkinter as tk
import random

class RainSimulator:
    def __init__(self, canvas, width, height, char_size=10):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.char_size = char_size
        self.characters = ['0', '1']
        self.drops = []
        self.is_rain_enabled = True
        self.update_count = 0

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

        # Clear the canvas
        self.canvas.delete("all")

        # Update and draw each raindrop
        for drop in self.drops:
            drop['y'] += self.char_size
            if drop['y'] > self.height:
                drop['y'] = random.randint(-self.char_size, 0)
                drop['char'] = random.choice(self.characters)

            self.canvas.create_text(drop['x'] + self.char_size / 2, drop['y'] + self.char_size / 2, text=drop['char'], fill='green', font=('Courier', self.char_size))

        self.update_count += 1

        self.canvas.after(50, self.update_rain)

    def reset(self):
        self.is_rain_enabled = True
        self.update_count = 0
        self.drops = []
        self.initialize_drops()
        self.update_rain()

class RainSimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary Rain Simulator")

        # Create a canvas
        self.canvas = tk.Canvas(root, bg='black', width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Create simulator instance
        self.simulator = RainSimulator(self.canvas, 800, 600, char_size=10)

        # Create buttons
        self.start_button = tk.Button(root, text="Start Simulation", command=self.start_simulation)
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_simulation)
        self.reset_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def start_simulation(self):
        if not self.simulator.is_rain_enabled:
            self.simulator.reset()
        else:
            self.simulator.update_rain()

    def reset_simulation(self):
        self.simulator.reset()

# Create the main window and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = RainSimulatorApp(root)
    root.mainloop()
