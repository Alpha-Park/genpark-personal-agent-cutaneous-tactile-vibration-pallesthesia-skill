"""
Example Usage: Cutaneous Vibration Perception Threshold (VPT) & Pallesthesia.
Demonstrates non-invasive evaluation of tuning fork Rydel-Seiffer vibration sensitivity.
"""

from client import VibrationPallesthesiaClient


def main():
    client = VibrationPallesthesiaClient()
    print("=== Cutaneous Vibration Perception Threshold (VPT) Demo ===")

    # Test Case 1: Healthy young adult (Fingertip)
    res1 = client.evaluate_vibration_threshold(
        rydel_seiffer_reading=7.5,
        biothesiometer_voltage_v=11.0,
        test_location="INDEX_FINGER",
        age_years=32.0
    )
    print("\nTest Case 1: Healthy Young Adult (Fingertip)")
    print(f"  Location: {res1['test_location']} | Age: {res1['age_years']} yrs")
    print(f"  Rydel-Seiffer Reading: {res1['rydel_seiffer_reading']} / 8.0 (Cutoff: {res1['age_adjusted_cutoff']})")
    print(f"  Biothesiometer: {res1['biothesiometer_voltage_v']} V")
    print(f"  Pallesthesia Score: {res1['pallesthesia_sensory_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Hand-Arm Vibration Syndrome (HAVS) / large-fiber sensory impairment
    res2 = client.evaluate_vibration_threshold(
        rydel_seiffer_reading=3.5,
        biothesiometer_voltage_v=22.0,
        test_location="INDEX_FINGER",
        age_years=48.0
    )
    print("\nTest Case 2: Vibratory Attenuation (Power Tool User)")
    print(f"  Rydel-Seiffer: {res2['rydel_seiffer_reading']} / 8.0 (Cutoff: {res2['age_adjusted_cutoff']})")
    print(f"  Score: {res2['pallesthesia_sensory_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()
