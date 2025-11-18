import streamlit as st
from model_helper import predict
# Header with custom color
st.markdown(
    """
    <h1 style='color:#1f77b4;'>Car Damage Detection</h1>
    """,
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader("Upload the file", type=["jpg", "png"])

if uploaded_file:
    image_path = "temp_file.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        st.image(uploaded_file, caption="Uploaded File", use_container_width=True)
        prediction = predict(image_path)
        st.info(f"Predicted Class: {prediction}")

st.markdown(
    """
    <hr>
    <p style='text-align:center; color:gray;'>Made by virajX</p>
    """,
    unsafe_allow_html=True
)