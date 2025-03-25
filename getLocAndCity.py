from pyicloud import PyiCloudService
from geopy.geocoders import Nominatim
import keyring

def getStateCity():
    """Fetches the user's current city and state from iCloud device location."""
    
    # Must have signed into / added information to keyring via pyicloud package
    email = "Your_email@example.com"
    password = keyring.get_password("pyicloud", email)
    
    api = PyiCloudService(email, password)

    # Handle Two-Factor Authentication (2FA) if required
    if api.requires_2fa:
        print("Two-Factor Authentication required.")
        code = input("Enter the 2FA code sent to your trusted devices: ")
        result = api.validate_2fa_code(code)
        if not result:
            print("Invalid 2FA code. Exiting...")
            return "your_default_City", "YourDefaultState"  # Default location if 2FA fails
        print("2FA authentication successful.")

    if not api.devices:
        print("No devices found on this iCloud account.")
        return "your_default_City", "your_default_State"

    # Select the device to track (modify the index if necessary)
    device = api.devices[3]  

    if device:
        location = device.location()
        if location:
            latitude = location['latitude']
            longitude = location['longitude']

            # Use geopy to find the city and state
            geolocator = Nominatim(user_agent="device_location_finder")
            try:
                location_info = geolocator.reverse((latitude, longitude), language='en')
                address = location_info.raw.get('address', {})

                city = (
                    address.get('city') or
                    address.get('town') or
                    address.get('village') or
                    address.get('hamlet') or
                    "Hagerstown"  # Default if city is unknown
                )

                state = (
                    address.get('state') or
                    "your_default_state"  # Default if state is unknown
                )

            except Exception as e:
                print(f"Error finding location: {e}")
                return "your_default_city", "your_default_state"  # Default in case of error
            
            print(f"Detected Location: {city}, {state}")
            return city, state  # Return both city and state
           
           
        else:
            print(f"Location not available for {device['name']}")
    
    return "your_default_city", "your_default_state"  # Default if location is not found

def getMyCoords():
    """Fetches the user's current city and state from iCloud device location."""
    
    # Must have signed into / added information to keyring via pyicloud package
    email = "Your_email@example.com"
    password = keyring.get_password("pyicloud", email)
    
    api = PyiCloudService(email, password)

    # Handle Two-Factor Authentication (2FA) if required
    if api.requires_2fa:
        print("Two-Factor Authentication required.")
        code = input("Enter the 2FA code sent to your trusted devices: ")
        result = api.validate_2fa_code(code)
        if not result:
            print("Invalid 2FA code. Exiting...")
            return "Hagerstown", "Maryland"  # Default location if 2FA fails
        print("2FA authentication successful.")

    if not api.devices:
        print("No devices found on this iCloud account.")
        return "your_default_City", "YourDefaultState"

    # Select the device to track (modify the index if necessary)
    device = api.devices[3]  

    if device:
        location = device.location()
        if location:
            latitude = location['latitude']
            longitude = location['longitude']
    
    return latitude, longitude



