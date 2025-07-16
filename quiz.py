import streamlit as st

# 📚 Quiz-Daten
quiz_data = {
    "Wirtschaft": [
        {"score": 20, "question": "Was versteht man unter dem Begriff 'Bruttoinlandsprodukt' (BIP)?", "options": ["Die Summe aller in einem Land produzierten Waren und Dienstleistungen in einem Jahr.", "Die Summe aller Exporte eines Landes.", "Die Differenz zwischen Importen und Exporten eines Landes.", "Die Gesamtausgaben eines Staates für Bildung und Infrastruktur."], "answer": 0},
        {"score": 40, "question": "Was ist der Unterschied zwischen Brutto- und Nettogehalt?", "options": ["Das Nettogehalt ist das Gehalt vor Abzug von Steuern und Sozialabgaben.", "Das Bruttogehalt ist das Gehalt nach Abzug von Steuern und Sozialabgaben.", "Das Nettogehalt ist das Gehalt nach Abzug von Steuern und Sozialabgaben.", "Es gibt keinen Unterschied zwischen Brutto- und Nettogehalt."], "answer": 2},
        {"score": 60, "question": "Was bedeutet der Begriff 'Inflation'?", "options": ["Ein Rückgang des allgemeinen Preisniveaus.", "Ein Anstieg des allgemeinen Preisniveaus über einen längeren Zeitraum.", "Ein plötzlicher Anstieg der Arbeitslosigkeit.", "Ein Rückgang der Exporte eines Landes."], "answer": 1},
        {"score": 80, "question": "Was ist der Zweck der Europäischen Zentralbank (EZB)?", "options": ["Die Regulierung der Steuern in der Europäischen Union.", "Die Kontrolle der Geldpolitik und Sicherung der Preisstabilität in der Eurozone.", "Die Verwaltung der Haushalte der Mitgliedsstaaten der EU.", "Die Förderung des internationalen Handels außerhalb der EU."], "answer": 1}
    ],
    "Recht": [
        {"score": 20, "question": "Was versteht man unter dem Begriff 'Rechtsfähigkeit'?", "options": ["Die Fähigkeit, vor Gericht zu sprechen.", "Die Fähigkeit, Rechte und Pflichten zu haben.", "Die Fähigkeit, Verträge abzuschließen.", "Die Fähigkeit, ein Unternehmen zu gründen."], "answer": 1},
        {"score": 40, "question": "Was ist ein 'Kaufvertrag'?", "options": ["Ein Vertrag, bei dem eine Partei eine Dienstleistung erbringt.", "Ein Vertrag, bei dem eine Partei eine Ware kauft und die andere Partei diese liefert.", "Ein Vertrag, der nur mündlich abgeschlossen werden kann.", "Ein Vertrag, der nur zwischen Unternehmen gültig ist."], "answer": 1},
        {"score": 60, "question": "Was ist der Unterschied zwischen 'Eigentum' und 'Besitz'?", "options": ["Eigentum ist das Recht an einer Sache, Besitz ist die tatsächliche Herrschaft über eine Sache.", "Besitz ist das Recht an einer Sache, Eigentum ist die tatsächliche Herrschaft über eine Sache.", "Es gibt keinen Unterschied zwischen Eigentum und Besitz.", "Eigentum bezieht sich nur auf Immobilien, Besitz auf bewegliche Sachen."], "answer": 0},
        {"score": 80, "question": "Was ist eine 'juristische Person'?", "options": ["Eine natürliche Person, die Jura studiert hat.", "Eine Organisation oder ein Unternehmen, das rechtlich wie eine Person behandelt wird.", "Eine Person, die vor Gericht steht.", "Eine Person, die ein Unternehmen gegründet hat."], "answer": 1}
    ],
    "Globalisierung": [
        {"score": 20, "question": "Was versteht man unter 'Globalisierung'?", "options": ["Die zunehmende Vernetzung der Welt in den Bereichen Wirtschaft, Politik, Kultur und Umwelt.", "Die Abschottung von Ländern durch Handelsbarrieren.", "Die Einführung einer einheitlichen Währung weltweit.", "Die Förderung von regionalen Produkten und Dienstleistungen."], "answer": 0},
        {"score": 40, "question": "Was ist ein 'multinationales Unternehmen'?", "options": ["Ein Unternehmen, das nur in einem Land tätig ist.", "Ein Unternehmen, das in mehreren Ländern tätig ist.", "Ein Unternehmen, das nur Produkte aus dem Ausland verkauft.", "Ein Unternehmen, das ausschließlich staatlich finanziert wird."], "answer": 1},
        {"score": 60, "question": "Was ist der Zweck der Welthandelsorganisation (WTO)?", "options": ["Die Förderung des internationalen Handels und die Regelung von Handelsstreitigkeiten.", "Die Einführung einer einheitlichen Währung weltweit.", "Die Regulierung der Steuern in allen Ländern.", "Die Förderung von regionalen Produkten und Dienstleistungen."], "answer": 0},
        {"score": 80, "question": "Was bedeutet der Begriff 'Freihandelsabkommen'?", "options": ["Ein Abkommen, das den Handel zwischen Ländern erleichtert, indem Zölle und Handelsbarrieren reduziert werden.", "Ein Abkommen, das den Handel zwischen Ländern verbietet.", "Ein Abkommen, das nur den Export von Waren regelt.", "Ein Abkommen, das nur zwischen Unternehmen abgeschlossen wird."], "answer": 0}
    ],
    "Nachhaltigkeit": [
        {"score": 20, "question": "Was bedeutet 'Nachhaltigkeit'?", "options": ["Die Nutzung von Ressourcen, ohne die Bedürfnisse zukünftiger Generationen zu gefährden.", "Die Maximierung des wirtschaftlichen Wachstums.", "Die Förderung von fossilen Brennstoffen.", "Die Einführung von neuen Technologien."], "answer": 0},
        {"score": 40, "question": "Was ist das Ziel der Agenda 2030 der Vereinten Nationen?", "options": ["Die Förderung von fossilen Brennstoffen.", "Die Erreichung von 17 Zielen für nachhaltige Entwicklung (SDGs).", "Die Einführung einer einheitlichen Währung weltweit.", "Die Abschaffung aller Handelsbarrieren."], "answer": 1},
        {"score": 60, "question": "Was bedeutet der Begriff 'Kreislaufwirtschaft'?", "options": ["Ein Wirtschaftssystem, das auf der linearen Nutzung von Ressourcen basiert.", "Ein Wirtschaftssystem, das Ressourcen wiederverwendet und Abfall minimiert.", "Ein Wirtschaftssystem, das nur auf fossilen Brennstoffen basiert.", "Ein Wirtschaftssystem, das ausschließlich auf Exporten basiert."], "answer": 1}
    ]
}

st.set_page_config(page_title="WBS Quiz", layout="wide")
st.title("📊 Quiz – WBS Klasse 11")

# 🧮 Matrix-Ansicht
col1, col2, col3, col4 = st.columns(len(quiz_data))

for col, category in zip([col1, col2, col3, col4], quiz_data.keys()):
    with col:
        st.subheader(category)
        for item in quiz_data[category]:
            if st.button(f"{item['score']} Punkte", key=f"{category}_{item['score']}"):
                st.session_state["selected_question"] = item

# 💡 Frage anzeigen
if "selected_question" in st.session_state:
    q = st.session_state["selected_question"]
    st.markdown(f"### ❓ {q['question']}")
    selected_option = st.radio("Antwortmöglichkeiten:", q["options"], index=None)
    if selected_option is not None:
        if q["options"].index(selected_option) == q["answer"]:
            st.success("✅ Richtig!")
        else:
            st.error("❌ Leider falsch.")
