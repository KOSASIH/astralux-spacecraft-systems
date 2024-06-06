# Interface for Astronauts to Interact with the AGI System

import tkinter as tk
from tkinter import messagebox

class AGIInterface:
    def __init__(self, agi_core):
        self.agi_core = agi_core
        self.root = tk.Tk()
        self.root.title("Astralux AGI Interface")

        self.situation_label = tk.Label(self.root, text="Enter Situation:")
        self.situation_label.pack()

        self.situation_entry = tk.Entry(self.root, width=50)
        self.situation_entry.pack()

        self.submit_button = tk.Button(self.root, text="Get Recommendations", command=self.get_recommendations)
        self.submit_button.pack()

        self.recommendations_label = tk.Label(self.root, text="Recommendations:")
        self.recommendations_label.pack()

        self.recommendations_text = tk.Text(self.root, width=50, height=10)
        self.recommendations_text.pack()

    def get_recommendations(self):
        situation = self.situation_entry.get()
        situation = np.array([float(x) for x in situation.split(',')])
        recommendations = self.agi_core.get_recommendations(situation)
        self.recommendations_text.delete(1.0, tk.END)
        self.recommendations_text.insert(tk.END, str(recommendations))

    def start_interface(self):
        self.root.mainloop()

# Example usage:
agi_core = AGICore()
agi_interface = AGIInterface(agi_core)
agi_interface.start_interface()
