#!/usr/bin/env python3
"""
Glyph Insights Aggregator
Provides daily and weekly summaries of glyph emissions, patterns, and system health.
"""

import json
from pathlib import Path
from datetime import datetime, timezone, timedelta
from collections import defaultdict

# Paths
REPO_ROOT = Path(__file__).resolve().parent.parent
BUNDLES_PATH = REPO_ROOT / "memory-bundles"
TRACE_LOG_PATH = BUNDLES_PATH / "TRACE_LOG.md"
GLYPH_MAPPING_PATH = BUNDLES_PATH / "glyph_mappings.json"
INSIGHTS_PATH = BUNDLES_PATH / "glyph_insights.json"
COUNCIL_HISTORY_PATH = BUNDLES_PATH / "council_history.json"

def load_glyph_history():
    """Load glyph emission history"""
    if GLYPH_MAPPING_PATH.exists():
        with open(GLYPH_MAPPING_PATH, 'r') as f:
            return json.load(f)
    return {"history": [], "dependencies": []}

def load_council_history():
    """Load council deliberation history"""
    if COUNCIL_HISTORY_PATH.exists():
        try:
            with open(COUNCIL_HISTORY_PATH, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {"deliberations": [], "agent_performance": {}}
    return {"deliberations": [], "agent_performance": {}}

def filter_by_timeframe(data, days=7):
    """Filter data by timeframe"""
    cutoff = datetime.now(timezone.utc).replace(tzinfo=None) - timedelta(days=days)
    filtered = []
    
    for item in data:
        if 'timestamp' in item:
            try:
                timestamp_str = item['timestamp'].replace('Z', '').replace('+00:00', '')
                item_time = datetime.fromisoformat(timestamp_str)
                if item_time > cutoff:
                    filtered.append(item)
            except (ValueError, AttributeError):
                continue
    
    return filtered

def analyze_glyph_patterns(history, days=7):
    """Analyze glyph emission patterns"""
    recent_glyphs = filter_by_timeframe(history, days)
    
    # Count emissions by glyph type
    glyph_counts = defaultdict(int)
    glyph_priorities = defaultdict(list)
    emitter_counts = defaultdict(int)
    
    for emission in recent_glyphs:
        glyph_name = emission.get('glyph_name', 'Unknown')
        glyph_counts[glyph_name] += 1
        glyph_priorities[emission.get('priority', 'medium')].append(glyph_name)
        emitter_counts[emission.get('emitter_node', 'Unknown')] += 1
    
    return {
        'total_emissions': len(recent_glyphs),
        'glyph_counts': dict(glyph_counts),
        'priority_distribution': {
            priority: len(glyphs) for priority, glyphs in glyph_priorities.items()
        },
        'emitter_activity': dict(emitter_counts),
        'most_common_glyph': max(glyph_counts.items(), key=lambda x: x[1])[0] if glyph_counts else None,
        'most_active_node': max(emitter_counts.items(), key=lambda x: x[1])[0] if emitter_counts else None
    }

def analyze_council_performance(history, days=7):
    """Analyze council deliberation performance"""
    recent_deliberations = filter_by_timeframe(history.get('deliberations', []), days)
    
    if not recent_deliberations:
        return {
            'total_deliberations': 0,
            'consensus_rate': 0.0,
            'avg_agreement': 0.0
        }
    
    consensus_count = sum(1 for d in recent_deliberations if d.get('consensus_reached', False))
    total_agreement = sum(d.get('avg_agreement', 0) for d in recent_deliberations)
    
    agent_perf = history.get('agent_performance', {})
    top_contributors = sorted(
        agent_perf.items(),
        key=lambda x: x[1].get('consensus_contribution', 0),
        reverse=True
    )[:3]
    
    return {
        'total_deliberations': len(recent_deliberations),
        'consensus_rate': consensus_count / len(recent_deliberations) if recent_deliberations else 0.0,
        'avg_agreement': total_agreement / len(recent_deliberations) if recent_deliberations else 0.0,
        'top_contributors': [{'agent': agent, 'contribution': data.get('consensus_contribution', 0)} 
                            for agent, data in top_contributors]
    }

def detect_recurring_issues(history, days=7):
    """Detect recurring issues and patterns"""
    recent_glyphs = filter_by_timeframe(history, days)
    
    # Track misalignment and recovery events
    misalignment_count = sum(1 for g in recent_glyphs if 'MISALIGNMENT' in g.get('glyph_name', ''))
    recovery_count = sum(1 for g in recent_glyphs if 'RECOVERY' in g.get('glyph_name', ''))
    
    # Track self-alignment checks
    alignment_checks = sum(1 for g in recent_glyphs if 'SELF_ALIGNMENT' in g.get('glyph_name', ''))
    
    issues = []
    if misalignment_count > 2:
        issues.append({
            'type': 'recurring_misalignment',
            'count': misalignment_count,
            'severity': 'high' if misalignment_count > 5 else 'medium',
            'description': f'System experienced {misalignment_count} misalignment events'
        })
    
    if recovery_count > 0:
        issues.append({
            'type': 'recovery_actions',
            'count': recovery_count,
            'severity': 'info',
            'description': f'Successfully recovered from {recovery_count} issues'
        })
    
    return issues

def calculate_system_health(glyph_analysis, council_analysis, issues):
    """Calculate overall system health score"""
    health_score = 100.0
    
    # Deduct points for issues
    for issue in issues:
        if issue['severity'] == 'high':
            health_score -= 15
        elif issue['severity'] == 'medium':
            health_score -= 10
        elif issue['severity'] == 'low':
            health_score -= 5
    
    # Adjust based on consensus rate
    consensus_rate = council_analysis.get('consensus_rate', 0)
    if consensus_rate < 0.5:
        health_score -= 10
    elif consensus_rate > 0.8:
        health_score += 5
    
    # Adjust based on critical glyphs
    critical_count = glyph_analysis['priority_distribution'].get('critical', 0)
    health_score -= critical_count * 5
    
    health_score = max(0, min(100, health_score))
    
    if health_score >= 90:
        status = 'Excellent'
    elif health_score >= 75:
        status = 'Good'
    elif health_score >= 60:
        status = 'Fair'
    elif health_score >= 40:
        status = 'Concerning'
    else:
        status = 'Critical'
    
    return {
        'score': health_score,
        'status': status
    }

def generate_daily_summary():
    """Generate daily summary of glyph activity"""
    glyph_data = load_glyph_history()
    council_data = load_council_history()
    
    # Analyze data for last 24 hours
    glyph_analysis = analyze_glyph_patterns(glyph_data.get('history', []), days=1)
    council_analysis = analyze_council_performance(council_data, days=1)
    issues = detect_recurring_issues(glyph_data.get('history', []), days=1)
    health = calculate_system_health(glyph_analysis, council_analysis, issues)
    
    summary = {
        'date': datetime.now(timezone.utc).replace(tzinfo=None).isoformat(),
        'timeframe': 'daily',
        'system_health': health,
        'glyph_activity': glyph_analysis,
        'council_performance': council_analysis,
        'issues_detected': issues,
        'recommendations': generate_recommendations(glyph_analysis, council_analysis, issues)
    }
    
    return summary

def generate_weekly_summary():
    """Generate weekly summary of glyph activity"""
    glyph_data = load_glyph_history()
    council_data = load_council_history()
    
    # Analyze data for last 7 days
    glyph_analysis = analyze_glyph_patterns(glyph_data.get('history', []), days=7)
    council_analysis = analyze_council_performance(council_data, days=7)
    issues = detect_recurring_issues(glyph_data.get('history', []), days=7)
    health = calculate_system_health(glyph_analysis, council_analysis, issues)
    
    summary = {
        'date': datetime.now(timezone.utc).replace(tzinfo=None).isoformat(),
        'timeframe': 'weekly',
        'system_health': health,
        'glyph_activity': glyph_analysis,
        'council_performance': council_analysis,
        'issues_detected': issues,
        'recommendations': generate_recommendations(glyph_analysis, council_analysis, issues),
        'trends': analyze_trends(glyph_data.get('history', []))
    }
    
    return summary

def analyze_trends(history):
    """Analyze trends over time"""
    # Compare first half vs second half of week
    recent = filter_by_timeframe(history, days=7)
    if len(recent) < 2:
        return {'trend': 'insufficient_data'}
    
    midpoint = len(recent) // 2
    first_half = recent[:midpoint]
    second_half = recent[midpoint:]
    
    first_critical = sum(1 for g in first_half if g.get('priority') == 'critical')
    second_critical = sum(1 for g in second_half if g.get('priority') == 'critical')
    
    if second_critical > first_critical:
        trend = 'increasing_critical_events'
    elif second_critical < first_critical:
        trend = 'decreasing_critical_events'
    else:
        trend = 'stable'
    
    return {
        'trend': trend,
        'activity_change': f"{((len(second_half) - len(first_half)) / max(len(first_half), 1)) * 100:.1f}%"
    }

def generate_recommendations(glyph_analysis, council_analysis, issues):
    """Generate actionable recommendations"""
    recommendations = []
    
    # Check critical glyph count
    critical_count = glyph_analysis['priority_distribution'].get('critical', 0)
    if critical_count > 3:
        recommendations.append({
            'priority': 'high',
            'action': 'Investigate recurring critical glyphs',
            'detail': f'{critical_count} critical events detected - review system alignment'
        })
    
    # Check consensus rate
    consensus_rate = council_analysis.get('consensus_rate', 0)
    if consensus_rate < 0.6:
        recommendations.append({
            'priority': 'medium',
            'action': 'Improve council deliberation',
            'detail': f'Consensus rate at {consensus_rate:.1%} - consider adjusting agent weights'
        })
    
    # Check for misalignment patterns
    misalignment_issues = [i for i in issues if 'misalignment' in i['type']]
    if misalignment_issues:
        recommendations.append({
            'priority': 'high',
            'action': 'Address system misalignment',
            'detail': 'Recurring misalignment detected - run diagnostics'
        })
    
    # Positive reinforcement
    if not recommendations:
        recommendations.append({
            'priority': 'info',
            'action': 'Maintain current operations',
            'detail': 'System performing optimally - no immediate action required'
        })
    
    return recommendations

def save_insights(summary):
    """Save insights to file"""
    # Load existing insights
    insights = {'daily': [], 'weekly': []}
    if INSIGHTS_PATH.exists():
        with open(INSIGHTS_PATH, 'r') as f:
            insights = json.load(f)
    
    # Add new summary
    timeframe = summary['timeframe']
    if timeframe not in insights:
        insights[timeframe] = []
    insights[timeframe].append(summary)
    
    # Keep only last 30 daily and 12 weekly summaries
    if timeframe == 'daily' and len(insights['daily']) > 30:
        insights['daily'] = insights['daily'][-30:]
    elif timeframe == 'weekly' and len(insights['weekly']) > 12:
        insights['weekly'] = insights['weekly'][-12:]
    
    with open(INSIGHTS_PATH, 'w') as f:
        json.dump(insights, f, indent=2)

def log_summary(summary):
    """Log summary to TRACE_LOG.md"""
    timeframe = summary['timeframe'].title()
    health = summary['system_health']
    
    log_entry = f"""
## {timeframe} Glyph Insights Summary: {summary['date']}

**System Health:** {health['status']} ({health['score']:.1f}/100)

### Glyph Activity
- Total Emissions: {summary['glyph_activity']['total_emissions']}
- Most Common: {summary['glyph_activity'].get('most_common_glyph', 'N/A')}
- Most Active Node: {summary['glyph_activity'].get('most_active_node', 'N/A')}

### Council Performance
- Deliberations: {summary['council_performance']['total_deliberations']}
- Consensus Rate: {summary['council_performance']['consensus_rate']:.1%}
- Avg Agreement: {summary['council_performance']['avg_agreement']:.2f}

### Issues Detected
"""
    
    if summary['issues_detected']:
        for issue in summary['issues_detected']:
            log_entry += f"- [{issue['severity'].upper()}] {issue['description']}\n"
    else:
        log_entry += "- No significant issues detected\n"
    
    log_entry += "\n### Recommendations\n"
    for rec in summary['recommendations']:
        log_entry += f"- [{rec['priority'].upper()}] {rec['action']}: {rec['detail']}\n"
    
    log_entry += "\n---\n"
    
    with open(TRACE_LOG_PATH, 'a') as f:
        f.write(log_entry)
    
    print(f"[INSIGHTS] Logged {timeframe.lower()} summary to TRACE_LOG.md")

def main():
    """Generate and log insights"""
    print("[INSIGHTS] Generating daily summary...")
    daily = generate_daily_summary()
    save_insights(daily)
    log_summary(daily)
    
    print(f"[INSIGHTS] Daily Summary:")
    print(f"  System Health: {daily['system_health']['status']} ({daily['system_health']['score']:.1f}/100)")
    print(f"  Glyph Emissions: {daily['glyph_activity']['total_emissions']}")
    print(f"  Consensus Rate: {daily['council_performance']['consensus_rate']:.1%}")
    print(f"  Issues: {len(daily['issues_detected'])}")
    
    print("\n[INSIGHTS] Generating weekly summary...")
    weekly = generate_weekly_summary()
    save_insights(weekly)
    log_summary(weekly)
    
    print(f"[INSIGHTS] Weekly Summary:")
    print(f"  System Health: {weekly['system_health']['status']} ({weekly['system_health']['score']:.1f}/100)")
    print(f"  Glyph Emissions: {weekly['glyph_activity']['total_emissions']}")
    print(f"  Consensus Rate: {weekly['council_performance']['consensus_rate']:.1%}")
    print(f"  Trend: {weekly['trends']['trend']}")

if __name__ == "__main__":
    main()
