# Importing necessary libraries
from tkinter import *

class App:
    def __init__(self, master):
        # Create Frame
        frame = Frame(master)
        frame.pack()

        # Set the background color to mint green
        frame.configure(bg='#66CDAA')

        # Create Labels for input fields
        self.input_labels = []
        for i, label_text in enumerate([
            "Hourly rate per week: ",
            "Weekly per diem: ",
            "License/CEU/Other: ",
            "Travel expenses: ",
            "Bonus/Referral: ",
            "Weekly admin fee: ",
            "Gross profit/week: ",
            "% gross profit: ",
            "Monthly housing: ",
            "Weekly invoice: ",
            "Starting location: ",
            "Ending location: ",
            "Gas allotment: "
        ]):
            label = Label(frame, text=label_text, bg='#66CDAA')  # Mint green background
            label.grid(row=i, column=0)
            self.input_labels.append(label)

        # Create Entries for input fields
        self.input_entries = []
        for i in range(13):
            entry = Entry(frame)
            entry.grid(row=i, column=1)
            self.input_entries.append(entry)

        # Create Labels for Results
        self.result_labels = []
        for i, label_text in enumerate([
            "Result 1: ",
            "Result 2: ",
            "Result 3: ",
            "Result 4: ",
            "Result 5: ",
            "Result 6: ",
            "Result 7: ",
            "Result 8: ",
            "Result 9: "
        ]):
            label = Label(frame, text=label_text, bg='#66CDAA')  # Mint green background
            label.grid(row=i, column=2)
            self.result_labels.append(label)

        # Create Button
        self.button1 = Button(frame, text="Calculate", command=self.calculate)
        self.button1.grid(row=13, columnspan=3)

    # Create a function for calculating results
    def calculate(self):
        # Retrieve values from Entry widgets
        input_values = [float(entry.get()) for entry in self.input_entries]

        # Perform calculations based on input values
        result1 = input_values[0] * 2
        result2 = input_values[2]
        result3 = input_values[3]
        result4 = input_values[4]
        result5 = input_values[5]
        result6 = input_values[6]
        result7 = input_values[7]
        result8 = input_values[8]
        result9 = input_values[9]

        # Update the results labels
        for i, label in enumerate(self.result_labels):
            label.config(text=f"Result {i + 1}: {input_values[i]:.2f}")

# Create the main GUI window
root = Tk()
root.title('Fusion Medical "Pulse" Dashboard')
app = App(root)

# Start the GUI main loop
root.mainloop()
