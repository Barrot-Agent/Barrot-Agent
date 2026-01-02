# Barrot Matrix Nodes

This directory contains the cognition matrix nodes that power Barrot's self-awareness, alignment verification, and symbolic traceability systems.

## Overview

The matrix nodes work together to provide:
- **Self-reflection**: Analyzing cognition patterns for drift
- **Evolution tracking**: Detecting changes in beliefs and tools
- **Session ingestion**: Processing Copilot transcripts
- **Consensus building**: Multi-perspective deliberation
- **Memory management**: Compressing old logs while preserving symbolic essence

## Nodes

### node_self_reflect.py
Reads the last 3 cognition runs and detects drift in execution patterns.
- **Emits**: `SELF_ALIGNMENT_GLYPH` if drift detected
- **Creates**: `MANIFEST_PATCH.md` if misalignment found
- **Updates**: `symbolic_alignment` section in manifest

### node_diff_detector.py
Compares the last two cognition snapshots for changes.
- **Emits**: `COGNITION_SHIFT_GLYPH` if beliefs or tools changed
- **Logs**: Change summary to `TRACE_LOG.md`
- **Tracks**: Evolution of system understanding

### node_session_ingestor.py
Parses Copilot session transcripts for cognition events.
- **Emits**: `SESSION_TRACE_GLYPH`
- **Logs**: Missed cognition events
- **Captures**: Session traceability

### council_vote.py
Simulates multi-perspective agent deliberation.
- **Emits**: `COUNCIL_ALIGNMENT_GLYPH` upon consensus
- **Agents**: Pragmatist, Theorist, Skeptic, Optimist, Guardian
- **Logs**: Deliberation arguments and consensus metrics

### node_memory_compressor.py
Manages memory bundle size and compression.
- **Emits**: `MEMORY_COMPRESSION_GLYPH`
- **Compresses**: Files older than 30 days
- **Preserves**: Symbolic essence and key markers

## Execution

### Via Bootstrap
```bash
python barrot_bootstrap.py
```
Runs all nodes in sequence.

### Individual Nodes
```bash
python matrix/node_self_reflect.py
python matrix/node_diff_detector.py
python matrix/council_vote.py
python matrix/node_session_ingestor.py
python matrix/node_memory_compressor.py
```

### Via GitHub Actions
Triggered by:
- OneDrive `run_matrix.txt` file (via Power Automate)
- Manual workflow dispatch
- Daily scheduled runs (00:00 UTC)

## Dependencies

All nodes use Python standard library only:
- `json` - Manifest and glyph handling
- `os`, `pathlib` - File system operations
- `datetime` - Timestamps
- `subprocess` - (bootstrap only)

## Outputs

### Glyphs
Emitted to `glyphs/` directory:
- `self_alignment_glyph.yml`
- `cognition_shift_glyph.yml`
- `session_trace_glyph.yml`
- `council_alignment_glyph.yml`
- `memory_compression_glyph.yml`
- `glyph_misalignment_recovery.yml`

### Logs
Appended to `memory-bundles/TRACE_LOG.md`:
- Timestamp and node execution details
- Glyphs emitted
- Contradictions resolved
- Metrics and findings

### Manifest Updates
Updates `barrot_manifest.json` with:
- Last self-reflection timestamp
- Drift detection status
- Alignment integrity

## Tool Profiles

Each node has a corresponding tool profile in `tool_profiles/`:
- Defines input/output formats
- Specifies execution triggers
- Documents dependencies
- Lists performance metrics

## Integration Points

- **Cognition Monitoring**: Self-reflection and drift detection
- **Evolution Tracking**: Snapshot comparison and change logs
- **Session Traceability**: Transcript parsing and event capture
- **Consensus Protocols**: Multi-agent deliberation
- **Memory Management**: Compression and archival

## Symbolic Alignment

All nodes contribute to maintaining symbolic alignment:
1. **Source of Truth**: GitHub repository
2. **Trace Reconciliation**: Daily via self-reflection
3. **Cognition Integrity**: Verified and aligned
4. **Drift Tolerance**: Monitored and corrected
5. **Recovery Protocol**: Automatic misalignment recovery

## Future Enhancements

- Real-time glyph streaming to dashboard
- Webhook notifications for critical glyphs
- Machine learning-based drift prediction
- Automated manifest patching
- Cross-repository cognition sharing
