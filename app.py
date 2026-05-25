import streamlit as st
import plotly.express as px
import pandas as pd
from dbhelper import Db

db=Db()

st.sidebar.title('Filght Analysis')

user_input=st.sidebar.selectbox('menu',['select one','check flight','Analysis'])
if user_input=='check flight':
    st.title('flight detail')
    col1,col2=st.columns(2)
    city=db.fetch_city_name()
    with col1:
        source=st.selectbox('Source',sorted(city))
    with col2:
        destination=st.selectbox('Destination',sorted(city))   
    if st.button('serach'):
        result=db.flight_df(source,destination)
        st.dataframe(result)     
elif user_input=='Analysis':
    st.title('Analysis') 

    airline,frequency=db.fetch_pie_data()
    df = pd.DataFrame(airline,frequency)
    fig = px.pie(
    df,
    values=frequency,  # Column with the values for each slice
    names=airline,  # Column with the labels for each slice
    title='Pie Chart', # Chart title
    hover_name=airline # Display category name on hover
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.title('Busiest Airline')
    city,freq1=db.data_for_chart()
    df = pd.DataFrame({
    "city": city,
    "freq1": freq1
     })
    st.dataframe(df, use_container_width=True)
    st.bar_chart(
            data=df,
            x="city",
            y="freq1",
            x_label="City Name",
            y_label="No of Flights",
            use_container_width=True
            )

else:
    st.title('Introduction')      
    st.markdown("""
    Welcome to the **Flight Analysis Dashboard**! ✈️
    
    This application connects to a flight database to help you explore and analyze flight information. Use the sidebar menu on the left to navigate through the application:
    - **check flight:** Search for available flights by selecting your desired source and destination cities.
    - **Analysis:** View analytical charts, including airline market share and the busiest cities for flight traffic.
    """)
