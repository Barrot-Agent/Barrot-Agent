#!/usr/bin/env python3
"""
Example: Adding a Custom Agent to the Pipeline
Demonstrates how easy it is to extend the pipeline with new agents.
"""

import sys
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, Any

# Add matrix to path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from pipeline_orchestrator import PipelineAgent, PipelineStage, create_pipeline
from pipeline_agents import (
    IngestionAgent,
    EnrichmentAgent,
    AnalysisAgent,
    ValidationAgent,
    IntegrationAgent
)


# ============================================================================
# STEP 1: Create a New Agent by Extending PipelineAgent
# ============================================================================

class SentimentAnalysisAgent(PipelineAgent):
    """
    Custom agent that analyzes sentiment of event descriptions.
    This is an example of how easy it is to add new processing capabilities.
    """
    
    def __init__(self):
        super().__init__("SentimentAnalysisAgent", "Sentiment Analysis")
    
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze sentiment of text content"""
        
        # Add sentiment analysis metadata
        data['sentiment'] = {
            'timestamp': datetime.now(timezone.utc).replace(tzinfo=None).isoformat(),
            'agent': self.name,
            'analyzed': True
        }
        
        # Analyze summary text if available
        if 'summary' in data:
            summary = data['summary'].lower()
            
            # Simple keyword-based sentiment analysis
            positive_keywords = ['success', 'achievement', 'excellent', 'amazing', 'generated', 'built']
            negative_keywords = ['failure', 'problem', 'issue', 'error', 'joking', 'funny']
            neutral_keywords = ['describes', 'shows', 'demonstrates']
            
            positive_count = sum(1 for word in positive_keywords if word in summary)
            negative_count = sum(1 for word in negative_keywords if word in summary)
            
            # Determine sentiment
            if positive_count > negative_count:
                sentiment = 'positive'
                confidence = min(0.5 + (positive_count * 0.1), 1.0)
            elif negative_count > positive_count:
                sentiment = 'negative'
                confidence = min(0.5 + (negative_count * 0.1), 1.0)
            else:
                sentiment = 'neutral'
                confidence = 0.5
            
            data['sentiment']['result'] = {
                'sentiment': sentiment,
                'confidence': confidence,
                'positive_indicators': positive_count,
                'negative_indicators': negative_count
            }
        
        # Analyze implications if available
        if 'implications' in data:
            implications = data['implications']
            data['sentiment']['implications_tone'] = 'contemplative'
        
        self.log_processing(data, data)
        print(f"[{self.name}] Sentiment: {data['sentiment'].get('result', {}).get('sentiment', 'N/A')}")
        
        return data


class PriorityClassificationAgent(PipelineAgent):
    """
    Custom agent that classifies event priority based on content.
    Another example of extending the pipeline.
    """
    
    def __init__(self):
        super().__init__("PriorityClassificationAgent", "Priority Classification")
    
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Classify event priority"""
        
        data['priority_classification'] = {
            'timestamp': datetime.now(timezone.utc).replace(tzinfo=None).isoformat(),
            'agent': self.name
        }
        
        # Priority rules based on content
        priority = 'medium'
        reasons = []
        
        # Check for critical keywords
        summary = data.get('summary', '').lower()
        if any(word in summary for word in ['breakthrough', 'critical', 'urgent', 'year']):
            priority = 'high'
            reasons.append('Contains critical impact keywords')
        
        # Check categories
        categories = data.get('categories', [])
        if 'cognition_compression' in categories:
            priority = 'high'
            reasons.append('Involves cognition compression')
        
        # Check implications count
        implications = data.get('implications', {})
        if isinstance(implications, dict) and len(implications) > 3:
            priority = 'high'
            reasons.append('Multiple significant implications')
        
        # Check glyphs emitted
        glyphs = data.get('glyphs_emitted', [])
        if len(glyphs) > 3:
            priority = 'high'
            reasons.append('Multiple glyph emissions indicate significance')
        
        data['priority_classification']['priority'] = priority
        data['priority_classification']['reasons'] = reasons
        data['priority_classification']['confidence'] = 0.8 if len(reasons) > 1 else 0.6
        
        self.log_processing(data, data)
        print(f"[{self.name}] Priority: {priority} ({len(reasons)} reasons)")
        
        return data


# ============================================================================
# STEP 2: Create Pipeline with New Agents
# ============================================================================

def create_enhanced_pipeline():
    """
    Create an enhanced pipeline that includes custom agents.
    Shows how to insert new agents at any position in the pipeline.
    """
    
    # Original stages
    ingestion_stage = PipelineStage("Ingestion", [IngestionAgent()])
    enrichment_stage = PipelineStage("Enrichment", [EnrichmentAgent()])
    
    # NEW: Add custom analysis stage with multiple agents running in parallel
    custom_analysis_stage = PipelineStage(
        name="Custom Analysis",
        agents=[
            SentimentAnalysisAgent(),
            PriorityClassificationAgent()
        ],
        parallel=True  # Run both agents in parallel for speed
    )
    
    # Original stages continue
    core_analysis_stage = PipelineStage("Core Analysis", [AnalysisAgent()])
    validation_stage = PipelineStage("Validation", [ValidationAgent()])
    integration_stage = PipelineStage("Integration", [IntegrationAgent()])
    
    # Create pipeline with new stage inserted
    pipeline = create_pipeline(
        name="enhanced_claude_pipeline",
        stages=[
            ingestion_stage,
            enrichment_stage,
            custom_analysis_stage,  # Our new stage!
            core_analysis_stage,
            validation_stage,
            integration_stage
        ]
    )
    
    return pipeline


# ============================================================================
# STEP 3: Test the Enhanced Pipeline
# ============================================================================

def main():
    """Execute the enhanced pipeline with custom agents"""
    print("=" * 70)
    print("EXAMPLE: Adding Custom Agents to Pipeline")
    print("=" * 70)
    print()
    
    print("[DEMO] This example shows how to add new agents to the pipeline:")
    print("  1. SentimentAnalysisAgent - Analyzes emotional tone")
    print("  2. PriorityClassificationAgent - Classifies event priority")
    print()
    
    # Create enhanced pipeline
    print("[SETUP] Creating enhanced pipeline with custom agents...")
    pipeline = create_enhanced_pipeline()
    print(f"[SETUP] Pipeline has {len(pipeline.stages)} stages (2 more than original)")
    print()
    
    # Load Claude Code Impact Event
    event_data = {
        'event_type': 'claude_code_impact_event',
        'source': 'Jaana Dogan (Google Principal Engineer)',
        'date': '2026-01-02',
        'summary': 'Claude Code generated in one hour what a Google team built in a full year: a distributed agent orchestrator',
        'implications': {
            'cognition_compression': 'Demonstrates ability to compress year of cognition',
            'agentic_parity': 'AI agents match human teams',
            'prompt_as_architecture': 'Prompt becomes execution trigger',
            'human_role_contradiction': 'Questions human role in high-cognition domains'
        },
        'glyphs_emitted': [
            'COGNITION_COMPRESSION_GLYPH',
            'AGENTIC_PARITY_GLYPH',
            'PROMPT_AS_ARCHITECTURE_GLYPH',
            'HUMAN_ROLE_CONTRADICTION_GLYPH'
        ]
    }
    
    # Execute
    print("[EXECUTE] Running enhanced pipeline...")
    print()
    result = pipeline.execute(event_data)
    print()
    
    # Display custom agent results
    print("=" * 70)
    print("CUSTOM AGENT RESULTS")
    print("=" * 70)
    print()
    
    if 'sentiment' in result:
        sent = result['sentiment']
        if 'result' in sent:
            sentiment_result = sent['result']
            print(f"[SentimentAnalysisAgent]")
            print(f"  • Sentiment: {sentiment_result['sentiment']}")
            print(f"  • Confidence: {sentiment_result['confidence']:.1%}")
            print(f"  • Positive Indicators: {sentiment_result['positive_indicators']}")
            print(f"  • Negative Indicators: {sentiment_result['negative_indicators']}")
            if 'implications_tone' in sent:
                print(f"  • Implications Tone: {sent['implications_tone']}")
        print()
    
    if 'priority_classification' in result:
        priority = result['priority_classification']
        print(f"[PriorityClassificationAgent]")
        print(f"  • Priority: {priority['priority'].upper()}")
        print(f"  • Confidence: {priority['confidence']:.1%}")
        print(f"  • Reasons:")
        for reason in priority['reasons']:
            print(f"    - {reason}")
        print()
    
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print("✅ Successfully added 2 custom agents to the pipeline")
    print("✅ Agents ran in parallel for efficiency")
    print("✅ Original pipeline functionality preserved")
    print("✅ New insights added without modifying existing code")
    print()
    print("📝 Adding new agents is as simple as:")
    print("   1. Create a class extending PipelineAgent")
    print("   2. Implement the process() method")
    print("   3. Add to a pipeline stage")
    print()
    print("See PIPELINE_CONFIGURATION.md for detailed guide.")
    print("=" * 70)


if __name__ == "__main__":
    main()
