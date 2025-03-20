# NearbyFuelTracker

## 🚀 Overview
NearbyFuelTracker is a Python-based application designed to help users find the cheapest fuel prices at nearby gas stations. It dynamically determines the user's location and scrapes online sources to fetch real-time fuel prices. The application also integrates Google Maps for driving directions and utilizes OpenStreetMap (OSM) to calculate the closest gas station in terms of travel distance.

## 🔥 Features
- **Real-time Fuel Prices**: Scrapes online sources to get the latest gas prices in your area.
- **Dynamic Location Detection**: Automatically determines your current city.
- **Google Maps Integration**: Provides driving directions to the cheapest gas station.
- **OpenStreetMap Distance Calculation**: Identifies the closest gas station based on travel distance.
- **Efficient Web Scraping**: Utilizes Puppeteer instead of Selenium for optimal performance.

## 🛠️ Tech Stack
- **Python** (Core logic and data processing)
- **Puppeteer** (Web scraping)
- **OpenStreetMap (OSM)** (Location and distance calculations)
- **Hugging Face (Optional)** (For possible future enhancements like sentiment-based fuel tracking)

## 📦 Installation
### Prerequisites
Ensure you have the following installed:
- **Python 3.x**
- **Node.js** (Required for Puppeteer)
- **Google Maps API Key**
- **Puppeteer**
- **OSM libraries** (e.g., `geopy` for distance calculations)
  
```bash
pip install geopy requests beautifulsoup4 playwright && playwright install && npm install puppeteer
```

### Setup

1. Install dependencies:
  ```bash
  pip install geopy requests beautifulsoup4 playwright && playwright install && npm install puppeteer
  ```
2. Ensure you replace the placeholder variables for your email address, default city, and default state in the getLocAndCity file.

3. This was designed for use with apple products. For optimal usage, you will want to setup the pyicloud keyring with your appropriate apple ID information for the getLocAndCity file functionality. Additionally, using this library, the devices array will contain all your associated devices in a list. The device I wanted the location of happened to be at position [3], you will need to find which location your device is at in the list and change the number accordingly. This can be done easily by just printing the list, then counting what position your device is in the list (keep in mind it is base 0).

## 🚀 Usage
Run the application with:
```sh
python fuel_price_main.py
```
The program will determine your location, fetch fuel prices, and display the cheapest and closest gas stations.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing
Contributions are welcome! To contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

## 📧 Contact
For any inquiries, feel free to open an issue or reach out via email at `1Chasebaker@gmail.com`.

