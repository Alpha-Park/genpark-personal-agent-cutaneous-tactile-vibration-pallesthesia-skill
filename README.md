# Cutaneous Vibration Perception Threshold (VPT) Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive evaluation of Cutaneous Vibration Perception Threshold (VPT), Rydel-Seiffer tuning fork pallesthesia, and large-fiber sensory neuropathy.

```mermaid
flowchart TD
    TuningFork["64 Hz Rydel-Seiffer Tuning Fork / Biothesiometer"] --> VisualScale["Visual Triangle Mark (0 - 8 Scale)"]
    VisualScale --> AgeNorm["Age-Adjusted Normative Cutoff Engine"]
    AgeNorm --> PallesthesiaScore["Pacinian Corpuscle & Pallesthesia Scoring"]
    PallesthesiaScore --> Agent["OpenClaw / Hermes Personal Agent Actions"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Clinical Neurological Standards**: Implements validated age-dependent Rydel-Seiffer cutoff formulas.
- **Hand-Arm Vibration & Large-Fiber Screening**: Non-invasive assessment of Pacinian mechanoreceptive integrity.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import VibrationPallesthesiaClient

client = VibrationPallesthesiaClient()
result = client.evaluate_vibration_threshold(
    rydel_seiffer_reading=7.5,
    age_years=32.0
)
print("Pallesthesia Score:", result["pallesthesia_sensory_score"])
print("Classification:", result["classification"])
```

## License
Apache-2.0
