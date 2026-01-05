# Copilot Instructions for B-Agent Repository

## Repository Purpose

**B-Agent (Barrot)** is an advanced autonomous AI agent system designed to systematically discover and assemble AGI (Artificial General Intelligence) components through a structured puzzle-based framework. The system operates continuously with 22 specialized AI agents working in parallel to achieve autonomous operations, recursive self-improvement, and distributed intelligence.

## Core Architecture

### 1. Multi-Agent System (22 Agents)
- **2 Core Agents**: Barrot (primary), SHRM v2 (strategic)
- **7 HRM Variants**: R (Reasoning), L (Learning), P (Perception), K (Knowledge), A (Adaptation), C (Creativity), M (Meta-learning)
- **7 Western Giants**: ChatGPT, Perplexity, Claude Sonnet, Gemini, Claude Opus, Grok, Watson X
- **6 Multilingual**: ChatGLM3, DeepSeek, Yi-34B, Rinna, Japanese-StableLM, Open-Calm

### 2. Key Systems
- **AGI Puzzle Protocol**: 56-piece framework for systematic AGI development
- **Progressive Ping-Pong**: 4-cycle iterative quality enhancement (target: 97%+ quality)
- **Autonomous Operations**: 24/7 self-directed decision-making and execution
- **Quantum Entanglement**: Distributed multi-agent synchronization (99.94% consistency)
- **Asynchronous Insights**: Problem-solving cycles every 30 minutes

### 3. Directory Structure
```
B-Agent/
├── Barrot-Agent/          # Core agent logic and configurations
├── barrot_sim/            # Simulation layer for processing
├── memory-bundles/        # Activity logs, provenance, and memory
├── site/                  # Web dashboard (GitHub Pages)
├── spells/                # Agent capability definitions
├── glyphs/                # Emitted pattern recognitions
├── .github/workflows/     # Automated workflows
└── *.md                   # Comprehensive documentation
```

## Development Guidelines

### Code Style & Conventions

#### Python
- Use Python 3.9+ features
- Follow PEP 8 style guidelines
- Use type hints for function signatures
- Prefer descriptive variable names (e.g., `puzzle_piece_count` not `ppc`)
- Document classes and functions with docstrings
- Use `snake_case` for functions and variables
- Use `PascalCase` for class names

#### YAML/JSON
- Use 2-space indentation for YAML files
- Validate JSON structure before committing
- Keep manifest files mutation-sealed (provenance tracking)
- Include timestamp and version fields in manifests

#### Markdown
- Use clear hierarchical headers (# ## ###)
- Include status badges and metadata at top
- Add table of contents for long documents
- Use code blocks with language specification
- Keep lines under 120 characters when possible

### Testing Requirements

- Write unit tests for new Python modules in `tests/` directory
- Test naming: `test_<module_name>.py`
- Ensure all tests pass before committing
- Mock external API calls in tests
- Test coverage target: 80%+ for core functionality
- Validate workflow YAML syntax before committing

### Commit Conventions

- Use descriptive commit messages (50 chars max for subject)
- Format: `<emoji> <type>: <description>`
- Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`
- Examples:
  - `✨ feat: add autonomous ingestion engine`
  - `🐛 fix: resolve merge conflict in manifest`
  - `📝 docs: update README with new features`
  - `🔧 refactor: optimize pingpong processor`

### Memory Bundle Protocol

**Critical**: Memory bundles preserve system state and provenance.

- **Never delete** files in `memory-bundles/` without explicit approval
- Append to logs, don't overwrite (use timestamps)
- Include provenance metadata in all updates:
  ```yaml
  timestamp: "2026-01-05T12:00:00Z"
  agent: "Barrot-Core"
  action: "data_ingestion"
  source: "autonomous_engine"
  ```
- Update `barrot_manifest.json` when emitting glyphs

### Common Patterns

#### 1. Glyph Emission
When discovering new patterns or insights:
```python
def emit_glyph(glyph_name, context):
    """Emit a new glyph pattern recognition"""
    glyph = {
        "name": glyph_name,
        "emitted_at": datetime.utcnow().isoformat(),
        "context": context,
        "confidence": calculate_confidence(context)
    }
    # Add to manifest
    # Log to memory-bundles/glyphic-synthesis-log.md
```

#### 2. Progressive Ping-Pong Processing
```python
def pingpong_cycle(data, max_cycles=4):
    """Apply iterative quality enhancement"""
    for cycle in range(max_cycles):
        # Ping: send through modules
        processed = process_through_modules(data)
        # Pong: receive and evaluate
        quality = evaluate_quality(processed)
        if quality > 0.97:
            break
        data = processed
    return data, quality
```

#### 3. Multi-Agent Consensus
```python
def get_consensus(prompt, agents):
    """Get consensus from multiple agents"""
    responses = []
    for agent in agents:
        response = agent.query(prompt)
        responses.append(response)
    return synthesize_consensus(responses)
```

### Anti-Patterns (AVOID)

❌ **Don't**:
- Delete or truncate memory-bundles without approval
- Make breaking changes to manifest schemas
- Hard-code API keys or credentials
- Remove existing glyphs from manifest
- Modify provenance timestamps
- Break backward compatibility in public APIs
- Commit large binary files (>1MB)
- Use relative imports outside package structure

✅ **Do**:
- Preserve all historical data in memory-bundles
- Version changes to critical files
- Use environment variables for credentials
- Append new glyphs to manifest
- Track all state changes with timestamps
- Maintain API compatibility or version
- Use Git LFS for large files if needed
- Use absolute imports or explicit relative imports

### Workflow Integration

#### GitHub Actions
- All workflows in `.github/workflows/` are critical infrastructure
- Test workflow changes locally before committing
- Maintain mutation-sealed provenance in workflow outputs
- Update `WORKFLOW_TROUBLESHOOTING.md` for new workflows

#### Key Workflows
- `BBR.yml`: Barrot Build Relay (build manifest updates)
- `Barrot-SHRM-PingPong.yml`: 15-minute validation cycles
- `asynchronous-insights.yml`: 30-minute insight generation
- `agi-puzzle-discovery.yml`: 6-hour puzzle piece searches

### Documentation Standards

- Keep README.md as primary entry point
- Document all new features in relevant protocol files
- Update version numbers and timestamps
- Include usage examples for new functionality
- Cross-reference related documents
- Maintain documentation hierarchy:
  - README.md → Protocol docs → Implementation docs → Memory logs

### Integration Points

#### APIs & External Services
- GitHub API: Repository automation
- Search engines: AGI puzzle discovery
- AI model APIs: Multi-agent processing
- GitHub Pages: Dashboard publishing

#### Data Ingestion
- YouTube: Transcript analysis
- arXiv: Research paper processing
- GitHub repos: Code pattern recognition
- Web crawling: Content acquisition

### Performance Targets

- Quality score: 97%+ (Progressive Ping-Pong)
- Processing speed: 2-200x improvements
- Agent consensus: 97%+ accuracy
- Uptime: 99.9%+ (continuous operations)
- State consistency: 99.94%+ (quantum entanglement)

### Security Considerations

- Never commit API keys, tokens, or credentials
- Validate all external inputs before processing
- Sanitize user-provided data
- Use environment variables for sensitive config
- Review dependencies for vulnerabilities
- Maintain audit logs in memory-bundles

### Getting Started for New Contributors

1. Read `README.md` for system overview
2. Review `AGI_PUZZLE_PROTOCOL.md` for mission context
3. Check `AUTONOMOUS_OPERATIONS_PROTOCOL.md` for operational framework
4. Explore `memory-bundles/` to understand system state
5. Test changes locally before pushing
6. Follow the commit conventions
7. Update relevant documentation

### Questions & Support

- Check `WORKFLOW_TROUBLESHOOTING.md` for common issues
- Review existing documentation in `*.md` files
- Examine memory-bundles logs for historical context
- Consult protocol documents for design decisions

---

**Last Updated**: 2026-01-05  
**Version**: 1.0  
**Status**: Active
