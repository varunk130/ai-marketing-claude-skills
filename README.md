<div align="center">

# AI Marketing Claude S kills

### AI-Powered Marketing Skills to Aut omate Operations and Drive Measurable ROI

Bu ilt by **[Varun Kulkarni](https://github.com/ varunk130)**

**12 battle-tested skills** wit h scoring algorithms, statistical frameworks,  and actionable outputs.
Built for [Claude Co de](https://docs.anthropic.com/en/docs/claude -code), [GitHub Copilot](https://github.com/f eatures/copilot), [Cursor](https://cursor.sh) , [OpenAI Codex](https://openai.com/codex), a nd any agent that supports markdown skill fil es.

[![Skills](https://img.shields.io/badge/ Skills-12-blue?style=for-the-badge)](#-skill- catalog)
[![License](https://img.shields.io/b adge/License-MIT-green?style=for-the-badge)]( LICENSE)
[![Agent Compatible](https://img.shi elds.io/badge/Agent-Compatible-purple?style=f or-the-badge)](#compatibility)
[![Built with  Claude Code](https://img.shields.io/badge/Bui lt_with-Claude_Code-D97757?logo=anthropic&log oColor=white)](https://claude.ai/code)

---

 *Turn your AI coding agent into a full-stack  marketing operations team.*

</div>

## ⚡ W hat This Is

Each skill is a **self-contained  markdown file** that transforms your AI codi ng agent into a specialized marketing operato r. No API keys required to start — just poi nt your agent at a skill and give it a natura l language command.

> **"Run an A/B test on  our pricing page"** → Growth Engine activat es Bayesian testing framework
>
> **"Score th is lead from Acme Corp"** → Sales Pipeline  runs multi-channel intent scoring
>
> **"Audi t our landing page for conversions"** → Con version runs 12-dimension Conversion Rate Opt imization (CRO) analysis

---

## 📋 Skill  Catalog

| # | Skill | Key Differentiations |  Link |
|:-:|-------|---------------------|:- ---:|
| 1 | **Growth Engine** | Bayesian test ing, multi-armed bandits, Controlled-experime nt Using Pre-Experiment Data (CUPED) variance  reduction, experiment dependency graphs | [� ��](./growth-engine/) |
| 2 | **Sales Pipelin e** | Multi-channel intent scoring, AI enrich ment (Clay/Apollo), predictive logistic regre ssion, champion job tracking | [→](./sales- pipeline/) |
| 3 | **Content** | Readability  scoring, AI detection patterns, content decay  monitoring, auto-refresh scheduling | [→]( ./content-ops/) |
| 4 | **Conversion** | Heat map-aware audits, session replay archetypes,  micro-conversion funnels, Cialdini 6-principl e scoring | [→](./conversion-ops/) |
| 5 |  **Outbound Engine** | Multi-channel sequences  (email+LinkedIn+video), deliverability warmu p planner, timezone-aware scheduling, reply c lassification | [→](./outbound-engine/) |
|  6 | **Search Engine Optimization (SEO)** | G enerative Engine Optimization (GEO) / Answer  Engine Optimization (AEO), topical authority  mapping, Search Engine Results Page (SERP) fe ature win probability, cannibalization detect ion | [→](./seo-ops/) |
| 7 | **Finance** |  Cohort Lifetime Value (LTV) / Customer Acqui sition Cost (CAC), channel unit economics, So ftware as a Service (SaaS) magic number, budg et allocation optimizer | [→](./finance-ops /) |
| 8 | **Revenue Intelligence** | Win/los s pattern recognition (chi-square), auto-gene rated battlecards, pricing sensitivity cliff  analysis, champion tracking | [→](./revenue -intelligence/) |
| 9 | **Podcast** | Guest f it scoring, sponsorship Cost Per Mille (CPM)  calculator, cross-promo network mapping, audi ogram automation | [→](./podcast-ops/) |
|  10 | **Team** | Skills gap matrix, capacity u tilization tracking, 1:1 prep generator, Obje ctives and Key Results (OKR) trajectory scori ng | [→](./team-ops/) |
| 11 | **Sales Play book** | MEDDPICC + BANT hybrid qualification , mutual action plans, Return on Investment ( ROI) calculator with Net Present Value (NPV),  competitive displacement scoring | [→](./s ales-playbook/) |
| 12 | **Creative Ops** | L inkedIn ad creative testing: 3-angle variant  generation, audience-aware sample sizing, seq uential / Bayesian / fixed-horizon test selec tion, post-test diagnostic with angle-level s ignal | [→](./creative-ops/) |

---

## � � How Skills Work

```mermaid
flowchart LR
     A["💬 You say:<br/><i>'Score this lead'</ i>"] --> B["🤖 Agent matches<br/>skill trig ger"]
    B --> C["📖 Skill README<br/>load s framework"]
    C --> D["⚙️ Agent execu tes<br/>scoring algorithm"]
    D --> E["📊  Structured output<br/>delivered"]

    style  A fill:#667eea,stroke:#764ba2,color:#fff
     style B fill:#764ba2,stroke:#667eea,color:#f ff
    style C fill:#667eea,stroke:#764ba2,co lor:#fff
    style D fill:#764ba2,stroke:#667 eea,color:#fff
    style E fill:#667eea,strok e:#764ba2,color:#fff
```

Each skill folder c ontains a `README.md` that defines:

| Compon ent | What It Covers |
|-----------|--------- ------|
| **Capabilities** | What the skill d oes and its key features |
| **Workflow** | S tep-by-step execution sequence |
| **Triggers ** | Natural language phrases that activate i t |
| **Configuration** | Environment variabl es and setup |
| **Methodology** | Scoring fr ameworks with formulas and algorithms |
| **O utputs** | Report formats and deliverables |
 | **Integrations** | Tools and platforms it c onnects with |

---

## 🚀 Quick Start

``` bash
# 1. Clone the repo
git clone https://gi thub.com/varunk130/ai-marketing-claude-skills .git

# 2. Navigate to any skill
cd ai-market ing-claude-skills/growth-engine

# 3. Read th e skill README — that's the entire skill de finition
cat README.md

# 4. Tell your AI age nt to use it (Claude Code, Copilot, Cursor, o r any markdown-skill-aware agent)
#    "Use t he growth-engine skill to design an A/B test  for our homepage"
```

### Using with Claude  Code
```bash
# Add as a skill directory, then  just use natural language:
> "Run a Bayesian  A/B test on our checkout flow"
> "Score and  enrich this lead list"
> "Generate a 90-day c ontent calendar"
```

---

## 🗺️ Skill I nteraction Map

Skills are designed to work i ndependently **or** together. Here's how they  connect:

```mermaid
graph LR
    SP["Sales< br/>Pipeline"] -->|qualified leads| OE["Outbo und<br/>Engine"]
    OE -->|meetings booked|  SB["Sales<br/>Playbook"]
    SB -->|deal inte l| RI["Revenue<br/>Intel"]
    RI -->|battlec ards| SB

    SE["SEO"] -->|traffic| CV["Conv ersion"]
    CV -->|optimized pages| GE["Grow th<br/>Engine"]
    GE -->|winning variants|  CO["Content"]
    CO -->|content| SE

    FO[ "Finance"] -.->|budget| OE
    FO -.->|ROI da ta| GE
    PO["Podcast"] -.->|content atoms|  CO
    TO["Team"] -.->|capacity| FO

    styl e SP fill:#FF6B6B,stroke:#CC5555,color:#fff
     style OE fill:#FF8E72,stroke:#CC7159,color :#fff
    style SB fill:#FF6B6B,stroke:#CC555 5,color:#fff
    style RI fill:#FF8E72,stroke :#CC7159,color:#fff
    style SE fill:#4ECDC4 ,stroke:#3BA39B,color:#fff
    style CV fill: #45B7AA,stroke:#368A80,color:#fff
    style G E fill:#4ECDC4,stroke:#3BA39B,color:#fff
     style CO fill:#45B7AA,stroke:#368A80,color:#f ff
    style FO fill:#7C83FD,stroke:#5F65CC,c olor:#fff
    style PO fill:#9B8FFF,stroke:#7 A70CC,color:#fff
    style TO fill:#7C83FD,st roke:#5F65CC,color:#fff
```

<div align="cent er">

| Track | Skills | Flow |
|:------|:--- ----|:-----|
| 🔴 **Sales & Revenue** | Sal es Pipeline → Outbound → Playbook → Rev enue Intel | Lead to close loop |
| 🟢 **Gr owth & Content** | SEO → Conversion → Gro wth Engine → Content | Traffic to optimizat ion loop |
| 🔵 **Operations** | Finance ·  Podcast · Team | Cross-functional support l ayer |

</div>

---

## 🧰 Compatibility

|  Agent | Status |
|-------|--------|
| Claude  Code | ✅ Full support |
| Cursor | ✅ Ful l support |
| OpenAI Codex | ✅ Full support  |
| Windsurf | ✅ Full support |
| GitHub C opilot | ✅ Full support |
| Any markdown-sk ill agent | ✅ Full support |

---

## 📁  Repository Structure

```
ai-marketing-claude -skills/
├── README.md                     ← You are here
├── growth-engine/R EADME.md      ← Bayesian A/B testing & expe rimentation
├── sales-pipeline/README.m d     ← Lead scoring & deal prediction
├� ��─ content-ops/README.md        ← Conten t quality & decay management
├── conver sion-ops/README.md     ← CRO audits & funne l optimization
├── outbound-engine/READ ME.md    ← Multi-channel outbound sequences 
├── seo-ops/README.md            ← S EO + GEO/AEO optimization
├── finance-o ps/README.md        ← Unit economics & budg et modeling
├── revenue-intelligence/RE ADME.md ← Win/loss analysis & battlecards
� ��── podcast-ops/README.md        ← Pod cast growth & monetization
├── team-ops /README.md           ← Team performance & c apacity
└── sales-playbook/README.md      ← Deal execution & methodology
```

---

 ## 🤝 Contributing

This repo is protected.  To contribute:

1. **Fork** the repository
2 . Create a **feature branch** (`git checkout  -b feature/my-skill`)
3. **Commit** your chan ges
4. Open a **Pull Request** — all PRs re quire review and approval before merging

Dir ect pushes to `main` are not allowed.

---

# # 📄 License

MIT — use these skills howe ver you like.

---

<div align="center">

*St ar ⭐ this repo if these skills save you tim e.*

**Built by [Varun Kulkarni](https://gith ub.com/varunk130)** · *Powered by Claude Cod e Opus 4.7 + GitHub Copilot*

</div>
 

## Python Runtime

In addition to the skill contracts (Markdown), this repo ships a small `python_runtime/` package with shared scoring, statistical, and IO helpers that skill executors can call into.

Requires **Python 3.10+**.

```bash
# Run the example
python examples/run_skill.py

# Run the unit tests
python -m unittest discover -v

# Try the CLI
python -m python_runtime.cli score-lead --features '{"title_match":80,"engagement":70}'
python -m python_runtime.cli ci --successes 120 --trials 1000
python -m python_runtime.cli sample-size --baseline 0.05 --mde 0.01
```

**Zero runtime dependencies** — pure Python standard library. Tests use the built-in `unittest` module.