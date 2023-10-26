import csv
import tkinter as tk
from tkinter import ttk
from tkinter import Scrollbar
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Define the path to the CSV file
csv_file_path = '/Users/moxybiel/Desktop/Python_Projects/Fusion App/hospital_data.csv'


# Function to find hospitals by various criteria
def find_hospitals(city, state, zip_code, hospital_type, hospital_name):
    hospitals = []
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for hospital in csv_reader:
            if (not city or hospital['City'] == city) and \
                    (not state or hospital['State'] == state) and \
                    (not zip_code or hospital['ZIP Code'] == zip_code) and \
                    (not hospital_type or hospital['Hospital Type'] == hospital_type) and \
                    (not hospital_name or hospital['name'] == hospital_name):
                hospitals.append(hospital)
    return hospitals


# Function to display search results in the Text widget
def display_results(hospitals):
    result_text.config(state="normal")
    result_text.delete("1.0", tk.END)
    for hospital in hospitals:
        result_text.insert("end", f"Hospital Name: {hospital['name']}\n")
        result_text.insert("end", f"Address: {hospital['Address']}\n")
        result_text.insert("end", f"City: {hospital['City']}\n")
        result_text.insert("end", f"State: {hospital['State']}\n")
        result_text.insert("end", f"ZIP Code: {hospital['ZIP Code']}\n")
        result_text.insert("end", f"County: {hospital['County']}\n")
        result_text.insert("end", f"Phone Number: {hospital['Phone Number']}\n")
        result_text.insert("end", f"Hospital Type: {hospital['Hospital Type']}\n")
        result_text.insert("end", f"Distance: {calculate_hospital_distance(hospital['City'])} miles\n\n")

    result_text.config(state="disabled")


# Function to calculate the distance between two locations
def calculate_distance():
    start_location = start_entry.get()
    end_location = end_entry.get()

    geolocator = Nominatim(user_agent="distance_calculator")
    start = geolocator.geocode(start_location)
    end = geolocator.geocode(end_location)

    if start and end:
        start_coords = (start.latitude, start.longitude)
        end_coords = (end.latitude, end.longitude)

        distance = geodesic(start_coords, end_coords).miles
        result_label.config(text=f"Distance: {distance:.2f} Miles")
    else:
        result_label.config(text="Invalid locations")


# Function to perform calculations based on user inputs
def calculate():
    input_values = []

    for entry in input_entries:
        value = entry.get()
        if not value:
            # Handle empty input
            input_values.append(0.0)
        else:
            try:
                numeric_value = float(value)
                input_values.append(numeric_value)
            except ValueError:
                # Handle non-numeric input
                input_values.append(0.0)

    for i, label in enumerate(result_labels[:-1]):
        label.config(text=f"Result {i + 1}: {input_values[i]:.2f}")


# Function for the search button
def search_button_clicked():
    city = city_entry.get()
    state = state_entry.get()
    zip_code = zip_code_entry.get()
    hospital_type = hospital_type_entry.get()
    hospital_name = hospital_name_entry.get()

    hospitals = find_hospitals(city, state, zip_code, hospital_type, hospital_name)
    display_results(hospitals)


# Function to calculate the distance from the starting point to a hospital
def calculate_hospital_distance(hospital_city):
    start_location = start_entry.get()
    geolocator = Nominatim(user_agent="distance_calculator")
    start = geolocator.geocode(start_location)

    if start:
        start_coords = (start.latitude, start.longitude)
        end_location = f"{hospital_city}, USA"  # Assuming all hospitals are in the USA
        end = geolocator.geocode(end_location)

        if end:
            end_coords = (end.latitude, end.longitude)
            distance = geodesic(start_coords, end_coords).miles
            return f"{distance:.2f}"
    return "N/A"


# Create the main application
app = tk.Tk()
app.title('Fusion Medical "Pulse" Dashboard and Hospital Information')
app.geometry("800x700")

# Create a notebook for tabbed interface
notebook = ttk.Notebook(app)
notebook.pack()

# Create the "Pulse" Dashboard tab
frame1 = ttk.Frame(notebook)
notebook.add(frame1, text='Pulse Dashboard')

frame1.configure(style='My.TFrame')
ttk.Style().configure('My.TFrame', background='#66CDAA')

input_labels = []
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
    label = ttk.Label(frame1, text=label_text, background='#66CDAA')
    label.grid(row=i, column=0)
    input_labels.append(label)

input_entries = []
for i in range(13):
    entry = ttk.Entry(frame1)
    entry.grid(row=i, column=1)
    input_entries.append(entry)

result_labels = []
for i, label_text in enumerate([
    "Result 1: ",
    "Result 2: ",
    "Result 3: ",
    "Result 4: ",
    "Result 5: ",
    "Result 6: ",
    "Result 7: ",
    "Result 8: ",
    "Result 9: ",
    "Distance: "  # Added distance result label
]):
    label = ttk.Label(frame1, text=label_text, background='#66CDAA')
    label.grid(row=i, column=2)
    result_labels.append(label)

button1 = ttk.Button(frame1, text="Calculate", command=calculate)
button1.grid(row=14, columnspan=3)

# Create the Distance Calculator tab
frame2 = ttk.Frame(notebook)
notebook.add(frame2, text='Distance Calculator')

frame2.configure(style='My.TFrame')
ttk.Style().configure('My.TFrame', background='#66CDAA')

start_label = ttk.Label(frame2, text="Start Location:")
end_label = ttk.Label(frame2, text="End Location:")
result_label = ttk.Label(frame2, text="Distance:")

start_entry = ttk.Entry(frame2)
end_entry = ttk.Entry(frame2)

calculate_button = ttk.Button(frame2, text="Calculate", command=calculate_distance)

start_label.grid(row=0, column=0, padx=10, pady=10)
end_label.grid(row=1, column=0, padx=10, pady=10)
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
start_entry.grid(row=0, column=1, padx=10, pady=10)
end_entry.grid(row=1, column=1, padx=10, pady=10)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create the Hospital Information Search tab
frame3 = ttk.Frame(notebook)
notebook.add(frame3, text='Hospital Information Search')

frame3.configure(style='My.TFrame')
ttk.Style().configure('My.TFrame', background='#66CDAA')


search_label = ttk.Label(frame3, text="City:")
search_label.grid(row=0, column=0, padx=10, pady=10)
city_entry = ttk.Entry(frame3)
city_entry.grid(row=0, column=1, padx=10, pady=10)

state_label = ttk.Label(frame3, text="State:")
state_label.grid(row=1, column=0, padx=10, pady=10)
state_entry = ttk.Entry(frame3)
state_entry.grid(row=1, column=1, padx=10, pady=10)

zip_code_label = ttk.Label(frame3, text="ZIP Code:")
zip_code_label.grid(row=2, column=0, padx=10, pady=10)
zip_code_entry = ttk.Entry(frame3)
zip_code_entry.grid(row=2, column=1, padx=10, pady=10)

hospital_type_label = ttk.Label(frame3, text="Hospital Type:")
hospital_type_label.grid(row=3, column=0, padx=10, pady=10)
hospital_type_entry = ttk.Entry(frame3)
hospital_type_entry.grid(row=3, column=1, padx=10, pady=10)

hospital_name_label = ttk.Label(frame3, text="Hospital Name:")
hospital_name_label.grid(row=4, column=0, padx=10, pady=10)
hospital_name_entry = ttk.Entry(frame3)
hospital_name_entry.grid(row=4, column=1, padx=10, pady=10)

search_button = ttk.Button(frame3, text="Search", command=search_button_clicked)
search_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Create a Text widget to display search results
result_text = tk.Text(frame3, wrap="none")
result_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
result_text.config(state="disabled")

# Add a scrollbar to the text widget
scrollbar = Scrollbar(frame3, command=result_text.yview)
scrollbar.grid(row=6, column=2, sticky="ns")
result_text.config(yscrollcommand=scrollbar.set)

if __name__ == "__main__":
    app.mainloop()
    
