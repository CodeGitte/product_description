# Import all relevant libraries 
from transformers import AutoTokenizer
import transformers
import torch

# Define the chosen LLM: IGEL 
model = AutoTokenizer.from_pretrained("philschmid/instruct-igel-001")

# Generate the tokenizer and pipeline
tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    device_map="auto",
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

# Insert data
unfiltered_data = {
    "Artikelnummer": "45345354",
    "Ärmellänge": "Ärmellos",
    "Bügel": "Ohne Bügel",
    "Ausschnitt": "V-Ausschnitt",
    "Marke": "feel good",
    "Farbe": "marine-weiß",
    "Verschluss": "Ohne Verschluss",
    "Materialfunktion": "Ohne Materialfunktion",
    "Material": "50% Baumwolle, 50% Modal",
    "Stoffart": "Jersey",
    "Länge": "Kurz",
    "Zusatzinformation": "Länge ca. 100 cm",
    "Pflegehinweis": "Maschinenwäsche bis 40 °C",
    "Art/Form": "Strandkleid geschlossen",
    "Pflegehinweis": "Reinigung"
}

data = filter_data(unfiltered_data)

# Put everthing together: pipeline and data 
sequences = pipeline(
    f"Schreibe einen Text, der dieses Produkt beschreibt, und verwende alle Daten {data}:",
    max_length=600,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
)

# Return the result
for seq in sequences: 
    print(f"Result: {seq['generated_text']}")