# SIPS - Seismic Intelligence & Prediction System

SIPS is a comprehensive platform for monitoring, analyzing, and predicting seismic events globally. It provides users with real-time seismic data visualization, machine learning-based risk assessment, and detailed safety protocols.

## 🚀 Key Features
- **Home Dashboard**: Real-time statistics, system capabilities, and recent alerts.
- **Prediction Lab**: ML-driven risk assessment simulation based on magnitude, depth, and location.
- **Live Map Dashboard**: Interactive mapping powered by Leaflet with magnitude-based color coding.
- **Data Insights**: Visual analytics (Bar, Scatter, Area charts) for trend analysis.
- **Safety & Preparedness**: Comprehensive educational content for earthquake safety.

## 🐍 Python Version (Streamlit)
The project has been expanded to include a Python implementation, optimized for deployment on **Streamlit Cloud**.

### Running the Python Version Locally
1. Ensure you have Python 3.9+ installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```


## 🛠️ Tech Stack

Technology	    Purpose

Streamlit	-    The core framework for the web interface and navigation.

Pandas	   -   Used for data manipulation, filtering, and managing seismic records.

Plotly      -    Express	Powers the interactive charts and histograms in the Data Insights section.

NumPy	      -   Handles the mathematical calculations for the Prediction Lab risk engine.

st.map	   -    Streamlit's built-in mapping tool for geospatial visualization.

Custom CSS	-   Injected via Markdown to maintain the "Deep Ocean" visual identity.


---
