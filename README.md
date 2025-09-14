# AIM4M Tools and Techniques for Geospatial visualization

## Summary
This capstone project demonstrates the practical application of geospatial visualization techniques learned through the "[Tools and Techniques for Geospatial ML - AIM4Mobility](https://factual-academy.com/bundle/aim4mobility)" program at [Factual Academy](https://factual-academy.com/).

## Foreword
This analysis investigates several key questions related to the distribution and characteristics of reported accidents throughout the year:

1. Seasonal Trends: Is there a noticeable variation in the number of accidents across different months? Specifically, do accident rates increase during the winter months or decrease in the summer, or vice versa?

2. Temporal Patterns: How does the frequency of accidents vary by both the day of the week and the hour of the day? What times of day exhibit the highest incidence of accidents? Are there distinct patterns between weekdays and weekends?

3. Spatial Dynamics: Does the geographic distribution of accidents change with the seasons? In particular, do accident 'hotspots' shift locations within the city depending on whether it's winter or summer?

## Answers
1. Seasonal Dependency:
There is no meaningful dependency between the number of accidents and the month of the year. The lowest accident counts occur in February, August, and December. Notably, if February’s count is adjusted to account for its shorter duration (estimating the total if the month had 31 days), its accident count (157) becomes similar to those of August (158) and December (155), suggesting that monthly differences are minimal and largely explained by the differing number of days rather than seasonality.

2. Temporal Patterns (Weekday & Time):
The heatmap showing accident counts as a function of weekday and hour reveals a concentration of accidents towards the end of the day, especially on Thursdays and Fridays. This suggests higher risk during late weekday hours, possibly due to increased activity and travel at those times.

3. Spatial Dynamics:
This Streamlit app enables interactive exploration by allowing users to select a month via a dropdown menu. The accident map updates dynamically to display a heatmap overlaid with individual accident points for the selected month. This setup allows users to visually assess whether accident hotspots shift or intensify in different parts of the city from winter to summer months, though no major seasonal migrations of hotspots are apparent in the available data.

## Future work
Besides the effect Thursday / Friday, would the meteorologic conditions affect accidents? Would the hourly distribution be different in December / January (winter) and July / August (Summer)? 


## Deployment

This project is to be acessible through [render](https://www.render.com), at [https://aim4m-pcp.onrender.com](https://aim4m-pcp.onrender.com)

Maia, September 2025
Pedro Pimenta