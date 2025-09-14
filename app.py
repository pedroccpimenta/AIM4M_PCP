import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from shapely.geometry import Point
from streamlit_folium import st_folium
from folium.plugins import HeatMap

import seaborn as sns

import matplotlib.pyplot as plt


# Set page config
st.set_page_config(page_title="Lisbon Road Accidents (Pedro Pimenta)", layout="wide")

st.title("Lisbon Road Accidents")
st.html("<h2>Capstone Project</h2>")
st.html("Developed in the context of \"Tools and Techniques for Geospatial Machine Learning\" (Factual <a href='https://factual-academy.com/bundle/aim4mobility' target='*'>AIM4Mobility</a>)")

st.html("<hr color=gray>" )

col1, col2 = st.columns(2)
# Load data
df = pd.read_csv("data/Road_Accidents_Lisbon.csv")

with col1:
    st.caption("An example of the vailable data:")
    st.title("dataset sample")
    st.dataframe(df.head()) 
with col2:
    st.caption("Just checking monthly dependency:")

    st.title('Number of Accidents by month')

    import calendar
    # list of month names using calendar module
    month_order = list(calendar.month_name)[1:]
    month_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month_order = [m[:3] for m in month_name]
    month_counts = df['month'].value_counts().reindex(month_order).fillna(0)
    month_counts.index = pd.CategoricalIndex(month_counts.index, categories=month_order, ordered=True)
    month_counts = month_counts.sort_index()
    st.bar_chart(month_counts)
    st.caption("No meaningful pattern was identified.")

st.html("<hr color=gray>")

heatmap_data = df.pivot_table(index='weekday', columns='hour', aggfunc='size', fill_value=0)

# Sort weekdays in natural order if needed
order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
heatmap_data = heatmap_data.reindex(order)

# Plot the heatmap
fig, ax = plt.subplots(figsize=(8,5))
sns.heatmap(
    heatmap_data, cmap='YlGnBu', annot=True, fmt='d', ax=ax,
    annot_kws={"size": 8},  # smaller annotation font size
    cbar_kws={'label': 'Count'}
    )

# Add titles and labels
ax.set_title('Occurrences by Weekday and Hour')
ax.set_xlabel('Hour of Day')
ax.set_ylabel('Weekday')

# Display plot in Streamlit
st.caption("Heatmap for hourly vs daily patterns")
st.pyplot(fig)
st.caption("This heatmap shows the biggest concentration of accidents happens from monday to friday - mainly Thursday and Friday - by the end of day.")


st.html("<hr color=orange>")

st.html("Explore how accident locations change throughout the year.<br>"
        " The visualization combines density heatmaps (showing concentration patterns) with individual points (exact locations) for complete spatial insight."
    )


col3, col4 = st.columns(2)


with col3:

    # Create dropdown
    selected_value = st.selectbox(
        "Select one month:",
                options=df['month'].unique(),  # Replace with your column name
                index=0
        )

    filtered_df = df[df['month'] == selected_value]


    # Convert to GeoDataFrame
    gdf = gpd.GeoDataFrame(
        filtered_df,
        geometry=[Point(xy) for xy in zip(filtered_df.longitude, filtered_df.latitude)],
        crs="EPSG:4326"
    )

    # Create base map centered on Lisbon
    center = [gdf["latitude"].mean(), gdf["longitude"].mean()]
    m = folium.Map(location=center, zoom_start=12, tiles="CartoDB Positron")


    # Prepare heatmap points
    heat_data = [[row['latitude'], row['longitude']] for _, row in filtered_df.iterrows()]

    # Create and center map
    center = [filtered_df['latitude'].mean(), filtered_df['longitude'].mean()]
    m = folium.Map(location=center, zoom_start=12, tiles='CartoDB Positron')
    HeatMap(heat_data, radius=12).add_to(m)


    # Add accident points
    for _, row in gdf.iterrows():
        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=4,
            color="red",
            fill=True,
            fill_opacity=0.6,
            popup=f"ID: {row['id']}<br>Hour: {row['hour']}<br>Fatalities: {row['fatalities_30d']}"
        ).add_to(m)


    #m


    # Render map in Streamlit

    st_data = st_folium(m, width=800, height=600)

with col4:
    st.html("<img src='./pics/hm_months.gif' alt='animated gif'>")

# Display notice
st.markdown( "**Important Notice:** Use of this data restricted for educational purposes within this course only." )

st.html( 
"<hr color=lime>"
"full code available "
"<i>Maia, Setembro 2025<br>Pedro Pimenta (<a href='https://www.linkedin.com/in/pedropimenta/' target='_'>https://www.linkedin.com/in/pedropimenta/</a>)"
"<hr color=lime>"
)
