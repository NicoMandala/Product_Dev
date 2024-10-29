# streamlit_app.py

# Import necessary libraries
import streamlit as st
import requests
from TaskA.main import suggest_cocktail

# Task 1: Get a Random Cocktail Recipe
st.header("Task 1: Get a Random Cocktail Recipe")

if st.button("Get Random Cocktail"):
    try:
        # Create three columns in Streamlit
        columns = st.columns(3)

        # Fetch and display a random cocktail in each column
        for col in columns:
            response = requests.get('http://127.0.0.1:8000/random_cocktail/')
            if response.status_code == 200:
                data = response.json()

                with col:
                    # Display the cocktail details
                    st.subheader(data["name"])
                    if data.get("tagline"):
                        st.markdown(f"<span style='color:green;'>{data['tagline']}</span>", unsafe_allow_html=True)

                    # Display the ingredients
                    st.markdown("### Ingredients")
                    for ingredient in data["ingredients"]:
                        st.write(ingredient)

                    # Display the instructions
                    st.markdown("### Instructions to Prepare the Cocktail")
                    st.write(data["instructions"])
            else:
                col.write("An error occurred while fetching the cocktail details")

    except Exception as e:
        st.error(f"An error occurred: {e}")

st.divider()

# Task A: Suggest a Cocktail
st.header("Task A: Suggest a Cocktail")

if st.button("Suggest a Cocktail"):
    try:
        # Create three columns for displaying suggestions
        columns = st.columns(3)

        # Run suggest_cocktail() three times and display results in columns
        for i, col in enumerate(columns):
            result = suggest_cocktail()

            with col:
                if "error" in result:
                    st.error(result["error"])
                else:
                    st.subheader(f"Cocktail Suggestion {i + 1}")
                    st.markdown(f"**First Name:** {result['first_name']}")
                    st.markdown(f"**First Letter:** {result['first_letter']}")
                    st.markdown(f"**Local Time:** {result['local_time']}")
                    st.markdown(f"**Suggestion:** {result['suggestion']}")

    except Exception as e:
        st.error(f"An error occurred: {e}")

st.divider()

# Task B: Visualize a Cocktail Recipe (Placeholder)
st.header("Task B: Visualize a Cocktail Recipe!")
st.write("This section is under construction...")
