"""
MCP Server for Cutaneous Vibration Perception Threshold (VPT) & Pallesthesia Skill.
Exposes JSON-RPC Model Context Protocol tools for assessing tuning fork Rydel-Seiffer and biothesiometry pallesthesia.
"""

import sys
import json
from typing import Dict, Any
from client import VibrationPallesthesiaClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_vibration_threshold",
                "description": "Calculates Rydel-Seiffer vibration threshold, age-adjusted normative cutoff, and pallesthesia sensory score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "rydel_seiffer_reading": {
                            "type": "number",
                            "description": "Graduated visual scale reading on 64 Hz tuning fork from 0.0 to 8.0 (e.g. 7.0 for healthy)."
                        },
                        "biothesiometer_voltage_v": {
                            "type": "number",
                            "description": "Optional electronic biothesiometer vibration threshold in volts (e.g. 12.0 V)."
                        },
                        "test_location": {
                            "type": "string",
                            "description": "Anatomical testing point (INDEX_FINGER, GREAT_TOE, MEDIAL_MALLEOLUS).",
                            "default": "INDEX_FINGER"
                        },
                        "age_years": {
                            "type": "number",
                            "description": "Age of the subject in years for normative adjustment.",
                            "default": 35.0
                        }
                    },
                    "required": ["rydel_seiffer_reading"]
                }
            }
        ]
    }


def handle_request(client: VibrationPallesthesiaClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_vibration_threshold":
            bio_v = args.get("biothesiometer_voltage_v")
            if bio_v is not None:
                bio_v = float(bio_v)

            res = client.evaluate_vibration_threshold(
                rydel_seiffer_reading=float(args.get("rydel_seiffer_reading", 7.0)),
                biothesiometer_voltage_v=bio_v,
                test_location=str(args.get("test_location", "INDEX_FINGER")),
                age_years=float(args.get("age_years", 35.0))
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method {name} not found"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": "Invalid request"
            }
        }


def main():
    client = VibrationPallesthesiaClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": str(e)}
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
