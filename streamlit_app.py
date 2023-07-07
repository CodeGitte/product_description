# Import all relevant libraries
import streamlit as st
from PIL import Image
import os
import warnings
warnings.filterwarnings("ignore")


# streamlit_app.py
def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("Password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    # Adding title
    st.title("Mockup: KI-generierte Produktbeschreibungen")
    st.markdown("Dieses Mockup generiert Produktbeschreibungen, in dem zuerst bestehende Produktdaten gefiltert werden und dann das Large Language Model (LLM) durch einen Prompt aufgefordert wird aus den gefilterten Daten einen beschreibenden Fließtext zu erstellen. Auch hier ergeben sich die gewöhnlichen Probleme bei LLMs: Halluzinationen, Doppelungen von Informationen und nicht ganz perfekte Grammatik.")
    st.divider()

    # Example images
    image_options_folder = "images"
    image_options = os.listdir(image_options_folder)

    # Define the product comparisons
    comparisons = [
        {
            "name": "Bluse",
            "product_image": "images/bluse.png",
            "old_description": "Vielseitig kombinierbare Bluse zum Reinschlüpfen. Mit einer breiten Blende, die mittig vom Hemdkragen bis zum Saum verläuft und elegant die kurze Knopfleiste verdeckt. Formgebende Brustabnäher. Lange Ärmel mit Knopfmanschetten",
            "new_description": "Dieses Produkt bietet eine vielseitige Kombination aus Stil und Komfort. Der lange Ärmel sorgt für eine angenehme Passform ohne Einschränkungen. Der Hemdkragen sorgt für einen eleganten Look, und das 100% Baumwoll-Gewebe sorgt für einen angenehmen Tragekomfort.",
            "unfiltered_data": {
                "Artikelnummer": "683.804.160",
                "Ärmellänge": "Langarm",
                "Kragenform": "Hemdkragen",
                "Farbe": "weiß",
                "Taschen": "Ohne Taschen",
                "Verschluss": "Ohne Verschluss",
                "Material": "100% Baumwolle",
                "Zusatzinformation": "Länge ca. 68 cm",
                "Pflegehinweis": "Maschinenwäsche"
            }
        },
        {
            "name": "Schuhe",
            "product_image": "images/schuhe.png",
            "old_description": "Wählen Sie bei dem Hausschuh von May Be Comfort Ihren Favoriten! Es gibt ihn ungefüttert mit atmungsaktivem Baumwoll-Futter und gefüttert mit wärmender Schurwolle. Das textile Obermaterial ist extra elastisch und anschmiegsam. Mit breitem Klettverschluss. Rutschhemmende Gummi-Laufsohle mit ca. 25 mm Absatz. Weite K für kräftige Füße.",
            "new_description": "Diese Hausschuhe sind für viele Anlässe geeignet. Die Antirutschsohle hilft, auf glatten und rutschigen Oberflächen einen sicheren Halt zu haben. Die flexible und bequeme Wechselfußbettung ist ideal für verschiedene Schuhgrößen. Das atmungsaktive textile Innenfutter sorgt für Atmungsaktivität und Komfort, und der weiche Gummi auf der Außensohle ist ideal für ein angenehmes Tragegefühl.",
            "unfiltered_data": {
                "Artikelnummer": "531.979.002",
                "Besonderheit": "Antirutschsohle, Wechselfußbett, Hallux Valgus, für orthopädische Einlagen",
                "Obermaterial": "Textil",
                "Innenfutter": "Ungefüttert",
                "Farbe": "beige",
                "Verschluss": "Klettverschluss",
                "Innensohle": "Textil",
                "Außensohle": "Gummi",
                "Futter": "100% Textil",
                "Material": "100% Textil",
                "Schuhweite": "sehr kräftig (Weite K)",
                "Art/Form": "Hausschuhe"
            },
        },
        {
            "name": "Sommerkleid",
            "product_image": "images/kleid.png",
            "old_description": "Hübsches Sommerkleid mit V-Ausschnitt. Aus wunderbar weichem Single-Jersey.",
            "new_description": "Das 'feel good' Strandkleid ist ein bequemer, bequemer und luftiger Look mit der passenden Farbpalette. Der ärmellose, V-förmige Ausschnitt, die lässige Passform und die Jerseyqualität machen das Kleid zu einem unverzichtbaren Outfit.",
            "unfiltered_data": {
                "Artikelnummer": "254.331.041",
                "Ärmellänge": "Ärmellos",
                "Ausschnitt": "V-Ausschnitt",
                "Marke": "feel good",
                "Farbe": "lagune-gemustert",
                "Verschluss": "Ohne Verschluss",
                "Materialfunktion": "Ohne Materialfunktion",
                "Material": "95% Viskose, 5% Elasthan",
                "Stoffart": "Jersey",
                "Länge": "Wadenlang",
                "Zusatzinformation": "Länge ca. 110 cm",
                "Art/Form": "Strandkleid geschlossen"
            },
        },
        {
            "name": "Herrenhose",
            "product_image": "images/hose.png",
            "old_description": "Die Hose von Marco Donati in klassischer Swing-Pocket-Form punktet durch die schmutz- und wasserabweisende Funktion. Mit Knopf- und Reißverschluss vorne sowie Gürtelschlaufen. 2 seitliche Taschen inklusive Münztäschchen, 2 Gesäßtaschen mit Knopfverschluss. Die Bügelfalte wirkt streckend und sorgt für die gepflegte Ausstrahlung. Unterstützt die Initiative Cotton made in Africa.",
            "new_description": "Diese Hose von Marco Donati ist eine stilvolle, vielseitige Hose mit einer klassischen 5-Pocket-Form. Die Hose ist wasserbeständig, hat eine feste Taille und ist aus einem Stretchmaterial gefertigt, das sich geschmeidig an den Körper anfügt. Die Hosenbeine können für zusätzlichen Komfort in der Länge angepasst werden. Der Knopf mit Reißverschluss und die Gesäßtaschen runden das Design ab, während die Länge der Hose an Ihre persönlichen Vorlieben angepasst werden kann.",
            "unfiltered_data": {
                "Artikelnummer": "415.133.002",
                "Bund": "Fester Bund",
                "Marke": "Marco Donati",
                "Farbe": "khaki",
                "Verschluss": "Knopf mit Reißverschluss",
                "Materialfunktion": "wasserabweisend",
                "Taschen": "Gesäßtaschen",
                "Stretch": "Mit Stretch",
                "Material": "98% Baumwolle, 2% Elasthan",
                "Länge": "Lang",
                "Zusatzinformation": "Innenbeinlänge ca. 82 cm",
                "Art/Form": "5-Pocket-Form",
                "Pflegehinweis": "Maschinenwäsche"
            }
        },
        {
            "name": "Taschentuch",
            "product_image": "images/taschentuch.png",
            "old_description": "In strapazierfähiger Qualität: Herren-Taschentücher.",
            "new_description": "Diese farbenfrohen, sortierten Taschentücher sind aus 100% Baumwolle gefertigt. Sie sind 8-teilig und messen 41 x 41 cm. Es handelt sich um Herren-Taschentücher.",
            "unfiltered_data": {
                "Artikelnummer": "503.129.003",
                "Farbe": "farbig-sortiert",
                "Material": "100% Baumwolle",
                "Packungsgröße": "8-Stück-Packung",
                "Pflegehinweis": "waschbar bis 60 °C",
                "Art/Form": "Herrentaschentuch",
                "Maße": "L 41 x B 41 cm"
            }
        }
    ]

    # Create a dropdown to select the comparison
    selected_comparison = st.selectbox(
        "Suche ein Bespielprodukt aus:",
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
        st.image(product_image, use_column_width=True)

        st.divider()

        # Display the old product description
        old_description = selected_comparison_data["old_description"]
        st.subheader("Bestehende Produktbeschreibung:")
        st.write(old_description)

        st.divider()
        
        # Display the new product description
        new_description = selected_comparison_data["unfiltered_data"]
        st.subheader("Ungefilterte Daten:")
        st.write(new_description)

        st.divider()
        
        # Display the new product description
        new_description = selected_comparison_data["new_description"]
        st.subheader("KI-generierte Produktbeschreibung:")
        st.write(new_description)

