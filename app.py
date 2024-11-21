from google.oauth2.service_account import Credentials
import gspread
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Define the updated scopes for accessing Google Sheets
scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]


# Use the path to your actual downloaded credentials JSON file
creds = Credentials.from_service_account_file("D:\\project_fr\\train-booking-system-442414-eebc3367c3dc.json", scopes=scopes)

# Authenticate with gspread
client = gspread.authorize(creds)

# Open the Google Sheet by its name ("passengers")
sheet = client.open("passengers").sheet1

# Stations and distances (example)
stations = ["Madurai", "Dindigul", "Trichy", "Villupuram", "Chennai"]
distances = {"Madurai-Dindigul": 60, "Dindigul-Trichy": 90, "Trichy-Villupuram": 150, "Villupuram-Chennai": 150}

def get_available_seat(from_station, to_station):
    # Get all records from the Google Sheet
    data = sheet.get_all_records()
    
    for row in data:
        if row["Seat Status"] == "Confirmed":
            start = stations.index(row["From Station"])
            end = stations.index(row["To Station"])
            new_start = stations.index(from_station)
            new_end = stations.index(to_station)
            # Check if seat is available between the requested range
            if new_start >= end:
                return row["Seat Number"]  # Return the seat number if available
    return None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/allocate-seat", methods=["POST"])
def allocate_seat():
    passenger_name = request.form["name"]
    from_station = request.form["from_station"]
    to_station = request.form["to_station"]
    
    # Find available seat
    seat = get_available_seat(from_station, to_station)
    if seat:
        # Calculate extra charge
        distance = sum(distances[f"{stations[i]}-{stations[i+1]}"] for i in range(stations.index(from_station), stations.index(to_station)))
        extra_charge = distance * 0.5  # Example rate: 0.5 currency units per km
        
        # Update Google Sheets with new allocation
        sheet.append_row([passenger_name, from_station, to_station, "Confirmed", seat])
        
        return jsonify({"seat": seat, "extra_charge": extra_charge})
    else:
        return jsonify({"error": "No available seats"})

if __name__ == "__main__":
    app.run(debug=True)
