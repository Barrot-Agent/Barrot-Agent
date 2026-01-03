# Pipeline Configuration Guide

## Overview

The processing pipeline is designed to be modular and extensible. Each agent in the pipeline performs a specific transformation, annotation, or validation on the data.

## Pipeline Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    PROCESSING PIPELINE                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Input Data                                                  │
│      │                                                       │
│      ▼                                                       │
│  ┌──────────────────┐                                       │
│  │ Ingestion Agent  │ Captures & validates events          │
│  └────────┬─────────┘                                       │
│           │                                                  │
│           ▼                                                  │
│  ┌──────────────────┐                                       │
│  │ Enrichment Agent │ Adds context & metadata              │
│  └────────┬─────────┘                                       │
│           │                                                  │
│           ▼                                                  │
│  ┌──────────────────┐                                       │
│  │ Analysis Agent   │ Extracts insights & patterns         │
│  └────────┬─────────┘                                       │
│           │                                                  │
│           ▼                                                  │
│  ┌──────────────────┐                                       │
│  │ Validation Agent │ Ensures data quality                 │
│  └────────┬─────────┘                                       │
│           │                                                  │
│           ▼                                                  │
│  ┌──────────────────┐                                       │
│  │Integration Agent │ Connects to existing systems         │
│  └────────┬─────────┘                                       │
│           │                                                  │
│           ▼                                                  │
│  Output Data (enriched, validated, integrated)              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Agent Roles

### 1. Ingestion Agent
**Purpose**: Captures and validates incoming events
**Input**: Raw event data
**Output**: Validated event with ingestion metadata
**Operations**:
- Validates data format
- Adds ingestion timestamp
- Checks for required fields
- Marks data as validated

### 2. Enrichment Agent
**Purpose**: Adds context, metadata, and related information
**Input**: Validated event
**Output**: Event enriched with contextual data
**Operations**:
- Adds symbolic representations
- Classifies into categories
- Adds temporal context
- Enriches with domain knowledge

### 3. Analysis Agent
**Purpose**: Extracts insights, patterns, and implications
**Input**: Enriched event
**Output**: Event with extracted insights and patterns
**Operations**:
- Identifies patterns
- Extracts implications
- Generates insights
- Calculates completeness score

### 4. Validation Agent
**Purpose**: Ensures data quality and consistency
**Input**: Analyzed event
**Output**: Validated event with quality metrics
**Operations**:
- Runs quality checks
- Validates stage completion
- Checks data consistency
- Calculates quality score

### 5. Integration Agent
**Purpose**: Integrates processed data with existing systems
**Input**: Validated event
**Output**: Fully integrated event
**Operations**:
- Generates glyphs
- Creates trace entries
- Stores processed events
- Connects to repository systems

## Adding New Agents

### Step 1: Create Agent Class

Create a new agent class that inherits from `PipelineAgent`:

```python
from pipeline_orchestrator import PipelineAgent
from typing import Dict, Any

class MyNewAgent(PipelineAgent):
    """Description of what this agent does"""
    
    def __init__(self):
        super().__init__("MyNewAgent", "Agent Role Description")
    
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Process data and perform transformations"""
        
        # Add your processing logic here
        data['my_agent_output'] = {
            'timestamp': datetime.now(timezone.utc).replace(tzinfo=None).isoformat(),
            'agent': self.name,
            'result': 'processing_complete'
        }
        
        self.log_processing(data, data)
        return data
```

### Step 2: Add Agent to Pipeline

Add the new agent to an existing stage or create a new stage:

```python
from pipeline_orchestrator import PipelineStage
from pipeline_agents import MyNewAgent

# Option 1: Add to existing stage
enrichment_stage = PipelineStage(
    name="Enrichment",
    agents=[EnrichmentAgent(), MyNewAgent()],  # Add your agent
    parallel=False
)

# Option 2: Create new stage
my_new_stage = PipelineStage(
    name="MyNewStage",
    agents=[MyNewAgent()],
    parallel=False
)
```

### Step 3: Register in Pipeline

Add the stage to the pipeline:

```python
pipeline = create_pipeline(
    name="my_pipeline",
    stages=[
        ingestion_stage,
        enrichment_stage,
        my_new_stage,  # Add your stage
        validation_stage,
        integration_stage
    ]
)
```

## Parallel Processing

Agents within a stage can run in parallel:

```python
# Create stage with parallel agents
parallel_stage = PipelineStage(
    name="ParallelProcessing",
    agents=[
        Agent1(),
        Agent2(),
        Agent3()
    ],
    parallel=True  # Agents run in parallel, results merge
)
```

## Pipeline Configuration Examples

### Example 1: Simple Sequential Pipeline
```python
pipeline = create_pipeline(
    name="simple_pipeline",
    stages=[
        PipelineStage("Stage1", [Agent1()]),
        PipelineStage("Stage2", [Agent2()]),
        PipelineStage("Stage3", [Agent3()])
    ]
)
```

### Example 2: Mixed Sequential and Parallel
```python
pipeline = create_pipeline(
    name="mixed_pipeline",
    stages=[
        PipelineStage("Ingestion", [IngestionAgent()], parallel=False),
        PipelineStage("Parallel Analysis", [AnalysisAgent1(), AnalysisAgent2()], parallel=True),
        PipelineStage("Validation", [ValidationAgent()], parallel=False)
    ]
)
```

### Example 3: Multi-Agent Stage
```python
pipeline = create_pipeline(
    name="multi_agent_pipeline",
    stages=[
        PipelineStage("Enrichment", [
            ContextAgent(),
            MetadataAgent(),
            ClassificationAgent()
        ], parallel=False)
    ]
)
```

## Using the Pipeline

### Execute a Pipeline
```python
from claude_impact_pipeline import create_claude_impact_pipeline

# Create pipeline
pipeline = create_claude_impact_pipeline()

# Prepare input data
input_data = {
    'event_type': 'my_event',
    'source': 'event_source',
    'data': {...}
}

# Execute pipeline
result = pipeline.execute(input_data)

# Access results
print(f"Quality Score: {result['validation']['quality_score']}")
print(f"Integration Complete: {result['integration']['complete']}")
```

### Get Pipeline Statistics
```python
stats = pipeline.get_statistics()
print(f"Executions: {stats['executions']}")
print(f"Average Duration: {stats['avg_duration']:.2f}s")
```

## Pipeline Registry

The registry allows managing multiple pipelines:

```python
from pipeline_orchestrator import registry

# List all pipelines
pipelines = registry.list_pipelines()

# Get specific pipeline
pipeline = registry.get("claude_code_impact_pipeline")

# Execute by name
result = registry.execute_pipeline("claude_code_impact_pipeline", input_data)
```

## Best Practices

1. **Single Responsibility**: Each agent should have one clear purpose
2. **Immutability**: Agents should not modify input data destructively
3. **Metadata**: Always add metadata about what the agent did
4. **Error Handling**: Use try-catch in stages to handle agent errors gracefully
5. **Logging**: Use the built-in logging methods for consistency
6. **Validation**: Validate inputs and outputs at each stage
7. **Documentation**: Document what each agent does and why

## Future Extensions

The pipeline architecture supports easy addition of:
- **Transformation Agents**: Data format converters
- **Filtering Agents**: Data selection and filtering
- **Aggregation Agents**: Combining data from multiple sources
- **Notification Agents**: Alerting on specific conditions
- **Caching Agents**: Performance optimization
- **Monitoring Agents**: Pipeline health checks
- **Security Agents**: Data sanitization and compliance
- **ML Agents**: Machine learning model inference

## Testing Agents

Create tests for your agents:

```python
def test_my_agent():
    agent = MyNewAgent()
    
    # Test input
    input_data = {'test': 'data'}
    
    # Process
    result = agent.process(input_data)
    
    # Assertions
    assert 'my_agent_output' in result
    assert result['my_agent_output']['result'] == 'processing_complete'
    assert agent.processed_count == 1
```

## Configuration Files

Store pipeline configurations in JSON/YAML:

```yaml
pipeline:
  name: "my_custom_pipeline"
  stages:
    - name: "Ingestion"
      agents: ["IngestionAgent"]
      parallel: false
    - name: "Processing"
      agents: ["Agent1", "Agent2", "Agent3"]
      parallel: true
    - name: "Output"
      agents: ["OutputAgent"]
      parallel: false
```

---

**Status**: Active  
**Version**: 1.0  
**Last Updated**: 2026-01-03
