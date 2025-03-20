# 🚀 Fuel Price Tracker
A Python application that scrapes **gas prices** from GasBuddy, finds the **cheapest, closest, and optimal gas stations**, and **provides driving directions using Google Maps**.

---

## 📌 Features
✅ **Scrapes gas prices** from GasBuddy using Pyppeteer  
✅ **Finds the cheapest gas station** based on price  
✅ **Finds the closest gas station** using OpenStreetMap (OSM)  
✅ **Calculates the optimal gas station** balancing price and distance  
✅ **Opens Google Maps for navigation**  
✅ **Supports dynamic locations**  

---

## 📂 Installation

### 1️⃣ Install Dependencies
Ensure you have **Python 3.8+** installed, then install the required libraries:
```bash
pip install pandas pyppeteer geopy
2️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/FuelPriceTracker.git
cd FuelPriceTracker
🚀 Usage
Run the script:

bash
Copy
Edit
python fuel_price_tracker.py
🔘 User Options
After scraping gas prices, the script will display:

Cheapest Gas Station (lowest price)
Closest Gas Station (shortest distance)
Optimal Gas Station (best balance of price & distance)
Example Output:
yaml
Copy
Edit
⛽ Cheapest Gas Station:
   Sunoco - $2.69 at 1501 New York Ave, Martinsburg, WV (Distance: Unknown)

📍 Closest Gas Station:
   BP - $2.72 at 123 Main St, Hagerstown, MD (2.1 miles away)

🔹 Optimal Gas Station:
   Exxon - $2.71 at 500 Market St, Frederick, MD (3.4 miles away)

🔘 Choose a gas station for directions:
   1. Cheapest
   2. Closest
   3. Optimal (Best balance of price & distance)

Enter your choice (1/2/3): 
After selecting an option, Google Maps will open automatically with driving directions.

🛠 Configuration
Change Location: Update city, state in the script to search different locations:
python
Copy
Edit
city, state = "Baltimore", "Maryland"
Adjust Maximum Distance for Selection: Modify the find_cheapest_within_distance() function:
python
Copy
Edit
def find_cheapest_within_distance(df, max_distance=5):
Modify Cost-Effectiveness Calculation: Change the weights in the formula:
python
Copy
Edit
alpha = 2  # Price weight
beta = 1   # Distance weight
df['weighted_score'] = (alpha * df['price']) + (beta * df['distance_miles'])
📌 How It Works
Scrapes GasBuddy for gas station names, prices, and addresses.
Uses OpenStreetMap (OSM) via Geopy to get latitude/longitude of each gas station.
Calculates distance from the user's location to each station.
Finds the best gas station based on:
Cheapest price
Shortest distance
Cost-effectiveness score
Opens Google Maps with directions to the selected station.
❓ Troubleshooting
🚨 Pyppeteer Issues
If Pyppeteer is failing, try reinstalling and ensuring Chromium is properly installed:

bash
Copy
Edit
pip uninstall pyppeteer
pip install pyppeteer
python -m pyppeteer install
🚨 Distance Showing as inf
This means the script couldn't get coordinates for an address. You can:

Improve address accuracy (e.g., "123 Main St, Baltimore, MD" instead of "123 Main St")
Increase retry attempts in get_coordinates() function
📜 License
This project is open-source and available under the MIT License.

👨‍💻 Author
Your Name
📧 Email: your@email.com
🔗 GitHub: yourusername
🔗 LinkedIn: yourprofile

🚀 Future Enhancements
☑ Auto-detect user location using GPS or IP address
☑ Schedule automatic gas price updates
☑ Integrate a GUI using Tkinter or Flask

🔥 Enjoy cheaper fuel and smarter driving! 🚗💨

yaml
Copy
Edit

---

### **📌 What This README Includes**
✔ **GitHub-friendly markdown formatting**  
✔ **Code blocks for installation & usage**  
✔ **User options & example output**  
✔ **Customization instructions**  
✔ **Troubleshooting tips**  

🚀 **Copy and paste it into your `README.md` on GitHub! Let me know if you'd like any changes!**
