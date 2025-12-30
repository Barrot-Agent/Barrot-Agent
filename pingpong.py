import json
from datetime import datetime, timezone

# Default output filename for pingpong requests
DEFAULT_REQUEST_FILE = "pingpong_request.json"

def emit_pingpong_request(payload: dict, output_file: str = DEFAULT_REQUEST_FILE):
    """
    Emits a ping-pong request to be handled by Sean's 22-agent entanglement system.
    
    Args:
        payload: Dictionary containing the request payload
        output_file: Path to the output JSON file (default: pingpong_request.json)
        
    Returns:
        None - writes the request to the specified output file
    """
    request = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "payload": payload,
        "origin": "barrot",
        "directive": "offload_pingpong",
        "notes": "Barrot defers to Sean's 22-agent entanglement system."
    }
    with open(output_file, "w") as f:
        json.dump(request, f, indent=2)
    print("Ping-Pong request emitted. Commit to GitHub to trigger external system.")
