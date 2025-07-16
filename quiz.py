import streamlit as st

# --- Initialisierung ---
if "beantwortet" not in st.session_state:
    st.session_state["beantwortet"] = {}
if "ausgewählte_frage" not in st.session_state:
    st.session_state["ausgewählte_frage"] = None
if "punkte_A" not in st.session_state:
    st.session_state["punkte_A"] = 0
if "punkte_B" not in st.session_state:
    st.session_state["punkte_B"] = 0
if "aktive_gruppe" not in st.session_state:
    st.session_state["aktive_gruppe"] = "A"

# --- Reset-Button ---
if st.button("🔄 Quiz zurücksetzen"):
    st.session_state["beantwortet"] = {}
    st.session_state["ausgewählte_frage"] = None
    st.session_state["punkte_A"] = 0
    st.session_state["punkte_B"] = 0
    st.session_state["aktive_gruppe"] = "A"
    st.success("Quiz wurde zurückgesetzt.")

# --- Punktestand & Gruppenanzeige ---
st.markdown("### 🎯 Punktestand")
st.write(f"**Gruppe A**: {st.session_state['punkte_A']} Punkte")
st.write(f"**Gruppe B**: {st.session_state['punkte_B']} Punkte")
st.write(f"👥 Aktive Gruppe: **Gruppe {st.session_state['aktive_gruppe']}**")

# --- Fragenstruktur mit gestaffeltem Schwierigkeitsgrad ---
fragen = {
    # Beispielkategorie: Wirtschaftssysteme
    ("Wirtschaftssysteme", 20): {
        "frage": "Welches Prinzip liegt der Marktwirtschaft zugrunde?",
        "antworten": ["Zufallsproduktion", "Planung durch Staat", "Angebot und Nachfrage", "Subventionierung"],
        "richtig": 2
    },
    ("Wirtschaftssysteme", 40): {
        "frage": "Was unterscheidet die soziale von der freien Marktwirtschaft?",
        "antworten": ["Höhere Preise", "Staatlicher Ausgleich sozialer Nachteile", "Private Produktionsmittel", "Kein Wettbewerb"],
        "richtig": 1
    },
    ("Wirtschaftssysteme", 60): {
        "frage": "Was beschreibt den magischen Viereck der Wirtschaftspolitik?",
        "antworten": ["Vier Wirtschaftszentren", "Vier Steuerarten", "Vier gleichrangige Ziele", "Vier Ministerien"],
        "richtig": 2
    },
    ("Wirtschaftssysteme", 80): {
        "frage": "Wie beeinflusst die Geldpolitik der EZB die soziale Marktwirtschaft?",
        "antworten": ["Gar nicht", "Über Zinsentscheidungen zur Stabilität", "Durch Werbung", "Durch Steuern"],
        "richtig": 1
    },
    # Weitere Kategorien und Fragen analog ergänzen...
}

# --- Anzeige: 4 breite Spalten nebeneinander mit kleineren Titeln ---
kategorien = list({key[0] for key in fragen.keys()})
punkte_liste = [20, 40, 60, 80]
spalten = st.columns([2, 2, 2, 2])

for i, kat in enumerate(kategorien):
    with spalten[i]:
        st.markdown(f"<div style='font-size:16px;height:40px'><b>{kat}</b></div>", unsafe_allow_html=True)
        for p in punkte_liste:
            frage_id = f"{kat}_{p}"
            status = st.session_state["beantwortet"].get(frage_id)
            label = f"{p} Punkte"

            if status == "richtig":
                st.button(f"~~{label}~~ ✔️", key=frage_id, disabled=True)
            elif status == "falsch":
                st.button(f"~~{label}~~ ❌", key=frage_id, disabled=True)
            else:
                if st.button(label, key=frage_id):
                    st.session_state["ausgewählte_frage"] = (kat, p)

# --- Frageanzeige mit Antwortauswertung & Zurück-Option ---
if st.session_state["ausgewählte_frage"]:
    kategorie, punkte = st.session_state["ausgewählte_frage"]
    frage_daten = fragen.get((kategorie, punkte))

    if frage_daten:
        st.markdown("---")
        st.subheader(f"📝 Frage aus {kategorie} – {punkte} Punkte")
        auswahl = st.radio(frage_daten["frage"], frage_daten["antworten"], key=f"radio_{kategorie}_{punkte}")

        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("✅ Antwort bestätigen", key=f"bestätigen_{kategorie}_{punkte}"):
                index = frage_daten["antworten"].index(auswahl)
                frage_id = f"{kategorie}_{punkte}"
                gruppe = st.session_state["aktive_gruppe"]

                if index == frage_daten["richtig"]:
                    st.success("Richtig!")
                    st.session_state["beantwortet"][frage_id] = "richtig"
                    if gruppe == "A":
                        st.session_state["punkte_A"] += punkte
                    else:
                        st.session_state["punkte_B"] += punkte
                else:
                    st.error("Leider falsch.")
                    st.session_state["beantwortet"][frage_id] = "falsch"

                # Automatischer Gruppenwechsel
                st.session_state["aktive_gruppe"] = "B" if gruppe == "A" else "A"
                st.session_state["ausgewählte_frage"] = None

        with col2:
            if st.button("↩️ Zurück", key=f"zurueck_{kategorie}_{punkte}"):
                st.session_state["ausgewählte_frage"] = None
