# Edge Guard Security Daemon (`edge_guard.py`)

A lightweight security and telemetry verification script built for edge computing nodes operating in restricted terminal environments. Designed and developed as part of practical DevSecOps laboratories.

## 🛡️ Overview
`edge_guard.py` acts as an automated security gatekeeper for incoming edge node telemetry and connection packets. Before any CPU resources are allocated or traffic is processed, the daemon subjects incoming payloads to rigorous validation checks, mathematical cycle distribution, and conditional threat analysis.

## ⚙️ Key Technical Features
* **Input Integrity & Sanitization:** Inspects device identification strings and measures metadata length (`len()`) to prevent malformed injections.
* **Modulo Telemetry Distribution (`%`):** Utilizes the modulo operator to evaluate incoming packet sizes against operational thresholds, ensuring balanced thread and cycle distribution.
* **Robust Control Flow (`if`, `elif`, `else`):** Automatically categorizes traffic streams into secure nodes, verified operations, or system security breaches.

---

## 🚀 How to Run

1. Open your terminal (such as Termux) inside your workspace directory.
2. Execute the script using the Python interpreter:
   ```bash
   python edge_guard.py
   