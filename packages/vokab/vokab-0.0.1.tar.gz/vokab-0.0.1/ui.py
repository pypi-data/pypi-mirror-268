import streamlit as st
import pandas as pd

from vokab import Collection, Request


def main():
    # Set the app's theme
    st.set_page_config(page_title="Named Entity Linking", layout="wide")
    st.title("Named Entity Linking")

    # Initialize the collection
    collection = Collection.load("~/.local/umls")

    # User input
    col1, col2, col3 = st.columns(3)
    with col1:
        term = st.text_input("Enter a term:")
    with col2:
        label = st.text_input("Enter a label (optional):")
    with col3:
        limit = st.number_input(
            "Limit:", value=10, min_value=5, max_value=100, step=5
        )

    if st.button("Search"):
        # Create a request object
        request = Request(
            term=term, labels=[label] if label else None, limit=limit
        )

        # Perform the search using the collection
        response = collection(request)

        # Display the results in a table
        if response.candidates:
            table_data = []
            for candidate in response.candidates:
                table_data.append(
                    [
                        candidate.ranks.get("rerank", 99),
                        candidate.distances.get("rerank", 99),
                        candidate.term,
                        candidate.entity.name,
                        candidate.ranks.get("vss", 99),
                        candidate.distances.get("vss", 99),
                        candidate.ranks.get("fuzz", 99),
                        candidate.distances.get("fuzz", 99),
                        "Yes" if candidate.is_alias else "No",
                        "Yes" if candidate.is_exact else "No",
                        candidate.entity.label,
                    ]
                )

            columns = [
                "Rank",
                "Dist",
                "Term",
                "Name",
                "VSS Rank",
                "VSS Dist",
                "Fuzz Rank",
                "Fuzz Dist",
                "Alias?",
                "Exact?",
                "Label",
            ]

            with st.expander(f"Top {len(table_data)} Results"):
                st.write(pd.DataFrame(table_data, columns=columns))
        else:
            st.info("No results found.")


if __name__ == "__main__":
    main()
