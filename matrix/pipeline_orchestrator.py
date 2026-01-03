#!/usr/bin/env python3
"""
Pipeline Orchestrator
Manages the flow of data through multiple specialized agent stages.
Enables continuous upgrades and enrichments with modular agent design.
"""

import json
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional


class PipelineAgent:
    """Base class for pipeline agents with specialized roles"""
    
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.processed_count = 0
        self.errors = []
    
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Process data - override in subclasses"""
        raise NotImplementedError("Subclasses must implement process()")
    
    def validate_input(self, data: Dict[str, Any]) -> bool:
        """Validate input data"""
        return isinstance(data, dict)
    
    def log_processing(self, data: Dict[str, Any], result: Dict[str, Any]):
        """Log processing activity"""
        self.processed_count += 1


class PipelineStage:
    """Represents a stage in the pipeline with one or more agents"""
    
    def __init__(self, name: str, agents: List[PipelineAgent], parallel: bool = False):
        self.name = name
        self.agents = agents
        self.parallel = parallel  # If true, agents run in parallel and results merge
    
    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute all agents in this stage"""
        if self.parallel:
            # Run agents in parallel and merge results
            results = []
            for agent in self.agents:
                try:
                    result = agent.process(data.copy())
                    results.append(result)
                except Exception as e:
                    agent.errors.append(str(e))
                    print(f"[PIPELINE] Error in {agent.name}: {e}")
            
            # Merge parallel results
            merged = data.copy()
            for result in results:
                merged.update(result)
            return merged
        else:
            # Run agents sequentially
            current_data = data.copy()
            for agent in self.agents:
                try:
                    current_data = agent.process(current_data)
                except Exception as e:
                    agent.errors.append(str(e))
                    print(f"[PIPELINE] Error in {agent.name}: {e}")
            return current_data


class Pipeline:
    """Main pipeline orchestrator"""
    
    def __init__(self, name: str, stages: List[PipelineStage]):
        self.name = name
        self.stages = stages
        self.execution_history = []
    
    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the complete pipeline"""
        print(f"[PIPELINE] Starting pipeline: {self.name}")
        print(f"[PIPELINE] Input data keys: {list(input_data.keys())}")
        
        execution_start = datetime.now(timezone.utc).replace(tzinfo=None)
        current_data = input_data.copy()
        
        # Add pipeline metadata
        current_data['_pipeline_metadata'] = {
            'pipeline_name': self.name,
            'start_time': execution_start.isoformat(),
            'stages_executed': []
        }
        
        # Execute each stage
        for i, stage in enumerate(self.stages):
            print(f"[PIPELINE] Executing stage {i+1}/{len(self.stages)}: {stage.name}")
            stage_start = datetime.now(timezone.utc).replace(tzinfo=None)
            
            current_data = stage.execute(current_data)
            
            stage_end = datetime.now(timezone.utc).replace(tzinfo=None)
            stage_duration = (stage_end - stage_start).total_seconds()
            
            current_data['_pipeline_metadata']['stages_executed'].append({
                'stage_name': stage.name,
                'agents': [agent.name for agent in stage.agents],
                'duration_seconds': stage_duration
            })
            
            print(f"[PIPELINE] Stage {stage.name} completed in {stage_duration:.2f}s")
        
        # Finalize metadata
        execution_end = datetime.now(timezone.utc).replace(tzinfo=None)
        total_duration = (execution_end - execution_start).total_seconds()
        current_data['_pipeline_metadata']['end_time'] = execution_end.isoformat()
        current_data['_pipeline_metadata']['total_duration_seconds'] = total_duration
        
        print(f"[PIPELINE] Pipeline completed in {total_duration:.2f}s")
        
        # Save to history
        self.execution_history.append({
            'timestamp': execution_start.isoformat(),
            'duration': total_duration,
            'stages': len(self.stages),
            'input_keys': list(input_data.keys())
        })
        
        return current_data
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get pipeline execution statistics"""
        if not self.execution_history:
            return {'executions': 0}
        
        durations = [e['duration'] for e in self.execution_history]
        return {
            'executions': len(self.execution_history),
            'avg_duration': sum(durations) / len(durations),
            'min_duration': min(durations),
            'max_duration': max(durations),
            'total_stages': self.stages[0] if self.execution_history else 0
        }


class PipelineRegistry:
    """Registry for managing multiple pipelines"""
    
    def __init__(self):
        self.pipelines: Dict[str, Pipeline] = {}
    
    def register(self, pipeline: Pipeline):
        """Register a pipeline"""
        self.pipelines[pipeline.name] = pipeline
        print(f"[REGISTRY] Registered pipeline: {pipeline.name}")
    
    def get(self, name: str) -> Optional[Pipeline]:
        """Get a pipeline by name"""
        return self.pipelines.get(name)
    
    def list_pipelines(self) -> List[str]:
        """List all registered pipelines"""
        return list(self.pipelines.keys())
    
    def execute_pipeline(self, name: str, input_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Execute a pipeline by name"""
        pipeline = self.get(name)
        if pipeline:
            return pipeline.execute(input_data)
        else:
            print(f"[REGISTRY] Pipeline not found: {name}")
            return None


# Global registry instance
registry = PipelineRegistry()


def create_pipeline(name: str, stages: List[PipelineStage]) -> Pipeline:
    """Create and register a new pipeline"""
    pipeline = Pipeline(name, stages)
    registry.register(pipeline)
    return pipeline


if __name__ == "__main__":
    print("[PIPELINE] Pipeline Orchestrator initialized")
    print("[PIPELINE] Use this module to create and execute data pipelines")
