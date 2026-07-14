# Security Policy

Thank you for helping keep **GitHub Push Protection Demo** secure. We take security reports seriously and appreciate responsible disclosure.

## Supported Versions

This repository is a demonstration project for GitHub Advanced Security features (push protection, secret scanning, and CodeQL). Security fixes are applied to the following branch:

| Version / Branch | Supported |
| ---------------- | --------- |
| `main`           | ✅        |
| Other branches   | ❌        |

## Reporting a Vulnerability

**Please do not open public GitHub issues for security vulnerabilities.**

Instead, report them privately using one of the options below:

1. **GitHub Private Vulnerability Reporting** (preferred)  
   Go to the repository **Security** tab → **Report a vulnerability** and submit your report there.

2. **Email**  
   If private reporting is unavailable, contact the maintainers through the contact method listed on the repository profile or organization page.

Include as much detail as possible:

- A clear description of the issue and its potential impact
- Steps to reproduce (proof of concept, if available)
- Affected files, endpoints, or workflow configurations
- Your suggested fix or mitigation, if you have one

### What to Expect

| Stage              | Target timeline |
| ------------------ | --------------- |
| Initial response   | Within 5 business days |
| Triage & severity  | Within 10 business days |
| Fix or mitigation  | Depends on severity; critical issues prioritized |
| Disclosure         | Coordinated with the reporter when possible |

We will keep you informed of progress and credit reporters in release notes when appropriate, unless you prefer to remain anonymous.

## Scope

### In scope

- Vulnerabilities in application code under `src/` (excluding intentionally vulnerable demo code — see below)
- Misconfigurations in GitHub Actions workflows under `.github/workflows/`
- CodeQL configuration issues in `.github/codeql/`
- Bypasses of secret scanning or push protection that affect this repository
- Dependency vulnerabilities in `requirements.txt`

### Out of scope

- **Intentionally vulnerable demo code** in `src/app.py` (hardcoded secrets and insecure patterns are present by design for demonstration)
- Social engineering, physical attacks, or denial-of-service against GitHub infrastructure
- Issues in third-party services outside this repository’s control
- Findings from automated scanners with no demonstrated exploitability (e.g., generic “informational” alerts without impact)

When in doubt, report it — we would rather receive a duplicate than miss a real issue.

## Security Practices for This Project

This demo illustrates both insecure and secure patterns:

| Pattern | Demo (insecure) | Recommended (secure) |
| ------- | ---------------- | -------------------- |
| API keys & secrets | Hardcoded in `src/app.py` | Environment variables, as in `src/proper_app.py` |
| Secret commits | Blocked by GitHub push protection | Use `.env` locally; never commit secrets |
| Static analysis | CodeQL on every push/PR to `main` | Fix critical/high findings before merging |

### For contributors

- **Never commit real credentials**, tokens, API keys, or private keys — even for testing.
- Use environment variables or a secrets manager for sensitive configuration.
- Run the application locally with `API_KEY` set in your environment when testing the secure example.
- Review CodeQL alerts in pull requests before requesting review.

## Security Tooling in This Repository

The following GitHub Advanced Security capabilities are enabled or demonstrated here:

| Tool | Purpose | Configuration |
| ---- | ------- | --------------- |
| **Push protection / Secret scanning** | Blocks commits containing known secret patterns | Repository settings |
| **CodeQL analysis** | Static analysis for Python security issues | [`.github/workflows/codeql-analysis.yml`](codeql-analysis.yml), [`.github/codeql/codeql-config.yml`](../codeql/codeql-config.yml) |
| **Dependabot** (recommended) | Automated dependency update PRs | Enable under **Settings → Security → Dependabot** |

CodeQL runs on:

- Push to `main`
- Pull requests targeting `main`
- Weekly schedule (Mondays at 06:00 UTC)

## Recognition

We are grateful to security researchers who report valid, in-scope vulnerabilities responsibly. With your permission, we will acknowledge your contribution in fix notes or release documentation.

---

*Last updated: July 2026*
