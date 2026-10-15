#!/usr/bin/env python3
"""
Simulador cinemático básico — Proyecto Serpiente

Modos:
- serpentine : onda clásica en yaw
- cobra      : levanta 1-2 segmentos de pitch (v1.1)
- diagonal   : combinación yaw+pitch para ~45° (v1.2)

Controles (ventana abierta):
  1 / 2 / 3   → cambiar modo
  + / -       → amplitud
  [ / ]       → velocidad
  q           → salir

Requisitos:
  pip install matplotlib numpy
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ===================== Parámetros =====================
NUM_SEGMENTS = 6          # Total de joints
LINK_LENGTH = 5.0         # cm (aprox para ~30 cm)
# Joints: even = yaw (lateral), odd = pitch (vertical)
# Para el prototipo chico usamos pocos pitch activos en cobra

# ===================== Estado =====================
mode = "serpentine"       # serpentine | cobra | diagonal
amplitude = 35.0          # grados
frequency = 0.6           # Hz
phase_lag = 0.9           # rad entre segmentos
cobra_pitch = 55.0        # grados de elevación en modo cobra
diagonal_ratio = 0.85     # relación amp_pitch / amp_yaw para ~45°

t = 0.0
dt = 0.03

def get_angles(t):
    """Devuelve lista de ángulos (grados) para cada joint."""
    angles = []
    for i in range(NUM_SEGMENTS):
        is_yaw = (i % 2 == 0)

        if mode == "serpentine":
            if is_yaw:
                ang = amplitude * np.sin(2 * np.pi * frequency * t - i * phase_lag)
            else:
                ang = 0.0

        elif mode == "cobra":
            if is_yaw:
                ang = amplitude * 0.4 * np.sin(2 * np.pi * frequency * t - i * phase_lag)
            else:
                # Solo los primeros 1-2 pitch se levantan
                if i == 1 or i == 3:
                    ang = cobra_pitch
                else:
                    ang = 0.0

        elif mode == "diagonal":
            # Onda en ambos planos con desfase para plano ~45°
            base = amplitude * np.sin(2 * np.pi * frequency * t - i * phase_lag)
            if is_yaw:
                ang = base
            else:
                ang = base * diagonal_ratio

        else:
            ang = 0.0

        angles.append(ang)
    return angles

def forward_kinematics(angles_deg):
    """Posiciones 3D de los joints (x, y, z)."""
    pos = np.zeros((NUM_SEGMENTS + 1, 3))
    # Orientación acumulada simple (aproximación para visualización)
    heading = 0.0
    pitch_acc = 0.0

    for i in range(NUM_SEGMENTS):
        ang = np.deg2rad(angles_deg[i])
        if i % 2 == 0:  # yaw
            heading += ang
        else:           # pitch
            pitch_acc += ang

        dx = LINK_LENGTH * np.cos(pitch_acc) * np.cos(heading)
        dy = LINK_LENGTH * np.cos(pitch_acc) * np.sin(heading)
        dz = LINK_LENGTH * np.sin(pitch_acc)

        pos[i + 1] = pos[i] + np.array([dx, dy, dz])

    return pos

# ===================== Visualización =====================
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection="3d")
ax.set_xlim(-40, 40)
ax.set_ylim(-40, 40)
ax.set_zlim(-5, 30)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Proyecto Serpiente — Simulador cinemático")

line, = ax.plot([], [], [], "o-", lw=2, markersize=6, color="#2ecc71")
text = ax.text2D(0.02, 0.95, "", transform=ax.transAxes)

def update(frame):
    global t
    t += dt
    angles = get_angles(t)
    pos = forward_kinematics(angles)

    line.set_data(pos[:, 0], pos[:, 1])
    line.set_3d_properties(pos[:, 2])

    info = f"Modo: {mode}  |  Amp: {amplitude:.0f}°  |  Freq: {frequency:.2f} Hz"
    text.set_text(info)
    return line, text

def on_key(event):
    global mode, amplitude, frequency
    if event.key == "1":
        mode = "serpentine"
    elif event.key == "2":
        mode = "cobra"
    elif event.key == "3":
        mode = "diagonal"
    elif event.key == "+":
        amplitude = min(amplitude + 5, 70)
    elif event.key == "-":
        amplitude = max(amplitude - 5, 5)
    elif event.key == "]":
        frequency = min(frequency + 0.1, 2.0)
    elif event.key == "[":
        frequency = max(frequency - 0.1, 0.1)
    elif event.key == "q":
        plt.close()

fig.canvas.mpl_connect("key_press_event", on_key)

ani = FuncAnimation(fig, update, interval=30, blit=False, cache_frame_data=False)
plt.tight_layout()
print("Controles: 1=serpentine  2=cobra  3=diagonal  +/- amp  [/] freq  q=salir")
plt.show()
