# AI Governance Design Index v2 — measurement guide and pilot coding

**Status: draft for author review. Not findings.**
The anchors below are proposed. The single coded framework is a first-pass coding
by a research assistant, not by the authors. Nothing here should be cited,
published or entered into the paper until all three authors have checked each
cell against the primary source and either accepted or overridden it.

Prepared 7 September 2026 · covers the 12-feature index (3 axes × 4 features,
equally weighted).

---

## 1. Scoring conventions

**Scale.** Every feature is scored 0–100 against three anchors (0 / 50 / 100).
Anchors are reference points, not the only permitted values. Where a case falls
clearly between two anchors, assign an intermediate value in steps of 5 and
record why in the coding note. Intermediate values are expected to be common —
international frameworks rarely sit exactly on an anchor.

**Aggregation.** Each axis score is the unweighted mean of its four features,
rounded to the nearest whole number.

**Direction.** Within each axis, 100 means more of the property the axis is
named after: more concentrated, more reversible, more efficient.

**Reverse-coded features.** Two features in the Reversibility axis are named for
the property that *reduces* reversibility. Their raw scores are recorded as
named, then inverted before entering the axis mean:

| Feature | Raw score means | Enters the mean as |
|---|---|---|
| 2.2 Amendment difficulty | how hard to amend | 100 − raw |
| 2.4 Path dependency | how self-reinforcing | 100 − raw |

This keeps your feature names and the paper's argument intact. State it
explicitly in the methods section — an unannounced inversion is the fastest way
to lose a reviewer.

**Audit trail.** Every cell carries a one-line justification and a citation to a
primary source. This is not decoration: Lincoln and Guba establish
*dependability* and *confirmability* through exactly such a trail, and the paper
anchors itself in their criteria. A score without a recorded justification fails
the standard the paper sets for itself.

---

## 2. The measurement guide

### Axis 1 — Power concentration
*100 = authority maximally concentrated.*

**1.1 Decision-making concentration** — who gets to vote.

- **0** — All parties hold an equal vote and an effective veto; no weighting, no delegation of decision rights.
- **50** — Weighted or majority voting among states; no single actor can decide alone.
- **100** — A single body takes binding decisions that bind non-consenting parties.

**1.2 Agenda-setting concentration** — who decides what is discussed.

- **0** — Any party, including non-state actors, can place items on the agenda; open co-decision on scope.
- **50** — Agenda set collectively by member states, or by a rotating or shared presidency.
- **100** — A single actor holds a formal or de facto monopoly on initiating proposals.

**1.3 Resource concentration** — material bargaining power.

- **0** — No material asymmetry converts into influence; formal equality is also practical equality.
- **50** — Larger economies carry informal weight, but the formal rules do not encode it.
- **100** — Material weight is formally encoded (population- or GDP-weighted voting, budget control), or the framework's leverage rests on a market a few parties control.

**1.4 Technical concentration** — know-how.

- **0** — Technical content set through open, well-resourced participation; expertise widely distributed.
- **50** — Technical work sits with a designated body, but participation is genuinely open and reviewable.
- **100** — Technical content delegated to a narrow expert body whose participation is costly, with documented asymmetry between large firms or dominant states and everyone else.

### Axis 2 — Reversibility
*100 = maximally reversible.*

**2.1 Exit possibility** — can a member state leave.

- **0** — No exit short of leaving a wider union; no withdrawal provision.
- **50** — Withdrawal provided for, with a notice period and moderate consequences.
- **100** — Participation voluntary throughout; a party may cease complying at any time with no consequence.

**2.2 Amendment difficulty** — how hard to change the core rules. **[reverse-coded]**

- **0** — Amendable by a single actor or simple majority; amendment is routine.
- **50** — Requires a defined multi-actor legislative procedure short of unanimity.
- **100** — Requires unanimity or ratification by every party.

**2.3 Sunset mechanisms** — frequent review or expiry of commitments.

- **0** — No review or expiry provision; commitments persist indefinitely.
- **50** — Mandatory periodic review with reporting, but no expiry — review alone cannot end the commitment.
- **100** — Commitments expire automatically unless actively renewed.

**2.4 Path dependency** — is the framework self-reinforcing. **[reverse-coded]**

- **0** — No lock-in; abandoning the framework strands no investment for parties or third parties.
- **50** — Some sunk compliance investment, but no dedicated institutions and no external adoption.
- **100** — Self-reinforcing: dedicated institutions, sunk compliance cost, certification or market infrastructure, and third-party adoption that raises the cost of reversal.

### Axis 3 — Efficiency
*100 = maximally efficient.*

**3.1 Deliberation speed** — how long commitment procedures take.

- **0** — Over five years from proposal to entry into force, or indefinite.
- **50** — One to three years.
- **100** — Under one year.
- *Interpolate 25 for three to five years, 75 for roughly one year.*

**3.2 Binding implementation** — application quality by members.

- **0** — No obligation to apply; adoption entirely discretionary.
- **50** — Obligation exists but requires national transposition, or is subject to broad discretion or deferral.
- **100** — Directly applicable and uniformly in force, with obligations that bite on their stated date.

**3.3 Optimised coordination** — absence of double effort or contradiction with local legislation.

- **0** — Substantial duplication or contradiction with existing law, unresolved.
- **50** — Overlaps identified and partly resolved, with residual duplication.
- **100** — Cleanly demarcated from adjacent regimes; no duplicated obligations.

**3.4 Compliance verification** — long-term monitoring.

- **0** — No monitoring of any kind.
- **50** — Self-reporting or peer review, without independent verification or consequence.
- **100** — Independent verification, with registries, incident reporting and enforceable penalties.

---

## 3. Pilot coding — EU Artificial Intelligence Act

Coded against Regulation (EU) 2024/1689 **as amended by Regulation (EU) 2026/1744**
(the Digital Omnibus on AI), published in the Official Journal 24 July 2026 and
in force 27 July 2026. See the note in section 5 — this amendment is the single
most consequential thing found during the coding.

### Axis 1 — Power concentration

| # | Feature | Score |
|---|---|---|
| 1.1 | Decision-making concentration | **75** |
| 1.2 | Agenda-setting concentration | **90** |
| 1.3 | Resource concentration | **70** |
| 1.4 | Technical concentration | **80** |

**1.1 — 75.** Adopted under the ordinary legislative procedure: Parliament plus
Council by qualified majority, requiring 55% of member states representing 65%
of the Union population (TEU Art 16(4)). No single actor decides — which argues
for the 50 anchor. But the Regulation binds dissenting member states and is
directly applicable without their consent, and the Commission separately holds
power to amend listed provisions and annexes by delegated act alone (Art 97),
subject only to an EP or Council objection. Above 50 for binding non-consenters
and delegated amendment power; below 100 because three institutions share the
decision, as the 2026 omnibus negotiation demonstrated.
*Sources: TEU Art 16(4); AI Act Art 97.*

**1.2 — 90.** The Commission holds a near-monopoly on legislative initiative
(TEU Art 17(2): Union legislative acts may be adopted only on the basis of a
Commission proposal, save where the Treaties provide otherwise). Both the AI Act
and the 2026 omnibus that amended it originated as Commission proposals. Below
the legislative level, agenda-setting over technical content sits with
CEN-CENELEC drafting groups, where acceleration measures concentrated drafting
authority in small expert circles and, per Cantero Gamito, raised "the risk of
agenda-setting capture by large firms or dominant national bodies." Just short of
the 100 anchor only because the Treaties admit narrow exceptions.
*Sources: TEU Art 17(2); Cantero Gamito (2025).*

**1.3 — 70.** Material weight is formally encoded: QMV requires 65% of the Union
population, so the largest member states carry proportionally greater weight. The
Act's extraterritorial reach rests on access to the single market — leverage
concentrated in the Union rather than distributed among parties. Offsetting this,
Art 99 caps penalties lower for SMEs and start-ups, and Regulation (EU) 2026/1744
lightened documentation and notified-body requirements for smaller enterprises,
reducing asymmetry in obligations if not in decision rights. Above 50 because the
weighting is formal, not merely informal; below 100 because no single party
controls the budget or holds a veto.
*Sources: TEU Art 16(4); AI Act Art 99; Regulation (EU) 2026/1744.*

**1.4 — 80.** Compliance with high-risk requirements runs through harmonised
standards drafted by CEN-CENELEC JTC 21 (Art 40). Cantero Gamito documents that
CEN-CENELEC's acceleration permitted publication after a positive Enquiry vote,
skipping the Formal Vote, and empowered small expert drafting groups to finalise
delayed texts — while SMEs, civil society and consumer groups "lack the permanent
Brussels presence and technical staff to engage effectively," a shift she
characterises as "a closed structure of privilege." Regulation (EU) 2026/1744
further concentrates technical supervision of general-purpose AI in the AI
Office. Held below 100 because JTC 21 membership is nominally open through
national mirror bodies.
*Sources: AI Act Art 40; Cantero Gamito (2025); Regulation (EU) 2026/1744.*

**Axis 1 mean = (75 + 90 + 70 + 80) ÷ 4 = 315 ÷ 4 = 78.75 → 79**

### Axis 2 — Reversibility

| # | Feature | Raw | Enters mean as |
|---|---|---|---|
| 2.1 | Exit possibility | **0** | 0 |
| 2.2 | Amendment difficulty *(reverse-coded)* | **40** | 100 − 40 = **60** |
| 2.3 | Sunset mechanisms | **50** | 50 |
| 2.4 | Path dependency *(reverse-coded)* | **85** | 100 − 85 = **15** |

**2.1 — 0.** A Regulation, directly applicable in every member state, with no
opt-out and no withdrawal clause. The only exit is withdrawal from the European
Union itself under TEU Art 50. This is the 0 anchor exactly.
*Source: Regulation (EU) 2024/1689; TEU Art 50.*

**2.2 — 40 (raw).** Amendment requires the ordinary legislative procedure —
Commission proposal, Parliament, Council by QMV — which is the 50 anchor. Two
things push below it. Art 97 lets the Commission amend a defined list of
provisions and annexes by delegated act alone, for five-year periods that extend
tacitly unless opposed, subject only to a three-month objection window. More
decisively, the Act was substantively amended within two years of entry into
force: Regulation (EU) 2026/1744 was proposed 19 November 2025, politically
agreed 6 May 2026, and in force 27 July 2026 — deferring high-risk deadlines,
adding prohibitions, expanding AI Office powers and lightening SME obligations.
This is demonstrated amendability, not theoretical.
*Sources: AI Act Art 97; Regulation (EU) 2026/1744.*

**2.3 — 50.** Art 112 imposes mandatory review: annually for the Annex III
high-risk list and the Art 5 prohibitions, every four years from 2 August 2028 on
Annex III extensions, transparency obligations and the governance system, and
from 2 August 2029 on enforcement structures and whether a Union agency is
needed. But nothing expires — no provision lapses if not renewed. This is the 50
anchor precisely: mandatory review, no automatic termination.
*Source: AI Act Art 112.*

**2.4 — 85 (raw).** Strongly self-reinforcing. The Act creates dedicated
institutions (AI Office, AI Board, Scientific Panel, notified bodies, national
market surveillance authorities), a conformity-assessment and CE-marking
infrastructure, an EU database of registered high-risk systems, and substantial
sunk compliance investment across the market. Regulation (EU) 2026/1744 granted
the AI Office investigative and inspection powers described as resembling
competition-law enforcement, deepening the institutional stake. Third-country
adoption of its risk-tiering raises the reversal cost further. Held below 100
because the omnibus showed the timetable is negotiable — but note that it
deferred deadlines without repealing a single high-risk obligation. The framework
bent; it did not unwind.
*Sources: AI Act Arts 64–68, 71; Regulation (EU) 2026/1744.*

**Axis 2 mean = (0 + 60 + 50 + 15) ÷ 4 = 125 ÷ 4 = 31.25 → 31**

### Axis 3 — Efficiency

| # | Feature | Score |
|---|---|---|
| 3.1 | Deliberation speed | **40** |
| 3.2 | Binding implementation | **65** |
| 3.3 | Optimised coordination | **45** |
| 3.4 | Compliance verification | **85** |

**3.1 — 40.** Commission proposal 21 April 2021 → adopted 13 June 2024 →
published in the Official Journal 12 July 2024 → in force 1 August 2024. Three
years and three months from proposal to entry into force, between the 50 anchor
(one to three years) and the interpolated 25 (three to five years).
**This score depends on a coding rule you have not yet fixed** — see section 4.
Measured instead to the point where core high-risk obligations actually bite
(now 2 December 2027 and 2 August 2028), the elapsed period exceeds six years
and the score would fall to roughly 10.
*Sources: COM(2021) 206 final; Regulation (EU) 2024/1689; Regulation (EU) 2026/1744.*

**3.2 — 65.** A Regulation, so directly applicable with no national transposition
— the first half of the 100 anchor is met. But the obligations do not bite on
their stated dates: Regulation (EU) 2026/1744 deferred standalone Annex III
high-risk requirements from 2 August 2026 to 2 December 2027, and AI embedded in
regulated products from 2 August 2027 to 2 August 2028. Penalties are real —
Art 99 provides up to €35 million or 7% of worldwide annual turnover for
prohibited practices — but member states lay down and apply them, introducing
variation. Directly applicable, unevenly timed.
*Sources: AI Act Arts 99, 113; Regulation (EU) 2026/1744.*

**3.3 — 45.** The Act overlaps materially with the GDPR, the Digital Services
Act, sectoral product-safety law and the Machinery Regulation. That duplication
was real enough that the legislator addressed it retrospectively: Regulation (EU)
2026/1744 exempts AI embedded in EU-regulated products from AI Act requirements
where sectoral legislation already imposes equivalent obligations, and inserted
Art 4a to clarify the legal basis for processing sensitive personal data for bias
detection — a direct GDPR interface fix. Enforcement remains split across 27
national market surveillance authorities plus the AI Office and the AI Board.
Just below the 50 anchor: overlaps identified and partly resolved, but the fix
arrived two years late and enforcement stays distributed.
*Sources: Regulation (EU) 2026/1744; AI Act Ch. VII.*

**3.4 — 85.** The strongest verification architecture likely to appear in this
sample. Third-party conformity assessment through notified bodies; an EU database
of registered high-risk systems (Art 71); post-market monitoring (Art 72);
serious-incident reporting (Art 73); national market surveillance authorities;
and enforceable penalties up to €35 million or 7% of worldwide turnover (Art 99),
with member states reporting fines annually to the Commission. Regulation (EU)
2026/1744 added direct investigative and inspection powers for the AI Office over
general-purpose AI. Held below 100 because the harmonised standards that
operationalise conformity assessment are not yet delivered — the architecture is
complete but not yet fully operable.
*Sources: AI Act Arts 71–73, 99; Regulation (EU) 2026/1744; Cantero Gamito (2025).*

**Axis 3 mean = (40 + 65 + 45 + 85) ÷ 4 = 235 ÷ 4 = 58.75 → 59**

### Result

| Axis | Score |
|---|---|
| Power concentration | **79** |
| Reversibility | **31** |
| Efficiency | **59** |

Read plainly: highly concentrated authority, very hard to reverse, moderately
efficient — with the efficiency score resting almost entirely on its verification
architecture rather than on speed or clean coordination.

---

## 4. Coding rules you still need to fix

These came up while coding and cannot be resolved by a research assistant. Each
will change scores across all five frameworks, so settle them before coding the
remaining four.

1. **Does "deliberation speed" measure proposal → entry into force, or proposal →
   obligations actually applying?** For the AI Act this is the difference between
   40 and about 10. For soft-law instruments with no application date it may be
   undefined. Recommend: proposal → entry into force, with the application lag
   captured under 3.2 instead, so the two are not double-counted.

2. **Do you code frameworks as they stand today, or as originally adopted?** The
   AI Act of 2024 and the AI Act of September 2026 score differently on at least
   four features. Recommend: code as in force on a stated cut-off date, and put
   that date on the page.

3. **Where a row bundles instruments** — the UNESCO Recommendation together with
   the Global Digital Compact — is the score the regime as a whole, the dominant
   instrument, or a mean of the two? Recommend: the regime as it operates, with a
   note naming which instrument drove each score.

4. **Is 1.3 resource concentration about concentration *among the parties*, or
   concentration *in the framework's sponsor*?** For the EU both readings point
   the same way; for the OECD and ASEAN they will diverge sharply.

---

## 5. Findings that affect the paper, not just the site

**The EU AI Act has been amended.** Regulation (EU) 2026/1744 — the Digital
Omnibus on AI — was published on 24 July 2026 and entered into force on
27 July 2026. It defers the high-risk application deadlines by over a year, adds
new prohibitions, expands the AI Office's enforcement powers, lightens SME
obligations, and carves out AI embedded in already-regulated products. Your
framework list describes the case as "the EU Artificial Intelligence Act (2024)."
If the paper codes the 2024 text, it is coding an instrument that no longer
exists in that form — and the amendment bears directly on three of your twelve
features. This is the most citable evidence in the sample on both amendment
difficulty and path dependency, so it strengthens the paper rather than
undermining it, but only if it is addressed rather than missed.

**Reversibility still mixes directions.** Handled here by reverse-coding 2.2 and
2.4, per your decision. State the inversion in the methods section explicitly.

**Lukes' third face is absent.** The index draws decision-making and
agenda-setting from Lukes, but agenda-setting as a "second face" originates with
Bachrach and Baratz (1962); Lukes' distinctive contribution is the *third*
dimension — shaping what actors come to want. In AI governance that dimension is
arguably where the action is: the Brussels effect, norm diffusion, and
third-country adoption of EU risk-tiering are all third-face phenomena, and the
index currently has nowhere to record them. Worth a paragraph either way — a
reviewer who knows Lukes will ask.

**"Deliberation speed" as a virtue cuts against your own framing.** The paper
argues that efficiency pressure leads treaties to concentrate power "instead of
distributing deliberation." Scoring faster deliberation as more efficient encodes
as a good the thing the paper elsewhere treats as a cost. Not wrong, but it needs
a sentence acknowledging the tension.

---

## 6. Sources

- Regulation (EU) 2024/1689 (AI Act) — https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- Regulation (EU) 2026/1744 (Digital Omnibus on AI) — https://artificialintelligenceact.eu/ai-act-explorer/digital-omnibus/
- AI Act Art 97, delegated powers — https://artificialintelligenceact.eu/article/97/
- AI Act Art 99, penalties — https://artificialintelligenceact.eu/article/99/
- AI Act Art 112, evaluation and review — https://artificialintelligenceact.eu/article/112/
- AI Act implementation timeline — https://artificialintelligenceact.eu/implementation-timeline/
- Digital Omnibus, scope of changes — https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/
- Digital Omnibus, OJ publication — https://www.nicfab.eu/en/posts/digital-omnibus-ai-official-journal/
- M. Cantero Gamito, "From Consensus to Exceptionality: What the EU's AI Standards Crisis Reveals About Delegated Technical Governance" (2025) — https://realaw.blog/2025/11/28/from-consensus-to-exceptionality-what-the-eus-ai-standards-crisis-reveals-about-delegated-technical-governance-by-marta-cantero-gamito/
- CEN-CENELEC, artificial intelligence work programme — https://www.cencenelec.eu/areas-of-work/cen-cenelec-topics/artificial-intelligence/
- S. Lukes, *Power: A Radical View*, 2nd ed. (2005); P. Bachrach and M. Baratz, "Two Faces of Power" (1962) *APSR* 56(4)
- Y. Lincoln and E. Guba, *Naturalistic Inquiry* (1985); on applying the criteria — https://files.eric.ed.gov/fulltext/EJ1320570.pdf
