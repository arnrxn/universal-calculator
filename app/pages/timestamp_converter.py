import streamlit as st
from datetime import datetime


def convert_timestamp(timestamp, unit):
    """Convert Unix timestamp to human-readable date-time."""
    if unit == "milliseconds":
        timestamp /= 1000  # Convert milliseconds to seconds
    return datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")


def main():
    st.title("Unix Timestamp Converter")
    st.subheader("Convert unix timestamp to human-readable date-time")
    st.write("\n")

    # Input fields
    col1, col2 = st.columns(2)
    timestamp = col1.number_input("Enter Unix Timestamp", step=1, format="%d")
    unit = col2.selectbox("Select Unit", ("milliseconds", "seconds"))

    # Conversion and Display
    try:
        readable_datetime = convert_timestamp(timestamp, unit)
        st.success(f"Human-readable Date-Time: {readable_datetime}")
    except Exception as e:
        st.error(f"Error: {e}")


if __name__ == "__main__":
    main()
