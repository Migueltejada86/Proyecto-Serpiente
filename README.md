# Proyecto Serpiente

Prototipo modular de robot serpiente impreso en 3D (~30 cm de longitud total) pensado como un juego hermoso que invite a soñar en grande.

El objetivo de esta primera versión es simple: que se mueva con un gait serpentina básico, que tenga una cámara frontal pequeña y que se pueda controlar por Bluetooth (o cable). Todo documentado y abierto para que después podamos escalarlo a algo realmente útil en búsqueda y rescate.

## Visión

- **Corto plazo**: Prototipo divertido, modular, imprimible en Alta Gracia, fácil de armar y modificar.
- **Mediano plazo**: Añadir sensores, mejor locomoción, autonomía básica.
- **Largo plazo**: Explorar ideas de robots para espacios colapsados, voids estrechos y terrenos agrestes (serpientes blandas, crawlers, micro-drones, etc.).

## Especificaciones del prototipo v0.1

| Parámetro              | Valor                          |
|-------------------------|--------------------------------|
| Longitud total          | ~30 cm                         |
| Segmentos               | 5 o 6                          |
| Actuadores              | MG90S (o SG90)                 |
| Controlador             | ESP32                          |
| Driver de servos        | PCA9685                        |
| Cámara                  | ESP32-CAM o cámara pequeña compatible |
| Control                 | Bluetooth (o USB/Serial)       |
| Impresión               | PLA / PETG (locales de Alta Gracia) |
| Alimentación            | Batería externa + regulador     |

## Estructura del repositorio

```
/
├── README.md
├── docs/
│   ├── BOM.md
│   ├── assembly.md
│   └── wiring.md
├── firmware/
│   └── snake_v01/
├── hardware/
│   ├── stl/          ← archivos de impresión 3D
│   └── cad/          ← fuentes (Fusion 360, OpenSCAD, etc.)
└── media/
```

## Próximos pasos

1. Diseñar o adaptar módulos 3D simples para MG90S (cabeza + segmentos + cola).
2. Lista de materiales (BOM) detallada.
3. Esquema de cableado básico.
4. Firmware inicial con gait sinusoidal y control Bluetooth.
5. Primera impresión y prueba de movimiento.

## Licencia

MIT — usá, modificá y compartí.

---

*Hecho en Alta Gracia / Córdoba. Un prototipo para jugar y soñar.*
