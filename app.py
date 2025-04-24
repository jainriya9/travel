import streamlit as st
import random
import requests

# -----------------------
# DATA SETUP
# -----------------------
destinations = {
    "Manali 🏔️": "Manali",
    "Goa 🏖️": "Goa",
    "Jaipur 🏰": "Jaipur",
    "Rishikesh 🧘‍♂️": "Rishikesh",
    "Mumbai 🌆": "Mumbai"
}

interests = {
    "Nature 🌿": ["Visit scenic valleys", "Forest walk", "Photography hike", "Botanical garden visit"],
    "Adventure 🧗‍♂️": ["Paragliding", "River rafting", "Ziplining", "Jungle safari"],
    "Culture 🎨": ["Visit temples & forts", "Traditional arts workshop", "Cultural dance show", "Folk museum tour"],
    "Foodie 🍲": ["Street food crawl", "Regional cooking class", "Local cafes", "Night food bazaar"],
    "Relaxation 💆": ["Beach sunset meditation", "Hot spring dip", "Spa day", "Slow café journaling"]
}

accommodations = {
    "Low": ["Backpacker hostel", "Budget guesthouse"],
    "Medium": ["3-star hotel", "Cozy Airbnb"],
    "High": ["Luxury resort", "Boutique hotel"]
}

travel_modes = {
    "Manali": ["Bike rental", "Cab service", "Walkable trails"],
    "Goa": ["Scooter rental", "Auto-rickshaw", "Beachside walks"],
    "Jaipur": ["Cycle rickshaw", "Local bus", "Metro"],
    "Rishikesh": ["Tuktuk", "Shared jeep", "By foot"],
    "Mumbai": ["Metro", "Local train", "Uber/Ola"]
}

packing_essentials = {
    "Manali": ["Warm jacket", "Trekking shoes", "Gloves", "Power bank"],
    "Goa": ["Sunscreen", "Flip flops", "Swimwear", "Hat"],
    "Jaipur": ["Cotton clothes", "Sunglasses", "Camera", "Cash for markets"],
    "Rishikesh": ["Yoga mat", "Water bottle", "Quick-dry towel", "Bug spray"],
    "Mumbai": ["Raincoat (monsoon)", "Power bank", "City map", "Travel card"]
}

fun_facts = {
    "Manali": "Did you know? Manali is named after the Hindu lawgiver Manu!",
    "Goa": "Fun Fact: Goa has over 7000 bars – cheers responsibly 🍻",
    "Jaipur": "Jaipur is also known as the Pink City for its distinct colored buildings.",
    "Rishikesh": "Known as the Yoga Capital of the World!",
    "Mumbai": "Mumbai local trains carry over 7.5 million people a day!"
}

# -----------------------
# WEATHER FUNCTION
# -----------------------
def get_weather(city):
    try:
        api_key = "your_openweathermap_api_key"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url).json()
        return f"{response['weather'][0]['description'].title()}, {response['main']['temp']}°C"
    except:
        return "Weather data not available ❌"

# -----------------------
# STREAMLIT UI
# -----------------------
st.set_page_config(page_title="Return Journey", layout="wide", page_icon="🌏")
st.markdown("<h1 style='text-align:center;'>🧠 Return Journey: Smart Trip Planner</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📍 Choose Destination")
    destination_display = st.selectbox("", list(destinations.keys()))
    destination = destinations[destination_display]

    st.subheader("📅 Duration (days)")
    days = st.slider("", 1, 10, 3)

    st.subheader("🎯 Interests")
    selected = st.multiselect("", list(interests.keys()), default=["Nature 🌿", "Foodie 🍲"])

    st.subheader("💸 Budget")
    budget = st.radio("", ["Low", "Medium", "High"], horizontal=True)

    if st.button("🚀 Plan My Trip!"):
        st.success(f"Here’s your {days}-day plan for {destination}!")

        st.subheader("☁️ Live Weather")
        st.info(get_weather(destination))

        st.subheader("🗺️ Your Itinerary")
        for i in range(1, days + 1):
            st.markdown(f"### Day {i}")
            for interest in selected:
                st.write(f"✅ {random.choice(interests[interest])}")
            st.write(f"🧭 Local experience: {random.choice(['Try a sunrise hike', 'Visit a community market', 'Join a yoga circle'])}")
            st.write("---")

        st.subheader("🏨 Stay Options")
        for place in accommodations[budget]:
            st.write(f"• {place}")

        st.subheader("🚌 Local Travel")
        for mode in travel_modes[destination]:
            st.write(f"• {mode}")

        st.subheader("🎒 Packing Essentials")
        for item in packing_essentials[destination]:
            st.write(f"✅ {item}")

        st.subheader("📢 Fun Fact")
        st.info(fun_facts[destination])

        st.download_button("📥 Download Itinerary", f"Trip to {destination}\nDays: {days}\nInterests: {', '.join(selected)}", file_name="my_itinerary.txt")

with col2:
    with st.container():
        st.markdown("### ✨ Imagine your destination...")
        st.image(
            "https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1",
            caption="Adventure is calling 📍",
            width=500
        )


st.markdown("---")
st.markdown("<center>🌐 Created with love by Team Return Journey 💙</center>", unsafe_allow_html=True)
