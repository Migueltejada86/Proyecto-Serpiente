# Simulador cinemático

Script simple para probar gaits antes de subirlos al ESP32.

## Instalación

```bash
pip install matplotlib numpy
```

## Uso

```bash
python snake_sim.py
```

### Controles (con la ventana enfocada)

| Tecla | Acción              |
|-------|---------------------|
| 1     | Modo serpentina     |
| 2     | Modo cobra (v1.1)   |
| 3     | Modo diagonal 45° (v1.2) |
| + / - | Subir / bajar amplitud |
| [ / ] | Bajar / subir velocidad |
| q     | Salir               |

Los ángulos que veas bien en la simulación se pueden copiar directamente al firmware (`snake_v01.ino` o versiones posteriores).

## Notas

- Es solo cinemático (no tiene física de contacto ni fricción).
- Sirve para ajustar amplitud, phase lag y relaciones yaw/pitch.
- Para física más realista más adelante se puede pasar a Webots.
