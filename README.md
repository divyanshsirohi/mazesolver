<h1 align="center">🧩 Python Maze Solver</h1>
<h3 align="center">A visual, algorithmic maze generator and solver using Tkinter</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" />
  <img src="https://img.shields.io/badge/Tkinter-GUI-green.svg" />
  <img src="https://img.shields.io/badge/Algorithms-Custom%20Logic-orange.svg" />
</p>

---

### 🎯 Overview

This project is a Python-based maze generation and solving visualizer, built using **Tkinter** for the interface and canvas rendering. The maze is generated using your own algorithmic logic, and then solved live on screen.  
You can later compare multiple algorithms (like BFS, DFS, A*, Dijkstra) in the same maze layout to visualize performance and efficiency.

---

### 🧠 Features

- 🧱 Maze generation from scratch (no libraries!)
- 👁️ Real-time visualization of solving steps
- 🐍 Pure Python logic for both creation and solving
- 🔁 Plan to test and compare multiple solving algorithms
- 📈 Eventually includes metrics like steps taken, path length, and time

---

### 📸 Demo Preview

---

### 🛠️ Tech Stack

- 🐍 Python 3.10+
- 🖼️ Tkinter (built-in)
- ✍️ Custom logic for grid, generation, solving, and GUI

---

### 🚀 Getting Started

Clone the repo and run the main file:

```

git clone [https://github.com/divyanshsirohi/python-maze-solver.git](https://github.com/divyanshsirohi/mazesolver.git)
cd mazesolver
python main.py

```

> No external dependencies needed!

---

### 🧩 Algorithms (Planned or In Progress)

| Algorithm    | Maze Generation | Maze Solving | Visualized? |
|--------------|------------------|---------------|-------------|
| DFS          | ✅               | ✅             | ✅          |
| BFS          | 🔜               | 🔜             | 🔜          |
| A*           | 🔜               | 🔜             | 🔜          |
| Dijkstra     | 🔜               | 🔜             | 🔜          |

---

### 📁 Folder Structure

```

python-maze-solver/
│
├── main.py           # Entry point — Tkinter setup and control loop
├── maze.py           # Maze generation logic
├── solver.py         # Maze solving algorithms
├── cell.py           # Cell object with walls, position, state
├── utils.py          # Grid helpers, visualization tools
└── README.md         # You're reading it!

```

---

### 👨‍💻 Author

**Divyansh Sirohi**  
🔗 [GitHub](https://github.com/divyanshsirohi) | [LinkedIn](https://linkedin.com/in/divyanshsirohi)

---

### ⭐ Fun Fact

> "The best way to understand an algorithm is to watch it think."  
This project was built to visually debug and **deeply understand pathfinding logic** — no black boxes!

---

### 💡 Future Additions

- Maze export/import functionality  
- Time/space complexity metrics  
- CLI version for benchmarking  

---
**If this helped you understand pathfinding better, drop a ⭐ on the repo!**
```

