import streamlit as st

# --- Quizdaten ---
fragen = {
    ("Wirtschaftssysteme", 20): { "frage": "...", "antworten": [...], "richtig": 2 },
    # 👉 Füge hier wie zuvor alle weiteren Fragen ein
    # Du kannst den vorherigen Block wiederverwenden
}

# --- Session-State initialisieren ---
if "beantwortet" not in st.session_state:
    st.session_state["beantwortet"] = {}

if "ausgewählte_frage" not in st.session_state:
    st.session_state["ausgewählte_frage"] = None

# --- Titel ---
st.title("📘 WBS Quiz – Klasse 11 (BW)")

# --- Kategorien und Punktwerte ---
kategorien = ["Wirtschaftssysteme", "Arbeitswelt", "Berufsorientierung", "Verbraucherverhalten"]
punkte_liste = [20, 40, 60, 80]

# --- Breite Spalten: Je 1/4 des Bildschirms (aber doppelt breit durch weniger Spalten)
# Nutze 2 Spalten – jede zeigt 2 Kategorien nebeneinander
abschnitte = [kategorien[:2], kategorien[2:]]

for abschnitt in abschnitte:
    spalten = st.columns([2, 2])  # Doppelte Breite pro Spalte
    for i, kat in enumerate(abschnitt):
        with spalten[i]:
            st.subheader(kat)
            for p in punkte_liste:
                frage_id = f"{kat}_{p}"
                status = st.session_state["beantwortet"].get(frage_id, None)

                if status == "richtig":
                    st.button(f"~~{p} Punkte~~ ✔️", key=frage_id, disabled=True)
                elif status == "falsch":
                    st.button(f"~~{p} Punkte~~ ❌", key=frage_id, disabled=True)
                else:
                    if st.button(f"{p} Punkte", key=frage_id):
                        st.session_state["ausgewählte_frage"] = (kat, p)

# --- Wenn Frage ausgewählt ist ---
if st.session_state["ausgewählte_frage"]:
    kategorie, punkte = st.session_state["ausgewählte_frage"]
    frage_daten = fragen.get((kategorie, punkte))

    if frage_daten:
        st.markdown("---")
        st.subheader(f"📝 Frage aus {kategorie} – {punkte} Punkte")
        auswahl = st.radio(frage_daten["frage"], frage_daten["antworten"], key=f"radio_{kategorie}_{punkte}")
        if st.button("Antwort bestätigen", key=f"bestätigen_{kategorie}_{punkte}"):
            index = frage_daten["antworten"].index(auswahl)
            frage_id = f"{kategorie}_{punkte}"
            if index == frage_daten["richtig"]:
                st.success("✅ Richtig! Weiter so! 🎉")
                st.session_state["beantwortet"][frage_id] = "richtig"
            else:
                st.error("❌ Leider falsch. Übung macht den Meister.")
                st.session_state["beantwortet"][frage_id] = "falsch"
            st.session_state["ausgewählte_frage"] = None
