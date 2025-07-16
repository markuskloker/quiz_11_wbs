import streamlit as st

# --- Quizdaten ---
fragen = {
    ("Wirtschaftssysteme", 20): {
        "frage": "Was kennzeichnet die soziale Marktwirtschaft?",
        "antworten": ["Planwirtschaft", "Freie Marktwirtschaft", "Staatliche Eingriffe", "Subsistenzwirtschaft"],
        "richtig": 2
    },
    ("Wirtschaftssysteme", 40): {
        "frage": "Wer gilt als Begründer der sozialen Marktwirtschaft?",
        "antworten": ["Adam Smith", "Karl Marx", "Ludwig Erhard", "John Keynes"],
        "richtig": 2
    },
    # 👉 Weitere Fragen entsprechend ergänzen – jede mit genau 4 Antwortmöglichkeiten
    # Tipp: Du kannst Fragen aus meinem vorherigen Code übernehmen
}

# --- Session-State vorbereiten ---
if "beantwortet" not in st.session_state:
    st.session_state["beantwortet"] = {}

if "ausgewählte_frage" not in st.session_state:
    st.session_state["ausgewählte_frage"] = None

# --- Layout starten ---
st.title("📚 WBS Quiz – 11. Klasse (BW)")
st.markdown("🔢 Wähle eine Frage aus jeder Kategorie anhand der Punkte:")

# --- Kategorien & Punkte ---
kategorien = ["Wirtschaftssysteme", "Arbeitswelt", "Berufsorientierung", "Verbraucherverhalten"]
punkte_liste = [20, 40, 60, 80]
spalten = st.columns(4)

for i, kat in enumerate(kategorien):
    with spalten[i]:
        st.subheader(kat)
        for p in punkte_liste:
            frage_id = f"{kat}_{p}"
            status = st.session_state["beantwortet"].get(frage_id, None)
            label = f"{p} Punkte"

            if status == "richtig":
                st.button(f"~~{label}~~ ✔️", key=frage_id, disabled=True)
            elif status == "falsch":
                st.button(f"~~{label}~~ ❌", key=frage_id, disabled=True)
            else:
                if st.button(label, key=frage_id):
                    st.session_state["ausgewählte_frage"] = (kat, p)

# --- Frageanzeige & Antwortlogik ---
if st.session_state["ausgewählte_frage"]:
    kategorie, punkte = st.session_state["ausgewählte_frage"]
    frage_daten = fragen.get((kategorie, punkte))

    if frage_daten and len(frage_daten["antworten"]) == 4:
        st.markdown("---")
        st.subheader(f"📝 Frage aus {kategorie} – {punkte} Punkte")
        auswahl = st.radio(frage_daten["frage"], frage_daten["antworten"], key=f"radio_{kategorie}_{punkte}")
        if st.button("Antwort bestätigen", key=f"bestätigen_{kategorie}_{punkte}"):
            index = frage_daten["antworten"].index(auswahl)
            frage_id = f"{kategorie}_{punkte}"
            if index == frage_daten["richtig"]:
                st.success("✅ Richtig beantwortet!")
                st.session_state["beantwortet"][frage_id] = "richtig"
            else:
                st.error("❌ Leider falsch.")
                st.session_state["beantwortet"][frage_id] = "falsch"
            st.session_state["ausgewählte_frage"] = None
    else:
        st.warning("⚠️ Frage fehlt oder hat nicht genau 4 Antwortmöglichkeiten.")
