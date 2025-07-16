import streamlit as st

from PIL import Image

# Logo laden und oben rechts anzeigen
logo = Image.open("logo.png")
st.markdown(
    """
    <div style='display: flex; justify-content: flex-end;'>
        <img src='data:image/png;base64,{0}' width='150'/>
    </div>
    """.format(st.image(logo, output_format="PNG").getvalue().decode("latin1")),
    unsafe_allow_html=True
)

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
    st.session_state["beantwortet"] = {}
    st.session_state["ausgewählte_frage"] = None
    st.session_state["punkte_A"] = 0
    st.session_state["punkte_B"] = 0
    st.session_state["aktive_gruppe"] = "A"
    st.session_state["antwortende_gruppen"] = {}

# --- Punktestand ---
st.markdown("### 🎯 Punktestand")
st.write(f"**Gruppe A**: {st.session_state['punkte_A']} Punkte")
st.write(f"**Gruppe B**: {st.session_state['punkte_B']} Punkte")
st.write(f"👥 Aktive Gruppe: **Gruppe {st.session_state['aktive_gruppe']}**")

# --- Fragen mit ausführlichen Erklärungen ---
fragen = {
    ("Soziale Marktwirtschaft", 20): {
        "frage": "Welche Rolle spielt der Staat in der sozialen Marktwirtschaft?",
        "antworten": ["Er greift nicht ein.", "Er plant zentral.", "Er sorgt für Ausgleich und reguliert Wettbewerb.", "Er kontrolliert alle Unternehmen."],
        "richtig": 2,
        "erklärung": "Der Staat sichert sozialen Ausgleich durch Maßnahmen wie Sozialversicherung und Mindestlohn. Gleichzeitig schützt er den Wettbewerb vor Monopolen. Er greift gezielt ein, ohne die Grundprinzipien der Marktwirtschaft aufzugeben."
    },
    ("Soziale Marktwirtschaft", 40): {
        "frage": "Was versteht man unter 'Ordnungspolitik'?",
        "antworten": ["Preisbindung", "Staatliche Rahmengestaltung", "Produktionssteuerung", "Wettbewerbsabschaffung"],
        "richtig": 1,
        "erklärung": "Ordnungspolitik bezeichnet die staatliche Festlegung von Regeln, die die Wirtschaft strukturieren. Sie sorgt für Wettbewerbsschutz, Vertragssicherheit und Konsumentenschutz, ohne direkt ins Marktgeschehen einzugreifen."
    },
    ("Soziale Marktwirtschaft", 60): {
        "frage": "Welche Maßnahme gehört NICHT zur sozialen Marktwirtschaft?",
        "antworten": ["Subventionen", "Mindestlöhne", "Zentrale Planung", "Sozialversicherungen"],
        "richtig": 2,
        "erklärung": "Zentrale Planung bedeutet, dass der Staat vorgibt, was produziert wird — das ist typisch für Planwirtschaft. In der sozialen Marktwirtschaft agieren Unternehmen weitgehend frei, gesteuert durch Marktmechanismen."
    },
    ("Soziale Marktwirtschaft", 80): {
        "frage": "Was ist ein Ziel der sozialen Marktwirtschaft?",
        "antworten": ["Wettbewerb abschaffen", "Monopole fördern", "Freiheit und soziale Sicherheit verbinden", "Planwirtschaft einführen"],
        "richtig": 2,
        "erklärung": "Die soziale Marktwirtschaft verbindet ökonomische Effizienz mit sozialer Gerechtigkeit. Sie will Wohlstand schaffen, dabei aber auch soziale Ungleichheit abmildern."
    },
    ("Wirtschaftswachstum", 20): {
        "frage": "Welche Kennzahl misst das Wirtschaftswachstum?",
        "antworten": ["Inflation", "BIP", "Arbeitslosenquote", "Außenhandel"],
        "richtig": 1,
        "erklärung": "Das Bruttoinlandsprodukt (BIP) beschreibt den Gesamtwert aller in einem Jahr produzierten Waren und Dienstleistungen. Ein steigendes BIP gilt als Indikator für wirtschaftliches Wachstum."
    },
    ("Wirtschaftswachstum", 40): {
        "frage": "Was ist qualitatives Wachstum?",
        "antworten": ["Produktionssteigerung", "Nachhaltiges Wachstum", "Subventioniertes Wachstum", "Industriewachstum"],
        "richtig": 1,
        "erklärung": "Qualitatives Wachstum bedeutet, dass nicht nur mehr produziert wird, sondern auch nachhaltiger. Es berücksichtigt Umweltschutz, soziale Standards und langfristige Stabilität."
    },
    ("Wirtschaftswachstum", 60): {
        "frage": "Was beschreibt ein Problem des Wirtschaftswachstums?",
        "antworten": ["Mehr Arbeitslosigkeit", "Umweltzerstörung und Ressourcenverbrauch", "Branchenübergreifende Gleichverteilung", "Innovationsverlust"],
        "richtig": 1,
        "erklärung": "Wachstum kann zu Umweltbelastungen führen, da Ressourcen ausgebeutet und Emissionen erhöht werden. Ohne Rücksicht auf Nachhaltigkeit gefährdet es künftige Generationen."
    },
    ("Wirtschaftswachstum", 80): {
        "frage": "Was ist ein Merkmal von nachhaltigem Wirtschaftswachstum?",
        "antworten": ["Ressourcenverschwendung", "Soziale und ökologische Verantwortung", "Konsummaximierung", "Verzicht auf Zukunftsperspektive"],
        "richtig": 1,
        "erklärung": "Nachhaltiges Wachstum achtet auf die Begrenztheit natürlicher Ressourcen und die sozialen Auswirkungen wirtschaftlichen Handelns. Es fördert Lebensqualität statt bloße Mengenproduktion."
    },
    ("Konjunktur", 20): {
        "frage": "Welche Phase gehört NICHT zum Konjunkturzyklus?",
        "antworten": ["Aufschwung", "Boom", "Deflation", "Rezession"],
        "richtig": 2,
        "erklärung": "Deflation beschreibt Preisverfall, ist jedoch keine Konjunkturphase. Ein Konjunkturzyklus umfasst Aufschwung, Boom, Abschwung und Rezession."
    },
    ("Konjunktur", 40): {
        "frage": "Was passiert in der Boom-Phase?",
        "antworten": ["Hohe Arbeitslosigkeit", "Sinkende Nachfrage", "Überhitzung & Preissteigerungen", "Investitionsrückgang"],
        "richtig": 2,
        "erklärung": "In der Boom-Phase ist die Wirtschaft stark ausgelastet. Nachfrage und Produktion steigen — oft schneller als nachhaltig möglich, was zu Preissteigerungen führt."
    },
    ("Konjunktur", 60): {
        "frage": "Maßnahme gegen Rezession?",
        "antworten": ["Steuern erhöhen", "Ausgaben senken", "In Infrastruktur investieren", "Zinsen erhöhen"],
        "richtig": 2,
        "erklärung": "Der Staat kann durch öffentliche Investitionen Arbeitsplätze schaffen und die Nachfrage stärken. Das hilft, die Wirtschaft aus der Rezession zu holen."
    },
    ("Konjunktur", 80): {
        "frage": "Was bedeutet antizyklische Fiskalpolitik?",
        "antworten": ["Zölle einführen", "Steuern in Rezession erhöhen", "Staatsausgaben gegen Konjunkturverlauf steuern", "Konsum reduzieren"],
        "richtig": 2,
        "erklärung": "Antizyklische Fiskalpolitik bedeutet: In Rezessionen steigen Staatsausgaben, in Booms sinken sie. So gleicht der Staat konjunkturelle Schwankungen aus."
    },
    ("Europäische Wirtschaftsunion", 20): {
        "frage": "Was ist das Ziel der EWWU?",
        "antworten": ["Zölle einführen", "Freier Handel & gemeinsame Währung", "Wettbewerb abschaffen", "Zentralplan für Europa"],
        "richtig": 1,
        "erklärung": "Die EWWU fördert wirtschaftliche Integration durch freien Handel und den Euro. Dadurch sollen Stabilität und Wohlstand in Europa steigen."
    },
    ("Europäische Wirtschaftsunion", 40): {
        "frage": "Welche Institution steuert die Geldpolitik der EU?",
        "antworten": ["EU-Kommission", "EuGH", "EZB", "Europäischer Rat"],
        "richtig": 2,
        "erklärung": "Die Europäische Zentralbank (EZB) ist für die Geldpolitik verantwortlich. Sie steuert den Leitzins und kontrolliert die Geldmenge, um Preisstabilität im Euroraum zu gewährleisten."
    },
    ("Europäische Wirtschaftsunion", 60): {
        "frage": "Welche Voraussetzung gilt für den Euro-Beitritt?",
        "antworten": ["NATO-Mitgliedschaft", "Exportüberschuss", "Stabiles Preisniveau und geringe Staatsverschuldung", "Bevölkerung über 10 Mio."],
        "richtig": 2,
        "erklärung": "Staaten müssen die sogenannten Konvergenzkriterien erfüllen: Inflation, Staatsverschuldung und Haushaltsdefizit müssen innerhalb bestimmter Grenzen liegen. Ziel ist ein stabiler und verlässlicher Euro-Raum."
    },
    ("Europäische Wirtschaftsunion", 80): {
        "frage": "Was ist ein Vorteil des Euro?",
        "antworten": ["Mehr Wechselkursrisiken", "Erleichterung des Handels", "Nationale Geldpolitik", "Weniger Integration"],
        "richtig": 1,
        "erklärung": "Eine gemeinsame Währung macht grenzüberschreitenden Handel einfacher, da keine Währungsumrechnung nötig ist. Das stärkt den Binnenmarkt und spart Kosten im internationalen Geschäft."
    },
}

# --- Frage-Button-Anzeige mit fixierter Struktur ---
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

            button_text = f"{label} {icon} {group_label}".strip()
            container = st.empty()

            if status:
                container.markdown(
                    f"<div style='height:48px; border:1px solid #ccc; border-radius:6px; display:flex; align-items:center; justify-content:center; font-size:14px; background-color:#f9f9f9'>{button_text}</div>",
                    unsafe_allow_html=True
                )
            else:
                if container.button(label, key=frage_id):
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
                    st.success("✅ Richtig!")
                    st.session_state["beantwortet"][frage_id] = "richtig"
                    if gruppe == "A":
                        st.session_state["punkte_A"] += punkte
                    else:
                        st.session_state["punkte_B"] += punkte
                else:
                    st.error("❌ Leider falsch.")
                    st.session_state["beantwortet"][frage_id] = "falsch"

                st.session_state["antwortende_gruppen"][frage_id] = gruppe

                # 📚 Erklärung anzeigen
                richtige_antwort = frage_daten["antworten"][frage_daten["richtig"]]
                erklärung = frage_daten.get("erklärung", "")
                st.info(f"👉 Richtige Antwort: **{richtige_antwort}**\n\n📚 **Erklärung:** {erklärung}")

                # 🔁 Gruppenwechsel
                st.session_state["aktive_gruppe"] = "B" if gruppe == "A" else "A"
                st.session_state["ausgewählte_frage"] = None

        with col2:
            if st.button("↩️ Zurück", key=f"zurueck_{kategorie}_{punkte}"):
                st.session_state["ausgewählte_frage"] = None
