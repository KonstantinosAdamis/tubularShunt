import numpy as np
import matplotlib.pyplot as plt

# Constants
R = 4e-3  # 4 milliohms
L = 90.3e-12  # 90.3 picohenries

# Frequency range in Hz (1 Hz to 100 MHz, log scale)
f = np.logspace(0, 8, 1000)  # 10^0 = 1 Hz, 10^8 = 100 MHz
omega = 2 * np.pi * f  # Convert Hz to rad/s

# Magnitude response
H_mag = R**2 / np.sqrt(4 * R**2 + (omega**2) * (L**2))
H_dB = 20 * np.log10(H_mag)

# Phase response
phase_rad = np.arctan(-omega * L / (2 * R))
phase_deg = phase_rad * (180 / np.pi)

# Plotting
fig, ax = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

# Magnitude plot
ax[0].semilogx(f, H_dB, color='blue')
ax[0].set_title("Frequency Response (1 Hz to 100 MHz)")
ax[0].set_ylabel("Magnitude (dB)")
ax[0].grid(True, which='both', ls='--')

# Phase plot
ax[1].semilogx(f, phase_deg, color='orange')
ax[1].set_xlabel("Frequency (Hz)")
ax[1].set_ylabel("Phase (°)")
ax[1].grid(True, which='both', ls='--')

plt.tight_layout()
plt.show()