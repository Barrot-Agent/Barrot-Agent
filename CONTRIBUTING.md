# 🤝 Contributing to Barrot-Agent

Welcome! We're excited you're interested in contributing to Barrot-Agent. This guide will help you understand our conventions, workflows, and best practices.

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [Repository Structure](#repository-structure)
- [Development Workflow](#development-workflow)
- [Naming Conventions](#naming-conventions)
- [Code Standards](#code-standards)
- [Documentation Standards](#documentation-standards)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Pull Request Process](#pull-request-process)
- [Testing Guidelines](#testing-guidelines)
- [Logging and Memory Bundles](#logging-and-memory-bundles)

## 🚀 Getting Started

### Prerequisites

- Git
- Basic understanding of YAML
- Familiarity with GitHub Actions (for workflow contributions)
- Docker (optional, for containerized development)

### Setup

1. **Fork the repository**
   ```bash
   # Fork via GitHub UI, then clone your fork
   git clone https://github.com/YOUR-USERNAME/Barrot-Agent.git
   cd Barrot-Agent
   ```

2. **Set up remote**
   ```bash
   git remote add upstream https://github.com/Barrot-Agent/Barrot-Agent.git
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Configure VS Code** (optional but recommended)
   - See [docs/guides/VSCODE_SETUP.md](docs/guides/VSCODE_SETUP.md)

## 📁 Repository Structure

Barrot-Agent follows a **SHRM v2.0 layer-based architecture**. Understanding this is crucial:

```
docs/guides/      → L1: Pattern Recognition (user-facing guides)
docs/reference/   → L2: Abstraction (deep knowledge)
scripts/          → L3: Narrative Simulation (executable flows)
docs/configs/     → L4: Meta-Reasoning (system configuration)
glyphs/           → L5: Symbolic Ethics (symbolic patterns)
```

See [ARCHITECTURE.md](ARCHITECTURE.md) for complete details.

## 🔄 Development Workflow

### Branch Strategy

- **`main`** - Default branch (stable)
- **`feature/*`** - New features
- **`fix/*`** - Bug fixes
- **`docs/*`** - Documentation updates
- **`refactor/*`** - Code refactoring
- **`copilot/*`** - GitHub Copilot automated work

### Workflow Steps

1. **Sync with upstream**
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Make changes**
   - Follow naming conventions (see below)
   - Add appropriate logging
   - Update documentation

3. **Test changes**
   - Verify locally
   - Check YAML syntax: `yamllint file.yml`
   - Test workflows locally if possible

4. **Commit**
   ```bash
   git add .
   git commit -m "feat: add new capability"
   ```

5. **Push and create PR**
   ```bash
   git push origin feature/your-feature-name
   ```

## 📝 Naming Conventions

### Files and Directories

- **YAML/YML**: Use `.yml` extension (not `.yaml` unless legacy)
- **Markdown**: Use `.md` extension
- **Scripts**: Use descriptive names with extension (`.sh`, `.ps1`)
- **Glyphs**: `{name}_glyph.yml` format
- **Configs**: `{system}-config.yml` format

### Examples

✅ **Good**:
- `organoid_reasoning_glyph.yml`
- `shrm-config.yaml`
- `migrate-default-branch.sh`
- `MOBILE_SETUP.md`

❌ **Bad**:
- `BBR,yml` (comma in filename)
- `config` (no extension)
- `script` (not descriptive)

### Directories

- Use lowercase with hyphens for multi-word names
- Examples: `memory-bundles`, `simulation-stack`, `docs/guides`

## 💻 Code Standards

### YAML Files

```yaml
# Use 2-space indentation
name: Example Workflow

# Add comments for complex sections
on:
  push:
    branches: [ main ]  # Trigger on main branch

# Use descriptive keys
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Descriptive step name
        run: |
          echo "Clear commands"
```

### Scripts

- **Bash**: Include shebang (`#!/bin/bash`)
- **PowerShell**: Use UTF-8 encoding
- Add error handling (`set -e` for bash)
- Include comments for complex logic

### Glyphs

Follow the established glyph format:

```yaml
glyph_name: example_glyph
glyph_id: EXM-001
version: 1.0.0
timestamp: 2025-12-28T00:00:00Z

description: >
  Clear description of the glyph's purpose

symbolic_representation: "🔮 ◬ ≋"

properties:
  dimension: cognitive
  mutability: adaptive
  
hermetic_correspondence:
  principle: vibration
  polarity: static ⟷ dynamic
```

## 📚 Documentation Standards

### Markdown

- Use clear headings (`#`, `##`, `###`)
- Add table of contents for long documents
- Include code examples with syntax highlighting
- Use emoji sparingly but meaningfully (✅, ❌, 🚀, etc.)

### Documentation Types

1. **Guides** (docs/guides/) - Step-by-step instructions
2. **Reference** (docs/reference/) - Comprehensive explanations
3. **Config** (docs/configs/) - Integration specifications

### Example Guide Structure

```markdown
# 📱 Guide Title

Brief introduction (1-2 sentences).

## Prerequisites

- Item 1
- Item 2

## Steps

### Step 1: First Action

Detailed instructions...

### Step 2: Second Action

More instructions...

## Troubleshooting

Common issues and solutions.
```

## 📝 Commit Message Guidelines

Follow **Conventional Commits**:

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting changes
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance tasks
- `workflow`: GitHub Actions changes

### Examples

```
feat(glyphs): add temporal navigation glyph

Add new glyph for temporal dimension navigation with quantum
coherence parameters and hermetic correspondence to rhythm principle.

Closes #123
```

```
fix(workflows): correct SHRM ping-pong timing

Changed cron schedule from */15 to */30 minutes to reduce
API calls and improve system stability.
```

```
docs(guides): update mobile setup for iOS 17

Added new screenshots and updated Termux configuration
for latest iOS version.
```

## 🔀 Pull Request Process

### Before Submitting

1. ✅ Ensure all tests pass
2. ✅ Update relevant documentation
3. ✅ Add entry to memory-bundles if significant
4. ✅ Verify YAML syntax
5. ✅ Check for merge conflicts

### PR Template

```markdown
## Description

Brief description of changes.

## Type of Change

- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring

## SHRM Layer

Which layer does this affect?
- [ ] L1: Pattern Recognition (guides)
- [ ] L2: Abstraction (reference)
- [ ] L3: Narrative Simulation (scripts)
- [ ] L4: Meta-Reasoning (configs)
- [ ] L5: Symbolic Ethics (glyphs)

## Testing

How were changes tested?

## Checklist

- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] No breaking changes
- [ ] Logged in memory-bundles (if applicable)
```

### Review Process

1. Automated checks must pass
2. At least one maintainer review required
3. Address feedback promptly
4. Squash commits if requested

## 🧪 Testing Guidelines

### Workflow Testing

Test GitHub Actions locally when possible:

```bash
# Install act (GitHub Actions local runner)
brew install act  # macOS
# or
curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash

# Run workflow
act -n  # Dry run
act     # Full run
```

### YAML Validation

```bash
# Install yamllint
pip install yamllint

# Validate files
yamllint .github/workflows/*.yml
yamllint glyphs/*.yml
```

### Manual Testing

- Test scripts in isolated environment first
- Verify dashboard changes locally before deploying
- Check mobile compatibility for UI changes

## 📊 Logging and Memory Bundles

### When to Log

Log significant activities to `memory-bundles/`:

- **activity-log.md** - General activities
- **data-ingestion-log.md** - New data sources
- **github-issue-resolutions.md** - Issue fixes
- **optimization-log.md** - Performance improvements
- **resource-discovery-log.md** - New resources found

### Log Format

```markdown
## YYYY-MM-DD - Activity Title

**Type**: Feature | Fix | Optimization | Discovery

**Description**: 
Clear description of what was done.

**Impact**:
- Impact point 1
- Impact point 2

**Resources**:
- Link 1
- Link 2

**Status**: Complete | In Progress | Blocked
```

### Example

```markdown
## 2025-12-28 - Added Temporal Navigation Glyph

**Type**: Feature

**Description**: 
Created new glyph for temporal dimension navigation with quantum
coherence support and hermetic rhythm principle mapping.

**Impact**:
- Enables multi-dimensional time reasoning
- Improves AGI temporal adaptability metrics
- Provides foundation for time-aware prediction rails

**Resources**:
- glyphs/temporal_navigation_glyph.yml
- ARCHITECTURE.md (updated)

**Status**: Complete
```

## 🎯 Specific Contribution Areas

### Adding a New Glyph

1. Create `glyphs/{name}_glyph.yml`
2. Follow glyph format standards
3. Add hermetic correspondence
4. Update `ARCHITECTURE.md`
5. Log to `memory-bundles/activity-log.md`

### Adding a New Workflow

1. Create `.github/workflows/{name}.yml`
2. Test with `act` if possible
3. Document in `ARCHITECTURE.md`
4. Add permissions section
5. Include error handling

### Adding Documentation

1. Determine correct location (guides/configs/reference)
2. Follow markdown standards
3. Update README.md if adding new guide
4. Cross-link related documents

### Improving Memory Bundles

1. Maintain consistent format
2. Add timestamps
3. Use clear, searchable titles
4. Link to relevant commits/PRs

## 🐛 Reporting Issues

### Bug Reports

Include:
- Clear description
- Steps to reproduce
- Expected vs actual behavior
- Environment (OS, browser, etc.)
- Screenshots if applicable

### Feature Requests

Include:
- Use case description
- Proposed solution
- Alternative solutions considered
- SHRM layer alignment (which layer would this affect?)

## 💬 Communication

- **Issues**: Bug reports, feature requests
- **Discussions**: General questions, ideas
- **PRs**: Code contributions

## 🙏 Recognition

All contributors are recognized in:
- Git commit history
- `docs/SPONSORS.md` (for sponsors)
- Release notes

## 📄 License

By contributing, you agree that your contributions will be licensed under the ISC License.

---

**Questions?** Open an issue or start a discussion!

**Barrot-Agent Team** 🦜✨
