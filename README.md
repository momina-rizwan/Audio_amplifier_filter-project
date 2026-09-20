# Audio Amplification & Noise Suppression Circuit Design

![Python](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python)
![SPICE](https://img.shields.io/badge/Simulation-SPICE-orange?style=for-the-badge)
![Course](https://img.shields.io/badge/Course-EE313%20Electronic%20Circuit%20%26%20Design-green?style=for-the-badge)

An audio filtering and multi-stage amplification system designed to suppress stereo noise and amplify low-frequency audio signals.

---

## 📌 Circuit Architecture

1. **Active Filter Stage (Sallen-Key 2nd-Order Butterworth):**
   - **Cutoff Frequency ($f_c$):** $318\text{ Hz}$ to $500\text{ Hz}$
   - **Components:** $R_1 = R_2 = 50\text{ k}\Omega$, $C_1 = C_2 = 10\text{ nF}$, $UA741\text{ Op-Amp}$[cite: 4]
   - **Passband Gain ($k$):** $1.586$ ($R_f = 5.86\text{ k}\Omega, R = 10\text{ k}\Omega$)[cite: 4]

2. **Amplifier Stage (BJT Common Emitter Voltage Divider Bias):**
   - **Transistor:** $BC547\text{ NPN BJT}$[cite: 4]
   - **Target Voltage Gain ($A_v$):** $2$[cite: 4]
   - **Biasing Parameters:** $V_{CC} = 14\text{V}$, $R_1 = 4.7\text{ k}\Omega$, $R_2 = 1\text{ k}\Omega$, $R_C = 1\text{ k}\Omega$, $R_E = 500\ \Omega$[cite: 4]

---

## 📂 Repository Structure

```text
├── circuit_simulation.cir  # SPICE Netlist modeling circuit topology
├── simulate_circuit.py     # Python script for transient wave simulation
└── README.md               # Project documentation
