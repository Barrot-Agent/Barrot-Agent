#!/usr/bin/env python3
"""
Node: Council Vote
Simulates agent disagreements and emits COUNCIL_ALIGNMENT_GLYPH upon consensus.
Represents multi-perspective reasoning and dialectical synthesis.
"""

import json
import random
from pathlib import Path
from datetime import datetime, timezone

# Paths
REPO_ROOT = Path(__file__).resolve().parent.parent
GLYPHS_PATH = REPO_ROOT / "glyphs"
BUNDLES_PATH = REPO_ROOT / "memory-bundles"
TRACE_LOG_PATH = BUNDLES_PATH / "TRACE_LOG.md"
HISTORY_PATH = BUNDLES_PATH / "council_history.json"

# Council agents with different perspectives
COUNCIL_AGENTS = [
    {
        "name": "Pragmatist",
        "bias": "practical_solutions",
        "weight": 1.0,
        "adjustable": True
    },
    {
        "name": "Theorist",
        "bias": "conceptual_frameworks",
        "weight": 0.8,
        "adjustable": True
    },
    {
        "name": "Skeptic",
        "bias": "critical_analysis",
        "weight": 1.2,
        "adjustable": True
    },
    {
        "name": "Optimist",
        "bias": "opportunity_seeking",
        "weight": 0.7,
        "adjustable": True
    },
    {
        "name": "Guardian",
        "bias": "risk_mitigation",
        "weight": 1.1,
        "adjustable": True
    },
    {
        "name": "Experimentalist",
        "bias": "empirical_validation",
        "weight": 0.9,
        "adjustable": True
    },
    {
        "name": "Error Spotter",
        "bias": "fault_detection",
        "weight": 1.0,
        "adjustable": True
    }
]

def load_historical_results():
    """Load historical council results for weight adjustment"""
    if HISTORY_PATH.exists():
        try:
            with open(HISTORY_PATH, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {"deliberations": [], "agent_performance": {}}
    return {"deliberations": [], "agent_performance": {}}

def save_historical_results(history):
    """Save historical council results"""
    with open(HISTORY_PATH, 'w') as f:
        json.dump(history, f, indent=2)

def adjust_agent_weights(history):
    """Dynamically adjust agent weights based on historical performance"""
    if not history.get("agent_performance"):
        return COUNCIL_AGENTS
    
    adjusted_agents = []
    for agent in COUNCIL_AGENTS:
        if not agent.get("adjustable", True):
            adjusted_agents.append(agent)
            continue
            
        agent_copy = agent.copy()
        perf = history["agent_performance"].get(agent["name"], {})
        
        # Adjust weight based on consensus contribution
        # Agents who historically contributed to successful consensus get slight boost
        consensus_contrib = perf.get("consensus_contribution", 0)
        if consensus_contrib > 0.6:
            agent_copy["weight"] = min(1.5, agent["weight"] * 1.05)
        elif consensus_contrib < 0.3 and consensus_contrib > 0:
            agent_copy["weight"] = max(0.5, agent["weight"] * 0.95)
        
        adjusted_agents.append(agent_copy)
    
    return adjusted_agents

def simulate_deliberation(topic="system_alignment", use_dynamic_weights=True):
    """Simulate council deliberation on a topic"""
    print(f"[COUNCIL_VOTE] Topic: {topic}")
    
    # Load history and adjust weights if enabled
    agents_to_use = COUNCIL_AGENTS
    if use_dynamic_weights:
        history = load_historical_results()
        agents_to_use = adjust_agent_weights(history)
        print(f"[COUNCIL_VOTE] Using dynamic weight adjustment based on {len(history.get('deliberations', []))} historical deliberations")
    
    votes = []
    arguments = []
    
    for agent in agents_to_use:
        # Each agent votes with some randomness influenced by their bias
        base_vote = random.uniform(0, 1)
        
        # Apply weight and normalize to agreement scale (0-1)
        agreement = min(1.0, base_vote * agent['weight'])
        
        votes.append({
            'agent': agent['name'],
            'agreement': agreement,
            'bias': agent['bias'],
            'weight_used': agent['weight']
        })
        
        # Generate argument
        if agreement > 0.7:
            stance = "strongly supports"
        elif agreement > 0.5:
            stance = "supports"
        elif agreement > 0.3:
            stance = "has reservations about"
        else:
            stance = "opposes"
        
        argument = f"{agent['name']} ({agent['bias']}) {stance} this approach"
        arguments.append(argument)
        print(f"[COUNCIL_VOTE]   {argument} (score: {agreement:.2f}, weight: {agent['weight']:.2f})")
    
    return votes, arguments

def calculate_consensus(votes):
    """Calculate whether consensus is reached"""
    # Calculate average agreement
    avg_agreement = sum(v['agreement'] for v in votes) / len(votes)
    
    # Calculate variance (disagreement level)
    variance = sum((v['agreement'] - avg_agreement) ** 2 for v in votes) / len(votes)
    
    # Consensus requires high average and low variance
    consensus_reached = avg_agreement > 0.6 and variance < 0.1
    
    return {
        'reached': consensus_reached,
        'avg_agreement': avg_agreement,
        'disagreement_level': variance,
        'threshold': 0.6
    }

def emit_glyph(consensus, votes, arguments):
    """Emit COUNCIL_ALIGNMENT_GLYPH when consensus reached"""
    glyph_file = GLYPHS_PATH / "council_alignment_glyph.yml"
    
    glyph_content = f"""glyph_name: COUNCIL_ALIGNMENT_GLYPH
glyph_id: COUNCIL-001
version: 1.0.0
timestamp: {datetime.now(timezone.utc).replace(tzinfo=None).isoformat()}Z

description: >
  Emitted when the council of diverse agent perspectives reaches consensus.
  Represents dialectical synthesis through multi-perspective deliberation.

symbolic_representation: "⚖ 🗳 ✓"

properties:
  dimension: multi_perspective
  mutability: consensus_based
  trigger: council_deliberation
  
attributes:
  - dialectical_reasoning
  - perspective_synthesis
  - consensus_building
  - disagreement_resolution
  
consensus_metrics:
  reached: {str(consensus['reached']).lower()}
  avg_agreement: {consensus['avg_agreement']:.2f}
  disagreement_level: {consensus['disagreement_level']:.3f}
  participating_agents: {len(votes)}

council_votes:
{chr(10).join([f"  - {v['agent']}: {v['agreement']:.2f} ({v['bias']})" for v in votes])}

integration_points:
  - multi_agent_reasoning
  - consensus_protocols
  - dialectical_synthesis
  
usage_context: >
  Invoke when simulating multi-perspective deliberation to ensure decisions
  incorporate diverse viewpoints and reach genuine consensus rather than
  premature agreement.
"""
    
    with open(glyph_file, 'w') as f:
        f.write(glyph_content)
    
    print(f"[COUNCIL_VOTE] Emitted COUNCIL_ALIGNMENT_GLYPH -> {glyph_file}")

def log_deliberation(consensus, votes, arguments):
    """Log council deliberation to TRACE_LOG.md"""
    log_entry = f"""
## Council Deliberation: {datetime.now(timezone.utc).replace(tzinfo=None).isoformat()}Z

**Consensus Reached:** {"Yes" if consensus['reached'] else "No"}
**Average Agreement:** {consensus['avg_agreement']:.2f}
**Disagreement Level:** {consensus['disagreement_level']:.3f}

### Council Arguments
"""
    
    for arg in arguments:
        log_entry += f"- {arg}\n"
    
    log_entry += f"""
### Decision
{'The council has reached consensus and moves forward with this approach.' if consensus['reached'] else 'The council requires further deliberation due to disagreement.'}

### Agent Weights Used
"""
    for vote in votes:
        log_entry += f"- {vote['agent']}: {vote.get('weight_used', 1.0):.2f}\n"
    
    log_entry += "\n---\n"
    
    # Append to trace log
    with open(TRACE_LOG_PATH, 'a') as f:
        f.write(log_entry)
    
    print(f"[COUNCIL_VOTE] Logged deliberation to TRACE_LOG.md")

def update_historical_performance(votes, consensus):
    """Update historical performance metrics for agents"""
    history = load_historical_results()
    
    # Initialize performance tracking if needed
    if "agent_performance" not in history:
        history["agent_performance"] = {}
    
    # Record this deliberation
    deliberation_record = {
        "timestamp": datetime.now(timezone.utc).replace(tzinfo=None).isoformat(),
        "consensus_reached": consensus['reached'],
        "avg_agreement": consensus['avg_agreement']
    }
    
    if "deliberations" not in history:
        history["deliberations"] = []
    history["deliberations"].append(deliberation_record)
    
    # Update agent performance
    for vote in votes:
        agent_name = vote['agent']
        if agent_name not in history["agent_performance"]:
            history["agent_performance"][agent_name] = {
                "total_votes": 0,
                "consensus_votes": 0,
                "avg_agreement": 0.0,
                "consensus_contribution": 0.0
            }
        
        perf = history["agent_performance"][agent_name]
        perf["total_votes"] += 1
        if consensus['reached']:
            perf["consensus_votes"] += 1
        
        # Update running average of agreement
        prev_avg = perf["avg_agreement"]
        perf["avg_agreement"] = (prev_avg * (perf["total_votes"] - 1) + vote['agreement']) / perf["total_votes"]
        
        # Update consensus contribution (how often this agent's votes align with consensus)
        perf["consensus_contribution"] = perf["consensus_votes"] / perf["total_votes"]
    
    # Keep only last 100 deliberations to prevent unbounded growth
    if len(history["deliberations"]) > 100:
        history["deliberations"] = history["deliberations"][-100:]
    
    save_historical_results(history)
    print(f"[COUNCIL_VOTE] Updated historical performance metrics")

def main():
    print("[COUNCIL_VOTE] Convening council for deliberation...")
    
    # Simulate deliberation with dynamic weights
    votes, arguments = simulate_deliberation("system_alignment", use_dynamic_weights=True)
    
    # Calculate consensus
    consensus = calculate_consensus(votes)
    
    # Report results
    print(f"[COUNCIL_VOTE] Average agreement: {consensus['avg_agreement']:.2f}")
    print(f"[COUNCIL_VOTE] Disagreement level: {consensus['disagreement_level']:.3f}")
    
    if consensus['reached']:
        print("[COUNCIL_VOTE] ✓ Consensus reached!")
        emit_glyph(consensus, votes, arguments)
    else:
        print("[COUNCIL_VOTE] ✗ No consensus - further deliberation needed")
    
    # Always log the deliberation
    log_deliberation(consensus, votes, arguments)
    
    # Update historical performance for dynamic weight adjustment
    update_historical_performance(votes, consensus)

if __name__ == "__main__":
    main()
