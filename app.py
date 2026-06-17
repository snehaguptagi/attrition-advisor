"""
Attrition Risk Advisor — a Streamlit app on top of the analysis in
Attrition_Analysis.ipynb.

HR enters an employee's attributes (the same factors the notebook studied) and
Claude returns a risk read + the driving factors + concrete retention actions,
grounded in the findings from the analysis. This is an AI advisor — it reasons
from the study's patterns, not a black-box model served on private data.

Run:  pip install -r requirements.txt && streamlit run app.py
Needs an Anthropic API key (sidebar, or ANTHROPIC_API_KEY env var).
"""
import os
import streamlit as st
import anthropic

MODEL = "claude-sonnet-4-6"

# Key findings distilled from Attrition_Analysis.ipynb — used to ground the model.
ANALYSIS_FINDINGS = """
Findings from the underlying attrition study (use these as priors):
- Tenure is the strongest signal: attrition peaks in the FIRST YEAR; risk drops
  sharply with tenure. Senior/long-tenure employees leave far less.
- Engagement score matters: inactive (attrited) employees skew toward lower
  engagement than active ones.
- Promotion dynamics: among promotion-eligible employees, roughly 1 in 5 (~21%)
  still left — being "due" for a promotion that doesn't come is a risk.
- Performance x Potential interaction matters more than either alone.
- Low engagement + early tenure + unmet promotion expectation is the highest-risk combination.
"""

st.set_page_config(page_title="Attrition Risk Advisor", page_icon="📉", layout="centered")
st.title("📉 Attrition Risk Advisor")
st.caption("AI risk read grounded in the analysis in Attrition_Analysis.ipynb. "
           "Estimates, not a verdict — for HR triage, not automated decisions.")

with st.sidebar:
    st.subheader("Anthropic API key")
    api_key = st.text_input(
        "Key (or set ANTHROPIC_API_KEY)",
        value=os.environ.get("ANTHROPIC_API_KEY", ""),
        type="password",
    )
    st.caption("Stored only in this session. Get one at console.anthropic.com.")

col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", 18, 70, 32)
    tenure = st.number_input("Tenure (years)", 0.0, 40.0, 1.0, step=0.5)
    engagement = st.slider("Engagement score (0–100)", 0, 100, 60)
with col2:
    performance = st.selectbox("Performance", ["Low", "Medium", "High"], index=1)
    potential = st.selectbox("Potential", ["Low", "Medium", "High"], index=1)
    promo_eligible = st.selectbox("Promotion-eligible (no recent promotion)?", ["No", "Yes"])

notes = st.text_area("Anything else? (role, recent changes, manager feedback)", "")

if st.button("Assess attrition risk", type="primary"):
    if not api_key:
        st.error("Enter your Anthropic API key in the sidebar first.")
        st.stop()

    profile = (
        f"Age: {age}\nTenure (years): {tenure}\nEngagement score (0-100): {engagement}\n"
        f"Performance: {performance}\nPotential: {potential}\n"
        f"Promotion-eligible without recent promotion: {promo_eligible}\n"
        f"Notes: {notes or 'none'}"
    )
    prompt = (
        "You are an HR retention advisor. Using the analysis findings and the employee "
        "profile below, respond with exactly three sections:\n"
        "1. Risk level — Low / Medium / High, with one sentence of justification tied to the factors.\n"
        "2. Top drivers — the 2-3 factors pushing risk up or down for THIS employee.\n"
        "3. Retention actions — 2-3 specific, realistic steps a manager could take in the next month.\n"
        "Do not invent precise probabilities or statistics.\n\n"
        f"{ANALYSIS_FINDINGS}\n\nEmployee profile:\n{profile}"
    )

    try:
        client = anthropic.Anthropic(api_key=api_key)
        with st.spinner("Assessing…"):
            resp = client.messages.create(
                model=MODEL,
                max_tokens=800,
                messages=[{"role": "user", "content": prompt}],
            )
        st.markdown(resp.content[0].text)
    except Exception as e:  # noqa: BLE001
        st.error(f"Request failed: {e}")
