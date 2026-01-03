#!/usr/bin/env python3
"""
Glyph Cascade Modeling
Predict glyph emissions and trace interactions across the symbolic system.
"""

import json
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional, Set
from collections import defaultdict


class GlyphNode:
    """Node in the glyph cascade graph"""
    
    def __init__(self, glyph_name: str):
        self.glyph_name = glyph_name
        self.triggers: List[str] = []  # Glyphs triggered by this one
        self.triggered_by: List[str] = []  # Glyphs that trigger this one
        self.emission_count = 0
        self.cascade_depth = 0
    
    def add_trigger(self, target_glyph: str):
        """Add a glyph that this one triggers"""
        if target_glyph not in self.triggers:
            self.triggers.append(target_glyph)
    
    def add_triggered_by(self, source_glyph: str):
        """Add a glyph that triggers this one"""
        if source_glyph not in self.triggered_by:
            self.triggered_by.append(source_glyph)
    
    def record_emission(self):
        """Record an emission of this glyph"""
        self.emission_count += 1
    
    def get_node_data(self) -> Dict[str, Any]:
        """Get node data"""
        return {
            "glyph_name": self.glyph_name,
            "triggers": self.triggers,
            "triggered_by": self.triggered_by,
            "emission_count": self.emission_count,
            "cascade_depth": self.cascade_depth
        }


class GlyphCascadeModel:
    """Model for glyph cascade interactions"""
    
    def __init__(self):
        self.nodes: Dict[str, GlyphNode] = {}
        self.cascade_history: List[Dict[str, Any]] = []
        self._initialize_known_glyphs()
    
    def _initialize_known_glyphs(self):
        """Initialize known glyphs from the system"""
        known_glyphs = [
            "COUNCIL_ALIGNMENT_GLYPH",
            "HERMETIC_QUANTUM_FUSION_GLYPH",
            "MEMORY_COMPRESSION_GLYPH",
            "TEMPORAL_PLASTICITY_GLYPH",
            "ORGANOID_REASONING_GLYPH",
            "SESSION_TRACE_GLYPH",
            "GLYPH_MISALIGNMENT_RECOVERY",
            # New simulation glyphs
            "SIMULATION_LAYER_INITIALIZED_GLYPH",
            "DIRECTIVE_FORECAST_GLYPH",
            "AGENTIC_SANDBOX_GLYPH",
            "COUNCIL_ECHO_GLYPH",
            "REALITY_DRIFT_GLYPH"
        ]
        
        for glyph in known_glyphs:
            self.add_glyph(glyph)
        
        # Define known cascade relationships
        self._define_cascade_relationships()
    
    def _define_cascade_relationships(self):
        """Define known cascade relationships between glyphs"""
        # Council alignment can trigger memory compression
        self.add_cascade_relationship(
            "COUNCIL_ALIGNMENT_GLYPH",
            "MEMORY_COMPRESSION_GLYPH"
        )
        
        # Simulation initialization triggers multiple subsystem glyphs
        self.add_cascade_relationship(
            "SIMULATION_LAYER_INITIALIZED_GLYPH",
            "AGENTIC_SANDBOX_GLYPH"
        )
        self.add_cascade_relationship(
            "SIMULATION_LAYER_INITIALIZED_GLYPH",
            "DIRECTIVE_FORECAST_GLYPH"
        )
        
        # Reality drift can trigger council echo
        self.add_cascade_relationship(
            "REALITY_DRIFT_GLYPH",
            "COUNCIL_ECHO_GLYPH"
        )
    
    def add_glyph(self, glyph_name: str) -> GlyphNode:
        """Add a glyph to the model"""
        if glyph_name not in self.nodes:
            self.nodes[glyph_name] = GlyphNode(glyph_name)
        return self.nodes[glyph_name]
    
    def add_cascade_relationship(self, source: str, target: str):
        """Add a cascade relationship between glyphs"""
        source_node = self.add_glyph(source)
        target_node = self.add_glyph(target)
        
        source_node.add_trigger(target)
        target_node.add_triggered_by(source)
    
    def simulate_emission(self, glyph_name: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Simulate the emission of a glyph and predict cascade"""
        if glyph_name not in self.nodes:
            self.add_glyph(glyph_name)
        
        node = self.nodes[glyph_name]
        node.record_emission()
        
        # Predict cascade
        cascade = self._predict_cascade(glyph_name)
        
        result = {
            "source_glyph": glyph_name,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "context": context or {},
            "predicted_cascade": cascade,
            "cascade_depth": len(cascade),
            "affected_glyphs": list(set(c["glyph"] for c in cascade))
        }
        
        self.cascade_history.append(result)
        return result
    
    def _predict_cascade(self, glyph_name: str, depth: int = 0, visited: Set[str] = None) -> List[Dict[str, Any]]:
        """Recursively predict glyph cascade"""
        if visited is None:
            visited = set()
        
        if glyph_name in visited or depth > 5:  # Prevent infinite loops and limit depth
            return []
        
        visited.add(glyph_name)
        cascade = []
        
        node = self.nodes.get(glyph_name)
        if not node:
            return cascade
        
        for triggered_glyph in node.triggers:
            cascade.append({
                "glyph": triggered_glyph,
                "depth": depth + 1,
                "triggered_by": glyph_name,
                "probability": 0.8  # Could be refined with historical data
            })
            
            # Recursively get cascades from triggered glyphs
            sub_cascade = self._predict_cascade(triggered_glyph, depth + 1, visited.copy())
            cascade.extend(sub_cascade)
        
        return cascade
    
    def analyze_cascade_pattern(self, glyph_name: str) -> Dict[str, Any]:
        """Analyze cascade patterns for a specific glyph"""
        if glyph_name not in self.nodes:
            return {"error": f"Glyph {glyph_name} not found"}
        
        node = self.nodes[glyph_name]
        
        # Analyze upstream (what triggers this)
        upstream_depth = self._calculate_upstream_depth(glyph_name)
        
        # Analyze downstream (what this triggers)
        downstream_glyphs = self._get_all_downstream(glyph_name)
        
        return {
            "glyph_name": glyph_name,
            "emission_count": node.emission_count,
            "direct_triggers": len(node.triggers),
            "triggered_by_count": len(node.triggered_by),
            "upstream_depth": upstream_depth,
            "downstream_cascade_size": len(downstream_glyphs),
            "downstream_glyphs": downstream_glyphs,
            "cascade_influence": self._calculate_influence(glyph_name)
        }
    
    def _calculate_upstream_depth(self, glyph_name: str, visited: Set[str] = None) -> int:
        """Calculate maximum upstream depth"""
        if visited is None:
            visited = set()
        
        if glyph_name in visited:
            return 0
        
        visited.add(glyph_name)
        node = self.nodes.get(glyph_name)
        
        if not node or not node.triggered_by:
            return 0
        
        max_depth = 0
        for upstream_glyph in node.triggered_by:
            depth = 1 + self._calculate_upstream_depth(upstream_glyph, visited.copy())
            max_depth = max(max_depth, depth)
        
        return max_depth
    
    def _get_all_downstream(self, glyph_name: str, visited: Set[str] = None) -> List[str]:
        """Get all downstream glyphs"""
        if visited is None:
            visited = set()
        
        if glyph_name in visited:
            return []
        
        visited.add(glyph_name)
        downstream = []
        
        node = self.nodes.get(glyph_name)
        if not node:
            return downstream
        
        for triggered_glyph in node.triggers:
            downstream.append(triggered_glyph)
            downstream.extend(self._get_all_downstream(triggered_glyph, visited.copy()))
        
        return downstream
    
    def _calculate_influence(self, glyph_name: str) -> float:
        """Calculate cascade influence score"""
        node = self.nodes.get(glyph_name)
        if not node:
            return 0.0
        
        # Influence based on emission count and downstream cascade
        downstream = self._get_all_downstream(glyph_name)
        influence = (node.emission_count * 0.3) + (len(downstream) * 0.7)
        
        return min(influence / 10.0, 1.0)  # Normalize to 0-1
    
    def get_cascade_statistics(self) -> Dict[str, Any]:
        """Get cascade statistics"""
        total_emissions = sum(node.emission_count for node in self.nodes.values())
        
        # Find most influential glyphs
        influence_scores = {
            name: self._calculate_influence(name)
            for name in self.nodes.keys()
        }
        
        most_influential = sorted(
            influence_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )[:5]
        
        return {
            "total_glyphs": len(self.nodes),
            "total_emissions": total_emissions,
            "cascade_history_count": len(self.cascade_history),
            "most_influential_glyphs": [
                {"glyph": name, "influence": score}
                for name, score in most_influential
            ],
            "avg_cascade_depth": sum(
                c["cascade_depth"] for c in self.cascade_history
            ) / len(self.cascade_history) if self.cascade_history else 0
        }
    
    def get_model_state(self) -> Dict[str, Any]:
        """Get complete model state"""
        return {
            "nodes": {name: node.get_node_data() for name, node in self.nodes.items()},
            "cascade_history": self.cascade_history,
            "statistics": self.get_cascade_statistics()
        }


if __name__ == "__main__":
    # Example usage
    model = GlyphCascadeModel()
    
    # Simulate emissions
    print("Simulating Glyph Emissions:\n")
    
    result1 = model.simulate_emission("SIMULATION_LAYER_INITIALIZED_GLYPH", {
        "initialization": "complete"
    })
    print("1. SIMULATION_LAYER_INITIALIZED_GLYPH")
    print(f"   Cascade depth: {result1['cascade_depth']}")
    print(f"   Affected glyphs: {result1['affected_glyphs']}\n")
    
    result2 = model.simulate_emission("REALITY_DRIFT_GLYPH", {
        "drift_level": 0.15
    })
    print("2. REALITY_DRIFT_GLYPH")
    print(f"   Cascade depth: {result2['cascade_depth']}")
    print(f"   Affected glyphs: {result2['affected_glyphs']}\n")
    
    # Analyze cascade pattern
    analysis = model.analyze_cascade_pattern("SIMULATION_LAYER_INITIALIZED_GLYPH")
    print("\nCascade Pattern Analysis:")
    print(json.dumps(analysis, indent=2))
    
    # Get statistics
    stats = model.get_cascade_statistics()
    print("\n\nCascade Statistics:")
    print(json.dumps(stats, indent=2))
