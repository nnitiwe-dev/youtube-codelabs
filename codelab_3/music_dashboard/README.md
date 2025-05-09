# 🎵 **Music Streaming Analytics Dashboard**

A **Streamlit-powered dashboard** for exploring real-time analytics from top global music streaming platforms: **Spotify** and **Apple Music**. This dashboard visualizes artist rankings, album streams, and song trends, offering interactive data exploration with powerful visuals.

---

## 🚀 **Features**

* **Real-Time Data Fetching:** Pulls live data from [Kworb.net](https://kworb.net) for Spotify and Apple Music.
* **Interactive Filters:** Seamlessly filter data by artist, album, and streaming counts.
* **Visualizations:** Dynamic bar charts, treemaps, and line charts for easy analysis.
* **User-Friendly UI:** Built with Streamlit for instant web-based interactivity.

---

## 🛠️ **Getting Started**

### **Prerequisites**

* Python 3.8+
* Streamlit
* Pandas
* Plotly

### **Installation**

Clone the repository:

```bash
git clone https://github.com/your-username/music-streaming-dashboard.git
cd music-streaming-dashboard
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### **Run the App**

```bash
streamlit run music_dashboard.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser to view the dashboard.

---

## 💡 **Recommended Improvement: Enhanced Data Loading**

The current version of the app fetches data directly from **Kworb.net** each time it runs, which can be **slow** and **unreliable** if the website changes its structure.

To **optimize load times** and handle **network failures gracefully**, consider the following improved `load_data` function:

```python
import pandas as pd
import os

CACHE_DIR = "cache"
os.makedirs(CACHE_DIR, exist_ok=True)

def load_data(url, table_index=0, filename="cached_data.csv", refresh=False):
    """
    Loads data from a URL and caches it as a CSV file for faster reloads.

    Args:
        url (str): The URL to fetch data from.
        table_index (int): The index of the HTML table to parse.
        filename (str): Local filename to cache the data.
        refresh (bool): Whether to refresh the cache.

    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
    cache_path = os.path.join(CACHE_DIR, filename)
    
    if os.path.exists(cache_path) and not refresh:
        print(f"Loading data from cache: {cache_path}")
        return pd.read_csv(cache_path)
    
    print(f"Fetching data from URL: {url}")
    df = pd.read_html(url)[table_index]
    df.to_csv(cache_path, index=False)
    return df
```

### **Usage**

```python
spotify_artists = load_data(
    "https://kworb.net/spotify/artists.html", 
    table_index=0, 
    filename="spotify_artists.csv"
)
```

### **Benefits:**

1. **Faster Loading Times:** Cached data is loaded instantly on subsequent runs.
2. **Offline Access:** If the URL is temporarily down, the app still functions.
3. **Automatic Updates:** Use the `refresh=True` flag to fetch new data:

   ```python
   spotify_artists = load_data("https://kworb.net/spotify/artists.html", refresh=True)
   ```

---

## 🌐 **Deployment**

To deploy this app, check out the following platforms:

* **Streamlit Community Cloud** (Free and simple)
* **Hugging Face** (Supports Python apps)
* **Render** (Free tier with auto-deploy from GitHub)

---

## 🤝 **Contributing**

Contributions are welcome! Please:

1. Fork the repo
2. Create a feature branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

---

## 📝 **License**

This project is licensed under the MIT License 

---

Would you like me to refactor the **music\_dashboard.py** to use this improved loader and make it more efficient?
