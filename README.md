# 🦜 Barrot-Agent

Welcome to **Barrot-Agent** - an intelligent agent system with advanced capabilities for data ingestion, prediction, and deployment.

> **📌 Note**: We are transitioning from `Main` to `main` as the default branch. See [DEFAULT_BRANCH_GUIDE.md](DEFAULT_BRANCH_GUIDE.md) for migration instructions.

## 🚀 Quick Start

### 💻 Desktop/Server Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Barrot-Agent/Barrot-Agent.git
   cd Barrot-Agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run health check:
   ```bash
   npm run health
   ```

4. View the current build manifest:
   ```bash
   cat build_manifest.yaml
   ```

5. Access the dashboard:
   - Visit: https://barrot-agent.github.io/Barrot-Agent/

**For Developers**: See [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) for setup, testing, and contribution guidelines.

### 📱 Mobile Setup
Want to access Barrot-Agent from your phone? 

**[📱 See Mobile Setup Guide](MOBILE_SETUP.md)**

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
│   ├── ci-cd.yml          # Comprehensive CI/CD pipeline
│   └── BBR.yml            # Build Relay workflow
├── tests/                 # Test suite
│   ├── test_manifest_validation.py
│   ├── test_workflow_integrity.py
│   └── test_documentation.py
├── scripts/               # Utility scripts
│   ├── validate_manifest.py
│   └── health_check.py
├── Barrot-Agent/          # Agent configuration
├── Barrot-Bundles/        # Bundle storage
├── memory-bundles/        # Memory and activity logs
├── site/                  # Web dashboard files
├── spells/                # Agent capability definitions
├── build_manifest.yaml    # Current build status
├── DEVELOPER_GUIDE.md     # Developer setup and guidelines
├── GAP_ANALYSIS.md        # Gap analysis and improvements
└── IMPLEMENTATION_SUMMARY.md  # Implementation summary
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

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Submit issues
- Create pull requests
- Improve documentation
- Add new features

**For Contributors**: See [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) for complete development setup, testing guidelines, and contribution workflow.

### Quick Contribution Workflow
```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
npm test

# Run health check
npm run health

# Validate manifest
npm run validate
```

## 📄 License

ISC License - See repository for details

## 🔗 Links

- **Repository**: https://github.com/Barrot-Agent/Barrot-Agent
- **Dashboard**: https://barrot-agent.github.io/Barrot-Agent/
- **Issues**: https://github.com/Barrot-Agent/Barrot-Agent/issues

## 📚 Documentation

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

### 🆕 Development & Quality Assurance
- **👨‍💻 [Developer Guide](DEVELOPER_GUIDE.md)** - Complete setup, testing, and contribution guide
- **🔍 [Gap Analysis](GAP_ANALYSIS.md)** - Comprehensive analysis and improvements
- **📋 [Implementation Summary](IMPLEMENTATION_SUMMARY.md)** - Complete implementation overview

## 💰 Support Barrot-Agent

Love Barrot-Agent? Consider becoming a sponsor!

[![Sponsor](https://img.shields.io/badge/Sponsor-💰-pink)](SPONSORSHIP.md)

Your sponsorship helps us:
- 🔬 Accelerate AGI research
- 🏆 Dominate AI benchmarks
- 🤖 Develop autonomous capabilities
- 📊 Improve transparency and logging
- 🌍 Grow the open-source community

**[View Sponsorship Tiers](SPONSORSHIP.md)**

---

**Barrot-Agent** - Intelligent automation and data processing at your fingertips 🦜✨
