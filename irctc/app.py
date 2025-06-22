import requests
import os
from dotenv import load_dotenv
load_dotenv()

class Irctc:

    def __init__(self):
        user_input = input(""" How would you like to proceed ?
              1. Enter 1 to check train live status
              2. Enter 2 to check PNR
              3. Enter 3 to check train schedule
Your choice: """)
        
        if user_input == "1":
            print("Live train status ")
        elif user_input == "2":
            print("PNR ")
        elif user_input == "3":
            self.train_schedule()
        else:
            print("Invalid option.")

    def train_schedule(self):
        train_number = input("Enter the Train Number: ")
        self.fetch_data(train_number)

    def fetch_data(self, train_number):
        api_key = os.getenv("API_KEY")
        url = f"https://indianrailapi.com/api/v2/TrainSchedule/apikey/{api_key}/TrainNumber/{train_number}/"
        try:
            response = requests.get(url)
            data = response.json()
            for i in data['Route']:
                print(i["StationName"]," | ",i['ArrivalTime']," | ",i['DepartureTime'])
        except Exception as e:
            print("Error fetching train data:", e)

# Run the program
obj = Irctc()
