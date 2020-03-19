import pandas as pd
# import pycountry as pc
# import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('Confirmed.csv')

# df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')

fig = go.Figure(data=go.Choropleth(locations=df['ISO'], z=df['3/18/20'], text=df['Country/Region'], colorscale='Blues', autocolorscale=False, reversescale=True,
                                   marker_line_color='darkgray', marker_line_width=0.5, colorbar_tickprefix='Confirmed = ', colorbar_title='Confirmed cases'))

fig.update_layout(title_text='Covid-19 Confirmed cases as of 18/03/2020', geo=dict(showframe=False, showcoastlines=False, projection_type='equirectangular'))

fig.show()
