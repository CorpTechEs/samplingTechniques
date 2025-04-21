# 🎯 Sampling Simulation System

A gamified educational simulation built using **Python** and **Pygame** that visually teaches and demonstrates different sampling techniques used in statistics. The simulation allows users to interactively generate samples from a population using multiple methods and compare their selections with those made by the system.

---

## 📌 Features

- **Spinning Wheel Interface** – Interactive wheel to guide sampling and create an engaging experience.
- **Sampling Techniques Supported**:
  - ✅ Simple Random Sampling (SRS)
  - ✅ Systematic Sampling
  - ✅ Stratified Sampling
  - ✅ Cluster Sampling
- **User vs System Comparison** – After sample collection, the system generates its own sample using the same technique, and the two are compared based on internal "points".
- **Clear Visual Feedback** – Colored shapes represent population members, dynamically updated as samples are selected.
- **MVC Architecture** – Clean separation between models (logic), views (rendering), and controllers (interaction).

---

## 🎮 How It Works

### 1. **Select Sampling Technique**
Choose one of the available techniques via on-screen buttons.

### 2. **Spin the Wheel**
Each spin selects an element (or cluster) based on the chosen sampling method.

- **SRS**: Random individuals from the population.
- **Systematic**: Every nth item in the list.
- **Stratified**: Individuals selected from distinct subgroups (strata).
- **Cluster**: First spin selects a group; subsequent spins sample from that group.

### 3. **Go Against the System**
After collecting your sample, click the **"Go Against"** button:
- The system generates its own sample.
- The system compares the total "points" from both samples.
- A winner is declared and displayed.

### 4. **Reset and Repeat**
After each match, the system resets everything for the next round.

---

### 5. **🛠 Tech Stack**

- Python 3.x
- Pygame
- MVC Design Pattern
---
### 6. 🚀 **Future Ideas**

- Scoring history tracking
- Exportable sample reports
- Custom population generation
- Multiplayer or class-based usage in EdTech settings

---

### 7. 👩‍🏫 **Educational Objective**

This system is built to help students and educators **understand sampling concepts** through interaction, visual feedback, and competition, making abstract statistical methods more concrete and memorable.

---
---

### 8. ✅ Installation

```bash
git clone https://github.com/yourusername/sampling-simulation.git
cd sampling-simulation
pip install -r requirements.txt
python main.py
---
## 🧠 Sample Data Structure

Each population member is a dictionary with:

```python
{
  'id': 0,
  'shape': '▲',
  'color': (255, 0, 0),
  'size': 'small',
  'shade': 'dark',
  'point': 5
}
