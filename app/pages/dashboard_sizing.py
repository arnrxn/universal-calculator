import streamlit as st


def calculate_chart_size(page_size: float, margin: float, num_charts: int) -> float:
    """Calculate the size of each chart to fit within a given page size.

    Args:
        page_size (float): The total available height or width for all charts.
        margin (float): The size of the margin to be applied around each chart.
        num_charts (int): The number of charts to be displayed.

    Returns:
        float: The calculated height or width for each chart/card.

    Raises:
        ValueError: If num_charts is less than or equal to 0.

    """

    if num_charts <= 0:
        raise ValueError("Number of charts/cards must be greater than 0.")

    # Subtract total margins from the available size, then divide by the number of charts
    chart_size = (page_size - (margin * (num_charts + 1))) / num_charts

    return chart_size


def main():
    st.title("Dashboard Sizing Calculator")
    st.subheader("A simple tool to perform daily calculations")

    # Input fields
    col1, col2, col3 = st.columns(3)
    page_size = col1.number_input("Page Height/Width", min_value=1, value=1280)
    margin = col2.number_input("Desired Margin Size", min_value=0, value=10)
    num_charts = col3.number_input("Number of Charts", min_value=1, step=1, value=4)

    # Calculation and display
    try:
        chart_size = calculate_chart_size(page_size, margin, num_charts)
        st.success(f"Each chart should be {chart_size:.1f} units high/wide.")
    except ValueError as e:
        st.error(str(e))


if __name__ == "__main__":
    main()
