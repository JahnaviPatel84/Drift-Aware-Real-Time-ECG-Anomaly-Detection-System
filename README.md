# Drift-Aware Real-Time ECG Anomaly Detection 

A real-time anomaly detection system for ECG signals using Kafka streaming, Isolation Forest, and adaptive retraining with concept drift monitoring.  
Built for production-style ML streaming scenarios and explainable clinical analysis.

**Live Report**: [Streamlit Dashboard](https://drift-aware-real-time-ecg-anomaly-detection-system.streamlit.app/)

---

## Overview

This project simulates real-time ECG monitoring and anomaly detection using:

- **Apache Kafka** for ECG signal streaming  
- **Isolation Forest** for anomaly detection  
- **Drift Detection** using KS-Test on signal windows  
- **Retraining Logic** triggered on drift detection  
- **Explainable Visualizations** in a Streamlit Dashboard

