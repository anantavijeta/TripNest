
import streamlit as st

st.set_page_config(
    page_title="TripNest | Your Travel Planner",
    page_icon="✈️",
    layout="wide"
)

# Website heading
st.title("✈️ TripNest")
st.subheader("Your next adventure starts here.")

st.write(
    "Plan your trips, explore destinations, "
    "and organise your travel budget in one place."
)

st.divider()

st.header("🌍 Let's plan your next trip!")

destination = st.text_input(
    "Where would you like to go?",
    placeholder="e.g. Goa, Manali, Jaipur, Paris"
)

travellers = st.number_input(
    "Number of travellers",
    min_value=1,
    max_value=20,
    value=2
)

budget = st.number_input(
    "Total trip budget (₹)",
    min_value=0,
    value=20000,
    step=1000
)

travel_style = st.selectbox(
    "Choose your travel style",
    [
        "Adventure",
        "Relaxation",
        "Culture and history",
        "Food and shopping",
        "Luxury",
        "Nature and wildlife"
    ]
)

if st.button("Plan My Trip ✨"):
    if destination.strip():
        st.success("Your TripNest plan has started!")
        st.write("**Destination:**", destination)
        st.write("**Travellers:**", travellers)
        st.write("**Total budget:** ₹", f"{budget:,}")
        st.write("**Travel style:**", travel_style)
    else:
        st.warning("Please enter a destination first.")
