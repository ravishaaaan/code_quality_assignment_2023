#EG_2020_4277 Welikumbura R.W.R.L.

from csv import *

hotel_rates = {}     # Dictionary for hotel rates
exchange_rates = {}  # Dictionary for exchange rates
flight_costs = {}    # Dictionary for flight costs

# Function to load hotel rates from a CSV file
def load_hotel_rates(file):
    with open(file) as hotel_file:
        csv_reader = reader(hotel_file)
        for row in csv_reader:
            hotel_rates[row[0]] = float(row[1])

# Function to load exchange rates from a CSV file
def load_exchange_rates(file):
    with open(file) as exchange_file:
        csv_reader = reader(exchange_file)
        for row in csv_reader:

            exchange_rates[row[0].upper()] = float(row[1]) # Store exchange rates as uppercase currency

# Function to load flight costs from a CSV file
def load_flight_costs(file):
    with open(file) as flight_file:
        csv_reader = reader(flight_file)
        for row in csv_reader:
            flight_costs[row[0]] = float(row[1])

# Main function to calculate and display total travel cost
def main():


# Load data from CSV files
    load_hotel_rates('data/hotel_rates.csv')
    load_exchange_rates('data/exchange_rates.csv')
    load_flight_costs('data/flight_costs.csv')


# Get the destination from the user and convert it to uppercase
    destination = input("Enter your destination: ").upper()


# Get flight cost and hotel rate with destination
    flight_cost = flight_costs.get(destination, 0.0)
    hotel_rate = hotel_rates.get(destination, 0.0)


# Get the duration of stay from the user and calculate hotel cost
    stay_duration = int(input("Enter your stay duration in days: "))
    hotel_cost = hotel_rate * stay_duration

# Calculate the total cost
    total_cost = flight_cost + hotel_cost




# Display flight cost, hotel cost, and total cost
    print(f"Flight cost: USD {flight_cost:.2f}")
    print(f"Hotel cost for {stay_duration} days: USD {hotel_cost:.2f}")
    print(f"Total: USD {total_cost:.2f}")

# Get the user's preferred currency for final price estimation
    available_currencies = ', '.join(exchange_rates.keys())
    selected_currency = input(f"Select your currency for final price estimation ({available_currencies}): ")

 # Calculate the total cost selected currency
    price_in_selected_currency = total_cost * exchange_rates.get(selected_currency, 1.0)
    print(f"Total in {selected_currency}: {price_in_selected_currency:.2f}")

if __name__ == "__main__":
    main()