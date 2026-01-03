#!/usr/bin/env python3
"""
Specialized Pipeline Agents
Each agent performs a specific transformation, annotation, or validation on data.
"""

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, List
from pipeline_orchestrator import PipelineAgent

# Paths
REPO_ROOT = Path(__file__).resolve().parent.parent
BUNDLES_PATH = REPO_ROOT / "memory-bundles"
GLYPHS_PATH = REPO_ROOT / "glyphs"


class IngestionAgent(PipelineAgent):
    """Captures and validates incoming events"""
    
    def __init__(self):
        super().__init__("IngestionAgent", "Event Ingestion & Validation")
    
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest and validate event data"""
        if not self.validate_input(data):
            raise ValueError("Invalid input data format")
        
        # Add ingestion metadata
        data['ingestion'] = {
            'timestamp': datetime.now(timezone.utc).replace(tzinfo=None).isoformat(),
            'agent': self.name,
            'validated': True,
            'source': data.get('source', 'unknown'),
            'event_type': data.get('event_type', 'unknown')
        }
        
        # Validate required fields
        required_fields = ['event_type', 'source']
        missing_fields = [field for field in required_fields if field not in data]
        
        if missing_fields:
            data['ingestion']['warnings'] = [f"Missing recommended field: {field}" for field in missing_fields]
        else:
            data['ingestion']['complete'] = True
        
        self.log_processing(data, data)
        print(f"[{self.name}] Ingested event: {data.get('event_type', 'unknown')}")
        
        return data


class EnrichmentAgent(PipelineAgent):
    """Adds context, metadata, and related information"""
    
    def __init__(self):
        super().__init__("EnrichmentAgent", "Context & Metadata Enrichment")
    
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Enrich data with additional context"""
        
        # Add enrichment metadata
        data['enrichment'] = {
            'timestamp': datetime.now(timezone.utc).replace(tzinfo=None).isoformat(),
            'agent': self.name,
            'context_added': []
        }
        
        # Add symbolic representation
        if 'event_type' in data:
            event_type = data['event_type']
            if 'cognition' in event_type.lower():
                data['symbolic_representation'] = '🧠 ⟿ ✦'
            elif 'code' in event_type.lower():
                data['symbolic_representation'] = '💻 ⟿ ✨'
            else:
                data['symbolic_representation'] = '📝 ⟿ ⚡'
            data['enrichment']['context_added'].append('symbolic_representation')
        
        # Add category classification
        if 'description' in data or 'summary' in data:
            text = data.get('description', data.get('summary', ''))
            
            # Classify based on content
            categories = []
            if 'compression' in text.lower() or 'acceleration' in text.lower():
                categories.append('cognition_compression')
            if 'agent' in text.lower() or 'ai' in text.lower():
                categories.append('agentic_systems')
            if 'prompt' in text.lower() or 'architecture' in text.lower():
                categories.append('prompt_engineering')
            if 'human' in text.lower() or 'team' in text.lower():
                categories.append('human_ai_interaction')
            
            data['categories'] = categories
            data['enrichment']['context_added'].append('categories')
        
        # Add temporal context
        data['temporal_context'] = {
            'processing_date': datetime.now(timezone.utc).replace(tzinfo=None).isoformat(),
            'year': datetime.now().year,
            'relevance_window': 'current'
        }
        data['enrichment']['context_added'].append('temporal_context')
        
        self.log_processing(data, data)
        print(f"[{self.name}] Enriched with {len(data['enrichment']['context_added'])} contexts")
        
        return data


class AnalysisAgent(PipelineAgent):
    """Extracts insights, patterns, and implications"""
    
    def __init__(self):
        super().__init__("AnalysisAgent", "Insight & Pattern Extraction")
    
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze data and extract insights"""
        
        # Add analysis metadata
        data['analysis'] = {
            'timestamp': datetime.now(timezone.utc).replace(tzinfo=None).isoformat(),
            'agent': self.name,
            'insights': [],
            'patterns': [],
            'implications': []
        }
        
        # Extract implications if available
        if 'implications' in data:
            implications_data = data['implications']
            if isinstance(implications_data, list):
                data['analysis']['implications'] = implications_data
            elif isinstance(implications_data, dict):
                data['analysis']['implications'] = list(implications_data.values())
        
        # Analyze categories for patterns
        if 'categories' in data:
            categories = data['categories']
            if 'cognition_compression' in categories:
                data['analysis']['patterns'].append({
                    'pattern': 'cognitive_efficiency',
                    'description': 'Event demonstrates compression of cognitive processes'
                })
            if 'agentic_systems' in categories:
                data['analysis']['patterns'].append({
                    'pattern': 'autonomous_capability',
                    'description': 'Event involves autonomous agent capabilities'
                })
        
        # Generate insights based on content
        if 'summary' in data:
            summary = data['summary']
            if isinstance(summary, str):
                # Simple keyword-based insight extraction
                if 'year' in summary.lower() and 'hour' in summary.lower():
                    data['analysis']['insights'].append({
                        'type': 'temporal_compression',
                        'insight': 'Significant time compression observed in cognitive task completion'
                    })
                if 'team' in summary.lower() and 'agent' in summary.lower():
                    data['analysis']['insights'].append({
                        'type': 'human_ai_parity',
                        'insight': 'AI agent demonstrating capabilities comparable to human teams'
                    })
        
        # Calculate analysis score
        analysis_score = (
            len(data['analysis']['insights']) * 3 +
            len(data['analysis']['patterns']) * 2 +
            len(data['analysis']['implications'])
        )
        data['analysis']['completeness_score'] = analysis_score
        
        self.log_processing(data, data)
        print(f"[{self.name}] Extracted {len(data['analysis']['insights'])} insights, "
              f"{len(data['analysis']['patterns'])} patterns")
        
        return data


class ValidationAgent(PipelineAgent):
    """Ensures data quality and consistency"""
    
    def __init__(self):
        super().__init__("ValidationAgent", "Quality Assurance & Validation")
    
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate data quality and consistency"""
        
        # Add validation metadata
        data['validation'] = {
            'timestamp': datetime.now(timezone.utc).replace(tzinfo=None).isoformat(),
            'agent': self.name,
            'checks': [],
            'passed': True,
            'warnings': [],
            'errors': []
        }
        
        # Check for required pipeline stages
        required_stages = ['ingestion', 'enrichment', 'analysis']
        for stage in required_stages:
            if stage in data:
                data['validation']['checks'].append({
                    'check': f'{stage}_complete',
                    'status': 'passed'
                })
            else:
                data['validation']['warnings'].append(f"Stage '{stage}' not found in data")
                data['validation']['checks'].append({
                    'check': f'{stage}_complete',
                    'status': 'warning'
                })
        
        # Validate data completeness
        if 'analysis' in data:
            analysis = data['analysis']
            if not analysis.get('insights') and not analysis.get('patterns'):
                data['validation']['warnings'].append("Analysis produced no insights or patterns")
        
        # Validate enrichment
        if 'enrichment' in data:
            enrichment = data['enrichment']
            if not enrichment.get('context_added'):
                data['validation']['warnings'].append("No context was added during enrichment")
        
        # Check data consistency
        if '_pipeline_metadata' in data:
            metadata = data['_pipeline_metadata']
            if len(metadata.get('stages_executed', [])) < 3:
                data['validation']['warnings'].append("Fewer than 3 pipeline stages executed")
        
        # Determine overall validation status
        if data['validation']['errors']:
            data['validation']['passed'] = False
        elif data['validation']['warnings']:
            data['validation']['passed'] = True
            data['validation']['status'] = 'passed_with_warnings'
        else:
            data['validation']['status'] = 'passed'
        
        # Calculate quality score
        checks_passed = sum(1 for check in data['validation']['checks'] if check['status'] == 'passed')
        total_checks = len(data['validation']['checks'])
        data['validation']['quality_score'] = (checks_passed / total_checks * 100) if total_checks > 0 else 0
        
        self.log_processing(data, data)
        print(f"[{self.name}] Validation {data['validation']['status']}: "
              f"{checks_passed}/{total_checks} checks passed")
        
        return data


class IntegrationAgent(PipelineAgent):
    """Integrates processed data with existing systems"""
    
    def __init__(self):
        super().__init__("IntegrationAgent", "System Integration")
    
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Integrate data with repository systems"""
        
        # Add integration metadata
        data['integration'] = {
            'timestamp': datetime.now(timezone.utc).replace(tzinfo=None).isoformat(),
            'agent': self.name,
            'integrations': [],
            'outputs': []
        }
        
        # Generate glyph if applicable
        if data.get('event_type') and 'validation' in data and data['validation']['passed']:
            glyph_data = self._generate_glyph(data)
            if glyph_data:
                data['integration']['integrations'].append('glyph_emission')
                data['integration']['outputs'].append(glyph_data)
        
        # Log to trace system
        trace_entry = self._create_trace_entry(data)
        data['integration']['integrations'].append('trace_log')
        data['integration']['outputs'].append(trace_entry)
        
        # Store processed event
        storage_path = self._store_event(data)
        if storage_path:
            data['integration']['integrations'].append('event_storage')
            data['integration']['storage_path'] = str(storage_path)
        
        # Mark integration complete
        data['integration']['complete'] = True
        data['integration']['integration_count'] = len(data['integration']['integrations'])
        
        self.log_processing(data, data)
        print(f"[{self.name}] Integrated with {len(data['integration']['integrations'])} systems")
        
        return data
    
    def _generate_glyph(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a glyph for the processed event"""
        event_type = data.get('event_type', 'UNKNOWN')
        glyph_name = f"{event_type.upper()}_GLYPH"
        
        return {
            'type': 'glyph',
            'name': glyph_name,
            'emitter': self.name,
            'timestamp': datetime.now(timezone.utc).replace(tzinfo=None).isoformat(),
            'symbolic_representation': data.get('symbolic_representation', '✦'),
            'context': {
                'event_type': event_type,
                'categories': data.get('categories', []),
                'quality_score': data.get('validation', {}).get('quality_score', 0)
            }
        }
    
    def _create_trace_entry(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a trace log entry"""
        return {
            'type': 'trace_entry',
            'timestamp': datetime.now(timezone.utc).replace(tzinfo=None).isoformat(),
            'event_type': data.get('event_type', 'unknown'),
            'pipeline': data.get('_pipeline_metadata', {}).get('pipeline_name', 'unknown'),
            'duration': data.get('_pipeline_metadata', {}).get('total_duration_seconds', 0),
            'quality_score': data.get('validation', {}).get('quality_score', 0)
        }
    
    def _store_event(self, data: Dict[str, Any]) -> Path:
        """Store processed event to file"""
        # Ensure directory exists
        events_dir = BUNDLES_PATH / "processed_events"
        events_dir.mkdir(exist_ok=True)
        
        # Create filename based on event type and timestamp
        event_type = data.get('event_type', 'unknown')
        timestamp = datetime.now(timezone.utc).replace(tzinfo=None).strftime('%Y%m%d_%H%M%S')
        filename = f"{event_type}_{timestamp}.json"
        filepath = events_dir / filename
        
        # Save event data
        try:
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)
            return filepath
        except Exception as e:
            print(f"[{self.name}] Error storing event: {e}")
            return None


if __name__ == "__main__":
    print("[PIPELINE_AGENTS] Specialized pipeline agents loaded")
