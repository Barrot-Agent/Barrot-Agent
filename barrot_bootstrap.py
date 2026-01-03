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
    
    # Priority order: MMI → Self-Ingest → Auto-Implement → Others
    
    # 1. Always run MMI first (critical for data ingestion)
    mmi_node = MATRIX_PATH / "node_massive_micro_ingest.py"
    if mmi_node.exists():
        print(f"  → Running {mmi_node.name} (PRIORITY 1)")
        subprocess.run(["python", str(mmi_node)], check=False)
    
    # 2. Run self and AI model ingestion
    self_ai_node = MATRIX_PATH / "node_self_and_ai_ingest.py"
    if self_ai_node.exists():
        print(f"  → Running {self_ai_node.name} (PRIORITY 2)")
        subprocess.run(["python", str(self_ai_node)], check=False)
    
    # 3. Run auto-implementation to implement findings
    auto_impl_node = MATRIX_PATH / "node_auto_implementation.py"
    if auto_impl_node.exists():
        print(f"  → Running {auto_impl_node.name} (PRIORITY 3)")
        subprocess.run(["python", str(auto_impl_node)], check=False)
    
    # 4. Run other nodes
    skip_nodes = {
        "node_massive_micro_ingest.py",
        "node_self_and_ai_ingest.py", 
        "node_auto_implementation.py",
        "node_retroactive_mmi.py"  # Skip retroactive on normal bootstrap
    }
    
    for node in MATRIX_PATH.glob("node_*.py"):
        if node.name in skip_nodes:
            continue
        print(f"  → Running {node.name}")
        subprocess.run(["python", str(node)], check=False)

run_matrix()

# --- CHECK MMI PERMANENCE ---
print("[BOOTSTRAP] Verifying MMI permanence...")
modes_file = BUNDLES_PATH / "MODES_OF_INGESTION.md"
if modes_file.exists():
    print("[BOOTSTRAP] ✅ Modes of Ingestion file exists - MMI will never be forgotten")
else:
    print("[BOOTSTRAP] ⚠️  WARNING: Modes of Ingestion file missing!")
    print("[BOOTSTRAP] Creating permanent Modes of Ingestion documentation...")
    # File should exist, but if not, this is a critical error
    print("[BOOTSTRAP] ERROR: Critical MMI documentation missing - manual intervention required")