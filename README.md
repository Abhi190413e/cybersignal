# 🚀 **CyberSignal**

**CyberSignal** is a unique cybersecurity CLI tool that blends **human-behavior signals**,
**process drift detection**, and **shadow-IT discovery** to generate an early-warning
**Cyber Risk Score (0–100)**.

Traditional tools only look at logs or vulnerabilities — CyberSignal predicts risk by
correlating *how humans behave*, *how code/projects evolve*, and *what suspicious files appear*.

🔗 **PyPI Package:** [https://pypi.org/project/cybersignal/](https://pypi.org/project/cybersignal/)



# ✨ **Features**

### 🧠 Human Behavior Signal Detection

Detects subtle user patterns that indicate risk, such as:

* Rapid repeated scans (rushed activity)
* Night-time working (fatigue indicator)
* Irregular action intervals (context switching)

### 🔧 Process Drift Detection

Analyzes your project directory for:

* Newly added large files
* Missing key files
* Structural changes indicating process drift

### 🛰 Shadow-IT Detection

Flags suspicious executables:

* `.exe`, `.sh`, `.bat`, `.ps1`, `.apk`, etc.

### 🔥 Unified Cyber Risk Score

A single risk score (0–100) combining all three dimensions:

* Human behavior
* File/process drift
* Shadow-IT signals

### 🛡 Works Offline

All detection logic runs locally — no data leaves your machine.



# 📦 **Installation**

From PyPI:

```sh
pip install cybersignal
```

If the CLI command is not immediately available on macOS, use:

```sh
python3 -m cybersignal.cli scan .
```

or add Python’s user script directory to PATH (explained in README).



# 🚀 **Usage**

### Scan a directory:

```sh
cybersignal scan <path>
```

Example:

```sh
cybersignal scan .
```

### Output Example

```
🔍 Running CyberSignal scan...

=== HUMAN SIGNALS ===
{'scan_frequency': 0, 'night_activity': 1, 'irregular_intervals': 0}

=== PROCESS DRIFT ===
{'new_large_files': 0, 'missing_key_files': 0, 'structure_changes': 1}

=== SHADOW IT ===
{'unknown_executables': 0}

🔥 FINAL RISK SCORE: 35 / 100
🟡 Medium Risk — Concerning patterns.
```



# 📁 **Project Structure**

```
cybersignal/
│
├── cybersignal/
│   ├── __init__.py
│   ├── cli.py
│   ├── core.py
│
├── LICENSE
├── README.md
├── pyproject.toml
├── MANIFEST.in
```



# 📌 **Why CyberSignal is Unique**

CyberSignal is the **first CLI tool** that correlates:

### ✔ Human behavior

### ✔ Project drift

### ✔ Shadow-IT presence

…to produce a predictive cyber-risk indicator.

This gives early warning for:

* Misconfigurations before they become exploits
* Employee burnout that leads to mistakes
* Files appearing that shouldn’t
* Silent process changes (common in breaches)



# 🧭 **Roadmap**

| Feature                        | Status |
| ------------------------------ | ------ |
| Basic CLI engine               | ✅      |
| Human behavior signals         | ✅      |
| Process drift detector         | ✅      |
| Shadow-IT detector             | ✅      |
| PyPI packaging                 | ✅      |
| JSON export                    | 🔜     |
| Watch-mode (real-time monitor) | 🔜     |
| Web dashboard                  | 🔜     |
| AI anomaly model               | 🔜     |
| Plug-in system                 | 🔜     |



# 🤝 **Contributing**

1. Fork the repo
2. Create a feature branch
3. Commit changes
4. Open a pull request

PRs for:

* new detectors
* OS-specific optimizations
* plugin system ideas
  are highly welcome!


# 📜 **License**

This project is licensed under the **MIT License** — free for personal & commercial use.



# ⭐ **Support**

If you like this project, consider:

* ⭐ Starring the repository
* 🔧 Contributing improvements
* 🐞 Opening issues for bugs or ideas




