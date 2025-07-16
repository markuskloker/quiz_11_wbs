import streamlit as st

# --- Session-State Initialisierung ---
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
if "antwortende_gruppen" not in st.session_state:
    st.session_state["antwortende_gruppen"] = {}

# --- Reset ---
if st.button("🔄 Quiz zurücksetzen"):
    st.session_state.clear()
    st.experimental_rerun()

# --- Punktestand ---
st.markdown("### 🎯 Punktestand")
st.write(f"**Gruppe A**: {st.session_state['punkte_A']} Punkte")
st.write(f"**Gruppe B**: {st.session_state['punkte_B']} Punkte")
st.write(f"👥 Aktive Gruppe: **Gruppe {st.session_state['aktive_gruppe']}**")

# --- Fragenstruktur ---
fragen = {
    ("Soziale Marktwirtschaft", 20): {
        "frage": "Welche Rolle spielt der Staat in der sozialen Marktwirtschaft?",
        "antworten": ["Er greift nicht ein.", "Er plant zentral.", "Er sorgt für Ausgleich und reguliert Wettbewerb.", "Er kontrolliert alle Unternehmen."],
        "richtig": 2,
        "erklärung": "Der Staat greift ein, um sozialen Ausgleich zu schaffen und Wettbewerb zu sichern."
    },
    ("Soziale Marktwirtschaft", 40): {
        "frage": "Was versteht man unter 'Ordnungspolitik'?",
        "antworten": ["Preisbindung", "Staatliche Rahmengestaltung", "Produktionssteuerung", "Wettbewerbsabschaffung"],
        "richtig": 1,
        "erklärung": "Ordnungspolitik schafft Wettbewerbsregeln für den Markt."
    },
    ("Soziale Marktwirtschaft", 60): {
        "frage": "Welche Maßnahme gehört NICHT zur sozialen Marktwirtschaft?",
        "antworten": ["Subventionen", "Mindestlöhne", "Zentrale Planung", "Sozialversicherungen"],
        "richtig": 2,
        "erklärung": "Zentrale Planung ist ein Merkmal der Planwirtschaft."
    },
    ("Soziale Marktwirtschaft", 80): {
        "frage": "Was ist ein Ziel der sozialen Marktwirtschaft?",
        "antworten": ["Wettbewerb abschaffen", "Monopole fördern", "Freiheit und soziale Sicherheit verbinden", "Planwirtschaft einführen"],
        "richtig": 2,
        "erklärung": "Sie verbindet Marktfreiheit mit sozialem Ausgleich."
    },
    ("Wirtschaftswachstum", 20): {
        "frage": "Welche Kennzahl misst das Wirtschaftswachstum?",
        "antworten": ["Inflation", "BIP", "Arbeitslosenquote", "Außenhandel"],
        "richtig": 1,
        "erklärung": "Das Bruttoinlandsprodukt zeigt die Wirtschaftsleistung eines Landes."
    },
    ("Wirtschaftswachstum", 40): {
        "frage": "Was ist qualitatives Wachstum?",
        "antworten": ["Produktionssteigerung", "Nachhaltiges Wachstum", "Subventioniertes Wachstum", "Industriewachstum"],
        "richtig": 1,
        "erklärung": "Qualitatives Wachstum setzt auf Nachhaltigkeit und Ressourcenschonung."
    },
    ("Wirtschaftswachstum", 60): {
        "frage": "Was beschreibt ein Problem des Wirtschaftswachstums?",
        "antworten": ["Mehr Arbeitslosigkeit", "Umweltzerstörung und Ressourcenverbrauch", "Branchenübergreifende Gleichverteilung", "Innovationsverlust"],
        "richtig": 1,
        "erklärung": "Wirtschaftswachstum kann die Umwelt stark belasten."
    },
    ("Wirtschaftswachstum", 80): {
        "frage": "Was ist ein Merkmal von nachhaltigem Wirtschaftswachstum?",
        "antworten": ["Ressourcenverschwendung", "Soziale und ökologische Verantwortung", "Konsummaximierung", "Verzicht auf Zukunftsperspektive"],
        "richtig": 1,
        "erklärung": "Nachhaltiges Wachstum bezieht auch zukünftige Generationen mit ein."
    },
    ("Konjunktur", 20): {
        "frage": "Welche Phase gehört NICHT zum Konjunkturzyklus?",
        "antworten": ["Aufschwung", "Boom", "Deflation", "Rezession"],
        "richtig": 2,
        "erklärung": "Deflation ist ein Preisphänomen, kein Konjunkturstadium."
    },
    ("Konjunktur", 40): {
        "frage": "Was passiert typischerweise in der Boom-Phase?",
        "antworten": ["Hohe Arbeitslosigkeit", "Sinkende Nachfrage", "Überhitzung & Preissteigerungen", "Investitionsrückgang"],
        "richtig": 2,
        "erklärung": "Im Boom steigen Nachfrage und Preise bei voller Kapazitätsauslastung."
    },
    ("Konjunktur", 60): {
        "frage": "Welche Maßnahme hilft gegen Rezession?",
        "antworten": ["Steuern erhöhen", "Ausgaben senken", "In Infrastruktur investieren", "Zinsen erhöhen"],
        "richtig": 2,
        "erklärung": "Investitionen erhöhen Nachfrage und schaffen Arbeitsplätze."
    },
    ("Konjunktur", 80): {
        "frage": "Was bedeutet antizyklische Fiskalpolitik?",
        "antworten": ["Zölle einführen", "Steuern in Rezession erhöhen", "Staatsausgaben gegen Konjunkturverlauf steuern", "Konsum reduzieren"],
        "richtig": 2,
        "erklärung": "Ausgaben werden antizyklisch angepasst, um Konjunktur zu stabilisieren."
    },
    ("Europäische Wirtschaftsunion", 20): {
        "frage": "Was ist das Ziel der EWWU?",
        "antworten": ["Zölle einführen", "Freier Handel & gemeinsame Währung", "Wettbewerb abschaffen", "Zentralplan für Europa"],
        "richtig": 1,
        "erklärung": "Die EWWU erleichtert Handel und stärkt Integration durch den Euro."
    },
    ("Europäische Wirtschaftsunion", 40): {
        "frage": "Welche Institution steuert die Geldpolitik der EU?",
        "antworten": ["EU-Kommission", "EuGH", "EZB", "Europäischer Rat"],
        "richtig": 2,
        "erklärung": "Die EZB ist zuständig für Preisstabilität und Geldpolitik."
    },
    ("Europäische Wirtschaftsunion", 60): {
        "frage": "Welche Voraussetzung gilt für den Euro-Beitritt?",
        "antworten": ["NATO-Mitglied", "Exportüberschuss", "Stabiles Preisniveau und geringe Staatsverschuldung", "Bevölkerung über 10 Mio."],
        "richtig": 2,
        "erklärung": "Die Konvergenzkriterien sichern finanzielle Stabilität."
    },
    ("Europäische Wirtschaftsunion", 80): {
        "frage": "Was ist ein Vorteil des Euro?",
        "antworten": ["Mehr Wechselkursrisiken", "Erleichterung des Handels", "Nationale Geldpolitik", "Weniger Integration"],
        "richtig": 1,
        "erklärung": "Der Euro ermöglicht reibungslosen Handel ohne Wechselkurskosten."
    },
}

# --- Spaltenlayout mit Fragenbuttons ---
punkte_liste = [20, 40, 60, 80]
kategorien = ["Soziale Marktwirtschaft", "Wirtschaftswachstum", "Konjunktur", "Europäische Wirtschaftsunion"]
spalten = st.columns([2, 2, 2, 2])

for i, kategorie in enumerate(kategorien):
    with spalten[i]:
        st.markdown(f"<div style='font-size:16px;height:40px'><b>{kategorie}</b></div><br>", unsafe_allow_html=True)

        for punkte in punkte_liste:
            frage_id = f"{kategorie}_{punkte}"
            status = st.session_state["beantwortet"].get(frage_id)
            gruppe = st.session_state["antwortende_gruppen"].get(frage_id)
            label = f"{punkte} Punkte"
            icon = ""
            group_label = ""

            if status == "richtig":
                icon = "✔️"
                group_label = f"(Gruppe {gruppe})"
            elif status == "falsch":
                icon = "❌"
                group_label = f"(Gruppe {gruppe})"

            if status in ["richtig", "falsch"]:
                st.button(f"~~{label}~~ {icon} {group_label}", key=frage_id, disabled=True)
            else:
                if st.button(label, key=frage_id):
                    st.session_state["ausgewählte_frage"] = (kategorie, punkte)

# --- Frageanzeige & Auswertung ---
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

                st.session_state["antwortende_gruppen"][frage_id] = gruppe

                # 📚 Erklärung anzeigen
                richtige_antwort = frage_daten["antworten"][frage_daten["richtig"]]
                erklärung = frage_daten.get("erklärung", "")
                st.info(f"👉 Richtige Antwort: **{richtige_antwort}**\n\n📚 **Warum?** {erklärung}")

                # 🔄 Gruppenwechsel
                st.session_state["aktive_gruppe"] = "B" if gruppe == "A" else "A"
                st.session_state["ausgewählte_frage"] = None

        with col2:
            if st.button("↩️ Zurück", key=f"zurueck_{kategorie}_{punkte}"):
                st.session_state["ausgewählte_frage"] = None
