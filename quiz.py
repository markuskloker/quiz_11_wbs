import streamlit as st

# 📚 Quiz-Daten
quiz_data = {
    "Wirtschaft": [
        {"score": 20, "question": "Was versteht man unter dem Begriff 'Bruttoinlandsprodukt' (BIP)?", "options": [...], "answer": 0},
        {"score": 40, "question": "Was ist der Unterschied zwischen Brutto- und Nettogehalt?", "options": [...], "answer": 2},
        {"score": 60, "question": "Was bedeutet der Begriff 'Inflation'?", "options": [...], "answer": 1},
        {"score": 80, "question": "Was ist der Zweck der Europäischen Zentralbank (EZB)?", "options": [...], "answer": 1}
    ],
    "Recht": [
        {"score": 20, "question": "Was versteht man unter dem Begriff 'Rechtsfähigkeit'?", "options": [...], "answer": 1},
        {"score": 40, "question": "Was ist ein 'Kaufvertrag'?", "options": [...], "answer": 1},
        {"score": 60, "question": "Was ist der Unterschied zwischen 'Eigentum' und 'Besitz'?", "options": [...], "answer": 0},
        {"score": 80, "question": "Was ist eine 'juristische Person'?", "options": [...], "answer": 1}
    ],
    "Globalisierung": [
        {"score": 20, "question": "Was versteht man unter 'Globalisierung'?", "options": [...], "answer": 0},
        {"score": 40, "question": "Was ist ein 'multinationales Unternehmen'?", "options": [...], "answer": 1},
        {"score": 60, "question": "Was ist der Zweck der Welthandelsorganisation (WTO)?", "options": [...], "answer": 0},
        {"score": 80, "question": "Was bedeutet der Begriff 'Freihandelsabkommen'?", "options": [...], "answer": 0}
    ],
    "Nachhaltigkeit": [
        {"score": 20, "question": "Was bedeutet 'Nachhaltigkeit'?", "options": [...], "answer": 0},
        {"score": 40, "question": "Was ist das Ziel der Agenda 2030 der Vereinten Nationen?", "options": [...], "answer": 1},
        {"score": 60, "question": "Was bedeutet der Begriff 'Kreislaufwirtschaft'?", "options": [...], "answer": 1},
        {"score": 80, "question": "Was versteht man unter 'ökologischem Fußabdruck'?", "options": [...], "answer": 0}
    ]
}

st.set_page_config(page_title="WBS Quiz", layout="wide")
st.title("📊 Quiz – WBS Klasse 11")

if "answered" not in st.session_state:
    st.session_state.answered = set()
if "selected_question" not in st.session_state:
    st.session_state.selected_question = None

# 🧮 Matrix-Ansicht
cols = st.columns(len(quiz_data))
for col, category in zip(cols, quiz_data.keys()):
    with col:
        st.subheader(category)
        for item in quiz_data[category]:
            key = f"{category}_{item['score']}"
            label = f"~~{item['score']} Punkte~~" if key in st.session_state.answered else f"{item['score']} Punkte"
            if st.button(label, key=key):
                if key not in st.session_state.answered:
                    st.session_state.selected_question = (key, item)

# 💡 Frage anzeigen
if st.session_state.selected_question:
    key, q = st.session_state.selected_question
    st.markdown(f"### ❓ {q['question']}")
    selected = st.radio("Antwortmöglichkeiten:", q["options"], index=None)
    if selected is not None:
        if q["options"].index(selected) == q["answer"]:
            st.success("✅ Richtig!")
        else:
            st.error("❌ Leider falsch.")
        st.session_state.answered.add(key)
        st.session_state.selected_question = None
        st.rerun()
