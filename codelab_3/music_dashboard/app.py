import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from urllib.error import URLError

# Streamlit page configuration
st.set_page_config(page_title="Music Streaming Analytics Dashboard", layout="wide")

# Header with styling
def display_header():
    header_html = """
    <div style="text-align: center; padding: 20px; background-color: #F4F4F4; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <h1 style="font-size: 36px; color: #333;">Music Streaming Analytics Dashboard</h1>
        <p style="font-size: 18px; color: #666;">
            Explore streaming trends and insights from 
            <a href="https://kworb.net" target="_blank" style="text-decoration: none; color: #1DB954; font-weight: bold;">Spotify</a> & 
            <a href="https://kworb.net" target="_blank" style="text-decoration: none; color: #007AFF; font-weight: bold;">Apple Music</a>
        </p>
    </div>
    """
    st.markdown(header_html, unsafe_allow_html=True)

# Load data from URL and handle errors
@st.cache_data
def load_data(url, table_index=0):
    try:
        data_frames = pd.read_html(url)
        return data_frames[table_index]
    except URLError:
        st.error(f"Failed to load data from {url}")
        return pd.DataFrame()

# Data cleaning function
def clean_data(df, column_name):
    if not df.empty:
        df["Streams"] = pd.to_numeric(df[column_name], errors="coerce")
    return df

# Visualization functions
def plot_treemap(df, title):
    fig = px.treemap(df, path=["Artist"], values='Streams', color="Artist", title=title)
    fig.update_traces(textinfo="label+value", hovertemplate='<b>%{label}</b><br>Streams: %{value:,}')
    st.plotly_chart(fig, use_container_width=True)

def plot_bar_chart(df, x_col, y_col, title, color):
    fig = px.bar(df, x=x_col, y=y_col, title=title, color_discrete_sequence=[color])
    fig.update_layout(xaxis=dict(tickangle=25, tickfont=dict(size=12)))
    st.plotly_chart(fig, use_container_width=True)

def plot_comparison_chart(apple_songs, spotify_songs):
    fig = go.Figure()
    # Apple Music
    fig.add_trace(go.Bar(
        x=apple_songs['Rank'],
        y=apple_songs['Streams'],
        name='Apple Music',
        text=apple_songs['Artist and Title'],
        textposition='inside',
        marker_color='#007AFF'
    ))
    # Spotify
    fig.add_trace(go.Bar(
        x=spotify_songs['Rank'],
        y=spotify_songs['Streams'],
        name='Spotify',
        text=spotify_songs['Artist and Title'],
        textposition='inside',
        marker_color='#1DB954'
    ))
    fig.update_layout(
        title="Top Songs (Daily Chart Totals): Spotify vs Apple Music",
        xaxis_title="Rank",
        yaxis_title="Total[Apple]/ PkStreams [Spotify]",
        barmode='group',
        template="plotly_white",
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)

# Footer
def display_footer():
    footer_html = """
    <div style="text-align: center; padding: 20px; font-size: 12px; color: #555;">
        <p>Data sourced from 
            <a href="https://kworb.net/spotify" target="_blank" style="text-decoration: none; color: #007AFF;">kworb.net</a> | 
            Visualizations powered by 
            <a href="https://plotly.com" target="_blank" style="text-decoration: none; color: #0054A6;">Plotly</a>
        </p>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)

# Main function
def main():
    display_header()

    # Load data
    spotify_albums = clean_data(load_data("https://kworb.net/spotify/toplists.html"), "Streams")
    apple_albums = clean_data(load_data("https://kworb.net/apple_albums/totals.html"), "Total")
    spotify_artists = clean_data(load_data("https://kworb.net/spotify/artists.html"), "Streams")
    apple_artists = clean_data(load_data("https://kworb.net/apple_albums/artisttotals.html"), "Total")
    spotify_songs = clean_data(load_data("https://kworb.net/spotify/country/global_daily_totals.html"), "PkStreams")
    apple_songs = clean_data(load_data("https://kworb.net/apple_songs/totals.html"), "Total")

    # Layout in columns
    col1, col2 = st.columns(2)

    with col1:
        if not apple_artists.empty:
            top_artists = apple_artists.sort_values("Streams", ascending=False).head(20)
            plot_treemap(top_artists, "Top 20 Artists (All Time): Apple Music")

    with col2:
        if not apple_albums.empty:
            top_albums = apple_albums.sort_values("Streams", ascending=False).head(10)
            # Truncate the "Artist and Title" if it exceeds the maximum length

            MAX_LABEL_LENGTH = 30
            top_albums["Artist and Title"] = top_albums["Artist and Title"].apply(
                lambda x: x if len(x) <= MAX_LABEL_LENGTH else x[:MAX_LABEL_LENGTH] + "..."
            )
            plot_bar_chart(top_albums, "Artist and Title", "Streams", "Top 10 Apple Music Albums", "#007AFF")

    col3, col4 = st.columns(2)

    with col3:
        if not spotify_albums.empty:
            top_spotify_albums = spotify_albums.sort_values("Streams", ascending=False).head(10)
            plot_bar_chart(top_spotify_albums, "Artist and Title", "Streams", "Top 10 Spotify Albums", "#1DB954")

    with col4:
        if not spotify_artists.empty:
            top_artists = spotify_artists.sort_values("Streams", ascending=False).head(20)
            plot_treemap(top_artists, "Top 20 Artists (All Time): Spotify")

    # Top songs comparison
    apple_top_songs = apple_songs.sort_values("Streams", ascending=False).head(10)
    apple_top_songs['Rank'] = range(1, 11)

    spotify_top_songs = spotify_songs.sort_values("Streams", ascending=False).head(10)
    spotify_top_songs['Rank'] = range(1, 11)

    plot_comparison_chart(apple_top_songs, spotify_top_songs)
    display_footer()

# Run the app
if __name__ == "__main__":
    main()
