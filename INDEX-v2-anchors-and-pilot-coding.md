# AI Governance Design Index v2 — measurement guide and pilot coding

**Status: draft for author review. Not findings.**
The anchors below are proposed. The single coded framework is a first-pass
coding by a research assistant, not by the authors. Nothing here should be
cited, published or entered into the paper until all three authors have checked
each cell against the primary source and either accepted or overridden it.

Revised 21 September 2026 · covers the 12-feature index (3 axes × 4 features,
equally weighted).

---

## 1. Scoring conventions

**Scale.** Every feature is scored 0–100 against three anchors (0 / 50 / 100).
Anchors are reference points, not the only permitted values. Where a case falls
clearly between two anchors, assign an intermediate value in steps of 5 and
record why. Intermediate values are expected to be common — international
frameworks rarely sit exactly on an anchor.

**Aggregation.** Each axis score is the unweighted mean of its four features,
rounded to the nearest whole number.

**Direction.** Within each axis, 100 means more of the property the axis is
named after: more concentrated, more reversible, more efficient.

**Reverse-coded features.** Two features on the reversibility axis are named for
the property that *reduces* reversibility. Their raw scores are recorded as
named, then inverted before entering the axis mean:

| Feature | Raw score means | Enters the mean as |
|---|---|---|
| 2.2 Amendment difficulty | how hard to amend | 100 − raw |
| 2.4 Path dependency | how self-reinforcing | 100 − raw |

State this explicitly in the methods section — an unannounced inversion is the
fastest way to lose a reviewer.

**Audit trail.** Every cell carries a one-line justification and a citation to a
primary source. This is not decoration: Lincoln and Guba establish
*dependability* and *confirmability* through exactly such a trail, and the paper
anchors itself in their criteria. A score without a recorded justification fails
the standard the paper sets for itself.

---

## 2. The four coding rules

Settled 21 September 2026. These bind every framework in the sample, and each
one moves scores, so they belong in the methods section verbatim.

**Rule 1 — Score the instrument, not its reception.**
Code what the text provides on its face. Do not model what happened to it
afterwards: enforcement records, lobbying, political resistance, actual
compliance rates and real-world adoption are all out of scope. They introduce
more variables than the index can carry, and they measure the environment rather
than the design. Where the text creates a power, the power counts even if it has
never been used.

**Rule 2 — Code the framework as adopted.**
The object of coding is the instrument at adoption, not as subsequently amended.
Later amendments are recorded as post-adoption developments and discussed in the
text, but they do not move a score. This keeps the sample internally comparable:
several frameworks in the set have never been amended, and coding one of them
against a 2026 consolidated text while the others stand at adoption would be
comparing different things.

*Consequence, stated plainly:* the index is a snapshot of design choices at the
moment of commitment. It does not claim to describe what any framework looks
like today. Say so on the page and in the paper.

**Rule 3 — Where a row covers several instruments, score the dominant one.**
Pick the instrument that actually carries the operative obligations — the one
that will end up being applied — and code that at face value under rules 1 and 2.
Name it. The others are context, not inputs to the score.

**Rule 4 — Resource and technical concentration measure concentration *among the
parties*, not in the framework's sponsor.** (This one was left to me; reasoning
below, override freely.)

Three reasons. First, your own framing: features 1.3 and 1.4 are grounded in
"middle and great powers who bargain based on their material resources and
know-how" — that is explicitly about parties bargaining with one another inside
a forum, not about the forum's leverage over outsiders. Second, coherence:
1.1 and 1.2 both measure how power is distributed *inside* the arrangement. If
1.3 and 1.4 measured external leverage instead, the axis would average two
different constructs and its mean would carry little information — the same
defect we just removed from the reversibility axis. Third, comparability: every
framework in the sample has parties; not every one has a sponsor with market
power, so the alternative reading would be undefined for several rows.

*What this costs.* The index then has no way to record the Brussels effect —
the EU's capacity to set global rules through market access rather than through
its members. That is a real omission, and it sits alongside the absence of
Lukes' third face as the strongest candidate for what a version 3 should add.
Both are about power exercised over those outside the room.

---

## 3. The measurement guide

### Axis 1 — Power concentration
*100 = authority maximally concentrated. Concentration is measured among the
parties to the framework (Rule 4).*

**1.1 Decision-making concentration** — who gets to vote.

- **0** — All parties hold an equal vote and an effective veto; no weighting, no delegation of decision rights.
- **50** — Weighted or majority voting among states; no single actor can decide alone.
- **100** — A single body takes binding decisions that bind non-consenting parties.

**1.2 Agenda-setting concentration** — who decides what is discussed.

- **0** — Any party, including non-state actors, can place items on the agenda; open co-decision on scope.
- **50** — Agenda set collectively by member states, or by a rotating or shared presidency.
- **100** — A single actor holds a formal or de facto monopoly on initiating proposals.

**1.3 Resource concentration** — material bargaining power among the parties.

- **0** — No material asymmetry converts into influence; formal equality is also practical equality.
- **50** — Larger economies carry informal weight, but the formal rules do not encode it.
- **100** — Material weight is formally encoded — population- or GDP-weighted voting, budget control, or contribution-proportional rights.

**1.4 Technical concentration** — where the know-how that defines compliance sits.

- **0** — Technical content set through open participation by the parties; expertise widely distributed among them.
- **50** — Technical work sits with a designated body, but participation is genuinely open and reviewable.
- **100** — Technical content delegated to a narrow expert body outside the parties' collective control.

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

- **0** — The instrument creates no institutions and requires no investment; ceasing to follow it strands nothing.
- **50** — Sunk compliance investment by regulated parties, but no dedicated institutions established by the instrument.
- **100** — The instrument establishes dedicated institutions, a certification or registration infrastructure, and continuing obligations, so that reversal would strand investment by states, institutions and regulated entities alike.

*Note on this anchor: an earlier draft included third-party adoption of the
framework by non-parties as a condition of the 100 anchor. Rule 1 excludes that
— it is a fact about reception, not design — and leaving it in would have made
the top anchor unreachable by construction. It now belongs with the Brussels
effect among the things a version 3 might measure separately.*

### Axis 3 — Efficiency
*100 = maximally efficient.*

**3.1 Deliberation speed** — how long commitment procedures take, from proposal to entry into force.

- **0** — Over five years, or indefinite.
- **50** — One to three years.
- **100** — Under one year.
- *Interpolate 25 for three to five years.*

**3.2 Binding implementation** — application quality by members.

- **0** — No obligation to apply; adoption entirely discretionary.
- **50** — Obligation exists but requires national transposition, or is subject to broad discretion.
- **100** — Directly applicable and uniformly binding, with obligations that take effect on dates fixed in the text.

**3.3 Optimised coordination** — absence of double effort or contradiction with local legislation.

- **0** — Substantial duplication or contradiction with existing law, unaddressed in the text.
- **50** — Overlaps identified and partly resolved on the face of the instrument, with residual duplication.
- **100** — Cleanly demarcated from adjacent regimes; no duplicated obligations.

**3.4 Compliance verification** — long-term monitoring.

- **0** — No monitoring of any kind.
- **50** — Self-reporting or peer review, without independent verification or consequence.
- **100** — Independent third-party verification, with registries, incident reporting and enforceable penalties.

---

## 4. Pilot coding — EU Artificial Intelligence Act

**Object of coding:** Regulation (EU) 2024/1689 **as adopted**, 13 June 2024,
published in the Official Journal 12 July 2024, in force 1 August 2024.
Per Rule 2, the Digital Omnibus on AI (Regulation (EU) 2026/1744) does **not**
enter the scores; it is recorded in section 6 as a post-adoption development.

### Axis 1 — Power concentration

| # | Feature | Score |
|---|---|---|
| 1.1 | Decision-making concentration | **75** |
| 1.2 | Agenda-setting concentration | **90** |
| 1.3 | Resource concentration | **70** |
| 1.4 | Technical concentration | **80** |

**1.1 — 75.** Adopted under the ordinary legislative procedure: Parliament plus
Council by qualified majority, requiring 55% of member states representing 65%
of the Union population (TEU Art 16(4)). No single actor decides, which argues
for the 50 anchor. Above it because the Regulation binds dissenting member
states and applies directly without their consent, and because Art 97 grants the
Commission power to amend a defined list of provisions and annexes by delegated
act alone. Below 100 because three institutions share the decision on the face
of the Treaties.
*Sources: TEU Art 16(4); AI Act Art 97.*

**1.2 — 90.** The Commission holds a near-monopoly on legislative initiative:
TEU Art 17(2) provides that Union legislative acts may be adopted only on the
basis of a Commission proposal, save where the Treaties provide otherwise. The
AI Act originated as a Commission proposal, COM(2021) 206 final. Art 40 further
delegates the technical agenda — what compliance concretely requires — to
harmonised standards drafted outside the co-legislature. Just short of the 100
anchor only because the Treaties admit narrow exceptions to the initiative
monopoly.
*Sources: TEU Art 17(2); AI Act Art 40.*

**1.3 — 70.** Material weight is formally encoded among the parties: qualified
majority requires 65% of the Union population, so the largest member states
carry proportionally greater weight in every Council vote on the file. That
meets the 100 anchor's substance. Held below it because the double-majority rule
also imposes a member-state count threshold and a blocking-minority floor that
deliberately protects smaller states from population weighting alone — the
encoding is real but bounded.
*Source: TEU Art 16(4).*

**1.4 — 80.** Compliance with the high-risk requirements runs through harmonised
standards drafted by CEN-CENELEC (Art 40), and Art 68 establishes a scientific
panel of independent experts to advise the AI Office. On the face of the text,
the technical content that determines what the obligations actually mean is
delegated to bodies outside the parties' collective control. Held below 100
because standardisation bodies operate through national mirror committees, which
gives member states an indirect route in. *(The empirical literature on
participation asymmetry in JTC 21 supports this reading but, per Rule 1, does not
drive the score.)*
*Sources: AI Act Arts 40, 68; context: Cantero Gamito (2025).*

**Axis 1 mean = (75 + 90 + 70 + 80) ÷ 4 = 315 ÷ 4 = 78.75 → 79**

### Axis 2 — Reversibility

| # | Feature | Raw | Enters mean as |
|---|---|---|---|
| 2.1 | Exit possibility | **0** | 0 |
| 2.2 | Amendment difficulty *(reverse-coded)* | **45** | 100 − 45 = **55** |
| 2.3 | Sunset mechanisms | **50** | 50 |
| 2.4 | Path dependency *(reverse-coded)* | **90** | 100 − 90 = **10** |

**2.1 — 0.** A Regulation, directly applicable in every member state, with no
opt-out and no withdrawal clause. The only exit is withdrawal from the European
Union itself under TEU Art 50. The 0 anchor exactly.
*Sources: Regulation (EU) 2024/1689; TEU Art 50.*

**2.2 — 45 (raw).** Amendment requires the ordinary legislative procedure —
Commission proposal, Parliament, Council by QMV — which is the 50 anchor
precisely. Pulled slightly below it by Art 97, which lets the Commission amend a
defined list of provisions and annexes by delegated act alone, for five-year
periods that extend tacitly unless opposed, subject only to a three-month
objection window. Part of the instrument is therefore amendable by a single
actor, which is the 0 anchor's condition applied to a subset.
*Sources: AI Act Art 97.*
*Changed from the earlier in-force coding of 40, which leaned on the 2026
amendment as demonstrated amendability. Rule 2 excludes that evidence.*

**2.3 — 50.** Art 112 imposes mandatory review: annually for the Annex III
high-risk list and the Art 5 prohibitions, every four years from 2 August 2028
on Annex III extensions, transparency obligations and the governance system, and
from 2 August 2029 on enforcement structures. Nothing expires — no provision
lapses if not renewed. The 50 anchor precisely: mandatory review, no automatic
termination.
*Source: AI Act Art 112.*

**2.4 — 90 (raw).** Meets all three conditions of the top anchor on the face of
the text. The Regulation establishes dedicated institutions (AI Office, AI Board,
advisory forum, scientific panel, notified bodies, national market surveillance
authorities); a registration and certification infrastructure (CE marking,
conformity assessment, the EU database of high-risk systems under Art 71); and
continuing obligations that do not end at market entry (post-market monitoring
under Art 72, incident reporting under Art 73). Reversal would strand investment
by member states, by the institutions created, and by every regulated provider
at once. Held marginally below 100 because Art 43 requires notified-body
involvement for almost none of the Annex III high-risk categories, so the
certification lock-in is thinner than the architecture suggests.
*Sources: AI Act Arts 43, 64–68, 71, 72, 73.*
*Changed from 85 in the in-force coding: the anchor was rewritten (see note
above) and the Art 43 reading cuts the other way.*

**Axis 2 mean = (0 + 55 + 50 + 10) ÷ 4 = 115 ÷ 4 = 28.75 → 29**

### Axis 3 — Efficiency

| # | Feature | Score |
|---|---|---|
| 3.1 | Deliberation speed | **45** |
| 3.2 | Binding implementation | **75** |
| 3.3 | Optimised coordination | **50** |
| 3.4 | Compliance verification | **70** |

**3.1 — 45.** Commission proposal 21 April 2021 → adopted 13 June 2024 →
published 12 July 2024 → in force 1 August 2024. Three years and three months,
which crosses just over the 50 anchor's upper bound into the three-to-five-year
band interpolated at 25. Interpolating within that band, three months past the
boundary out of a two-year span gives roughly 46; rounded to the nearest step
of 5, **45**.
*Sources: COM(2021) 206 final; Regulation (EU) 2024/1689 Art 113.*
*Changed from 40. The earlier figure quietly discounted for the gap between
entry into force and application — Rule 1 puts that in 3.2 instead.*

**3.2 — 75.** A Regulation, so directly applicable with no national
transposition, and Art 113 fixes the application dates in the text itself
(2 February 2025 for prohibitions, 2 August 2025 for general-purpose AI,
governance and penalties, 2 August 2026 generally, 2 August 2027 for Annex I
systems, as adopted). That is close to the 100 anchor. Held below it by two
discretions on the face of the text: Art 99 leaves member states to lay down the
penalty rules, so the consequence of breach varies by jurisdiction, and Art 6(3)
lets a provider self-assess out of high-risk classification where it judges the
system poses no significant risk.
*Sources: AI Act Arts 6(3), 99, 113.*
*Changed from 65, which discounted for the 2026 deferrals. Rule 2 excludes them.*

**3.3 — 50.** The instrument addresses its own overlaps rather than ignoring
them: Art 2 carves out scope exclusions, and Annex I integrates the high-risk
regime into existing Union harmonisation legislation rather than duplicating it.
But substantial residual overlap with the GDPR and the Digital Services Act is
left unresolved on the face of the text, and enforcement is distributed across 27
national market surveillance authorities plus the AI Office and the AI Board.
The 50 anchor precisely: overlaps identified and partly resolved, residual
duplication remaining.
*Sources: AI Act Art 2, Annex I, Ch. VII, Ch. IX.*

**3.4 — 70.** Strong on three of the four elements the 100 anchor requires: an
EU database of registered high-risk systems (Art 71), post-market monitoring
(Art 72), serious-incident reporting (Art 73), and enforceable penalties up to
€35 million or 7% of worldwide annual turnover (Art 99). Weak on the headline
element. Under Art 43, **high-risk systems in points 2 to 8 of Annex III —
employment, education, credit, essential services, law enforcement, migration
and justice — follow conformity assessment based on internal control, which does
not involve a notified body at all.** Only point 1, biometrics, offers a
third-party route, and even there the provider may choose internal control.
Most of the high-risk regime is self-assessed, which is the 50 anchor's
condition, lifted by the registry, incident-reporting and penalty machinery.
*Sources: AI Act Arts 43, 71, 72, 73, 99; Annexes VI–VII.*
*Changed from 85. Reading Art 43 properly is what moved it — the earlier score
credited an independence the text does not provide.*

**Axis 3 mean = (45 + 75 + 50 + 70) ÷ 4 = 240 ÷ 4 = 60**

### Result

| Axis | Score | Previous (in-force coding) |
|---|---|---|
| Power concentration | **79** | 79 |
| Reversibility | **29** | 31 |
| Efficiency | **60** | 59 |

The axis totals barely moved, but that stability is misleading and should not be
read as confirmation that the coding rules made no difference. Five of the twelve
cells changed, several by 10 or 15 points, and the efficiency components very
nearly cancelled out: 40/65/45/85 became 45/75/50/70. Check the cells, not the
totals.

Read plainly: a framework that concentrates authority heavily, commits almost
irreversibly, and is moderately efficient — efficient in its binding force and
its reporting machinery, much less so in its speed and in the independence of
its verification.

---

## 5. What changed, and why

| Feature | In-force coding | As-adopted coding | Reason |
|---|---|---|---|
| 2.2 Amendment difficulty | 40 | **45** | Rule 2 removes the 2026 amendment as evidence |
| 2.4 Path dependency | 85 | **90** | Anchor rewritten to drop an empirical condition Rule 1 excludes |
| 3.1 Deliberation speed | 40 | **45** | Rule 1 stops the score double-counting the application lag |
| 3.2 Binding implementation | 65 | **75** | Rule 2 removes the 2026 deferrals |
| 3.4 Compliance verification | 85 | **70** | Art 43 read properly: most Annex III high-risk systems are self-assessed |

The last of these is not a rule change but a correction. It is the one to check
me on hardest: if you read Art 43 and Annexes VI–VII differently, 3.4 moves.

---

## 6. Post-adoption developments — recorded, not scored

Per Rule 2 these do not enter the coding, but they belong in the paper's
discussion of the EU case.

**Regulation (EU) 2026/1744, the Digital Omnibus on AI** — proposed 19 November
2025, politically agreed 6 May 2026, published in the Official Journal 24 July
2026, in force 27 July 2026. It defers the high-risk application deadlines from
2 August 2026 to 2 December 2027 and from 2 August 2027 to 2 August 2028; adds
prohibitions on AI generating non-consensual intimate imagery and CSAM; grants
the AI Office direct investigative and inspection powers over general-purpose
AI; lightens documentation and notified-body requirements for SMEs; and exempts
AI embedded in already-regulated products where sectoral law imposes equivalent
obligations.

Why it matters to the argument even though it does not move a score: an
instrument amended within two years of entry into force, before its core
obligations ever applied, is empirical evidence bearing on exactly what the
reversibility axis theorises. Under your own rules that evidence sits in the
discussion rather than the score — which is a defensible place for it, and worth
a paragraph saying so.

---

## 7. Still open

- **Lukes' third face is not measured.** The power axis captures who votes and
  who sets the agenda. It does not capture the shaping of what parties come to
  want. In AI governance that dimension is substantial.
- **External leverage is not measured**, following Rule 4. The Brussels effect
  and regulatory templating are invisible to the index as designed.
- **No inter-coder reliability testing.** Nothing has been coded blind or coded
  twice. With twelve features and five frameworks, double-coding even two
  frameworks would materially strengthen the dependability claim.
- **The index describes design at adoption, not governance today.** Say this
  prominently. It is a defensible scope, not a weakness, but only if declared.

---

## 8. Sources

- Regulation (EU) 2024/1689 (AI Act) — https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- AI Act Art 43, conformity assessment — https://artificialintelligenceact.eu/article/43/
- AI Act Art 97, delegated powers — https://artificialintelligenceact.eu/article/97/
- AI Act Art 99, penalties — https://artificialintelligenceact.eu/article/99/
- AI Act Art 112, evaluation and review — https://artificialintelligenceact.eu/article/112/
- AI Act Art 113, entry into force and application — https://artificialintelligenceact.eu/article/113/
- Regulation (EU) 2026/1744 (Digital Omnibus on AI) — https://artificialintelligenceact.eu/ai-act-explorer/digital-omnibus/
- Digital Omnibus, OJ publication — https://www.nicfab.eu/en/posts/digital-omnibus-ai-official-journal/
- M. Cantero Gamito, "From Consensus to Exceptionality" (2025) — https://realaw.blog/2025/11/28/from-consensus-to-exceptionality-what-the-eus-ai-standards-crisis-reveals-about-delegated-technical-governance-by-marta-cantero-gamito/
- S. Lukes, *Power: A Radical View*, 2nd ed. (2005); P. Bachrach and M. Baratz, "Two Faces of Power" (1962) *APSR* 56(4)
- Y. Lincoln and E. Guba, *Naturalistic Inquiry* (1985); on applying the criteria — https://files.eric.ed.gov/fulltext/EJ1320570.pdf
