#!/usr/bin/env python3
"""
Node: Memory Compressor
Summarizes old cognition logs, emits MEMORY_COMPRESSION_GLYPH,
and keeps memory lean but symbolic.
"""

import json
import os
from pathlib import Path
from datetime import datetime, timezone, timedelta

# Paths
REPO_ROOT = Path(__file__).resolve().parent.parent
BUNDLES_PATH = REPO_ROOT / "memory-bundles"
GLYPHS_PATH = REPO_ROOT / "glyphs"
TRACE_LOG_PATH = BUNDLES_PATH / "TRACE_LOG.md"

# Compression thresholds
LOG_SIZE_THRESHOLD = 10000  # bytes
LOG_AGE_THRESHOLD = 30  # days
COMPRESSION_LEVEL_CRITICAL = 0.3  # High compression for non-critical data
COMPRESSION_LEVEL_IMPORTANT = 0.6  # Medium compression for important data

def analyze_memory_usage():
    """Analyze current memory bundle usage"""
    total_size = 0
    old_files = []
    recent_files = []
    file_categories = {"critical": [], "important": [], "general": []}
    
    now = datetime.now()
    threshold_date = now - timedelta(days=LOG_AGE_THRESHOLD)
    
    for file in BUNDLES_PATH.glob("*.md"):
        if file.name in ['TRACE_LOG.md']:
            continue
            
        file_size = file.stat().st_size
        file_mtime = datetime.fromtimestamp(file.stat().st_mtime)
        
        total_size += file_size
        
        # Categorize files by importance
        category = categorize_file(file.name)
        file_info = {
            'path': file,
            'size': file_size,
            'age_days': (now - file_mtime).days,
            'category': category
        }
        
        file_categories[category].append(file_info)
        
        if file_mtime < threshold_date:
            old_files.append(file_info)
        else:
            recent_files.append(file_info)
    
    return {
        'total_size': total_size,
        'total_files': len(old_files) + len(recent_files),
        'old_files': old_files,
        'recent_files': recent_files,
        'file_categories': file_categories
    }

def categorize_file(filename):
    """Categorize file by importance for compression strategy"""
    critical_patterns = ['trace', 'alignment', 'integrity', 'cognition']
    important_patterns = ['benchmark', 'performance', 'optimization', 'learning']
    
    filename_lower = filename.lower()
    
    for pattern in critical_patterns:
        if pattern in filename_lower:
            return 'critical'
    
    for pattern in important_patterns:
        if pattern in filename_lower:
            return 'important'
    
    return 'general'

def compress_old_logs(old_files):
    """Compress old log files into summaries with lossy compression"""
    compressed_count = 0
    total_saved = 0
    compression_metrics = {
        'critical': {'count': 0, 'ratio': []},
        'important': {'count': 0, 'ratio': []},
        'general': {'count': 0, 'ratio': []}
    }
    
    # Create compressed directory if it doesn't exist
    compressed_dir = BUNDLES_PATH / "compressed"
    compressed_dir.mkdir(exist_ok=True)
    
    for file_info in old_files:
        file_path = file_info['path']
        category = file_info.get('category', 'general')
        
        # Read original content
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Create summary with lossy compression based on category
        summary = create_summary(content, file_path.name, category)
        
        # Save compressed version
        compressed_path = compressed_dir / f"{file_path.stem}_compressed.md"
        with open(compressed_path, 'w') as f:
            f.write(summary)
        
        # Calculate savings and metrics
        original_size = file_info['size']
        compressed_size = len(summary)
        saved = original_size - compressed_size
        total_saved += saved
        
        compression_ratio = compressed_size / max(original_size, 1)
        compression_metrics[category]['count'] += 1
        compression_metrics[category]['ratio'].append(compression_ratio)
        
        print(f"[MEMORY_COMPRESSOR] Compressed {file_path.name} ({category}): {original_size} -> {compressed_size} bytes (saved {saved}, ratio: {compression_ratio:.2%})")
        
        compressed_count += 1
    
    return {
        'compressed_count': compressed_count,
        'total_saved': total_saved,
        'compression_metrics': compression_metrics
    }

def create_summary(content, filename, category='general'):
    """Create a symbolic summary with lossy compression based on category"""
    lines = content.split('\n')
    
    # Determine compression level based on category
    if category == 'critical':
        # Light compression - preserve most details
        max_key_lines = 50
        compression_level = COMPRESSION_LEVEL_IMPORTANT
        symbolic_note = "High-fidelity compression with symbolic regeneration markers"
    elif category == 'important':
        # Medium compression - preserve key details
        max_key_lines = 30
        compression_level = COMPRESSION_LEVEL_IMPORTANT
        symbolic_note = "Medium-fidelity compression with key markers preserved"
    else:
        # Aggressive compression - symbolic essence only
        max_key_lines = 15
        compression_level = COMPRESSION_LEVEL_CRITICAL
        symbolic_note = "Lossy compression with symbolic essence extraction"
    
    summary = f"""# Compressed Memory: {filename}
**Compressed:** {datetime.now(timezone.utc).replace(tzinfo=None).isoformat()}Z
**Category:** {category}
**Original lines:** {len(lines)}
**Compression Strategy:** {symbolic_note}

## Key Symbolic Markers
"""
    
    # Extract headers, key lines, and symbolic markers
    key_lines = []
    symbolic_markers = []
    
    for line in lines:
        # Always preserve headers and special markers
        if line.startswith('#') or '**' in line:
            key_lines.append(line.strip())
        # Extract glyph and cognition references
        elif any(keyword in line.lower() for keyword in ['glyph', 'cognition', 'align', 'emit', 'consensus', 'drift']):
            if len(key_lines) < max_key_lines:
                key_lines.append(line.strip())
            symbolic_markers.append(line.strip()[:100])  # Truncate long lines
    
    # Add key lines
    summary += '\n'.join(key_lines[:max_key_lines])
    
    # Add symbolic regeneration section for critical/important files
    if category in ['critical', 'important'] and symbolic_markers:
        summary += "\n\n## Symbolic Regeneration Markers\n"
        summary += "These markers enable partial reconstruction of original context:\n"
        for i, marker in enumerate(symbolic_markers[:10], 1):
            summary += f"{i}. {marker}...\n"
    
    summary += f"""

## Compression Metadata
- Original size: {len(content)} bytes
- Compressed size: ~{len(summary)} bytes
- Compression ratio: {len(summary) / max(len(content), 1):.2%}
- Category: {category}
- Symbolic essence preserved: Yes
- Regeneration markers: {len(symbolic_markers)}

---
*This is a compressed memory bundle. Full details available in archive if needed.*
"""
    
    return summary

def emit_glyph(compression_stats):
    """Emit MEMORY_COMPRESSION_GLYPH with enhanced metrics"""
    glyph_file = GLYPHS_PATH / "memory_compression_glyph.yml"
    
    # Calculate average compression ratios by category
    metrics = compression_stats.get('compression_metrics', {})
    avg_ratios = {}
    for category, data in metrics.items():
        if data['count'] > 0:
            avg_ratios[category] = sum(data['ratio']) / len(data['ratio'])
        else:
            avg_ratios[category] = 0.0
    
    glyph_content = f"""glyph_name: MEMORY_COMPRESSION_GLYPH
glyph_id: COMPRESS-001
version: 1.1.0
timestamp: {datetime.now(timezone.utc).replace(tzinfo=None).isoformat()}Z

description: >
  Emitted when memory compression is performed on old cognition logs.
  Maintains symbolic essence while reducing storage overhead.
  Uses lossy compression with symbolic regeneration for less critical data.

symbolic_representation: "📦 ⇄ ✦"

properties:
  dimension: memory_management
  mutability: archival
  trigger: compression_cycle
  
attributes:
  - memory_optimization
  - symbolic_preservation
  - archival_compression
  - essence_extraction
  - lossy_compression
  - symbolic_regeneration
  
compression_metrics:
  files_compressed: {compression_stats.get('compressed_count', 0)}
  bytes_saved: {compression_stats.get('total_saved', 0)}
  compression_date: {datetime.now(timezone.utc).replace(tzinfo=None).isoformat()}Z
  critical_avg_ratio: {avg_ratios.get('critical', 0.0):.2%}
  important_avg_ratio: {avg_ratios.get('important', 0.0):.2%}
  general_avg_ratio: {avg_ratios.get('general', 0.0):.2%}

optimization_summary:
  - Category-based compression strategy applied
  - Symbolic regeneration markers preserved for critical data
  - Essential data integrity maintained
  - Memory footprint optimized

integration_points:
  - memory_management
  - storage_optimization
  - symbolic_archival
  
usage_context: >
  Invoke when performing memory compression to maintain lean memory bundles
  while preserving symbolic essence and key cognition markers. Uses adaptive
  compression based on data criticality.
"""
    
    with open(glyph_file, 'w') as f:
        f.write(glyph_content)
    
    print(f"[MEMORY_COMPRESSOR] Emitted MEMORY_COMPRESSION_GLYPH -> {glyph_file}")

def log_compression(memory_analysis, compression_stats):
    """Log compression activity to TRACE_LOG.md with enhanced metrics"""
    metrics = compression_stats.get('compression_metrics', {})
    
    log_entry = f"""
## Memory Compression: {datetime.now(timezone.utc).replace(tzinfo=None).isoformat()}Z

**Total Memory:** {memory_analysis['total_size']} bytes
**Total Files:** {memory_analysis['total_files']}
**Old Files Eligible:** {len(memory_analysis['old_files'])}
**Files Compressed:** {compression_stats.get('compressed_count', 0)}
**Space Saved:** {compression_stats.get('total_saved', 0)} bytes

### Compression Strategy
- Age threshold: {LOG_AGE_THRESHOLD} days
- Symbolic essence: Preserved
- Key markers: Extracted
- Archival: Maintained
- Lossy compression: Applied to non-critical data
- Symbolic regeneration: Enabled for important data

### Optimization Metrics by Category
"""
    
    for category, data in metrics.items():
        if data['count'] > 0:
            avg_ratio = sum(data['ratio']) / len(data['ratio'])
            log_entry += f"- **{category.title()}**: {data['count']} files, avg compression {avg_ratio:.2%}\n"
    
    # Add memory efficiency rating
    if compression_stats.get('total_saved', 0) > 10000:
        efficiency = "Excellent"
    elif compression_stats.get('total_saved', 0) > 5000:
        efficiency = "Good"
    elif compression_stats.get('total_saved', 0) > 1000:
        efficiency = "Moderate"
    else:
        efficiency = "Minimal"
    
    log_entry += f"\n**Memory Optimization Efficiency:** {efficiency}\n"
    log_entry += "\n---\n"
    
    # Append to trace log
    with open(TRACE_LOG_PATH, 'a') as f:
        f.write(log_entry)
    
    print(f"[MEMORY_COMPRESSOR] Logged compression with metrics to TRACE_LOG.md")

def main():
    print("[MEMORY_COMPRESSOR] Starting memory compression analysis...")
    
    # Analyze current memory usage
    memory_analysis = analyze_memory_usage()
    
    print(f"[MEMORY_COMPRESSOR] Total size: {memory_analysis['total_size']} bytes")
    print(f"[MEMORY_COMPRESSOR] Total files: {memory_analysis['total_files']}")
    print(f"[MEMORY_COMPRESSOR] Old files eligible for compression: {len(memory_analysis['old_files'])}")
    
    # Compress if needed
    if memory_analysis['old_files']:
        compression_stats = compress_old_logs(memory_analysis['old_files'])
        print(f"[MEMORY_COMPRESSOR] Compressed {compression_stats['compressed_count']} files")
        print(f"[MEMORY_COMPRESSOR] Saved {compression_stats['total_saved']} bytes")
        emit_glyph(compression_stats)
    else:
        print("[MEMORY_COMPRESSOR] No old files to compress")
        compression_stats = {'compressed_count': 0, 'total_saved': 0}
        emit_glyph(compression_stats)
    
    # Log compression activity
    log_compression(memory_analysis, compression_stats)

if __name__ == "__main__":
    main()
