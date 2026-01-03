#!/usr/bin/env python3
"""
Retroactive Massive Micro Ingestion
Applies MMI to all historical data in the repository
"""

import sys
import json
from pathlib import Path
from datetime import datetime, timezone
import subprocess

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from matrix.node_massive_micro_ingest import MassiveMicroIngestor

REPO_ROOT = Path(__file__).resolve().parent.parent
BUNDLES_PATH = REPO_ROOT / "memory-bundles"
RETROACTIVE_LOG = BUNDLES_PATH / "retroactive-ingestion-log.md"


class RetroactiveIngestor:
    """Retroactively apply MMI to all historical data"""
    
    def __init__(self):
        self.mmi = MassiveMicroIngestor()
        self.files_ingested = 0
        self.total_components = 0
        self.errors = []
    
    def ingest_all_files(self):
        """Ingest all repository files"""
        print("[RETROACTIVE] Starting repository-wide ingestion...")
        
        # File patterns to ingest
        patterns = [
            "**/*.md",
            "**/*.json",
            "**/*.yaml",
            "**/*.yml",
            "**/*.py",
            "**/*.js",
            "**/*.ts",
            "**/*.txt",
        ]
        
        # Directories to skip
        skip_dirs = {".git", "node_modules", "__pycache__", ".vscode", "site"}
        
        all_files = []
        for pattern in patterns:
            for file_path in REPO_ROOT.glob(pattern):
                # Skip files in excluded directories
                if any(skip_dir in file_path.parts for skip_dir in skip_dirs):
                    continue
                all_files.append(file_path)
        
        print(f"[RETROACTIVE] Found {len(all_files)} files to ingest")
        
        for file_path in all_files:
            try:
                self._ingest_file(file_path)
            except Exception as e:
                error_msg = f"Error ingesting {file_path}: {str(e)}"
                print(f"[RETROACTIVE] {error_msg}")
                self.errors.append(error_msg)
        
        print(f"[RETROACTIVE] Repository ingestion complete: {self.files_ingested} files processed")
    
    def _ingest_file(self, file_path: Path):
        """Ingest a single file"""
        relative_path = file_path.relative_to(REPO_ROOT)
        
        # Read file content
        try:
            content = file_path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            # Skip binary files
            return
        
        # Create payload structure
        payload = {
            "file_path": str(relative_path),
            "file_type": file_path.suffix,
            "content": content,
            "size_bytes": len(content),
            "line_count": len(content.split('\n')),
            "modified_time": datetime.fromtimestamp(file_path.stat().st_mtime, tz=timezone.utc).isoformat(),
        }
        
        # Parse structured content
        if file_path.suffix == '.json':
            try:
                payload["parsed_data"] = json.loads(content)
            except json.JSONDecodeError:
                pass
        
        # Ingest with MMI
        result = self.mmi.ingest_payload(payload, f"file:{relative_path}")
        
        # Track stats
        self.files_ingested += 1
        self.total_components += sum(d['count'] for d in result['granularity_levels'].values())
        
        if self.files_ingested % 10 == 0:
            print(f"[RETROACTIVE] Progress: {self.files_ingested} files, {self.total_components} components")
    
    def ingest_memory_bundles(self):
        """Ingest all memory bundle files"""
        print("[RETROACTIVE] Ingesting memory bundles...")
        
        if not BUNDLES_PATH.exists():
            print("[RETROACTIVE] No memory bundles directory found")
            return
        
        bundle_files = list(BUNDLES_PATH.glob("*.md")) + list(BUNDLES_PATH.glob("*.json"))
        
        for bundle_file in bundle_files:
            # Skip the retroactive log itself
            if bundle_file == RETROACTIVE_LOG:
                continue
            
            try:
                content = bundle_file.read_text(encoding='utf-8')
                
                payload = {
                    "bundle_name": bundle_file.name,
                    "bundle_type": bundle_file.suffix,
                    "content": content,
                    "size": len(content),
                }
                
                # Parse JSON bundles
                if bundle_file.suffix == '.json':
                    try:
                        payload["data"] = json.loads(content)
                    except json.JSONDecodeError:
                        pass
                
                result = self.mmi.ingest_payload(payload, f"bundle:{bundle_file.name}")
                self.files_ingested += 1
                self.total_components += sum(d['count'] for d in result['granularity_levels'].values())
                
            except Exception as e:
                error_msg = f"Error ingesting bundle {bundle_file.name}: {str(e)}"
                print(f"[RETROACTIVE] {error_msg}")
                self.errors.append(error_msg)
        
        print(f"[RETROACTIVE] Memory bundle ingestion complete")
    
    def ingest_system_state(self):
        """Ingest current system state"""
        print("[RETROACTIVE] Ingesting system state...")
        
        # Ingest manifests
        manifest_files = [
            REPO_ROOT / "barrot_manifest.json",
            REPO_ROOT / "build_manifest.yaml",
            REPO_ROOT / "app.json",
            REPO_ROOT / "package.json",
        ]
        
        for manifest_file in manifest_files:
            if manifest_file.exists():
                try:
                    content = manifest_file.read_text()
                    
                    payload = {
                        "manifest_type": manifest_file.name,
                        "content": content,
                    }
                    
                    if manifest_file.suffix == '.json':
                        try:
                            payload["data"] = json.loads(content)
                        except json.JSONDecodeError:
                            pass
                    
                    result = self.mmi.ingest_payload(payload, f"manifest:{manifest_file.name}")
                    self.files_ingested += 1
                    self.total_components += sum(d['count'] for d in result['granularity_levels'].values())
                    
                except Exception as e:
                    error_msg = f"Error ingesting manifest {manifest_file.name}: {str(e)}"
                    print(f"[RETROACTIVE] {error_msg}")
                    self.errors.append(error_msg)
        
        print("[RETROACTIVE] System state ingestion complete")
    
    def ingest_git_history(self):
        """Ingest git commit history and metadata"""
        print("[RETROACTIVE] Ingesting git history...")
        
        try:
            # Get recent commit history
            result = subprocess.run(
                ["git", "log", "--pretty=format:%H|%an|%ae|%ad|%s", "-n", "100"],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                check=True
            )
            
            commits = []
            for line in result.stdout.split('\n'):
                if line:
                    parts = line.split('|')
                    if len(parts) >= 5:
                        commits.append({
                            "hash": parts[0],
                            "author": parts[1],
                            "email": parts[2],
                            "date": parts[3],
                            "message": parts[4],
                        })
            
            payload = {
                "source": "git_history",
                "commit_count": len(commits),
                "commits": commits,
            }
            
            result = self.mmi.ingest_payload(payload, "git:history")
            self.files_ingested += 1
            self.total_components += sum(d['count'] for d in result['granularity_levels'].values())
            
        except subprocess.CalledProcessError as e:
            error_msg = f"Error ingesting git history: {str(e)}"
            print(f"[RETROACTIVE] {error_msg}")
            self.errors.append(error_msg)
        
        print("[RETROACTIVE] Git history ingestion complete")
    
    def ingest_documentation(self):
        """Ingest all documentation files with special handling"""
        print("[RETROACTIVE] Ingesting documentation...")
        
        doc_files = [
            "README.md",
            "INGESTION_MANIFEST.md",
            "MMI_ANALYSIS_REPORT.md",
            "MMI_COMPLETION_SUMMARY.md",
            "AGI_PUZZLE_PROTOCOL.md",
            "AUTONOMOUS_OPERATIONS_PROTOCOL.md",
            "WORKFLOW_TROUBLESHOOTING.md",
        ]
        
        for doc_file in doc_files:
            file_path = REPO_ROOT / doc_file
            if file_path.exists():
                try:
                    content = file_path.read_text()
                    
                    payload = {
                        "document": doc_file,
                        "content": content,
                        "word_count": len(content.split()),
                        "line_count": len(content.split('\n')),
                    }
                    
                    result = self.mmi.ingest_payload(payload, f"doc:{doc_file}")
                    self.files_ingested += 1
                    self.total_components += sum(d['count'] for d in result['granularity_levels'].values())
                    
                except Exception as e:
                    error_msg = f"Error ingesting doc {doc_file}: {str(e)}"
                    print(f"[RETROACTIVE] {error_msg}")
                    self.errors.append(error_msg)
        
        print("[RETROACTIVE] Documentation ingestion complete")
    
    def finalize_retroactive_ingestion(self):
        """Finalize retroactive ingestion and generate report"""
        print("[RETROACTIVE] Finalizing retroactive ingestion...")
        
        # Generate summary
        summary = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "files_ingested": self.files_ingested,
            "total_components": self.total_components,
            "errors": len(self.errors),
            "error_messages": self.errors,
            "mmi_manifest": self.mmi.manifest,
        }
        
        # Finalize with MMI
        final_result = self.mmi.finalize_ingestion(summary)
        
        # Log the retroactive ingestion
        self._log_retroactive_ingestion(final_result)
        
        print(f"[RETROACTIVE] ════════════════════════════════════════")
        print(f"[RETROACTIVE] Retroactive Ingestion Complete!")
        print(f"[RETROACTIVE] Files Ingested: {self.files_ingested}")
        print(f"[RETROACTIVE] Total Components: {self.total_components}")
        print(f"[RETROACTIVE] Errors: {len(self.errors)}")
        print(f"[RETROACTIVE] ════════════════════════════════════════")
        
        return final_result
    
    def _log_retroactive_ingestion(self, result: dict):
        """Log retroactive ingestion results"""
        BUNDLES_PATH.mkdir(parents=True, exist_ok=True)
        
        log_entry = f"""
# Retroactive MMI Ingestion Report

**Timestamp**: {result['timestamp']}  
**Status**: ✅ COMPLETE

## Summary

- **Files Ingested**: {result['files_ingested']}
- **Total Components**: {result['total_components']}
- **Errors**: {result['errors']}

## Ingestion Scope

### Repository Files
- All .md, .json, .yaml, .py, .js, .ts files
- Configuration files
- Documentation files

### Memory Bundles
- All historical bundle files
- All log files
- All state files

### System State
- barrot_manifest.json
- build_manifest.yaml
- app.json
- package.json

### Git History
- Recent commit history
- Author metadata
- Commit messages

## MMI Manifest State

```json
{json.dumps(result['mmi_manifest'], indent=2)}
```

## Errors Encountered

"""
        if result['error_messages']:
            for error in result['error_messages']:
                log_entry += f"- {error}\n"
        else:
            log_entry += "- None\n"
        
        log_entry += f"""

## Next Steps

- [ ] Review ingestion results
- [ ] Address any errors
- [ ] Verify granularity coverage
- [ ] Confirm gap-filling effectiveness
- [ ] Monitor proposed process implementations

---

**Generated by**: Retroactive MMI Engine  
**Version**: 1.0.0
"""
        
        with open(RETROACTIVE_LOG, 'w') as f:
            f.write(log_entry)
        
        print(f"[RETROACTIVE] Logged to {RETROACTIVE_LOG}")


def main():
    """Main execution"""
    print("[RETROACTIVE] ════════════════════════════════════════════════")
    print("[RETROACTIVE] Retroactive Massive Micro Ingestion")
    print("[RETROACTIVE] Applying MMI to all historical data")
    print("[RETROACTIVE] ════════════════════════════════════════════════\n")
    
    ingestor = RetroactiveIngestor()
    
    # Ingest everything
    ingestor.ingest_all_files()
    ingestor.ingest_memory_bundles()
    ingestor.ingest_system_state()
    ingestor.ingest_git_history()
    ingestor.ingest_documentation()
    
    # Finalize
    final_result = ingestor.finalize_retroactive_ingestion()
    
    return final_result


if __name__ == "__main__":
    main()
