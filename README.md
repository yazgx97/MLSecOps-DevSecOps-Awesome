# MLSecOps - DevSecOps - Awesome

This project is dedicated to curating a comprehensive list of resources, tools, and best practices at the intersection of Machine Learning Security Operations (MLSecOps), and Development Security Operations (DevSecOps). Our goal is to provide a centralized hub for professionals, researchers, and enthusiasts who are passionate about integrating security into the development and deployment of machine learning systems.

## Contents

- [What is MLSecOps?](#what-is-mlsecops)
- [What is DevSecOps?](#what-is-devsecops)
- [Repository Overview](#repository-overview)
- [Proposed Pipeline](#proposed-pipeline)
- [Resources](#resources)
  - [Articles](#articles)
  - [Papers](#papers)
  - [Tutorials](#tutorials)
  - [Courses](#courses)
  - [Kubernetes](#kubernetes)
- [Tools](#tools)
  - [MLSecOps](#mlsecops)
  - [DevSecOps](#devsecops)
  - [Monitoring](#monitoring)
  - [Key Management](#key-management)
- [Best Practices](#best-practices)
- [Case Studies](#case-studies)
- [Community](#community)
- [Contribution](#contribution)

## What is MLSecOps?

MLSecOps is an emerging field that focuses on the secure and efficient operation of machine learning models in production environments. It combines the principles of DevSecOps with the unique challenges of machine learning, emphasizing the importance of security, privacy, and compliance throughout the ML lifecycle.

## What is DevSecOps?

DevSecOps extends the traditional DevOps framework by incorporating security practices into the entire software development process. It aims to automate security checks and integrate them seamlessly into the CI/CD pipeline, ensuring that security is a fundamental part of the development workflow.

## Repository Overview

In this repository, you will find:

* Resources: Articles, papers, and tutorials on MLSecOps and DevSecOps.
* Tools: A curated list of open-source tools for securing ML models and development pipelines.
* Best Practices: Guidelines and methodologies for implementing security measures in ML projects.
* Case Studies: Real-world examples of successful MLSecOps and DevSecOps implementations.
* Community: Links to forums, conferences, and groups where you can connect with others interested in these fields.

# Proposed Pipeline

### 💥 MLSecOps Pipeline

![image](https://github.com/user-attachments/assets/44ce27e4-5e41-41cf-ad3e-4a22286c54ef)

Article analysis for this MLO pipeline 👉 [MLSECOPS: Secure your Large Language Model (LLM) applications](https://lethanhphuc-pk.medium.com/mlsecops-secure-your-large-language-model-llm-applications-6b60cb25c4fa)

### 💥 DevSecOps Pipeline

![image](https://github.com/user-attachments/assets/dabe6315-e05f-4a3d-8c2a-501b9e329c2d)

Article analysis for this DSO pipeline 👉 [DevSecOps: A journey to protect your applications](https://lethanhphuc-pk.medium.com/devsecops-a-journey-to-protect-your-applications-fdee7b4700eb)

## Resources

### Articles

- [Visualizing Secure MLOps (MLSecOps): A Practical Guide for Building Robust AI/ML Pipeline Security](https://openssf.org/blog/2025/08/05/visualizing-secure-mlops-mlsecops-a-practical-guide-for-building-robust-ai-ml-pipeline-security/) - OpenSSF whitepaper walkthrough: layer-by-layer MLSecOps using SLSA, Sigstore, and Scorecard.
- [How River takes security work from a fix to merge](https://shopify.engineering/river-vulnerability-remediation) - Shopify’s agentic remediation loop from finding through merge and evidence checks (2026).
- [Building an agentic harness that outlasts the model](https://shopify.engineering/building-an-agentic-harness-that-outlasts-the-model) - Shopify Application Security on multi-agent vuln discovery, test oracles, and PR-ready fixes.
- [MLSecOps: Protecting the AI/ML Lifecycle in telecom](https://www.ericsson.com/en/reports-and-papers/white-papers/mlsecops-protecting-the-ai-ml-lifecycle-in-telecom) - Ericsson on secure-by-design MLSecOps for telecom AI/ML lifecycles.
- [MLSecOps Practical Reference Guide](https://github.com/MHaghighian/MLSecOps) - Open-source AI and ML security handbook.
- [How MLSecOps Can Reshape AI Security](https://www.forbes.com/sites/forbestechcouncil/2023/12/04/how-mlsecops-can-reshape-ai-security/)
- [MLSecOps Explained: Building Security Into ML & AI](https://www.brighttalk.com/business/products/custom-webinars-sponsorable-events/originals-episode/SBA56-mlsecops-explained-building-security-into-ml-ai)
- [The Comprehensive Evolution Of DevSecOps In Modern Software Ecosystems](https://www.forbes.com/sites/forbestechcouncil/2024/03/06/the-comprehensive-evolution-of-devsecops-in-modern-software-ecosystems/)

### Papers

| Title | Summary |
| --- | --- |
| [Attesting LLM Pipelines: Enforcing Verifiable Training and Release Claims](https://arxiv.org/abs/2603.28988) | Attestation-aware promotion gate that binds training/release claims to LLM pipeline artifacts before trusted deploy. |
| [SecMLOps: A Comprehensive Framework for Integrating Security Throughout the MLOps Lifecycle](https://arxiv.org/abs/2601.10848) | Lifecycle framework that embeds security across MLOps using a People/Technology/Process/Governance/Compliance lens. |
| [Towards Secure MLOps: Surveying Attacks, Mitigation Strategies, and Research Challenges](https://arxiv.org/abs/2506.02032) | Survey of MLOps attacks and early mitigations mapped with MITRE ATLAS, plus open research gaps. |
| [Atlas: A Framework for ML Lifecycle Provenance & Transparency](https://arxiv.org/abs/2502.19567) | Attestable ML pipelines via open provenance specs, trusted hardware, and transparency logs. |
| [Integrating MLSecOps in the Biotechnology Industry 5.0](https://arxiv.org/abs/2402.07967) | How MLSecOps practices and regulation apply to Biotechnology Industry 5.0 threat surfaces. |
| [Security Risks and Best Practices of MLOps: A Multivocal Literature Review](https://ceur-ws.org/Vol-3731/paper13.pdf) | Multivocal review synthesizing 15 MLOps risks and 27 related best practices across 8 themes. |
| [Backdoor Attacks to Deep Neural Networks: A Survey of the Literature, Challenges, and Future Research Directions](https://ieeexplore.ieee.org/abstract/document/10403914) | Survey of DNN backdoor attack strategies, defenses, and open research questions. |
| [The emergence and importance of DevSecOps: Integrating and reviewing security practices within the DevOps pipeline](https://wjaets.com/content/emergence-and-importance-devsecops-integrating-and-reviewing-security-practices-within) | Overview of DevSecOps principles—automation, collaboration, culture—for securing the DevOps pipeline. |


### Tutorials

- [MLSecOps with Automated Online and Offline ML Model Evaluations on Kubernetes](https://www.youtube.com/watch?v=5WUhmWTMo4g&pp=ygURbWxzZWNvcHMgdHV0b3JpYWw%3D)
- ["What is MLSecOps?" Building security into MLOps workflows by leveraging DevSecOps principles.](https://www.youtube.com/watch?v=iwPKQbZumN0&pp=ygURbWxzZWNvcHMgdHV0b3JpYWw%3D)
- [DevSecOps Tutorial for Beginners | CI Pipeline with GitHub Actions and Docker Scout](https://www.youtube.com/watch?v=gLJdrXPn0ns&pp=ygUSZGV2c2Vjb3BzIHR1dG9yaWFs)
- [DevSecOps Pipeline Project: Deploy Netflix Clone on Kubernetes](https://www.youtube.com/watch?v=g8X5AoqCJHc&pp=ygUSZGV2c2Vjb3BzIHR1dG9yaWFs)
- [DevSecOps with Jenkins | Boost Your CICD Pipeline Security !!](https://www.youtube.com/watch?v=QUIXJW_h_K0&pp=ygUSZGV2c2Vjb3BzIHR1dG9yaWFs)

### Courses

- [Practical DevSecOps](https://www.practical-devsecops.com/)
- [DevSecOps Training](https://www.eccouncil.org/train-certify/certified-devsecops-engineer-ecde/)
- [DevSecOps : Master Securing CI/CD | DevOps Pipeline |Handson](https://www.udemy.com/course/devsecops/?utm_source=adwords&utm_medium=udemyads&utm_campaign=Search_DSA_Beta_Prof_la.EN_cc.ROW-English&campaigntype=Search&portfolio=ROW-English&language=EN&product=Course&test=&audience=DSA&topic=&priority=Beta&utm_content=deal4584&utm_term=_._ag_162511579564_._ad_696197165427_._kw__._de_c_._dm__._pl__._ti_dsa-1677053911888_._li_9198559_._pd__._&matchtype=&gad_source=1&gclid=CjwKCAjw74e1BhBnEiwAbqOAjOS1FIYA31Sgo8GjmN7B6Gh5pWR_x1yWCZ0ftdx38RLWVytcJiTdzRoCWtgQAvD_BwE&couponCode=2021PM25)

### Kubernetes

- [KubeStellar Console](https://github.com/kubestellar/console) - Multi-cluster Kubernetes dashboard with AI-powered operations, real-time observability, and CNCF project integrations across edge and cloud clusters.

## Tools

### MLSecOps

#### Stage 1

| Tool | Description |
| --- | --- |
| [Pre-Commit Hook Scans](https://pre-commit.com/) | A framework for managing and maintaining multi-language pre-commit hooks. |
| [Trivy Vulnerability Scanner](https://marketplace.visualstudio.com/items?itemName=AquaSecurityOfficial.trivy-vulnerability-scanner) | Comprehensive vulnerability scanner for containers and other artifacts. |
| [Trunk Check](https://marketplace.visualstudio.com/items?itemName=trunk.io) | Automated Code Quality for Teams: universal formatting, linting, static analysis, and security. |

#### Stage 2

| Tool | Description |
| --- | --- |
| [AWS S3 bucket](https://aws.amazon.com/s3/) | A bucket is a container for objects stored in Amazon S3. |
| [Nexus Repository](https://www.sonatype.com/products/sonatype-nexus-repository) | Sonatype Nexus Repository |

#### Stage 3

| Tool | Description |
| --- | --- |
| [Gitleak](https://gitleaks.io/) | Secret scanner for git repositories, files, and directories. |
| [Sonarqube](https://www.sonatype.com/products/sonatype-nexus-repository) | Open-source platform for continuous inspection of code quality. |
| [Trivy](https://aquasecurity.github.io/trivy/) | Comprehensive vulnerability scanner for containers and other artifacts. |
| [Horusec](https://horusec.io/) | Tool to perform static code analysis to identify security flaws. |
| [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/) | Tool that identifies project dependencies and checks for known vulnerabilities. |
| [NB Defense](https://nbdefense.ai/) | Security tool for Jupyter notebooks, scanning for vulnerabilities and risks. |
| Compliance check | PIC/DSS, ISO/IEC 27001, NIST 800-53B, ... |
| [compliance-checker](https://github.com/ioos/compliance-checker) | Python tool to check your datasets against compliance standards |

#### Stage 4

| Tool | Description |
| --- | --- |
| Quality Gate | Define a rule/ policy for test result. |

#### Stage 5

| Tool | Description |
| --- | --- |
| [EarlyStopping](https://keras.io/api/callbacks/early_stopping/) | Stop training when a monitored metric has stopped improving. |
| [KFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html) | K-Fold cross-validator. |

#### Stage 6

| Tool | Description |
| --- | --- |
| [EarlyStopping](https://scikit-learn.org/stable/modules/model_evaluation.html) | Metrics and scoring: quantifying the quality of predictions. |

#### Stage 7

| Tool | Description |
| --- | --- |
| [modelscan](https://github.com/protectai/modelscan) | Protection Against ML Model Serialization Attacks. |
| [Vigil](https://github.com/deadbits/vigil-llm) | LLM prompt injection and security scanner. |
| [Garak](https://github.com/leondz/garak) | LLM vulnerability scanner. |
| [promptfoo](https://github.com/promptfoo/promptfoo) | LLM red teaming and evaluation framework with adversarial attacks. |

#### Stage 8

| Tool | Description |
| --- | --- |
| Quality Gate | Define a rule/ policy for test result. |

#### Stage 9

| Tool | Description |
| --- | --- |
| [OpenPubKey](https://github.com/openpubkey/openpubkey) | OpenPubkey is a protocol for leveraging OpenID Providers (OPs) to bind identities to public keys. |

#### Stage 10

| Tool | Description |
| --- | --- |
| [AWS S3 bucket](https://aws.amazon.com/s3/) | A bucket is a container for objects stored in Amazon S3. |
| [Nexus Repository](https://www.sonatype.com/products/sonatype-nexus-repository) | Sonatype Nexus Repository |

### DevSecOps

#### Stage 1

| Tool | Description |
| --- | --- |
| [Pre-Commit Hook Scans](https://pre-commit.com/) | A framework for managing and maintaining multi-language pre-commit hooks. |
| [Trivy Vulnerability Scanner](https://marketplace.visualstudio.com/items?itemName=AquaSecurityOfficial.trivy-vulnerability-scanner) | Comprehensive vulnerability scanner for containers and other artifacts. |
| [Trunk Check](https://marketplace.visualstudio.com/items?itemName=trunk.io) | Automated Code Quality for Teams: universal formatting, linting, static analysis, and security. |

#### Stage 2

| Tool | Description |
| --- | --- |
| [AWS S3 bucket](https://aws.amazon.com/s3/) | A bucket is a container for objects stored in Amazon S3. |
| [Nexus Repository](https://www.sonatype.com/products/sonatype-nexus-repository) | Sonatype Nexus Repository |

#### Stage 3

| Tool | Description |
| --- | --- |
| [Gitleak](https://gitleaks.io/) | Secret scanner for git repositories, files, and directories. |
| [Sonarqube](https://www.sonatype.com/products/sonatype-nexus-repository) | Open-source platform for continuous inspection of code quality. |
| [Trivy](https://aquasecurity.github.io/trivy/) | Comprehensive vulnerability scanner for containers and other artifacts. |
| [Horusec](https://horusec.io/) | Tool to perform static code analysis to identify security flaws. |
| [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/) | Tool that identifies project dependencies and checks for known vulnerabilities. |
| [Checkov](https://www.checkov.io/) | Checkov scans cloud infrastructure configurations to find misconfigurations. |
| [TFlint](https://github.com/terraform-linters/tflint) | A Pluggable Terraform Linter. |
| [terraform-compliance](https://terraform-compliance.com/) | terraform-compliance is a lightweight, security and compliance focused test framework against terraform to enable negative testing capability for your infrastructure-as-code. |
| [tfsec](https://github.com/aquasecurity/tfsec) | tfsec uses static analysis of your terraform code to spot potential misconfigurations. |
| [OpenPubKey](https://github.com/openpubkey/openpubkey) | OpenPubkey is a protocol for leveraging OpenID Providers (OPs) to bind identities to public keys. |

#### Stage 4

| Tool | Description |
| --- | --- |
| Quality Gate | Define a rule/ policy for test result. |

#### Stage 5

| Tool | Description |
| --- | --- |
| [Build image](https://docs.docker.com/reference/cli/docker/buildx/build/) | Docker buildx build. |

#### Stage 6

| Tool | Description |
| --- | --- |
| [Snyk](https://docs.snyk.io/scan-using-snyk/snyk-container/scan-container-images) | Snyk Container helps you find and fix vulnerabilities in container images, based on container registry scans. |
| [Docker Scout](https://docs.docker.com/scout/) | Scan docker image. |
| [Burp Suite](https://portswigger.net/burp) | The class-leading vulnerability scanning, penetration testing, and web app security platform. |
| [Acunetix](https://www.acunetix.com/) | Acunetix is an end-to-end web security scanner. |
| [OWASP ZAP](https://www.zaproxy.org/) | ZAP is a free and open source web application scanner that can help you find vulnerabilities and test your web applications. |
| [Darkmoon](https://github.com/ASCIT31/Dark-Moon) | Open-source (GPLv3) autonomous AI penetration-testing tool: 50 specialist agents, 140+ offensive tools over MCP, and a dedicated LLM-security agent for the OWASP LLM Top 10; runs DAST/pentest in CI on a local (Ollama/llama.cpp) or cloud LLM. |
| [2mny-security-scan](https://github.com/RanaKhan77/2mny-security-scan) | Free GitHub Action for website security checks in CI: TLS/SSL health, security headers, cookie flags, with a full report. |
| [Website Vulnerability Scanner](https://github.com/RanaKhan77/Website-Vulnerability-Scanner) | Open-source website vulnerability scanner: 200 deterministic modules (PHP/Laravel 12), Apache-2.0, one-command Docker install. |
| [VibeLocked LeakCheck Scan](https://github.com/karlaCastro00/vibelocked-leakcheck-action) | Free MIT GitHub Action and web scanner for leaked keys in build output, plus a read only live URL check for exposed Supabase tables, .env, .git, and source map files. |
| [VibeShield](https://shipbastion.com/) | Pre-launch web security scanner and MIT CLI ([vibeshield-cli](https://github.com/zColdWater/vibeshield-cli)) that inspects live JS bundles against 52 secret patterns, performs read-only Supabase PostgREST RLS & public storage bucket checks, audits 10 Mozilla Observatory security headers, and generates copy-paste SQL/CSP fixes. |

#### Stage 7

| Tool | Description |
| --- | --- |
| Quality Gate | Define a rule/ policy for test result. |

#### Stage 8

| Tool | Description |
| --- | --- |
| [OpenPubKey](https://github.com/openpubkey/openpubkey) | OpenPubkey is a protocol for leveraging OpenID Providers (OPs) to bind identities to public keys. |
| [Docker content trust key](https://docs.docker.com/engine/security/trust/#docker-content-trust-keys) | Trust for an image tag is managed through the use of signing keys. |

#### Stage 9

| Tool | Description |
| --- | --- |
| [AWS S3 bucket](https://aws.amazon.com/s3/) | A bucket is a container for objects stored in Amazon S3. |
| [Nexus Repository](https://www.sonatype.com/products/sonatype-nexus-repository) | Sonatype Nexus Repository |

#### Stage 10

| Tool | Description |
| --- | --- |
| [Nessus](https://www.tenable.com/products/nessus) | Nessus Vulnerability Scanner. |
| [Nmap](https://nmap.org/) | Security Scanner, Port Scanner, & Network Exploration Tool. |
| [OpenPubKey](https://github.com/openpubkey/openpubkey) | OpenPubkey is a protocol for leveraging OpenID Providers (OPs) to bind identities to public keys. |
| [Docker content trust key](https://docs.docker.com/engine/security/trust/#docker-content-trust-keys) | Trust for an image tag is managed through the use of signing keys. |
| Compliance check | PIC/DSS, ISO/IEC 27001, NIST 800-53B, ... |
| [OpenSCAP](https://github.com/OpenSCAP/openscap) | OpenSCAP is an open source project that provides tools and policies for managing system security and standards compliance |

#### Stage 11

| Tool | Description |
| --- | --- |
| Quality Gate | N/A |

#### Stage 12

| Tool | Description |
| --- | --- |
| [gemini-self-protector](https://github.com/noobpk/gemini-self-protector) | Gemini - Runtime Application Self Protection Solution (G-SP). |

### Monitoring

#### All stages

| Tool | Description |
| --- | --- |
| [Slack webhook](https://api.slack.com/messaging/webhooks) | Sending messages using incoming webhooks. |
| [Telegram Bot](https://core.telegram.org/bots/api) | Telegram Bot API. |
| [Deject Dojo](https://www.defectdojo.org/) | Application vulnerability management tool. |
| [ELK stack](https://www.elastic.co/elastic-stack) | Elasticsearch, Logstash and Kibana. |
| [PagerDuty](https://www.pagerduty.com/) | Automate, manage, and improve your operations with over 700 integrations and generative AI. |
| [Prometheus](https://prometheus.io/) | Power your metrics and alerting with the leading open-source monitoring solution. |
| [Grafana](https://grafana.com/) | Grafana is the open source analytics & monitoring solution for every database. |

### Key Management

#### All stages that use keys or credentials

| Tool | Description |
| --- | --- |
| [HashiCorp Vault](https://www.hashicorp.com/products/vault) | Manage access to secrets and stop credentials from falling into the wrong hands with identity-based security. |
| [AWS Key Management Service](https://aws.amazon.com/kms/) | Create and control keys used to encrypt or digitally sign your data. |
| [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) | Centrally manage the lifecycle of secrets. |
| [BlackVault](https://github.com/venkat22022202/black-vault) | Proxy gateway for AI API keys. Agents never see the real key. Kill access instantly.. |


## Best Practices

- [OpenSSF Visualizing Secure MLOps (MLSecOps) Whitepaper](https://openssf.org/wp-content/uploads/2025/08/OpenSSF_MLSecOps_Whitepaper.pdf) - Practical layer-by-layer guide for securing AI/ML pipelines with OpenSSF tooling.
- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) - Peer-reviewed risks and mitigations for autonomous AI agents.
- [NIST AI RMF Generative AI Profile (NIST.AI.600-1)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) - Companion profile for governing, mapping, measuring, and managing GenAI risk.
- [CSA Agentic Secure Development Lifecycle (ASDL)](https://labs.cloudsecurityalliance.org/agentic/agentic-secure-development-lifecycle-v1/) - Five-phase SDL for agent systems informed by MAESTRO and OWASP Agentic Top 10.
- [CSA AI Controls Matrix (AICM)](https://cloudsecurityalliance.org/artifacts/ai-controls-matrix) - Control set for AI system security and governance.
- [OWASP LLMSVS](https://owasp.org/www-project-llm-verification-standard/)
- [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [OWASP Machine Learning Security Top Ten](https://owasp.org/www-project-machine-learning-security-top-10/)
- [MITRE ATLAS™ (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/)
- [OWASP DevSecOps](https://devsecops.owasp.org/)
- [OWASP DevSecOps Verification Standard (DSOVS)](https://owasp.org/www-project-devsecops-verification-standard/)
- [OWASP Devsecops Maturity Model](https://owasp.org/www-project-devsecops-maturity-model/)
- [OWASP DevSecOps Guideline](https://owasp.org/www-project-devsecops-guideline/)
- [DevSecOps-Playbook-Securestack](https://github.com/6mile/DevSecOps-Playbook)
- [DevSecOps-Department of Defense (DoD)](https://public.cyber.mil/devsecops/)

## Case Studies

- [How River takes security work from a fix to merge (Shopify)](https://shopify.engineering/river-vulnerability-remediation) - Agentic vulnerability remediation from Slack finding to verified merge.
- [Building an agentic harness that outlasts the model (Shopify)](https://shopify.engineering/building-an-agentic-harness-that-outlasts-the-model) - Multi-agent AppSec scanning with test oracles across a large Rails estate.
- [Defending the Open Source Supply Chain in a New Regulatory Era (Red Hat / OpenSSF)](https://openssf.org/blog/2026/03/02/case-study-defending-the-open-source-supply-chain-in-a-new-regulatory-era/) - Aligning OpenSSF baselines and SLSA with EU CRA compliance.
- [Kusari’s Implementation of OpenSSF Tools and Services](https://openssf.org/blog/2024/10/24/case-study-kusaris-implementation-of-openssf-tools-and-services/) - GUAC, Scorecard, AllStar, SLSA L3, OpenVEX, and S2C2F in production supply-chain defense.
- [Verizon NBI: Sigstore for Provenance and Customer Confidence](https://blog.sigstore.dev/security-by-default-how-verizon-new-business-incubation-uses-sigstore-to-demonstrate-provenance-7beed5714738/) - Automating SLSA provenance signing/verification in enterprise DevOps pipelines.
- [Large scale transformation with DevSecOps (UKHSA)](https://www.capacitas.co.uk/ukhsa-case-study)
- [Enhancing the GuardRails solution](https://maddevs.io/case-studies/guardrails/)

## Community

- [OWASP GenAI Security Project](https://genai.owasp.org/) - Global community for GenAI and agentic application security guidance.
- [OpenSSF AI/ML Security](https://github.com/ossf/ai-ml-security) - OpenSSF working material for securing AI/ML systems and pipelines.
- [OpenSSF Working Groups](https://openssf.org/community/openssf-working-groups/) - SLSA, Sigstore, Scorecard, and related supply-chain security communities.
- [Cloud Security Alliance AI Working Group](https://cloudsecurityalliance.org/research/working-groups/artificial-intelligence) - AI security research, AICM, and agentic guidance.
- [MLSecOps Community](https://community.mlsecops.com/)
- [OWASP Slack](https://owasp.org/slack/invite) - Chapters and project channels, including DevSecOps / DSOVS discussion.
- [DevSecOps on DEV](https://dev.to/t/devsecops)

## Contribution

We welcome contributions from the community to help us expand and improve this repository. If you have suggestions, tools, or resources that you believe should be included, please feel free to submit a pull request or open an issue.

Thank you for visiting our repository. We hope you find it a valuable resource in your journey towards secure and effective machine learning operations.
