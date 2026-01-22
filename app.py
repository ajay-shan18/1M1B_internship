import streamlit as st

st.set_page_config(
    page_title="Sustainable Living AI Assistant",
    page_icon="🌍",
    layout="centered"
)

st.title("🌱 Sustainable Living AI Assistant")
st.caption("An AI-powered awareness tool for responsible consumption and daily sustainability")

st.markdown(
    """
This assistant helps users understand **simple, practical actions** they can take to live more sustainably.
It is designed as an awareness and decision-support tool aligned with **SDG 12: Responsible Consumption and Production**.
"""
)

# Question bank
question_bank = {
    "Reducing plastic usage": [
        "How can I reduce plastic use in daily life?",
        "What are alternatives to plastic bags?",
        "How can I avoid single-use plastics?"
    ],
    "Waste management": [
        "How should I segregate waste at home?",
        "What is the correct way to dispose e-waste?",
        "How can I reduce waste generation?"
    ],
    "Energy conservation": [
        "How can students save electricity in hostels?",
        "What are energy-efficient habits?",
        "How can I make my room energy efficient?"
    ],
    "Water conservation": [
        "How can I save water daily?",
        "What are simple water-saving habits?",
        "Why is water conservation important?"
    ],
    "Climate & awareness": [
        "How does climate change affect daily life?",
        "How can I reduce my carbon footprint?",
        "What is responsible consumption?",
        "How can I encourage others to live sustainably?"
    ]
}

category = st.selectbox("Select a category", list(question_bank.keys()))
question = st.selectbox("Select a question", question_bank[category])

if question:
    st.divider()
    st.subheader("AI Sustainability Insight")

    response = f"""
**Question:** {question}

**Recommended Sustainable Actions**
- Choose reusable products instead of disposable ones
- Segregate waste into wet, dry, and electronic categories
- Switch off unused electrical appliances
- Conserve water by using only what is necessary
- Prefer eco-friendly transportation methods
- Support sustainable brands and local products
- Share awareness with peers and family

**Impact**
Following these actions helps reduce resource waste, lowers pollution, and supports a healthier environment for future generations.
"""

    st.markdown(response)

st.divider()
st.caption("Responsible AI: This assistant provides general sustainability guidance without collecting personal data.")
