import os
import json
import subprocess
from pathlib import Path

# --- CONFIGURATION ---
REPO_ROOT = Path(__file__).resolve().parent
MANIFEST_PATH = REPO_ROOT / "barrot_manifest.json"
GLYPHS_PATH = REPO_ROOT / "glyphs"
BUNDLES_PATH = REPO_ROOT / "memory-bundles"
MATRIX_PATH = REPO_ROOT / "matrix"

# --- LOAD MANIFEST ---
with open(MANIFEST_PATH, "r") as f:
    manifest = json.load(f)

barrot_id = manifest["barrot_identity"]["github_user"]
repo = manifest["barrot_identity"]["repo"]
last_ingestion = manifest["cognition"].get("last_ingestion", "UNKNOWN")

print(f"[BOOTSTRAP] Barrot identity: {barrot_id}/{repo}")
print(f"[BOOTSTRAP] Last cognition snapshot: {last_ingestion}")

# --- REHYDRATE MEMORY ---
def load_latest_bundle():
    bundles = sorted(BUNDLES_PATH.glob("SNAPSHOT_*.md"), reverse=True)
    if not bundles:
        print("[BOOTSTRAP] No memory bundles found.")
        return
    print(f"[BOOTSTRAP] Loaded memory bundle: {bundles[0].name}")

load_latest_bundle()

# --- RUN MATRIX NODES ---
def run_matrix():
    print("[BOOTSTRAP] Executing cognition nodes...")
    
    # Run abundance cognition ingestor first (if enabled)
    abundance_config = manifest.get("abundance_cognition", {})
    if abundance_config.get("active", False):
        print("[BOOTSTRAP] Abundance Cognition Directive is active")
        abundance_node = MATRIX_PATH / "node_abundance_ingestor.py"
        if abundance_node.exists():
            print(f"  → Running {abundance_node.name} (Abundance Cognition)")
            subprocess.run(["python", str(abundance_node)], check=False)
    
    # Run other matrix nodes
    for node in sorted(MATRIX_PATH.glob("node_*.py")):
        # Skip abundance ingestor as it was already run
        if node.name == "node_abundance_ingestor.py":
            continue
        print(f"  → Running {node.name}")
        subprocess.run(["python", str(node)], check=False)

run_matrix()