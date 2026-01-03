#!/usr/bin/env python3
"""
Test Suite for Barrot Simulation Layer
Tests all simulation components: engine, sandbox, forecast, cascade, echo, drift
"""

import sys
import json
import tempfile
from pathlib import Path

# Add barrot_sim to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from barrot_sim.simulation_engine import SimulationEngine, SimulationMode, get_engine
from barrot_sim.agentic_sandbox import create_sandbox
from barrot_sim.directive_forecast import DirectiveForecaster
from barrot_sim.glyph_cascade import GlyphCascadeModel
from barrot_sim.council_echo import CouncilEchoSimulator
from barrot_sim.reality_drift import RealityDriftDetector


def test_simulation_engine():
    """Test simulation engine core functionality"""
    print("\n[TEST] Testing simulation engine...")
    
    engine = get_engine()
    
    # Create chamber
    chamber = engine.create_chamber("test_chamber_1", SimulationMode.FORECAST)
    assert chamber is not None, "Chamber creation failed"
    assert chamber.chamber_id == "test_chamber_1", "Chamber ID mismatch"
    
    # Add agent
    chamber.add_agent({"name": "Test Agent", "type": "forecaster"})
    assert len(chamber.state["agents"]) == 1, "Agent not added"
    
    # Inject directive
    chamber.inject_directive({"name": "TEST_DIRECTIVE"})
    assert len(chamber.state["directives"]) == 1, "Directive not injected"
    
    # Run simulation
    results = engine.run_simulation("test_chamber_1", {
        "directives": [{"name": "TEST_DIRECTIVE"}]
    })
    assert "outcomes" in results, "Simulation results missing outcomes"
    
    # Close chamber
    final = engine.close_chamber("test_chamber_1")
    assert not final["active"], "Chamber still active after close"
    
    print("✓ Simulation engine working correctly")
    return True


def test_agentic_sandbox():
    """Test agentic sandbox functionality"""
    print("\n[TEST] Testing agentic sandbox...")
    
    sandbox = create_sandbox("test_sandbox_1")
    assert sandbox.sandbox_id == "test_sandbox_1", "Sandbox ID mismatch"
    
    # Deploy agent
    agent = sandbox.deploy_agent("agent_1", {
        "name": "Test Agent",
        "type": "forecaster",
        "capabilities": ["prediction"]
    })
    assert agent.agent_id == "agent_1", "Agent ID mismatch"
    
    # Test protocol
    test_results = sandbox.test_agent_protocol("agent_1", {
        "name": "TEST_PROTOCOL"
    })
    assert test_results["test_passed"] == True, "Protocol test failed"
    assert "performance" in test_results, "Performance metrics missing"
    
    # Mutate agent
    mutated = sandbox.mutate_agent("agent_1", {
        "type": "capability_enhancement"
    })
    assert len(mutated.mutations) == 1, "Mutation not recorded"
    
    # Get state
    state = sandbox.get_sandbox_state()
    assert state["agent_count"] == 1, "Agent count mismatch"
    
    print("✓ Agentic sandbox working correctly")
    return True


def test_directive_forecast():
    """Test directive forecasting"""
    print("\n[TEST] Testing directive forecasting...")
    
    forecaster = DirectiveForecaster()
    
    # Forecast directive
    directive = {
        "name": "MEMORY_ENHANCEMENT_DIRECTIVE",
        "description": "Enhance memory compression",
        "impact_areas": ["memory", "matrix"]
    }
    
    report = forecaster.forecast_directive(directive)
    assert "impacts" in report, "Impacts missing from report"
    assert "confidence" in report, "Confidence missing from report"
    assert "risks" in report, "Risks missing from report"
    assert "opportunities" in report, "Opportunities missing from report"
    assert 0 <= report["confidence"] <= 1, "Invalid confidence score"
    
    # Forecast multiple
    directives = [
        {"name": "TEST_1"},
        {"name": "TEST_2"}
    ]
    reports = forecaster.forecast_multiple(directives)
    assert len(reports) == 2, "Not all directives forecasted"
    
    # Compare forecasts
    comparison = forecaster.compare_forecasts([0, 1])
    assert "avg_confidence" in comparison, "Average confidence missing"
    
    print("✓ Directive forecasting working correctly")
    return True


def test_glyph_cascade():
    """Test glyph cascade modeling"""
    print("\n[TEST] Testing glyph cascade modeling...")
    
    model = GlyphCascadeModel()
    
    # Check known glyphs initialized
    assert "SIMULATION_LAYER_INITIALIZED_GLYPH" in model.nodes, "Simulation glyph not initialized"
    assert "REALITY_DRIFT_GLYPH" in model.nodes, "Drift glyph not initialized"
    
    # Simulate emission
    result = model.simulate_emission(
        "SIMULATION_LAYER_INITIALIZED_GLYPH",
        {"test": "context"}
    )
    assert "predicted_cascade" in result, "Cascade prediction missing"
    assert "cascade_depth" in result, "Cascade depth missing"
    
    # Analyze pattern
    analysis = model.analyze_cascade_pattern("REALITY_DRIFT_GLYPH")
    assert "cascade_influence" in analysis, "Influence score missing"
    assert 0 <= analysis["cascade_influence"] <= 1, "Invalid influence score"
    
    # Get statistics
    stats = model.get_cascade_statistics()
    assert "total_glyphs" in stats, "Total glyphs count missing"
    assert stats["total_glyphs"] > 0, "No glyphs in model"
    
    print("✓ Glyph cascade modeling working correctly")
    return True


def test_council_echo():
    """Test council echo simulation"""
    print("\n[TEST] Testing council echo simulation...")
    
    simulator = CouncilEchoSimulator()
    
    # Check agents initialized
    assert len(simulator.agents) > 0, "No agents initialized"
    
    # Simulate deliberation
    result = simulator.simulate_deliberation(
        "Test topic",
        {
            "practicality": "high",
            "complexity": "medium",
            "risk": "low"
        }
    )
    assert "baseline" in result, "Baseline missing from result"
    assert "consensus" in result["baseline"], "Consensus missing"
    
    # Simulate with altered conditions
    result2 = simulator.simulate_deliberation(
        "Test topic 2",
        {"practicality": "low"},
        altered_conditions={"practicality": "high"}
    )
    assert "altered" in result2, "Altered results missing"
    assert "delta" in result2, "Delta missing"
    
    # Test sensitivity
    sensitivity = simulator.test_condition_sensitivity(
        "Test topic",
        {"practicality": "medium"},
        "risk",
        ["low", "high"]
    )
    assert "parameter_impact" in sensitivity, "Parameter impact missing"
    
    # Get summary
    summary = simulator.get_simulation_summary()
    assert "total_simulations" in summary, "Simulation count missing"
    
    print("✓ Council echo simulation working correctly")
    return True


def test_reality_drift():
    """Test reality drift detection"""
    print("\n[TEST] Testing reality drift detection...")
    
    detector = RealityDriftDetector()
    
    # Set live state
    detector.set_live_state({
        "memory_utilization": 0.75,
        "matrix_coherence": 0.88,
        "council_consensus": 0.82
    })
    assert detector.live_state is not None, "Live state not set"
    
    # Add simulated state
    detector.add_simulated_state("sim_1", {
        "memory_utilization": 0.72,
        "matrix_coherence": 0.85,
        "council_consensus": 0.80
    })
    assert "sim_1" in detector.simulated_states, "Simulated state not added"
    
    # Detect drift
    drift = detector.detect_drift("sim_1")
    assert "drift_detected" in drift, "Drift detection missing"
    assert "avg_drift" in drift, "Average drift missing"
    assert "severity" in drift, "Severity missing"
    assert "recommendations" in drift, "Recommendations missing"
    
    # Add another state
    detector.add_simulated_state("sim_2", {
        "memory_utilization": 0.60,
        "matrix_coherence": 0.70,
        "council_consensus": 0.65
    })
    detector.detect_drift("sim_2")
    
    # Compare multiple
    comparison = detector.compare_multiple_simulations(["sim_1", "sim_2"])
    assert "best_simulation" in comparison, "Best simulation missing"
    assert "worst_simulation" in comparison, "Worst simulation missing"
    
    # Get statistics
    stats = detector.get_drift_statistics()
    assert "total_checks" in stats, "Total checks missing"
    assert stats["total_checks"] >= 2, "Check count should be at least 2"
    
    print("✓ Reality drift detection working correctly")
    return True


def test_integration():
    """Test integration between components"""
    print("\n[TEST] Testing component integration...")
    
    # Create engine and chamber
    engine = get_engine()
    chamber = engine.create_chamber("integration_test", SimulationMode.TEST)
    
    # Create sandbox and deploy agent
    sandbox = create_sandbox("integration_sandbox")
    agent = sandbox.deploy_agent("integration_agent", {
        "name": "Integration Agent",
        "type": "tester"
    })
    
    # Link agent to chamber
    chamber.add_agent(agent.get_profile())
    
    # Run simulation
    results = engine.run_simulation("integration_test", {
        "protocols": [{"name": "INTEGRATION_TEST"}]
    })
    
    assert len(chamber.state["agents"]) == 1, "Agent not in chamber"
    assert "outcomes" in results, "Simulation outcomes missing"
    
    # Clean up
    engine.close_chamber("integration_test")
    
    print("✓ Component integration working correctly")
    return True


def test_edge_cases():
    """Test edge cases and error handling"""
    print("\n[TEST] Testing edge cases...")
    
    engine = get_engine()
    
    # Try to create duplicate chamber
    try:
        chamber1 = engine.create_chamber("dup_test", SimulationMode.FORECAST)
        chamber2 = engine.create_chamber("dup_test", SimulationMode.FORECAST)
        assert False, "Should have raised ValueError for duplicate chamber"
    except ValueError:
        pass
    
    # Clean up
    if "dup_test" in engine.chambers:
        engine.close_chamber("dup_test")
    
    # Try to get non-existent chamber
    chamber = engine.get_chamber("nonexistent")
    assert chamber is None, "Should return None for non-existent chamber"
    
    # Test drift detector without live state
    detector = RealityDriftDetector()
    detector.add_simulated_state("test", {})
    try:
        detector.detect_drift("test")
        assert False, "Should have raised ValueError without live state"
    except ValueError:
        pass
    
    print("✓ Edge cases handled correctly")
    return True


def run_all_tests():
    """Run all tests"""
    print("=" * 60)
    print("Running Barrot Simulation Layer Test Suite")
    print("=" * 60)
    
    tests = [
        ("Simulation Engine", test_simulation_engine),
        ("Agentic Sandbox", test_agentic_sandbox),
        ("Directive Forecast", test_directive_forecast),
        ("Glyph Cascade", test_glyph_cascade),
        ("Council Echo", test_council_echo),
        ("Reality Drift", test_reality_drift),
        ("Integration", test_integration),
        ("Edge Cases", test_edge_cases)
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
    
    print("\n" + "=" * 60)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
