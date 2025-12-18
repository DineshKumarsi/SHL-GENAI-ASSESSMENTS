import streamlit as st
import requests
import json

# Page config
st.set_page_config(
    page_title="SHL GenAI Assessment Recommendation",
    layout="wide"
)

st.title("SHL GenAI Assessment Recommendation System")
st.write(
    "Enter a job description or hiring requirement to get recommended SHL assessments."
)

# FastAPI endpoint
API_URL = "http://127.0.0.1:8000/recommend"

# Input box
query = st.text_area(
    label="Job Description / Hiring Requirement",
    placeholder="Hiring a Java developer with good communication skills...",
    height=150
)

# Button
if st.button("Get Recommendations"):
    if query.strip() == "":
        st.warning("Please enter a job description.")
    else:
        with st.spinner("Generating recommendations..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"query": query},
                    timeout=60
                )

                # if response.status_code == 200:
                #     data = response.json()
                #
                #     st.success("Recommendations generated successfully")
                #
                #     for item in data["recommendations"]:
                #         st.write(f"### {item['name']}")
                #         st.write(f"- Type: {item['test_type']}")
                #         st.write(f"- Duration: {item['duration']}")
                #         st.write("---")
                # else:
                #     st.error(response.text)

                if response.status_code == 200:
                    data = response.json()

                    st.success("Recommendations generated successfully!")

                    st.subheader("Recommended Assessments")
                    st.json(data["recommended_assessments"])
                    # for item in data["recommendations"]:
                    #      st.write(f"### {item['name']}")
                    #      st.write(f"- Type: {item['test_type']}")
                    #      st.write(f"- Duration: {item['duration']}")
                    #      st.write("---")

                else:
                    st.error(
                        f"API Error: {response.status_code} - {response.text}"
                    )

            except Exception as e:
                st.error(f"Unable to connect to API: {e}")