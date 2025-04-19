import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="ECG Anomaly Detection Report",
    layout="wide"
)

# Utility function to safely display images
def show_img(path, caption=None, width=600):
    try:
        st.image(Image.open(path), caption=caption, use_container_width=False, width=width)
    except FileNotFoundError:
        st.warning(f"Image not found: `{path}`")

# Title
st.title("ECG Anomaly Detection: Final Analysis Report")
st.markdown("""
This interactive report summarizes the development and outcomes of a real-time **ECG anomaly detection system** using **Isolation Forest** and **Kafka streaming**.  
We dive into anomaly insights, drift detection, explainability, retraining behavior, and strategic takeaways.

---
""")

# SECTION 1: Introduction
st.header("1. Project Objective")
st.markdown("""
Our goal was to build a **production-style anomaly detection pipeline** for ECG signals that could:

- Ingest real-time signals using **Apache Kafka**
- Detect anomalies using **unsupervised learning (Isolation Forest)**
- Identify **concept drift** via statistical tests
- Trigger **automated model retraining**
- Provide **explainable visualizations** for clinical trust
""")

# SECTION 2: System Design
st.header("2. Architecture Overview")
st.markdown("""
Our pipeline simulates a streaming ECG scenario:
1. **Kafka Producer** sends 30,000 ECG signal rows  
2. **Kafka Consumer** runs real-time predictions  
3. **Drift Detection** flags when the data changes too much  
4. **Retraining Module** updates the model on-the-fly  
5. **Streamlit Dashboard** enables live visibility and decision-making
""")

# SECTION 3: Real-Time Anomaly Detection
st.header("3. Real-Time Anomaly Detection Insights")
st.markdown("""
We streamed ECG signals and detected **17.3% anomalies** across the dataset.

### What we observed:
- **Regular waveforms** were tagged as normal
- **Amplitude spikes** and irregularities were correctly flagged as anomalies
- Anomalies often occurred in **bursts**, mimicking real physiological responses

These results validate the model's real-time sensitivity.
""")
show_img("results/ECG Signals with Anomalies Highlighted.png", "ECG Signals with Highlighted Anomalies", width=900)
show_img("results/Anomaly Count per Simulated Minute.png", "Anomaly Frequency Over Time", width=900)

st.info("**Label Summary:**  \nAnomaly Count: 5,187  Normal Count: 23,723  Total Records: 28,910")

# SECTION 4: Drift Detection
st.header("4. Concept Drift Monitoring")
st.markdown("""
We monitored **z-scores** and used **KS-test** to detect concept drift.

### Drift Behavior:
- ECG1 and ECG2 stayed mostly within range, but some clear **outlier spikes** occurred
- We observed **drift triggers** aligned with **anomaly spikes**, prompting retraining
""")
show_img("results/Z-Scores of ECG Signals Over Time.png", "Z-Score Timeline with Anomaly Thresholds", width=900)

# SECTION 5: Explainability & Model Behavior
st.header("5. Explainability and Anomaly Reasoning")
st.markdown("""
To understand **why** a signal was flagged, we analyzed:

- **Anomaly score distributions** from Isolation Forest
- How **ECG1 & ECG2 z-scores** contributed to those decisions

These insights build **clinical trust** in the system's logic.
""")

col1, col2 = st.columns(2)
with col1:
    show_img("results/Distribution of Isolation Forest Anomaly Scores.png", "Anomaly Score Distribution")
with col2:
    show_img("results/Anomalous Points in Z-Score Space.png", "Z-Scores of Anomalies")

col1, col2 = st.columns(2)
with col1:
    show_img("results/Z-Score vs Anomaly Score (ECG1).png", "Z-Score vs Anomaly Score (ECG1)", width=450)
with col2:
    show_img("results/Z-Score vs Anomaly Score (ECG2).png", "Z-Score vs Anomaly Score (ECG2)", width=450)

# SECTION 6: Local Anomaly Windows
st.header("6. Anomaly Event Snapshots")
st.markdown("""
Zoomed-in ECG segments show **anomaly detection in action**.

This helps clinical teams verify flagged regions visually.
""")
show_img("results/ECG Signal Snippet around Anomaly.png", "ECG Signal Around Anomaly")

# SECTION 7: Evaluation Metrics
st.header("7. Model Evaluation Summary")
st.markdown("""
We simulated a 2% anomaly baseline to generate **precision and recall metrics**.

### Highlights:
- Precision was ~98%, showing **very few false positives**
- Recall was modest, suggesting **future improvements in capturing edge anomalies**
""")
show_img("results/confusion_matrix.png", "Confusion Matrix on Prediction Log")

# SECTION 8: Retraining Behavior
st.header("8. Model Retraining Timeline")
st.markdown("""
We logged each **retraining event** triggered by concept drift.

- Early retrains used ~36 points
- Later retrains used too few — suggesting **batch retraining** would be better

""")
show_img("results/retraining_timeline.png", "Model Retraining Events Over Time")

# SECTION 9: Recommendations
st.header("9. Strategic Recommendations")
st.markdown("""
Based on all insights, we suggest:

- ✅ Use **batch-size triggers** for retraining, not per spike  
- ✅ Integrate **medical rules** (e.g., BPM thresholds) to assist anomaly detection  
- ✅ Replace dummy ground truth with **clinically annotated ECGs** for final validation  
- ✅ Explore **multimodal models** for ECG + vitals in future iterations  
""")

# Footer
st.markdown("---")
st.caption("Report generated by Jahnavi Patel · Data Scientist · April 2025")
