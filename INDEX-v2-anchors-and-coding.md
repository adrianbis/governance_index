# AI Governance Design Index v2 — measurement guide and full coding

**Status: draft for author review. Not findings.**
The anchors below are proposed. All five codings are a first-pass by a
research assistant, not by the authors. Nothing here should be
cited, published or entered into the paper until all three authors have checked
each cell against the primary source and either accepted or overridden it.

Revised 21 September 2026 · all five frameworks coded · covers the 12-feature index (3 axes × 4 features,
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

## 4. Coding — all five frameworks

All five are coded under the four rules in section 2. Every cell has a
justification and a primary source. **None of it has been checked by all three
authors, nothing was coded blind, and no inter-coder reliability testing has
been done — so none of it is yet a finding.**

| Framework | Power concentration | Reversibility | Efficiency |
|---|---|---|---|
| OECD AI Principles (2019) | 38 | 65 | 53 |
| EU AI Act (2024) | **79** | **29** | **60** |
| UNESCO Recommendation (2021) | 49 | 70 | 40 |
| AU Continental AI Strategy (2024) | 41 | **76** | 41 |
| ASEAN Guide (2024) | **24** | 70 | 39 |

Bold marks the extreme value on each axis.

---

### 4.1 EU Artificial Intelligence Act

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

**EU result: power concentration 79 · reversibility 29 · efficiency 60**

Against the earlier in-force coding of 79 / 31 / 59.

The axis totals barely moved, but that stability is misleading and should not be
read as confirmation that the coding rules made no difference. Five of the twelve
cells changed, several by 10 or 15 points, and the efficiency components very
nearly cancelled out: 40/65/45/85 became 45/75/50/70. Check the cells, not the
totals.

Read plainly: a framework that concentrates authority heavily, commits almost
irreversibly, and is moderately efficient — efficient in its binding force and
its reporting machinery, much less so in its speed and in the independence of
its verification.

| Feature | In-force coding | As-adopted coding | Reason |
|---|---|---|---|
| 2.2 Amendment difficulty | 40 | **45** | Rule 2 removes the 2026 amendment as evidence |
| 2.4 Path dependency | 85 | **90** | Anchor rewritten to drop an empirical condition Rule 1 excludes |
| 3.1 Deliberation speed | 40 | **45** | Rule 1 stops the score double-counting the application lag |
| 3.2 Binding implementation | 65 | **75** | Rule 2 removes the 2026 deferrals |
| 3.4 Compliance verification | 85 | **70** | Art 43 read properly: most Annex III high-risk systems are self-assessed |

---

### 4.2 OECD AI Principles

**Object of coding:** Recommendation of the Council on Artificial Intelligence,
OECD/LEGAL/0449, **as adopted 22 May 2019**. Per Rule 2 the May 2024 revision is
recorded but not scored; it revised the definition of an AI system rather than
the instrument's design, and would not move any of the twelve features.

*Note a tension for you to resolve: your framework list names this case "OECD AI
Principles (2019, updated 2024)", which points at the revised text, while Rule 2
points at the 2019 adoption. I have applied the rule, for consistency with the
EU treatment. If you prefer the list, say so — the scores barely move, but the
method note has to match whichever you pick.*

| # | Feature | Raw | Enters mean as |
|---|---|---|---|
| 1.1 | Decision-making concentration | **15** | 15 |
| 1.2 | Agenda-setting concentration | **45** | 45 |
| 1.3 | Resource concentration | **35** | 35 |
| 1.4 | Technical concentration | **55** | 55 |
| 2.1 | Exit possibility | **100** | 100 |
| 2.2 | Amendment difficulty *(rev.)* | **60** | **40** |
| 2.3 | Sunset mechanisms | **50** | 50 |
| 2.4 | Path dependency *(rev.)* | **30** | **70** |
| 3.1 | Deliberation speed | **80** | 80 |
| 3.2 | Binding implementation | **10** | 10 |
| 3.3 | Optimised coordination | **80** | 80 |
| 3.4 | Compliance verification | **40** | 40 |

**1.1 — 15.** The Council takes decisions and makes recommendations "by mutual
agreement of all the Members" (OECD Convention Art 6(1)), and abstention does not
invalidate the act but excludes the abstaining member from it (Art 6(2)). Every
party therefore holds an effective opt-out and nothing binds a dissenter. Near
the 0 anchor; above it only because a standing Council exists and adherence is a
recorded formal act rather than ad hoc alignment. *Sources: OECD Convention Arts 5, 6.*

**1.2 — 45.** The Digital Policy Committee (then CDEP) proposed the instrument
with input from the AI Group of experts, and the Council of all members adopts —
state-collective agenda-setting, the 50 anchor. Marginally below it because no
actor holds an initiative monopoly and the Secretariat's drafting role, while
real, is not a formal gatekeeping power. *Sources: OECD Convention Art 6; C/MIN(2024)17.*

**1.3 — 35.** No weighted voting: mutual agreement gives each member one voice,
and the 47 adherents include eight non-members whose participation is unconnected
to any financial contribution. OECD budget contributions are scaled to member
economies, which confers informal influence over the Organisation, but the rules
for adopting or revising this Recommendation encode no material weighting at all.
Below the 50 anchor. *Sources: OECD Convention Art 6; oecd.ai (47 adherents, 8 non-members).*

**1.4 — 55.** Technical elaboration sits with a designated body — the Digital
Policy Committee working with the AI Group of experts, supported by the
Secretariat and the OECD.AI Policy Observatory. Participation is open to member
delegations and the outputs are public, which is the 50 anchor. Just above it
because the expert group is convened rather than elected and the Secretariat
drafts. *Sources: C/MIN(2024)17; oecd.ai.*

**Axis 1 = (15 + 45 + 35 + 55) ÷ 4 = 150 ÷ 4 = 37.5 → 38**

**2.1 — 100.** A Recommendation is not legally binding (Convention Art 5(b)). An
adherent may stop following it at any time with no procedure and no consequence,
and a member may abstain at adoption and fall outside it entirely. The 100 anchor
exactly. *Sources: OECD Convention Arts 5(b), 6(2).*

**2.2 — 60 (raw) → 40.** Revision requires a Council decision by mutual agreement
of all members, which is formally the 100 anchor's unanimity condition. Pulled
well below it by Art 6(2): an unwilling member can abstain rather than block, so
no single objector can prevent revision, and no ratification is required of
anyone. *Sources: OECD Convention Art 6; C/MIN(2024)17.*

**2.3 — 50.** On adoption the Council instructed the Committee "to monitor, in
consultation with other relevant Committees, the implementation of this
Recommendation and report thereon to the Council no later than five years
following its adoption" — a mandatory review, delivered in 2024. Nothing expires
if the report is not made or not acted on. The 50 anchor precisely.
*Source: C/MIN(2024)17, quoting the 2019 instruction.*

**2.4 — 30 (raw) → 70.** The Recommendation establishes no institution of its
own, no certification or registration infrastructure, and no continuing
obligation on adherents; it gives an existing committee a monitoring mandate.
Above the 0 anchor because adherents that have aligned national policy have sunk
real effort, but well below 50 because that effort is policy alignment rather
than compliance machinery. *Sources: OECD Convention Art 5(b); C/MIN(2024)17.*

**Axis 2 = (100 + 40 + 50 + 70) ÷ 4 = 260 ÷ 4 = 65**

**3.1 — 80.** The AI Group of experts convened in 2018 and the Recommendation was
adopted on 22 May 2019 — roughly a year from the start of drafting, and for a
Recommendation adoption *is* entry into force. Near the 100 anchor (under one
year), held below it because the drafting start date is approximate rather than
a dated proposal. *Sources: C/MIN(2024)17; oecd.ai.*
*Flag: this is the weakest-sourced cell in the OECD column. If you can date the
CDEP mandate precisely, the score should be pinned to it.*

**3.2 — 10.** Not binding. Art 5(b) empowers the Organisation to make
recommendations; adherents are under no obligation to apply, and an abstaining
member is not covered at all. Just above the 0 anchor because adherence is a
formal act carrying a reporting expectation. *Sources: OECD Convention Arts 5(b), 6(2).*

**3.3 — 80.** By design the Principles impose no obligations, so they duplicate
none, and they are framed as a common reference to be given effect through
national law — they have been adopted by reference into other instruments rather
than competing with them. Short of 100 because the same generality that avoids
duplication also leaves the boundary with national regimes undefined rather than
demarcated. *Sources: OECD/LEGAL/0449; oecd.ai.*

**3.4 — 40.** Monitoring is peer-based: the Committee monitors implementation and
reports to Council, and the OECD.AI Policy Observatory records national policies.
No independent verification, no registry of regulated entities, no consequence
for non-implementation. Just below the 50 anchor because the review is aggregate
and periodic rather than country-by-country. *Sources: C/MIN(2024)17; oecd.ai.*

**Axis 3 = (80 + 10 + 80 + 40) ÷ 4 = 210 ÷ 4 = 52.5 → 53**

> **Rounding note.** 52.5 is the one score in the whole matrix that lands on an
> exact half. The webpage rounds half-up (JavaScript `Math.round`) and gives 53;
> Python's built-in `round` uses half-to-even and gives 52. The figure script has
> been changed to round half-up so the figures and the table cannot disagree.
> If you recompute this in Excel or R, check which convention you get.

---

### 4.3 UNESCO Recommendation on the Ethics of AI

**Object of coding:** the Recommendation **as adopted 23 November 2021** by the
41st General Conference. Per Rule 3 this is the scored instrument for the row;
the Global Digital Compact is context.

| # | Feature | Raw | Enters mean as |
|---|---|---|---|
| 1.1 | Decision-making concentration | **30** | 30 |
| 1.2 | Agenda-setting concentration | **60** | 60 |
| 1.3 | Resource concentration | **35** | 35 |
| 1.4 | Technical concentration | **70** | 70 |
| 2.1 | Exit possibility | **95** | 95 |
| 2.2 | Amendment difficulty *(rev.)* | **30** | **70** |
| 2.3 | Sunset mechanisms | **55** | 55 |
| 2.4 | Path dependency *(rev.)* | **40** | **60** |
| 3.1 | Deliberation speed | **50** | 50 |
| 3.2 | Binding implementation | **15** | 15 |
| 3.3 | Optimised coordination | **45** | 45 |
| 3.4 | Compliance verification | **50** | 50 |

**1.1 — 30.** Adopted by the General Conference, where each member state has one
vote and decisions are by majority — no weighting and no veto. That falls between
the 0 anchor (equal vote plus effective veto) and the 50 anchor (weighted or
majority voting). Majority voting without weighting is the milder form of the 50
anchor, so below its midpoint. *Source: UNESCO Constitution Art IV.*

**1.2 — 60.** The 40th General Conference mandated the instrument in November
2019, but the text was drafted by a 24-member Ad Hoc Expert Group convened by the
Director-General, and the Director-General and Executive Board control what
reaches the General Conference. Above the 50 anchor: the agenda and the draft
originated with a body the Secretariat constituted rather than with the parties
collectively. *Source: UNESCO (AHEG of 24 convened by the Director-General, first met April 2020).*

**1.3 — 35.** Assessed contributions follow the UN scale and are economy-weighted,
which confers real informal influence over UNESCO. But General Conference voting
is one state, one vote, and the rules for adopting or revising a Recommendation
encode no material weighting. Below the 50 anchor, and level with the OECD for
the same reason. *Source: UNESCO Constitution Art IV.*

**1.4 — 70.** The substance was produced by a 24-member expert group appointed by
the Director-General rather than negotiated among the parties from the outset,
and the instruments that determine what the Recommendation means in practice —
the Readiness Assessment Methodology (launched November 2022) and the Ethical
Impact Assessment (June 2023) — were developed by UNESCO *after* adoption,
outside member-state control. Near the 100 anchor, held below because member
states did negotiate the final text. *Sources: UNESCO AHEG; RAM; EIA.*

**Axis 1 = (30 + 60 + 35 + 70) ÷ 4 = 195 ÷ 4 = 48.75 → 49**

**2.1 — 95.** Non-binding, with no withdrawal mechanism because none is needed —
a member state may simply not implement. Marginally below 100 because the UNESCO
Constitution obliges member states to report on the action they take on
Recommendations, so ceasing to comply is not procedurally invisible.
*Sources: UNESCO Constitution Art VIII; non-binding status.*

**2.2 — 30 (raw) → 70.** Revision requires the General Conference to adopt a
revised text — a defined procedure involving the Secretariat, the Executive Board
and member states, but by majority vote, with no ratification and no veto. Below
the 50 anchor, which contemplates qualified majority or bicameral approval.
*Source: UNESCO Constitution Art IV.*

**2.3 — 55.** Member states must report on implementation **every four years**,
with the first reports due 23 November 2025 — a recurring mandatory cycle,
firmer than the OECD's single five-year report. No expiry provision. Slightly
above the 50 anchor for the recurrence. *Sources: UNESCO Recommendation, monitoring and evaluation provisions; UNESCO Constitution Art VIII.*

**2.4 — 40 (raw) → 60.** Creates no institution with authority over parties and
no certification infrastructure, but does impose a continuing four-yearly
reporting obligation, and states that have run the Readiness Assessment
Methodology have sunk institutional effort into it. Below the 50 anchor because
the machinery is reporting rather than compliance. *Sources: UNESCO Recommendation monitoring provisions; RAM.*

**Axis 2 = (95 + 70 + 55 + 60) ÷ 4 = 280 ÷ 4 = 70**

**3.1 — 50.** Mandated by the 40th General Conference in November 2019 and
adopted by the 41st in November 2021 — twenty-four months from mandate to
adoption, and adoption is entry into force. The 50 anchor precisely.
*Sources: UNESCO (40th GC mandate, November 2019; adoption 23 November 2021).*

**3.2 — 15.** Non-binding soft law; member states are under no obligation to
apply it. Above the 0 anchor because UNESCO Recommendations carry a
constitutional reporting duty that pure guidance does not, which makes
non-implementation visible even though nothing follows from it.
*Sources: UNESCO Constitution Art VIII; non-binding status.*

**3.3 — 45.** The Recommendation spans eleven policy action areas — data,
environment, gender, labour, health, education, culture, communication and more —
and in each it sits alongside existing national law and existing international
instruments without demarcating the boundary. It situates itself relative to
international human rights law, which is partial resolution, but the breadth
guarantees overlap. Just below the 50 anchor. *Source: UNESCO Recommendation, policy action areas.*

**3.4 — 50.** Four-yearly member-state reporting, plus voluntary self-assessment
through the Readiness Assessment Methodology and the Ethical Impact Assessment.
Self-reporting and peer accountability without independent verification or
consequence — the 50 anchor exactly. *Sources: UNESCO Recommendation monitoring provisions; RAM; EIA.*

**Axis 3 = (50 + 15 + 45 + 50) ÷ 4 = 160 ÷ 4 = 40**

---

### 4.4 African Union Continental AI Strategy

**Object of coding:** the Strategy **as endorsed by the AU Executive Council at
its 45th Ordinary Session, Accra, 18–19 July 2024.**

| # | Feature | Raw | Enters mean as |
|---|---|---|---|
| 1.1 | Decision-making concentration | **20** | 20 |
| 1.2 | Agenda-setting concentration | **55** | 55 |
| 1.3 | Resource concentration | **45** | 45 |
| 1.4 | Technical concentration | **45** | 45 |
| 2.1 | Exit possibility | **100** | 100 |
| 2.2 | Amendment difficulty *(rev.)* | **35** | **65** |
| 2.3 | Sunset mechanisms | **65** | 65 |
| 2.4 | Path dependency *(rev.)* | **25** | **75** |
| 3.1 | Deliberation speed | **65** | 65 |
| 3.2 | Binding implementation | **5** | 5 |
| 3.3 | Optimised coordination | **70** | 70 |
| 3.4 | Compliance verification | **25** | 25 |

**1.1 — 20.** Endorsed by the Executive Council, but the Strategy creates no
decision-making body and confers no authority to bind member states — it "calls
upon" and "supports" them, and authority stays with each state. Above the 0
anchor because endorsement ran through a continental organ rather than being
purely voluntary alignment. *Source: AU Executive Council, 45th Ordinary Session, 18–19 July 2024.*

**1.2 — 55.** Drafted by the African Union Commission with AUDA-NEPAD and an
expert process, then put to member states for endorsement. The Commission holds
the initiative, which is above the 50 anchor — but well short of a monopoly,
since endorsement required the Executive Council. *Sources: AU Continental AI Strategy; Executive Council endorsement.*

**1.3 — 45.** The Strategy depends on resource mobilisation it does not itself
provide, so the states and partners that fund implementation will shape it. But
it encodes no decision rights proportional to contribution, and creates no voting
mechanism at all. Just below the 50 anchor.
*Source: AU Continental AI Strategy (resource mobilisation).*
*Flag: I have not verified the AU's scale of assessed contributions against a
primary source in this pass. If AU contributions are tiered by economic capacity,
that strengthens the case for 50 rather than 45.*

**1.4 — 45.** The Strategy *calls for* — but does not establish — an Advisory
Board on AI, a regional AI Ethics Board, and an expert group on AI's impact on
peace and security. Technical capacity is explicitly to be built at national and
regional levels. Below the 50 anchor because the bodies that would hold technical
authority do not yet exist, leaving expertise distributed by default.
*Source: AU Continental AI Strategy, governance arrangements.*

**Axis 1 = (20 + 55 + 45 + 45) ÷ 4 = 165 ÷ 4 = 41.25 → 41**

**2.1 — 100.** Advisory and recommendatory throughout. Member states are urged to
"accelerate the domestication of the strategy"; nothing obliges them to, and
nothing follows from declining. The 100 anchor.
*Source: AU Continental AI Strategy (advisory language).*

**2.2 — 35 (raw) → 65.** Revision would follow the route the Strategy itself
took: the Commission prepares, the Executive Council endorses. A defined
multi-actor procedure, by endorsement rather than ratification, with no
member-state veto over the text. Below the 50 anchor.
*Source: AU Executive Council endorsement process.*

**2.3 — 65.** Time-bounded by design: a five-year implementation plan, with
objectives targeted for 2030. A strategy with a horizon lapses into obsolescence
unless renewed, which is materially closer to expiry than to indefinite
persistence — though it contains no formal sunset clause and no mandatory review
cycle. Between the 50 and 100 anchors, and the highest score on this feature in
the sample. *Source: AU Continental AI Strategy (5-year implementation plan; 2030 objectives).*

**2.4 — 25 (raw) → 75.** Establishes no institution, no registration or
certification infrastructure, and no continuing obligation. It calls for bodies
to be created rather than creating them, and implementation depends on national
plans that largely do not yet exist. Near the 0 anchor, held above it by the sunk
effort of states that have begun domesticating the strategy.
*Source: AU Continental AI Strategy, institutional arrangements.*

**Axis 2 = (100 + 65 + 65 + 75) ÷ 4 = 305 ÷ 4 = 76.25 → 76**

**3.1 — 65.** Developed through 2023 and the first half of 2024 and endorsed in
July 2024 — roughly twelve to eighteen months from drafting to endorsement, with
endorsement operating as entry into force for a non-binding strategy. Between the
50 and 100 anchors. *Source: AU Continental AI Strategy; Executive Council endorsement July 2024.*
*Flag: the drafting start date is approximate. This cell should be pinned to the
Executive Council or Specialised Technical Committee decision that commissioned
the Strategy, which I did not locate.*

**3.2 — 5.** Advisory throughout. No obligation to apply, no dates in the text by
which anything must happen, and no mechanism to make it apply. Essentially the 0
anchor; above zero only because endorsement by the Executive Council carries a
political expectation of domestication.
*Source: AU Continental AI Strategy (advisory language).*

**3.3 — 70.** Explicitly integrative: it positions itself alongside existing AU
instruments and national strategies, and its purpose is to align rather than to
add obligations. Its multi-tiered design — continental, Regional Economic
Communities, national — is a coordination architecture rather than a duplicated
obligation. Above the 50 anchor; short of 100 because the three tiers themselves
generate coordination cost. *Source: AU Continental AI Strategy, implementation arrangements.*

**3.4 — 25.** Calls for "monitoring, evaluation and learning" but specifies no
mechanism, no cycle, no reporting obligation and no body to receive reports.
Between the 0 and 50 anchors, much nearer the former: the intention to monitor is
stated, the machinery is absent. *Source: AU Continental AI Strategy, monitoring and evaluation.*

**Axis 3 = (65 + 5 + 70 + 25) ÷ 4 = 165 ÷ 4 = 41.25 → 41**

---

### 4.5 ASEAN Guide on AI Governance and Ethics

**Object of coding:** the Guide **as unveiled at the 4th ASEAN Digital Ministers'
Meeting, 2 February 2024.** Per Rule 2 the January 2025 generative-AI expansion is
recorded but not scored.

| # | Feature | Raw | Enters mean as |
|---|---|---|---|
| 1.1 | Decision-making concentration | **5** | 5 |
| 1.2 | Agenda-setting concentration | **30** | 30 |
| 1.3 | Resource concentration | **20** | 20 |
| 1.4 | Technical concentration | **40** | 40 |
| 2.1 | Exit possibility | **100** | 100 |
| 2.2 | Amendment difficulty *(rev.)* | **40** | **60** |
| 2.3 | Sunset mechanisms | **35** | 35 |
| 2.4 | Path dependency *(rev.)* | **15** | **85** |
| 3.1 | Deliberation speed | **75** | 75 |
| 3.2 | Binding implementation | **0** | 0 |
| 3.3 | Optimised coordination | **75** | 75 |
| 3.4 | Compliance verification | **5** | 5 |

**1.1 — 5.** ASEAN decides by consultation and consensus, so every member state
holds an effective veto, and the Guide is addressed to organisations and
governments as advice rather than as a decision binding anyone. The 0 anchor
almost exactly; above zero only because it was issued through a standing
ministerial forum. *Sources: ASEAN Charter Art 20; 4th ADGMIN, 2 February 2024.*

**1.2 — 30.** The Guide originates in the ASEAN Digital Masterplan 2025, Enabling
Action 2.7, and was developed through member-state working-level processes under
a rotating chairmanship, with the Digital Ministers' Meeting issuing it. Below
the 50 anchor: agenda-setting is collective *and* rotating, so no standing body or
secretariat holds the initiative from one cycle to the next.
*Sources: ASEAN Guide (ADM2025 EA 2.7); 4th ADGMIN.*

**1.3 — 20.** ASEAN's operational budget is met by equal annual contributions
from member states regardless of economic size, and decisions are by consensus,
so neither funding nor voting encodes material weight. The lowest score on this
feature in the sample. Above the 0 anchor because larger economies carry real
informal influence — Singapore's national AI governance framework was a visible
input to the text. *Source: ASEAN Charter Arts 20, 30.*
*Flag: I cite Arts 20 and 30 from the Charter but could not machine-verify the
article text in this pass. Please spot-check both before publication.*

**1.4 — 40.** The Guide proposes an ASEAN Working Group on AI Governance
"comprising representatives from each ASEAN member state" — open by construction,
one seat per state — and its technical content draws on existing national
frameworks rather than on a supranational expert body. Below the 50 anchor.
*Source: ASEAN Guide, regional recommendations.*

**Axis 1 = (5 + 30 + 20 + 40) ÷ 4 = 95 ÷ 4 = 23.75 → 24**

**2.1 — 100.** Explicitly voluntary: "adoption of the framework laid out herein
is voluntary." There is no commitment to exit from. The 100 anchor.
*Source: ASEAN Guide (voluntary adoption).*

**2.2 — 40 (raw) → 60.** Revision requires ASEAN consensus, which formally means
every member state must agree — the 100 anchor's condition. But the Guide calls
itself "a living document that should be periodically reviewed and assessed by
relevant ASEAN sectorial bodies", which puts revision in a sectoral process
rather than a ministerial renegotiation, and nothing requires ratification. Well
below the anchor. *Sources: ASEAN Charter Art 20; ASEAN Guide (living document).*

**2.3 — 35.** The Guide provides for its own periodic review — it "should be
periodically reviewed and assessed by relevant ASEAN sectorial bodies, in
consultation with industry partners". But the review is hortatory rather than
mandatory, has no fixed cycle, and carries no expiry. Between the 0 and 50
anchors. *Source: ASEAN Guide (living document provision).*

**2.4 — 15 (raw) → 85.** Creates nothing. It proposes a Working Group it does not
establish, imposes no continuing obligation, and builds no certification or
registration infrastructure. Organisations that adopt its risk-assessment
practices sink some effort, which is the only lock-in present. Near the 0 anchor,
and the lowest path dependency in the sample.
*Source: ASEAN Guide, regional and national recommendations.*

**Axis 2 = (100 + 60 + 35 + 85) ÷ 4 = 280 ÷ 4 = 70**

**3.1 — 75.** Mandated through the ASEAN Digital Masterplan 2025 and unveiled at
the 4th ADGMIN on 2 February 2024, with drafting running over roughly the
preceding twelve to eighteen months. Issuance is entry into force for voluntary
guidance. Between the 50 and 100 anchors, toward the fast end.
*Sources: ASEAN Guide (ADM2025 EA 2.7); 4th ADGMIN, 2 February 2024.*
*Flag: drafting start is approximate, as for the AU.*

**3.2 — 0.** Voluntary on its face, addressed to organisations as guidance, with
no obligation on member states to apply it and no date on which anything takes
effect. The 0 anchor exactly — the only 0 on this feature in the sample.
*Source: ASEAN Guide (voluntary adoption).*

**3.3 — 75.** Designed to complement rather than displace: it builds on existing
national frameworks, is addressed to organisations operating across
jurisdictions, and creates no obligation that could conflict with domestic law.
Above the 50 anchor. Short of 100 because leaving everything to national
implementation produces divergence across ten jurisdictions rather than
demarcation. *Source: ASEAN Guide, national-level recommendations.*

**3.4 — 5.** No monitoring, no reporting, no registry, no penalties, and no body
charged with verification — the proposed Working Group is for coordination, not
oversight. The 0 anchor. *Source: ASEAN Guide, regional recommendations.*

**Axis 3 = (75 + 0 + 75 + 5) ÷ 4 = 155 ÷ 4 = 38.75 → 39**

---

## 5. What the completed matrix shows

Three observations that are properties of the *data*, not of any one framework.
Each is a claim you can check, and each is a candidate finding for the paper.

**The EU is the outlier on two axes, and it is the same outlier twice.** It
scores 79 on power concentration where the next highest is 49, and 29 on
reversibility where the next lowest is 65. On the power/reversibility plane the
four non-binding instruments cluster tightly and the EU sits alone, far away.
That is the index doing its job: the design trade-off it was built to detect is
visible in a single scatter.

**Efficiency does not track either of the other axes, and barely varies.** The
spread is 21 points (39 to 60) against 55 on power concentration and 47 on
reversibility. The most concentrated framework and the least concentrated one
score 60 and 39 — a real gap, but a fifth of the range on the concentration axis.
This weakens a tempting story (that concentrating power buys efficiency) and is
worth saying out loud: on this sample, it mostly does not. Note also that the
EU's efficiency lead rests almost entirely on 3.2 binding implementation, where
it scores 75 against 0–15 for everyone else. Strip that one feature and the
efficiency axis is nearly flat across the whole sample.

**Reversibility barely discriminates among the soft-law instruments.** UNESCO,
the AU and ASEAN all score 65–76, and three of the five land within six points of
each other. The axis separates binding from non-binding sharply and then stops
telling you much. If the paper wants reversibility to do more work, the place to
look is 2.3 sunset mechanisms, which is the only feature that spread the soft-law
cases meaningfully (35 for ASEAN, 65 for the AU).

---

## 6. Where I am least confident

Ranked. Check these first.

1. **EU 3.4 compliance verification (70).** Rests on reading Art 43 and Annexes
   VI–VII as meaning most Annex III high-risk systems are self-assessed. If you
   read them differently this moves substantially.
2. **The three "deliberation speed" cells with approximate start dates** — OECD
   (80), AU (65), ASEAN (75). Each should be pinned to a dated mandate. I could
   not locate dated commissioning decisions for the AU and ASEAN instruments.
3. **ASEAN 1.3 (20)** — cites ASEAN Charter Arts 20 and 30 for consensus and equal
   contributions. Both are well-established provisions but I could not
   machine-verify the article text in this pass.
4. **AU 1.3 (45)** — I did not verify the AU's scale of assessed contributions.
5. **OECD, coded as adopted in 2019** rather than as revised in 2024, which
   follows Rule 2 but contradicts how your framework list names the case.
6. **Every cell scored on an instrument's silence.** Where a text simply does not
   address something — AU monitoring machinery, ASEAN review cycles — I scored the
   absence. That is the correct reading under Rule 1, but silence is the easiest
   thing to read wrongly, and it drives the low scores on 3.4 across the soft-law
   cases.

---

## 7. Post-adoption developments — recorded, not scored

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

## 8. Still open

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

## 9. Sources

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

**OECD**
- OECD Convention, Arts 5 and 6 — https://www.oecd.org/en/about/legal/text-of-the-convention-on-the-organisation-for-economic-co-operation-and-development.html
- Recommendation on AI, OECD/LEGAL/0449 — https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449
- Five-year implementation report and 2024 revision, C/MIN(2024)17 — https://one.oecd.org/document/C/MIN(2024)17/en/pdf
- Adherents and overview — https://oecd.ai/en/ai-principles

**UNESCO**
- Recommendation on the Ethics of AI — https://www.unesco.org/en/artificial-intelligence/recommendation-ethics
- Ad Hoc Expert Group and the 40th General Conference mandate — https://www.unesco.org/en/articles/unescos-international-expert-group-begins-work-drafting-first-global-recommendation-ethics-ai-0
- Four-yearly reporting, RAM and EIA — https://regulations.ai/regulations/unesco-recommendation-ethics-ai-2021

**African Union**
- Continental AI Strategy (landing page and endorsement) — https://au.int/en/documents/20240809/continental-artificial-intelligence-strategy
- Continental AI Strategy (full text, July 2024) — https://au.int/sites/default/files/documents/44004-doc-EN-_Continental_AI_Strategy_July_2024.pdf

**ASEAN**
- ASEAN Guide on AI Governance and Ethics (2024) — https://asean.org/wp-content/uploads/2024/02/ASEAN-Guide-on-AI-Governance-and-Ethics_beautified_201223_v2.pdf
- Expanded guide, generative AI (2025) — https://asean.org/wp-content/uploads/2025/01/Expanded-ASEAN-Guide-on-AI-Governance-and-Ethics-Generative-AI.pdf
- Issuance at the 4th ADGMIN, 2 February 2024 — https://www.rajahtannasia.com/wp-content/uploads/2024/10/2024-03_ASEAN-Guide-AI-Governance-Ethics-v2.pdf
- ASEAN Charter (Arts 20, 30 — cited, not machine-verified) — https://asean.org/wp-content/uploads/images/archive/publications/ASEAN-Charter.pdf
