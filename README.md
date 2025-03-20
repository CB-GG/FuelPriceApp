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
- **Google Maps API** (Driving directions and mapping)
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
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/NearbyFuelTracker.git
   cd NearbyFuelTracker
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Install Puppeteer:
   ```sh
   npm install puppeteer
   ```
4. Set up your Google Maps API Key:
   - Create a `.env` file and add:
     ```sh
     GOOGLE_MAPS_API_KEY=your_api_key_here
     ```

## 🚀 Usage
Run the application with:
```sh
python main.py
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
For any inquiries, feel free to open an issue or reach out via email at `your-email@example.com`.

