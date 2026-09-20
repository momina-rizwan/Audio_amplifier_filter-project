import numpy as np
import matplotlib.pyplot as plt

# --- CIRCUIT PARAMETERS ---
# Filter Parameters
R_a, R_b = 50e3, 50e3  # 50 kOhm
C1, C2 = 10e-9, 10e-9  # 10 nF
fc = 1 / (2 * np.pi * np.sqrt(R_a * R_b * C1 * C2))  # Cutoff frequency ~318 Hz

# BJT Stage Parameters (Av = 2)
Av_bjt = 2.0
Vcc = 14.0

# --- SIMULATION TIME & INPUT SIGNALS ---
time = np.linspace(0, 0.01, 1000)  # 10 ms time span
freq_in = 300  # Passband audio signal (300 Hz)
freq_noise = 2500  # High-frequency noise signal (2.5 kHz)

# Input: Low-frequency audio signal mixed with high-frequency noise
audio_signal = 0.1 * np.sin(2 * np.pi * freq_in * time)
noise_signal = 0.05 * np.sin(2 * np.pi * freq_noise * time)
v_in = audio_signal + noise_signal

# --- SIMULATED STAGE OUTPUTS ---
# Stage 1: Filter suppresses high-frequency noise
v_filtered = 1.586 * audio_signal + 0.005 * noise_signal

# Stage 2: BJT Common Emitter amplifies signal (inverted phase, Av = 2)
v_out = -1 * Av_bjt * v_filtered

# --- PLOTTING WAVEFORMS ---
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(time * 1000, v_in, color='red', label='Input Signal (Audio + Noise)')
plt.ylabel('Voltage (V)')
plt.title('Stage Analysis: Filter & BJT Audio Amplifier Circuit')
plt.grid(True)
plt.legend(loc='upper right')

plt.subplot(3, 1, 2)
plt.plot(time * 1000, v_filtered, color='blue', label='Filtered Output (Sallen-Key Stage)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.legend(loc='upper right')

plt.subplot(3, 1, 3)
plt.plot(time * 1000, v_out, color='green', label='Final Output (BJT Amplified, Av=2)')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.legend(loc='upper right')

plt.tight_layout()
plt.savefig('simulation_waveform.png', dpi=300)
plt.show()
