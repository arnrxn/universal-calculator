import streamlit as st


def calculate_percentage(part: float, whole: float) -> float:
    """Calculate the percentage of a part in relation to the whole.

    Args:
        part (float): The part or subset of the total.
        whole (float): The total or whole amount.

    Returns:
        float: The percentage of the part in relation to the whole.
    """
    if whole == 0:
        raise ValueError("The whole cannot be zero.")
    return (part / whole) * 100


def main():
    st.title("Percentage Calculator")
    st.subheader("A simple tool to calculate percentages")

    # Input fields
    col1, col2 = st.columns(2)
    part = col1.number_input("Part Value", min_value=0.0, format="%.2f")
    whole = col2.number_input("Whole Value", min_value=0.0, format="%.2f")

    # Calculation and display
    try:
        result = calculate_percentage(part, whole)
        st.success(f"The percentage is {result:.2f}%")
    except ValueError as e:
        st.error(str(e))


if __name__ == "__main__":
    main()
