# Import all relevant libraries
import streamlit as st
from PIL import Image
from transformers import AutoTokenizer
import transformers
import torch

# Define the chosen LLM: IGEL
model = "philschmid/instruct-igel-001"

# Generate the tokenizer and pipeline
tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)

# Define a function to filter the given data
def filter_data(data):
    """
    Filters the given data dictionary by removing specific keys ('Artikelnummer', 'Pflegehinweis')
    and values that contain the substring 'Ohne'.

    Args:
        data (dict): The input data dictionary.

    Returns:
        dict: The filtered data dictionary.

    """
    filtered_data = {}
    for key, value in data.items():
        if key not in ["Artikelnummer", "Pflegehinweis"] and "Ohne" not in value:
            filtered_data[key] = value
    return filtered_data

# Define the product comparisons
comparisons = [
    {
        "name": "Comparison 1",
        "product_image": "product_image1.jpg",
        "old_description": "Old Product Description 1",
        "unfiltered_data": {
            # Data dictionary for comparison 1
        },
    },
    {
        "name": "Comparison 2",
        "product_image": "product_image2.jpg",
        "old_description": "Old Product Description 2",
        "unfiltered_data": {
            # Data dictionary for comparison 2
        },
    },
    {
        "name": "Comparison 3",
        "product_image": "product_image3.jpg",
        "old_description": "Old Product Description 3",
        "unfiltered_data": {
            # Data dictionary for comparison 3
        },
    },
    {
        "name": "Comparison 4",
        "product_image": "product_image4.jpg",
        "old_description": "Old Product Description 4",
        "unfiltered_data": {
            # Data dictionary for comparison 4
        },
    },
    {
        "name": "Comparison 5",
        "product_image": "product_image5.jpg",
        "old_description": "Old Product Description 5",
        "unfiltered_data": {
            # Data dictionary for comparison 5
        },
    },
]

# Create a Streamlit app
st.title("Product Description Comparisons")

# Create a dropdown to select the comparison
selected_comparison = st.selectbox(
    "Select a Comparison",
    options=[comparison["name"] for comparison in comparisons],
)

# Find the selected comparison
selected_comparison_data = next(
    (comparison for comparison in comparisons if comparison["name"] == selected_comparison),
    None,
)

if selected_comparison_data is not None:
    # Load and display the product image
    product_image = Image.open(selected_comparison_data["product_image"])
    st.image(product_image, caption="Product Image", use_column_width=True)

    # Display the old product description
    old_description = selected_comparison_data["old_description"]
    st.subheader("Old Product Description")
    st.write(old_description)

    # Put everything together: pipeline and data
    sequences = pipeline(
        f"Schreibe einen Text, der dieses Produkt beschreibt, und verwende alle Daten {filter_data(selected_comparison_data['unfiltered_data'])}:",
        max_length=600,
        top_k=10,
        num_return_sequences=1,
    )

    # Display the new product description
    new_description = sequences[0]["generated_text"]
    st.subheader("New Product Description")
    st.write(new_description)

# Run the Streamlit app
if __name__ == "__main__":
    st.write("")