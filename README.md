# smart-water-dashboard-by-HydroBeat
# 💧 HydroBeat – Smart Water Pressure Management System

A real-time, zone-based smart water monitoring and pressure management system designed to ensure equitable water distribution across elevated, mid-level, and tail-end regions in urban municipal networks.

---

##  Problem Statement

Urban water distribution systems face:

- Low pressure in elevated and tail-end areas
- Excess pressure in low-lying regions
- Uneven distribution across wards
- High water loss due to leaks and bursts
- Delayed fault detection
- Manual dependency in operations

These challenges lead to inequality in water access and increased operational burden on municipal authorities.

---

##  Proposed Solution

HydroBeat introduces an intelligent, modular water pressure management system that:

- Utilizes **gravity-based flow optimization**
- Integrates **in-pipe micro turbines**
- Implements **mid-elevation break tanks**
- Deploys **booster-assisted pressure regulation**
- Monitors real-time data using **pressure sensors and flow meters**
- Enables centralized decision-making via a **municipal dashboard**

This solution enhances the existing infrastructure without replacing it.

---

##  System Architecture

###  Mechanical & Hydraulic Design
- Gravity-fed reservoir supply
- In-pipe micro turbine for energy harvesting
- Break tanks placed at elevation points
- Pressure-assisted booster pumps
- Smart flow divider at ¾ downhill point

###  Smart Monitoring (DMA-Based)
- Zone-wise pressure sensors
- Flow meters at distribution points
- Real-time monitoring of:
  - Pressure variation
  - Flow imbalance
  - Sudden drops (leak detection)

###  Central Command Dashboard
- Live zone-wise pressure readings
- Flow rate monitoring
- Status classification (Normal / Warning / Critical)
- Real-time updates every few seconds
- Fault identification for faster municipal response

---

##  Dashboard Features

- Real-time pressure display (in bar)
- Real-time flow rate monitoring (L/min)
- Zone-based alert system
- Auto-refresh every 3 seconds
- Scalable architecture for IoT integration
- Ready for integration with ESP32 / PLC systems

---

##  Break Tank Concept

The break tank is a compact mid-elevation pressure-balancing structure that:

- Stabilizes incoming pressure
- Reduces turbulence
- Resets hydraulic head
- Activates booster only when required
- Ensures uniform pressure to elevated regions

It improves supply reliability without large-scale infrastructure modification.

---

##  Technology Stack

- Python
- Flask (Backend)
- HTML/CSS
- JavaScript
- Real-time data simulation
- Git & GitHub for version control

---

## 🚀 How to Run the Project Locally

1. Clone the repository:
