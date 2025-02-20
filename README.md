# ⛅Weather App

A simple web-based Weather App built with Streamlit that fetches real-time weather data and displays current temperature, along with a weekly forecast. Users can choose temperature units (Celsius, Fahrenheit, or Kelvin) for better readability.
Try the Deployment: https://weathermap.streamlit.app/

## 🪶Features

- Fetch current weather for a given city
- Display temperature in Celsius, Fahrenheit, or Kelvin
- Show a weekly weather forecast with a temperature trend chart
- User-friendly interface with a clean UI
- Logging for debugging and monitoring

## 👨🏻‍💻Technologies Used

- **Streamlit** - For building the web UI
- **Matplotlib** - For rendering the forecast chart
- **Requests** - For making API calls
- **Logging** - For application logging and debugging

## ℹ️Installation

1. Clone the repository:
   ```sh
   https://github.com/Paramjit-tiger/WeathersMap
   cd WeathersMap
   ```
2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the application with:
```sh
streamlit run app.py
```

## File Structure
```
WeathersMap/
│── app.py                   # Main application file
│── requirements.txt         # Project dependencies
│── .gitignore               # Git ignore file
│── modules/
│   │── api_handler.py       # Handles API requests
│   │── ui_components.py     # UI rendering functions
│   │── utils.py             # Utility functions
│── assets/
│   │── weather_icon.png     # App icon
|   |── img.jpg              # Background image
```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

---

🚀 **Developed with ❤️ using Streamlit**

