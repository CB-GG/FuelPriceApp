import getLocAndCity
import asyncio
import pandas as pd
from pyppeteer import launch
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import webbrowser
import time


async def scrape_gasbuddy(city, state):
    """Scrapes gas prices, station names, and addresses from GasBuddy using Pyppeteer."""
    formatted_city = city.lower().replace(" ", "-")
    formatted_state = state.lower().replace(" ", "-")
    url = f"https://www.gasbuddy.com/gasprices/{formatted_state}/{formatted_city}"

    browser = await launch(
        headless=True,
        executablePath=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    )

    page = await browser.newPage()
    await page.goto(url, {'waitUntil': 'networkidle2'})  # Wait for full page load

    # Wait for elements to load
    await page.waitForSelector("h3 a", timeout=10000)  # Gas station names
    await page.waitForSelector("span.text__xl___2MXGo.text__left___1iOw3.StationDisplayPrice-module__price___3rARL", timeout=10000)  # Gas prices
    await page.waitForSelector("div.StationDisplay-module__address___2_c7v", timeout=10000)  # Addresses

    stations = []
    try:
        # Extract station names, prices, and addresses
        station_elements = await page.querySelectorAll("h3 a")
        price_elements = await page.querySelectorAll("span.text__xl___2MXGo.text__left___1iOw3.StationDisplayPrice-module__price___3rARL")
        address_elements = await page.querySelectorAll("div.StationDisplay-module__address___2_c7v")

        for station, price, address in zip(station_elements, price_elements, address_elements):
            station_name = await page.evaluate('(element) => element.textContent', station)
            price_text = await page.evaluate('(element) => element.textContent', price)
            address_text = await page.evaluate('(element) => element.innerHTML', address)
            address_text = address_text.replace("<br>", ", ").strip()  # Convert <br> to a readable address

            stations.append({
                "name": station_name.strip(),
                "price": price_text.strip().replace("$", ""),
                "address": address_text.strip(),
                "city": city,
                "state": state
            })
    except Exception as e:
        print("Error during scraping:", e)

    await browser.close()
    return stations

def get_coordinates(address, max_retries = 2):
    """Converts an address to latitude/longitude using OpenStreetMap (OSM), with retries."""
    geolocator = Nominatim(user_agent="gas_station_locator")

    for attempt in range(max_retries):
        try:
            location = geolocator.geocode(address, timeout=5)  # 10s timeout
            if location:
                return (location.latitude, location.longitude)
        except Exception as e:
            print(f"⚠ Error getting coordinates for {address} (Attempt {attempt + 1}): {e}")
            time.sleep(2)  # Wait before retrying

    print(f"❌ Failed to get coordinates for {address} after {max_retries} attempts.")
    return None  # Return None if unsuccessful

def calculate_distance(user_location, station_address):
    """Calculates distance in miles between user and station."""
    station_coords = get_coordinates(station_address)
    if station_coords:
        return geodesic(user_location, station_coords).miles
    return float('inf')  # If coordinates are unavailable, return infinite distance

def find_closest_gas_station(user_location, df):
    """Finds the closest gas station based on geodesic distance."""
    df['distance_miles'] = df['address'].apply(lambda addr: calculate_distance(user_location, addr))
    df = df.sort_values(by='distance_miles')  # Sort by nearest
    return df.iloc[0]  # Return the closest gas station

def open_google_maps(destination_address):
    """Opens Google Maps with directions to the chosen gas station."""
    base_url = "https://www.google.com/maps/dir/?api=1"
    destination_url = f"{base_url}&destination={destination_address.replace(' ', '+')}"
    print(f"🔗 Opening Google Maps: {destination_url}")
    webbrowser.open(destination_url)  # Open in default web browser

def find_optimal_gas_station(df):
    """Finds the best gas station balancing price and distance."""
    df['cost_effectiveness'] = df['price'] / (df['distance_miles'] + 1)  # Avoid division by zero
    optimal_station = df.sort_values(by='cost_effectiveness', ascending=False).iloc[0]
    

    return optimal_station








if __name__ == "__main__":
    city, state = getLocAndCity.getStateCity()
    user_location = getLocAndCity.getMyCoords() 
    stations = asyncio.run(scrape_gasbuddy(city, state))

    df = pd.DataFrame(stations)
    df['price'] = df['price'].astype(float)  # Convert price to float
    # Ensure every gas station has distance_miles
    df['distance_miles'] = df['address'].apply(lambda addr: calculate_distance(user_location, addr))


    # Remove stations with 'inf' distance (missing coordinates)
    df = df[df['distance_miles'] != float('inf')]
    print(df)

    if user_location:
        # Add distances to DataFrame
        df['distance_miles'] = df['address'].apply(lambda addr: calculate_distance(user_location, addr))

        # Find cheapest station
        cheapest_station = df.iloc[0] if not df.empty else None

        df_valid_distances = df[df['distance_miles'] != float('inf')]


    # Find closest station (only from stations with valid distances)
        closest_station = df_valid_distances.sort_values(by='distance_miles').iloc[0] if not df_valid_distances.empty else None

        # Find optimal station using cost-effectiveness score (only from valid stations)
        optimal_station = find_optimal_gas_station(df_valid_distances) if not df_valid_distances.empty else None

        
        # Display choices
        print("\n⛽ Cheapest Gas Station:")
        print(f"   {cheapest_station['name']} - ${cheapest_station['price']} at {cheapest_station['address']} ({cheapest_station['distance_miles']:.2f} miles away)")

        print("\n📍 Closest Gas Station:")
        print(f"   {closest_station['name']} - ${closest_station['price']} at {closest_station['address']} ({closest_station['distance_miles']:.2f} miles away)")

        print("\n🔹 Optimal Gas Station (Best Price-to-Distance Balance):")
        print(f"   {optimal_station['name']} - ${optimal_station['price']} at {optimal_station['address']} ({optimal_station['distance_miles']:.2f} miles away)")

        # Ask user for selection
        choice = input("\n🔘 Which gas station do you want directions to? (Enter 'cheapest', 'closest', or 'optimal'): ").strip().lower()

        if choice == "cheapest":
            open_google_maps(cheapest_station['address'])
        elif choice == "closest":
            open_google_maps(closest_station['address'])
        elif choice == "optimal":
            open_google_maps(optimal_station['address'])
        else:
            print("❌ Invalid choice. Exiting.")
    else:
        print("❌ Could not determine user location.")

