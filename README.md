# 🦜 Barrot-Agent

Welcome to **Barrot-Agent** - an intelligent agent system with advanced capabilities for data ingestion, prediction, and deployment.

> **📌 Note**: We are transitioning from `Main` to `main` as the default branch. See [DEFAULT_BRANCH_GUIDE.md](docs/guides/DEFAULT_BRANCH_GUIDE.md) for migration instructions.

## 🚀 Quick Start

### 💻 Desktop/Server Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Barrot-Agent/Barrot-Agent.git
   cd Barrot-Agent
   ```

2. View the current build manifest:
   ```bash
   cat build_manifest.yaml
   ```

3. Access the dashboard:
   - Visit: https://barrot-agent.github.io/Barrot-Agent/

### 📱 Mobile Setup
Want to access Barrot-Agent from your phone? 

**[📱 See Mobile Setup Guide](docs/guides/MOBILE_SETUP.md)**

The mobile guide covers:
- 🌐 Web dashboard access
- 📱 GitHub Mobile app usage
- 🔧 Terminal setup for Android (Termux)
- 🔧 Terminal setup for iOS (iSH)
- 🔐 Authentication configuration
- 📊 Monitoring and workflows

## 📁 Repository Structure

```
Barrot-Agent/
├── .github/workflows/      # GitHub Actions automation
├── docs/                   # Documentation
│   ├── guides/            # Setup and usage guides
│   ├── configs/           # Configuration documentation
│   └── reference/         # Reference documentation
├── scripts/               # Utility scripts
├── Barrot-Bundles/        # Bundle storage
├── memory-bundles/        # Memory and activity logs
├── gumroad/               # Gumroad integration
├── site/                  # Web dashboard files
├── spells/                # Agent capability definitions
├── glyphs/                # Advanced capability definitions
├── SHRM-System/           # SHRM reasoning engine
├── simulation-stack/      # Simulation configurations
└── build_manifest.yaml    # Current build status
```

## 🎯 Features

### Core Modules
- **Prediction Methodologies** - Advanced prediction capabilities
- **Deployment Integrity** - Reliable deployment systems
- **Microagent Logic** - Builder.io integration
- **Search Engine** - Comprehensive search capabilities
- **Dashboard** - Real-time status monitoring
- **Manifest Rail** - Build tracking system

### Agent Spells
- **Ω-Ingest** (Omega-Ingest) - Quantum data assimilation
- **Keyseer's Insight** - Intelligent key analysis

### Data Resources
The agent can access and process data from:
- Kaggle datasets
- GitHub repositories
- Research papers
- Video platforms
- Podcasts and interviews
- Books and journals
- And many more sources...

## 🔧 Configuration

### Build Manifest
The `build_manifest.yaml` file tracks:
- Build signature and timestamp
- Active modules
- Rail status (ingestion, deployment, microagent, etc.)
- Resource connections
- Provenance hash

### Workflows
Automated workflows handle:
- Build manifest updates
- Repository cleanup
- Dashboard publishing
- Bundle management

## 📊 Monitoring

### Web Dashboard
Access the live dashboard at:
```
https://barrot-agent.github.io/Barrot-Agent/
```

### GitHub Actions
Monitor workflow runs:
```
https://github.com/Barrot-Agent/Barrot-Agent/actions
```

### Build Status
Check current build status:
```bash
cat build_manifest.yaml
```

View recent activity:
```bash
cat memory-bundles/outcome-relay.md | tail -20
```

## 🚀 Deployment

Barrot-Agent can be deployed to multiple cloud platforms:

- **GitHub Pages** (Current): https://barrot-agent.github.io/Barrot-Agent/
- **Heroku**: One-click deployment with `app.json`
- **Render**: Static site deployment with `render.yaml`
- **Railway**: Docker-based deployment with `railway.json`
- **Fly.io**: Global edge deployment with `fly.toml`
- **Docker**: Self-hosted container deployment

**[📖 See Full Deployment Guide](DEPLOYMENT.md)**

### Quick Deploy

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Barrot-Agent/Barrot-Agent)

### Docker

```bash
docker build -t barrot-agent .
docker run -p 8080:8080 barrot-agent
```

The Dockerfile includes:
- Ubuntu 22.04 base
- Git, curl, and essential tools
- GitHub Actions runner setup

## 🏛️ Architecture

Barrot-Agent is built on **SHRM v2.0** (Sapient's Hierarchy Reasoning Model), featuring a five-layer cognitive architecture where the repository structure itself embodies intelligent reasoning principles:

- **Layer 1** (docs/guides/) - Pattern Recognition: User-facing interaction patterns
- **Layer 2** (docs/reference/) - Abstraction: Deep knowledge structures  
- **Layer 3** (scripts/) - Narrative Simulation: Executable action sequences
- **Layer 4** (docs/configs/) - Meta-Reasoning: System introspection
- **Layer 5** (glyphs/) - Symbolic Ethics: Meaning and resonance

Each directory corresponds to a distinct cognitive layer, creating a living, reasoning codebase. See [ARCHITECTURE.md](ARCHITECTURE.md) for complete details.

## 🤝 Contributing

Contributions are welcome! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) guide for:
- Development workflow and branch strategy
- Naming conventions and code standards
- Commit message guidelines
- Pull request process
- Testing and logging guidelines

New contributors should start with [ARCHITECTURE.md](ARCHITECTURE.md) to understand the SHRM v2.0 layer mappings.

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and migration guides.

## 📄 License

ISC License - See repository for details

## 🔗 Links

- **Repository**: https://github.com/Barrot-Agent/Barrot-Agent
- **Dashboard**: https://barrot-agent.github.io/Barrot-Agent/
- **Issues**: https://github.com/Barrot-Agent/Barrot-Agent/issues
- **Architecture**: [ARCHITECTURE.md](ARCHITECTURE.md)
- **Contributing**: [CONTRIBUTING.md](CONTRIBUTING.md)
- **Changelog**: [CHANGELOG.md](CHANGELOG.md)

## 📚 Documentation

### Setup Guides
- **🔄 [Default Branch Guide](docs/guides/DEFAULT_BRANCH_GUIDE.md)** - Migrating to `main` branch
- **📱 [Mobile Setup](docs/guides/MOBILE_SETUP.md)** - Access Barrot from your phone
- **💻 [VS Code Setup](docs/guides/VSCODE_SETUP.md)** - Optimal development environment
- **✅ [Setup Verification](docs/guides/SETUP_VERIFICATION.md)** - Verify your setup

### Reference Documentation
- **🚀 [AGI Development](docs/reference/AGI_DEVELOPMENT.md)** - AGI acceleration protocols
- **📥 [Ingestion Manifest](docs/reference/INGESTION_MANIFEST.md)** - Complete ingestion capabilities
- **💸 [Monetization Framework](docs/reference/MONETIZATION_FRAMEWORK.md)** - Autonomous revenue generation (12+ streams)
- **📊 [Output Logging](docs/reference/OUTPUT_LOGGING.md)** - Comprehensive logging framework
- **🔄 [Data Transformation](docs/reference/DATA_TRANSFORMATION.md)** - Data transformation guide

### Configuration
- **💰 [Gumroad Integration](docs/configs/GUMROAD.md)** - E-commerce integration

### Community
- **💰 [Sponsorship](docs/SPONSORSHIP.md)** - Support Barrot-Agent development
- **🎖️ [Sponsors](docs/SPONSORS.md)** - Our amazing sponsors
- **🔬 [Platform Alternatives Research](PLATFORM_ALTERNATIVES_RESEARCH.md)** - Research free platforms for revolutionary search engine
- **🚀 [Deployment Guide](DEPLOYMENT.md)** - Deploy to Heroku, Render, Railway, Fly.io, or Docker
- **🔄 [Default Branch Guide](DEFAULT_BRANCH_GUIDE.md)** - Migrating to `main` branch
- **📱 [Mobile Setup](MOBILE_SETUP.md)** - Access Barrot from your phone
- **💻 [VS Code Setup](VSCODE_SETUP.md)** - Optimal development environment
- **💰 [Sponsorship](SPONSORSHIP.md)** - Support Barrot-Agent development
- **🎖️ [Sponsors](SPONSORS.md)** - Our amazing sponsors
- **💸 [Monetization Framework](MONETIZATION_FRAMEWORK.md)** - Autonomous revenue generation (12+ streams)
- **📊 [Output Logging](OUTPUT_LOGGING.md)** - Comprehensive logging framework
- **🔄 [Data Transformation](DATA_TRANSFORMATION.md)** - Data transformation guide
- **🚀 [AGI Development](AGI_DEVELOPMENT.md)** - AGI acceleration protocols
- **📥 [Ingestion Manifest](INGESTION_MANIFEST.md)** - Complete ingestion capabilities

## 💰 Support Barrot-Agent

Love Barrot-Agent? Consider becoming a sponsor!

[![Sponsor](https://img.shields.io/badge/Sponsor-💰-pink)](docs/SPONSORSHIP.md)

Your sponsorship helps us:
- 🔬 Accelerate AGI research
- 🏆 Dominate AI benchmarks
- 🤖 Develop autonomous capabilities
- 📊 Improve transparency and logging
- 🌍 Grow the open-source community

**[View Sponsorship Tiers](docs/SPONSORSHIP.md)**

---

**Barrot-Agent** - Intelligent automation and data processing at your fingertips 🦜✨
