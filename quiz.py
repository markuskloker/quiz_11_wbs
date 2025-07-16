import streamlit as st

# --- Session-State initialisieren ---
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

# --- Reset-Funktion ---
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

# --- Fragenstruktur (4×4 + Erklärung) ---
fragen = {
    ("Wirtschaftssysteme", 20): {
        "frage": "Was ist ein typisches Merkmal der freien Marktwirtschaft?",
        "antworten": ["Staatliche Preiskontrolle", "Angebot und Nachfrage", "Zentraler Wirtschaftsplan", "Subventionierung aller Branchen"],
        "richtig": 1,
        "erklärung": "In einer freien Marktwirtschaft regeln Angebot und Nachfrage den Preis, nicht der Staat."
    },
    ("Wirtschaftssysteme", 40): {
        "frage": "Was unterscheidet die soziale von der freien Marktwirtschaft?",
        "antworten": ["Privatbesitz ist verboten", "Der Staat gleicht soziale Unterschiede aus", "Der Staat plant die Produktion", "Es gibt keinen Wettbewerb"],
        "richtig": 1,
        "erklärung": "Die soziale Marktwirtschaft ergänzt die freie durch sozialen Ausgleich, z. B. durch Sozialleistungen."
    },
    ("Wirtschaftssysteme", 60): {
        "frage": "Was umfasst das magische Viereck?",
        "antworten": ["Vier Wirtschaftszentren", "Vier Ministerien", "Vollbeschäftigung, Preisstabilität, Wachstum, Außenwirtschaftliches Gleichgewicht", "Subvention, Steuern, Schulden, Rente"],
        "richtig": 2,
        "erklärung": "Diese vier Ziele gelten als gleichrangige Hauptziele der Wirtschaftspolitik."
    },
    ("Wirtschaftssysteme", 80): {
        "frage": "Wie wirken sich Subventionen auf den Wettbewerb aus?",
        "antworten": ["Sie steigern Konkurrenz", "Sie fördern gezielt bestimmte Marktteilnehmer", "Sie unterdrücken Innovation", "Sie senken die Steuerlast"],
        "richtig": 1,
        "erklärung": "Subventionen unterstützen gezielt Unternehmen oder Branchen und können Marktungleichgewichte erzeugen."
    },
    ("Arbeitswelt", 20): {
        "frage": "Was bedeutet „duale Ausbildung“?",
        "antworten": ["Nur Berufsschule", "Nur Betrieb", "Kombination von Schule und Betrieb", "Selbststudium mit Zertifikat"],
        "richtig": 2,
        "erklärung": "Das duale System kombiniert praktisches Lernen im Betrieb mit Theorie in der Berufsschule."
    },
    ("Arbeitswelt", 40): {
        "frage": "Was ist ein Berichtsheft?",
        "antworten": ["Gehaltsbescheinigung", "Ausbildungsnachweis", "Krankmeldung", "Arbeitsvertrag"],
        "richtig": 1,
        "erklärung": "Das Berichtsheft dokumentiert regelmäßig die Inhalte der Ausbildung für den Ausbildungsbetrieb."
    },
    ("Arbeitswelt", 60): {
        "frage": "Was regelt das Berufsbildungsgesetz?",
        "antworten": ["Steuern und Abgaben", "Tarifverträge", "Pflichten und Rechte in der Ausbildung", "Beförderungsregeln im Unternehmen"],
        "richtig": 2,
        "erklärung": "Das BBiG ist die zentrale rechtliche Grundlage für die Berufsausbildung in Deutschland."
    },
    ("Arbeitswelt", 80): {
        "frage": "Welche Konsequenzen drohen bei Verstoß gegen Ausbildungspflichten?",
        "antworten": ["Nichts", "Kündigung durch Berufsschule", "Bußgeld und Entzug der Ausbildungsbefugnis", "Rentenstreichung"],
        "richtig": 2,
        "erklärung": "Gesetzlich kann ein Ausbilder bei Pflichtverletzung sanktioniert und Lizenz entzogen werden."
    },
    ("Berufsorientierung", 20): {
        "frage": "Was gehört in eine vollständige Bewerbung?",
        "antworten": ["Steuer-ID", "Lebenslauf & Anschreiben", "Mietvertrag", "Zeugnisse der Geschwister"],
        "richtig": 1,
        "erklärung": "Die klassischen Bestandteile sind Anschreiben, Lebenslauf und relevante Zeugnisse."
    },
    ("Berufsorientierung", 40): {
        "frage": "Was ist das Ziel eines Assessment-Centers?",
        "antworten": ["Firmenvorstellung", "Stärken & Schwächen der Bewerber erkennen", "Gehaltsverhandlung", "Mitarbeiterfotos machen"],
        "richtig": 1,
        "erklärung": "In Assessment-Centern werden Kompetenzen wie Kommunikation oder Problemlösen geprüft."
    },
    ("Berufsorientierung", 60): {
        "frage": "Was versteht man unter Soft Skills?",
        "antworten": ["Excel-Kenntnisse", "Technische Fähigkeiten", "Zwischenmenschliche Kompetenzen", "Logikaufgaben lösen"],
        "richtig": 2,
        "erklärung": "Soft Skills umfassen soziale und persönliche Fähigkeiten wie Teamwork und Empathie."
    },
    ("Berufsorientierung", 80): {
        "frage": "Wie sollte man mit eigenen Schwächen im Bewerbungsgespräch umgehen?",
        "antworten": ["Verheimlichen", "Ehrlich benennen und Lösung beschreiben", "Lustig machen", "Ignorieren"],
        "richtig": 1,
        "erklärung": "Selbstreflexion und Lösungsansätze zeigen Professionalität und Lernbereitschaft."
    },
    ("Verbraucherverhalten", 20): {
        "frage": "Was ist nachhaltiger Konsum?",
        "antworten": ["Unüberlegtes Kaufen", "Ökologisch und sozial verantwortliches Einkaufen", "Luxuskäufe", "Rabatt-Shopping"],
        "richtig": 1,
        "erklärung": "Ziel ist eine bewusste Entscheidung zugunsten der Umwelt und fairer Produktion."
    },
    ("Verbraucherverhalten", 40): {
        "frage": "Was bedeutet Fair Trade?",
        "antworten": ["Nur Bio-Produkte", "Handel zu fairen Bedingungen für Produzenten", "Billige Produktion", "Qualitätslabel für Maschinen"],
        "richtig": 1,
        "erklärung": "Fair Trade unterstützt Produzenten mit Mindestpreisen und sozialen Standards."
    },
    ("Verbraucherverhalten", 60): {
        "frage": "Wie wirkt Werbung auf Konsumenten?",
        "antworten": ["Informativ und rational", "Manipulativ über Emotionen", "Nicht relevant", "Verboten beim Online-Kauf"],
        "richtig": 1,
        "erklärung": "Werbung spricht oft unbewusste Bedürfnisse an und beeinflusst das Kaufverhalten."
    },
    ("Verbraucherverhalten", 80): {
        "frage": "Was bezeichnet der ökologische Fußabdruck?",
        "antworten": ["CO₂-Ausstoß und Ressourcenverbrauch einer Person", "Schuhgröße", "Einkaufsbudget", "Steuerklasse"],
        "richtig": 0,
        "erklärung": "Er misst, wie viel Umwelt durch individuellen Lebensstil belastet wird."
    },
}

# --- Spaltenlayout ---
spalten = st.columns([2, 2, 2, 2])
kategorien = ["Wirtschaftssysteme", "Arbeitswelt", "Berufsorientierung", "Verbraucherverhalten"]

for i, kat in enumerate(kategorien):
    with spalten[i]:
        st.markdown(f"<div style='font-size:16px;height:40px'><b>{kat}</b></div>", unsafe_allow_html=True)
                for p in [20, 40, 60, 80]:
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

# --- Frageanzeige ---
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
                    st.success("Richtig! 🎉")
                    st.session_state["beantwortet"][frage_id] = "richtig"
                    if gruppe == "A":
                        st.session_state["punkte_A"] += punkte
                    else:
                        st.session_state["punkte_B"] += punkte
                else:
                    st.error("Leider falsch.")
                    st.session_state["beantwortet"][frage_id] = "falsch"

                # ✅ Erklärung anzeigen
                richtige_antwort = frage_daten["antworten"][frage_daten["richtig"]]
                erklärung = frage_daten.get("erklärung", "")
                st.info(f"👉 Richtige Antwort: **{richtige_antwort}**\n\n📚 **Warum?** {erklärung}")

                # 🔄 Gruppenwechsel
                st.session_state["aktive_gruppe"] = "B" if gruppe == "A" else "A"
                st.session_state["ausgewählte_frage"] = None

        with col2:
            if st.button("↩️ Zurück", key=f"zurueck_{kategorie}_{punkte}"):
                st.session_state["ausgewählte_frage"] = None
