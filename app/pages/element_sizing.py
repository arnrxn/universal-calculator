import streamlit as st


def calculate_size_with_relative_proportions(
    total_dimension: float, margin: float, proportions: list
) -> list:
    """Calculate the actual size of each element based on their relative proportions.

    Args:
        total_dimension (float): Total available space along the dimension.
        margin (float): Margin size on one side of each element.
        proportions (list): List of relative proportions for each element.

    Returns:
        list: List of actual calculated sizes for each element.
    """

    total_proportion = sum(proportions)
    available_space = total_dimension - margin * (len(proportions) + 1)

    calculated_sizes = [
        (available_space * (prop / total_proportion)) for prop in proportions
    ]

    return calculated_sizes


def main():
    st.title("Element Sizing Calculator")
    st.subheader("A simple tool to calculate sizes of elements in a page")
    st.write("\n")

    # Input fields
    col1, col2, col3 = st.columns(3)
    total_dimension = col1.number_input("Page Size", min_value=1, value=1280)
    margin = col2.number_input("Margin Size", min_value=0, value=10)
    num_elements = col3.number_input("Number of Elements", min_value=1, step=1, value=4)

    # Input for relative proportions
    st.write("\n")
    st.write("Relative proportion of each element")
    columns = st.columns(num_elements)
    relative_proportions = []
    for i in range(num_elements):
        with columns[i]:
            proportion = st.number_input(f"Element {i + 1}", min_value=1, step=1)
            relative_proportions.append(proportion)

    # Calculation and display
    try:
        st.write("\n")
        sizes = calculate_size_with_relative_proportions(
            total_dimension, margin, relative_proportions
        )
        st.write("Size in units of each element")
        columns = st.columns(num_elements)
        for i, size in enumerate(sizes):
            with columns[i]:
                st.metric(f"Element {i + 1}", value=f"{size:.1f}")
    except ValueError as e:
        st.error(str(e))


if __name__ == "__main__":
    main()
