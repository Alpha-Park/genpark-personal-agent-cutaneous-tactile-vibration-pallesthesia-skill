"""
Cutaneous Vibration Perception Threshold (VPT) & Pallesthesia Biomechanics Engine.
Provides deterministic, zero-dependency modeling of Rydel-Seiffer 64 Hz tuning fork scales,
electronic biothesiometry voltage thresholds, and large myelinated A-beta dorsal column pallesthesia.
"""

from typing import Dict, Any, List, Optional


class VibrationPallesthesiaClient:
    """
    Deterministic client for calculating Cutaneous Vibration Perception Threshold (VPT).
    Assesses rapidly adapting type II (RA II) Pacinian corpuscle mechanoreceptor function,
    dorsal column-medial lemniscal sensory transmission, and hand-arm vibration syndrome (HAVS).
    """

    def __init__(self):
        pass

    def evaluate_vibration_threshold(
        self,
        rydel_seiffer_reading: float,
        biothesiometer_voltage_v: Optional[float] = None,
        test_location: str = "INDEX_FINGER",
        age_years: float = 35.0
    ) -> Dict[str, Any]:
        """
        Evaluates vibration perception threshold:
        - Rydel-Seiffer scale: 0 (loss of perception) to 8 (highest sensitivity)
        - Biothesiometer voltage: < 15 V (normal), 16 - 24 V (impaired), >= 25 V (severe deficit)
        """
        if rydel_seiffer_reading < 0.0 or rydel_seiffer_reading > 8.0:
            return {"error": "Rydel-Seiffer reading must be between 0.0 and 8.0"}

        loc = test_location.upper()

        # Age-adjusted normal reference cutoff
        if age_years < 40.0:
            cutoff = 6.5
        elif age_years <= 65.0:
            cutoff = 5.5
        else:
            cutoff = 4.5

        # Pallesthesia Sensory Score (0 - 100):
        # Reading 7.0 - 8.0 -> 90 - 100.
        # Reading < 4.0 -> < 50.
        score = (rydel_seiffer_reading / 8.0) * 100.0

        if biothesiometer_voltage_v is not None:
            if biothesiometer_voltage_v > 25.0:
                score = min(score, 35.0)
            elif biothesiometer_voltage_v > 15.0:
                score = min(score, 65.0)

        final_score = round(min(100.0, max(5.0, score)), 1)

        is_normal = rydel_seiffer_reading >= cutoff

        if rydel_seiffer_reading >= cutoff:
            tier = "NORMAL_VIBRATION_PALLESTHESIA"
            interp = f"Preserved high-frequency vibratory sensitivity (reading {rydel_seiffer_reading}/8, age cutoff {cutoff}) at {loc}; intact Pacinian-dorsal column conduction."
            guidance = "Excellent mechanoreceptive vibratory feedback. Standard sensory integrity for fine motor and postural control."
        elif rydel_seiffer_reading >= cutoff - 1.5:
            tier = "MILD_PALLESTHESIA_ATTENUATION"
            interp = f"Mild reduction in vibration threshold ({rydel_seiffer_reading}/8 < {cutoff}); early signs of sensory blunting or vibrational fatigue."
            guidance = "Incorporate anti-vibration ergonomic grips, limit prolonged vibrating tool exposure, and check peripheral microcirculation."
        elif rydel_seiffer_reading >= 2.5:
            tier = "MODERATE_LARGE_FIBER_IMPAIRMENT"
            interp = f"Moderate pallesthesia deficit ({rydel_seiffer_reading}/8); significant loss of large myelinated A-beta afferents."
            guidance = "Elevated risk of sensory ataxia or hand-arm vibration syndrome (HAVS). Recommend formal neurological nerve conduction testing."
        else:
            tier = "SEVERE_VIBRATORY_SENSORY_LOSS"
            interp = f"Severe vibratory loss ({rydel_seiffer_reading}/8 <= 2.0); near-complete dorsal column pallesthesia abolition."
            guidance = "Severe sensory neuropathy detected. Avoid hazardous vibrational tasks and implement strict visual compensation strategies."

        return {
            "test_location": loc,
            "age_years": age_years,
            "rydel_seiffer_reading": rydel_seiffer_reading,
            "age_adjusted_cutoff": cutoff,
            "biothesiometer_voltage_v": biothesiometer_voltage_v,
            "pallesthesia_sensory_score": final_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
