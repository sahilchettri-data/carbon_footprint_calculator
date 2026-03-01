import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Carbon Footprint Calculator", page_icon="🌿", layout="centered")

st.markdown("""
<style>
div[data-testid="metric-container"] {
    background-color: #f0fdf4;
    border: 1px solid #bbf7d0;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
div[data-testid="metric-container"] label {
    color: #166534 !important;
    font-weight: 600;
}
div[data-testid="metric-container"] div[data-testid="stMetricValue"] > div {
    color: #15803d;
    font-size: 1.8rem;
}
</style>
""", unsafe_allow_html=True)

st.title("🌿 Carbon Footprint Calculator")
st.markdown("Calculate and track your company Scope 1, 2, and 3 emissions.")

st.sidebar.header("🌍 Company Data Input")

st.sidebar.subheader("Scope 1")
natural_gas = st.sidebar.number_input("Natural Gas (m³/year)", min_value=0.0, value=None)
diesel = st.sidebar.number_input("Diesel (liters/year)", min_value=0.0, value=None)
fleet_km = st.sidebar.number_input("Company Vehicles (km/year)", min_value=0.0, value=None)

st.sidebar.subheader("Scope 2")
electricity = st.sidebar.number_input("Electricity (kWh/year)", min_value=0.0, value=None)

st.sidebar.subheader("Scope 3")
flights = st.sidebar.number_input("Business Flights (km/year)", min_value=0.0, value=None)
commuting = st.sidebar.number_input("Employee Commuting (km/year)", min_value=0.0, value=None)
waste = st.sidebar.number_input("Waste Generated (tonnes/year)", min_value=0.0, value=None)

val_ng = natural_gas if natural_gas is not None else 0.0
val_diesel = diesel if diesel is not None else 0.0
val_fleet = fleet_km if fleet_km is not None else 0.0
val_elec = electricity if electricity is not None else 0.0
val_flights = flights if flights is not None else 0.0
val_commute = commuting if commuting is not None else 0.0
val_waste = waste if waste is not None else 0.0

EF_NATURAL_GAS = 2.04
EF_DIESEL = 2.68
EF_FLEET = 0.21
EF_ELECTRICITY = 0.233
EF_FLIGHTS = 0.255
EF_COMMUTING = 0.17
EF_WASTE = 467

scope1 = (val_ng * EF_NATURAL_GAS + val_diesel * EF_DIESEL + val_fleet * EF_FLEET) / 1000
scope2 = (val_elec * EF_ELECTRICITY) / 1000
scope3 = (val_flights * EF_FLIGHTS + val_commute * EF_COMMUTING + val_waste * EF_WASTE) / 1000

total = scope1 + scope2 + scope3

st.divider()

tab1, tab2 = st.tabs(["Results Dashboard", "Visual Breakdown"])

with tab1:
    st.subheader("Emissions Summary")
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col1.metric("Scope 1", f"{scope1:.2f} tCO₂e")
    col2.metric("Scope 2", f"{scope2:.2f} tCO₂e")
    col3.metric("Scope 3", f"{scope3:.2f} tCO₂e")
    col4.metric("Total Impact", f"{total:.2f} tCO₂e")

with tab2:
    st.subheader("Where are your emissions coming from?")
    
    data = pd.DataFrame({
        'Scope': ['Scope 1 (Direct)', 'Scope 2 (Electricity)', 'Scope 3 (Value Chain)'],
        'Emissions (tCO2e)': [scope1, scope2, scope3]
    })

    fig = px.pie(
        data, 
        values='Emissions (tCO2e)', 
        names='Scope',
        color='Scope',
        hole=0.45,
        color_discrete_map={
            'Scope 1 (Direct)': '#2a9d8f',
            'Scope 2 (Electricity)': '#a8d5ba',
            'Scope 3 (Value Chain)': '#e9c46a'
        }
    )
    
    fig.update_traces(
        textposition='outside',
        texttemplate='<b>%{percent:.2%}</b>',
        textfont=dict(color=['#2a9d8f', '#a8d5ba', '#e9c46a'], size=15)
    )
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=80, b=40, l=40, r=40)
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()
st.header("Reduction Recommendations")

if total == 0:
    st.info("Enter your company data in the sidebar to see recommendations.")
else:
    scopes = {'Scope 1': scope1, 'Scope 2': scope2, 'Scope 3': scope3}
    highest = max(scopes, key=scopes.get)
    
    st.warning(f"Your highest emission source is {highest}. Focus here first.")
    
    if highest == 'Scope 1':
        st.markdown("""
        **Priority Actions:**
        Transition your vehicle fleet to electric vehicles. Replace gas-powered heating systems with heat pumps. 
        Install on-site solar panels to reduce dependence on fossil fuels.
        """)
    elif highest == 'Scope 2':
        st.markdown("""
        **Priority Actions:**
        Switch to a renewable energy tariff immediately — this is the single fastest way to reduce Scope 2 emissions. 
        Conduct an energy audit to identify inefficiencies and upgrade to LED lighting throughout your facilities.
        """)
    elif highest == 'Scope 3':
        st.markdown("""
        **Priority Actions:**
        Introduce a remote work policy to reduce employee commuting emissions. 
        Replace business flights with video conferencing where possible. 
        Implement a supplier ESG screening process and set waste reduction targets.
        """)