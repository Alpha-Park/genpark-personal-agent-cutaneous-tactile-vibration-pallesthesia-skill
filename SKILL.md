---
name: genpark-personal-agent-cutaneous-tactile-vibration-pallesthesia-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for calculating cutaneous vibration perception thresholds (VPT), Rydel-Seiffer tuning fork pallesthesia, and large-fiber sensory neuropathy.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Cutaneous Vibration Perception Threshold (VPT) Skill

A sovereign personal agent capability for assessing rapidly adapting type II (RA II) Pacinian corpuscle mechanoreceptor sensitivity, Rydel-Seiffer 64 Hz tuning fork pallesthesia, and dorsal column sensory nerve conduction.

## Core Capabilities
- **Rydel-Seiffer Standardization**: Evaluates graduated visual triangle vibration marks (0 to 8).
- **Age-Adjusted Normative Cutoffs**: Automatically adjusts threshold expectations based on subject age.
- **Biothesiometry Integration**: Correlates electronic voltage thresholds with qualitative tuning fork scores.
- **Vibrational Ergonomics (HAVS)**: Provides exposure thresholds and rest recommendations for power tool and high-vibration work.

## Fast Invocation
```python
from client import VibrationPallesthesiaClient

client = VibrationPallesthesiaClient()
res = client.evaluate_vibration_threshold(
    rydel_seiffer_reading=7.5,
    biothesiometer_voltage_v=11.0,
    age_years=32.0
)
print("Reading:", res["rydel_seiffer_reading"], "/ 8")
print("Pallesthesia Score:", res["pallesthesia_sensory_score"])
```
