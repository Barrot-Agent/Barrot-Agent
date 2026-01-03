#!/usr/bin/env python3
"""
Test Suite for Pipeline Processing System
Tests pipeline orchestrator, agents, and integration
"""

import sys
import json
import tempfile
from pathlib import Path
from datetime import datetime

# Add matrix to path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from pipeline_orchestrator import (
    PipelineAgent, PipelineStage, Pipeline, PipelineRegistry,
    create_pipeline, registry
)
from pipeline_agents import (
    IngestionAgent,
    EnrichmentAgent,
    AnalysisAgent,
    ValidationAgent,
    IntegrationAgent
)


class TestAgent(PipelineAgent):
    """Test agent for unit tests"""
    
    def __init__(self, name="TestAgent"):
        super().__init__(name, "Test Agent")
    
    def process(self, data):
        data[f'{self.name}_processed'] = True
        self.log_processing(data, data)
        return data


def test_pipeline_agent_base():
    """Test base PipelineAgent functionality"""
    print("\n[TEST] Testing PipelineAgent base class...")
    
    agent = TestAgent()
    assert agent.name == "TestAgent"
    assert agent.role == "Test Agent"
    assert agent.processed_count == 0
    
    # Test processing
    data = {'test': 'data'}
    result = agent.process(data)
    assert result['TestAgent_processed'] == True
    assert agent.processed_count == 1
    
    # Test validation
    assert agent.validate_input({'key': 'value'}) == True
    assert agent.validate_input("not a dict") == False
    
    print("✓ PipelineAgent base class working correctly")
    return True


def test_pipeline_stage():
    """Test PipelineStage functionality"""
    print("\n[TEST] Testing PipelineStage...")
    
    # Test sequential stage
    agent1 = TestAgent("Agent1")
    agent2 = TestAgent("Agent2")
    stage = PipelineStage("TestStage", [agent1, agent2], parallel=False)
    
    data = {'input': 'data'}
    result = stage.execute(data)
    
    assert 'Agent1_processed' in result
    assert 'Agent2_processed' in result
    assert agent1.processed_count == 1
    assert agent2.processed_count == 1
    
    # Test parallel stage
    agent3 = TestAgent("Agent3")
    agent4 = TestAgent("Agent4")
    parallel_stage = PipelineStage("ParallelStage", [agent3, agent4], parallel=True)
    
    result2 = parallel_stage.execute(data)
    assert 'Agent3_processed' in result2
    assert 'Agent4_processed' in result2
    
    print("✓ PipelineStage working correctly")
    return True


def test_pipeline_execution():
    """Test full pipeline execution"""
    print("\n[TEST] Testing Pipeline execution...")
    
    stage1 = PipelineStage("Stage1", [TestAgent("S1Agent")])
    stage2 = PipelineStage("Stage2", [TestAgent("S2Agent")])
    stage3 = PipelineStage("Stage3", [TestAgent("S3Agent")])
    
    pipeline = Pipeline("TestPipeline", [stage1, stage2, stage3])
    
    input_data = {'test': 'input'}
    result = pipeline.execute(input_data)
    
    # Check all stages processed
    assert 'S1Agent_processed' in result
    assert 'S2Agent_processed' in result
    assert 'S3Agent_processed' in result
    
    # Check metadata
    assert '_pipeline_metadata' in result
    metadata = result['_pipeline_metadata']
    assert metadata['pipeline_name'] == 'TestPipeline'
    assert len(metadata['stages_executed']) == 3
    assert 'start_time' in metadata
    assert 'end_time' in metadata
    assert 'total_duration_seconds' in metadata
    
    # Check execution history
    assert len(pipeline.execution_history) == 1
    
    print("✓ Pipeline execution working correctly")
    return True


def test_pipeline_registry():
    """Test PipelineRegistry functionality"""
    print("\n[TEST] Testing PipelineRegistry...")
    
    test_registry = PipelineRegistry()
    
    # Create and register pipeline
    pipeline = Pipeline("RegistryTest", [])
    test_registry.register(pipeline)
    
    # Test retrieval
    retrieved = test_registry.get("RegistryTest")
    assert retrieved is not None
    assert retrieved.name == "RegistryTest"
    
    # Test listing
    pipelines = test_registry.list_pipelines()
    assert "RegistryTest" in pipelines
    
    print("✓ PipelineRegistry working correctly")
    return True


def test_ingestion_agent():
    """Test IngestionAgent"""
    print("\n[TEST] Testing IngestionAgent...")
    
    agent = IngestionAgent()
    
    input_data = {
        'event_type': 'test_event',
        'source': 'test_source',
        'data': 'test_data'
    }
    
    result = agent.process(input_data)
    
    # Check ingestion metadata
    assert 'ingestion' in result
    assert result['ingestion']['validated'] == True
    assert result['ingestion']['agent'] == 'IngestionAgent'
    assert 'timestamp' in result['ingestion']
    
    # Check warnings for missing fields
    incomplete_data = {'data': 'test'}
    result2 = agent.process(incomplete_data)
    assert 'warnings' in result2['ingestion']
    
    print("✓ IngestionAgent working correctly")
    return True


def test_enrichment_agent():
    """Test EnrichmentAgent"""
    print("\n[TEST] Testing EnrichmentAgent...")
    
    agent = EnrichmentAgent()
    
    input_data = {
        'event_type': 'cognition_test',
        'description': 'This is about compression and acceleration of cognition processes'
    }
    
    result = agent.process(input_data)
    
    # Check enrichment metadata
    assert 'enrichment' in result
    assert 'context_added' in result['enrichment']
    assert len(result['enrichment']['context_added']) > 0
    
    # Check added context
    assert 'symbolic_representation' in result
    assert 'categories' in result
    assert 'temporal_context' in result
    
    # Check category classification
    assert 'cognition_compression' in result['categories']
    
    print("✓ EnrichmentAgent working correctly")
    return True


def test_analysis_agent():
    """Test AnalysisAgent"""
    print("\n[TEST] Testing AnalysisAgent...")
    
    agent = AnalysisAgent()
    
    input_data = {
        'event_type': 'test_event',
        'categories': ['cognition_compression', 'agentic_systems'],
        'summary': 'AI completed in one hour what a team built in a year',
        'implications': ['implication1', 'implication2']
    }
    
    result = agent.process(input_data)
    
    # Check analysis metadata
    assert 'analysis' in result
    assert 'insights' in result['analysis']
    assert 'patterns' in result['analysis']
    assert 'implications' in result['analysis']
    assert 'completeness_score' in result['analysis']
    
    # Check that patterns were identified
    assert len(result['analysis']['patterns']) > 0
    
    # Check insights extracted
    assert len(result['analysis']['insights']) > 0
    
    print("✓ AnalysisAgent working correctly")
    return True


def test_validation_agent():
    """Test ValidationAgent"""
    print("\n[TEST] Testing ValidationAgent...")
    
    agent = ValidationAgent()
    
    # Complete data
    complete_data = {
        'ingestion': {'validated': True},
        'enrichment': {'context_added': ['item1']},
        'analysis': {'insights': [{'insight': 'test'}], 'patterns': []},
        '_pipeline_metadata': {'stages_executed': [1, 2, 3]}
    }
    
    result = agent.process(complete_data)
    
    # Check validation metadata
    assert 'validation' in result
    assert 'checks' in result['validation']
    assert 'passed' in result['validation']
    assert 'quality_score' in result['validation']
    
    # Should pass with complete data
    assert result['validation']['passed'] == True
    
    # Test with incomplete data
    incomplete_data = {}
    result2 = agent.process(incomplete_data)
    assert len(result2['validation']['warnings']) > 0
    
    print("✓ ValidationAgent working correctly")
    return True


def test_integration_agent():
    """Test IntegrationAgent"""
    print("\n[TEST] Testing IntegrationAgent...")
    
    agent = IntegrationAgent()
    
    input_data = {
        'event_type': 'test_event',
        'validation': {'passed': True, 'quality_score': 95}
    }
    
    result = agent.process(input_data)
    
    # Check integration metadata
    assert 'integration' in result
    assert 'integrations' in result['integration']
    assert 'outputs' in result['integration']
    assert result['integration']['complete'] == True
    
    # Check that integrations were performed
    assert len(result['integration']['integrations']) > 0
    
    print("✓ IntegrationAgent working correctly")
    return True


def test_full_pipeline_with_agents():
    """Test complete pipeline with all agents"""
    print("\n[TEST] Testing complete pipeline with all agents...")
    
    # Create pipeline stages
    stages = [
        PipelineStage("Ingestion", [IngestionAgent()]),
        PipelineStage("Enrichment", [EnrichmentAgent()]),
        PipelineStage("Analysis", [AnalysisAgent()]),
        PipelineStage("Validation", [ValidationAgent()]),
        PipelineStage("Integration", [IntegrationAgent()])
    ]
    
    pipeline = Pipeline("FullTestPipeline", stages)
    
    # Input data
    input_data = {
        'event_type': 'test_cognition_event',
        'source': 'test_source',
        'summary': 'AI completed in one hour what team built in year',
        'description': 'Testing compression and acceleration of cognition with agents'
    }
    
    # Execute pipeline
    result = pipeline.execute(input_data)
    
    # Verify all stages completed
    assert 'ingestion' in result
    assert 'enrichment' in result
    assert 'analysis' in result
    assert 'validation' in result
    assert 'integration' in result
    
    # Verify data flow
    assert result['ingestion']['validated'] == True
    assert len(result['enrichment']['context_added']) > 0
    assert 'completeness_score' in result['analysis']
    assert 'quality_score' in result['validation']
    assert result['integration']['complete'] == True
    
    # Verify pipeline metadata
    assert len(result['_pipeline_metadata']['stages_executed']) == 5
    
    print("✓ Complete pipeline working correctly")
    return True


def test_error_handling():
    """Test error handling in pipeline"""
    print("\n[TEST] Testing error handling...")
    
    class ErrorAgent(PipelineAgent):
        def __init__(self):
            super().__init__("ErrorAgent", "Error Test")
        
        def process(self, data):
            raise ValueError("Test error")
    
    stage = PipelineStage("ErrorStage", [ErrorAgent()])
    
    # Should handle error gracefully
    result = stage.execute({'test': 'data'})
    assert result is not None
    
    print("✓ Error handling working correctly")
    return True


def test_parallel_processing():
    """Test parallel agent processing"""
    print("\n[TEST] Testing parallel processing...")
    
    agent1 = TestAgent("Parallel1")
    agent2 = TestAgent("Parallel2")
    agent3 = TestAgent("Parallel3")
    
    parallel_stage = PipelineStage("ParallelTest", [agent1, agent2, agent3], parallel=True)
    
    input_data = {'initial': 'data'}
    result = parallel_stage.execute(input_data)
    
    # All agents should have processed
    assert 'Parallel1_processed' in result
    assert 'Parallel2_processed' in result
    assert 'Parallel3_processed' in result
    
    print("✓ Parallel processing working correctly")
    return True


def test_pipeline_statistics():
    """Test pipeline statistics collection"""
    print("\n[TEST] Testing pipeline statistics...")
    
    pipeline = Pipeline("StatsTest", [PipelineStage("S1", [TestAgent()])])
    
    # Execute multiple times
    for i in range(3):
        pipeline.execute({'test': f'data_{i}'})
    
    # Get statistics
    stats = pipeline.get_statistics()
    
    assert stats['executions'] == 3
    assert 'avg_duration' in stats
    assert 'min_duration' in stats
    assert 'max_duration' in stats
    
    print("✓ Pipeline statistics working correctly")
    return True


def run_all_tests():
    """Run all pipeline tests"""
    print("=" * 70)
    print("Running Pipeline Processing System Test Suite")
    print("=" * 70)
    
    tests = [
        ("PipelineAgent Base", test_pipeline_agent_base),
        ("PipelineStage", test_pipeline_stage),
        ("Pipeline Execution", test_pipeline_execution),
        ("Pipeline Registry", test_pipeline_registry),
        ("Ingestion Agent", test_ingestion_agent),
        ("Enrichment Agent", test_enrichment_agent),
        ("Analysis Agent", test_analysis_agent),
        ("Validation Agent", test_validation_agent),
        ("Integration Agent", test_integration_agent),
        ("Full Pipeline", test_full_pipeline_with_agents),
        ("Error Handling", test_error_handling),
        ("Parallel Processing", test_parallel_processing),
        ("Pipeline Statistics", test_pipeline_statistics)
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
        except Exception as e:
            print(f"✗ {test_name} failed: {e}")
            import traceback
            traceback.print_exc()
            failed += 1
    
    print("\n" + "=" * 70)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("=" * 70)
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
