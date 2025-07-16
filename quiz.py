import streamlit as st

# Datenstruktur
quiz_data = {
    "Wirtschaftssysteme": [20, 40, 60, 80],
    "Arbeitswelt": [20, 40, 60, 80],
    "Berufsorientierung": [20, 40, 60, 80],
    "Verbraucherverhalten": [20, 40, 60, 80]
}

fragen = {
    # Beispielhafte Fragen je Kategorie & Punktzahl
    ("Wirtschaftssysteme", 20): {"frage": "Was kennzeichnet die soziale Marktwirtschaft?", "antworten": ["Planwirtschaft", "Freie Marktwirtschaft", "Staatliche Eingriffe", "Subsistenzwirtschaft"], "richtig": 2},
    # Weitere Fragen hier einfügen analog...
    # Du kannst deine bestehenden Fragen aus dem ersten Code übernehmen.
}

# Session-State für beantwortete Fragen
if "beantwortet" not in st.session_state:
    st.session_state["beantwortet"] = []

st.title("🎓 WBS Quiz – Klasse 11")
st.markdown("Wähle eine Frage pro Kategorie anhand der Punkte.")

# Vier Spalten für Kategorien
spalten = st.columns(4)

for i, (kategorie, punkte_liste) in enumerate(quiz_data.items()):
    with spalten[i]:
        st.subheader(kategorie)
        for punkte in punkte_liste:
            frage_id = f"{kategorie}_{punkte}"
            button_label = f"{punkte} Punkte"

            # Wenn Frage beantwortet, Button durchgestrichen anzeigen
            if frage_id in st.session_state["beantwortet"]:
                st.button(f"~~{button_label}~~", key=frage_id, disabled=True)
            else:
                if st.button(button_label, key=frage_id):
                    frage_daten = fragen.get((kategorie, punkte))
                    if frage_daten:
                        auswahl = st.radio(frage_daten["frage"], frage_daten["antworten"], key=f"auswahl_{frage_id}")
                        if st.button("Antwort bestätigen", key=f"antwort_{frage_id}"):
                            if frage_daten["antworten"].index(auswahl) == frage_daten["richtig"]:
                                st.success("Richtig! 🎉")
                            else:
                                st.error("Leider falsch. 😕")
                            st.session_state["beantwortet"].append(frage_id)
                    else:
                        st.warning("Frage zu diesem Punkt wurde noch nicht hinterlegt.")
