# AI Governance Design Index — website

A three-page static site publishing an index that scores international AI
governance frameworks on how they are built: how much power they concentrate,
how entrenched their rules are, and how much friction they create in
implementation.

**Getting it online for the first time:** follow [SETUP.md](SETUP.md).
**Changing it afterwards:** this file.

---

## What's here

```
index.html          The About page — project summary and the three authors
rubric.html         The index — three axes, fifteen indicators, all anchors
frameworks.html     The scores — framework list, matrix, figures
404.html            Shown if someone follows a broken link

assets/
  style.css         All the design. Colours and type are set at the very top.
  site.js           Recalculates axis averages and draws the bars
  img/              Portraits, figures, favicon, social sharing card

tools/
  make-figures.py   Regenerates the two charts (optional — see below)

LICENSE             MIT — covers the website code
LICENSE-CONTENT.md  CC BY 4.0 — covers the index, scores and text
```

There is **no build step**. The files you see are the files the web serves. You
can double-click `index.html` on your own computer to preview any change before
you commit it.

---

## How to make a change

1. Go to your repository on github.com.
2. Click the file you want to change.
3. Click the **pencil icon** (top right of the file).
4. Edit.
5. Scroll down, write a short note in the commit box (e.g. `Update x
   bio`), click **Commit changes**.
6. Wait about thirty seconds and refresh the live site.

If you break something, GitHub keeps every version: open the file → **History**
→ open the version from before → copy the good version back in.

---

## The three things you'll change most often

### 1. A person's photo or bio — `index.html`

Find the block that starts `<li class="person">`. Each author has one. Change
the name, the role line, the bio paragraph and the LinkedIn URL.

For a photo: upload a square image (JPG or PNG, at least 300 × 300 pixels) into
`assets/img/`, then change the `src="assets/img/person-1.svg"` to your file
name. The site crops it into a circle for you. Keep the `alt` text accurate —
that's what a screen reader announces.

### 2. A score — `frameworks.html`

Find the table under the heading **The full matrix**. Each score looks like this:

```html
<td class="score" data-fw="eu" data-score="75">75</td>
```

**Change both numbers** — the one in `data-score="75"` and the one between the
tags. They must match.

You never need to update an axis average. The page recalculates every average
from the individual scores each time it loads, so the averages and the summary
cards at the top can't drift out of step with the numbers you edited.

When the real scores go in, **delete the yellow placeholder notice** at the top
of `frameworks.html` — the block that starts `<div class="notice"`.

### 3. Wording anywhere

All the text lives directly in the HTML files between the tags. Change the words,
leave the `<tags>` alone, commit. If you accidentally delete a tag the page will
look wrong — revert via History and try again.

---

## Adding a new framework to the index

Four edits in `frameworks.html`, all copy-and-paste:

1. **Framework list** — copy one `<li>` block under *Frameworks included*, paste
   it below, change the name, dates, description and source links.
2. **Summary card** — copy one `<article class="summary-card" data-fw="...">`
   block, paste it, change the name and give it a new short `data-fw` code
   (lowercase, no spaces, e.g. `uk`).
3. **Table header** — add one `<th scope="col">Your Framework</th>` at the end of
   the header row.
4. **Table body** — add one `<td class="score" data-fw="uk" data-score="50">50</td>`
   at the end of **every** row in the table, including the three average rows.
   The `data-fw` code must match the one you used in step 2.

Then regenerate the figures (below), or replace them with your own images.

---

## Adding a whole new page

1. In GitHub, open `rubric.html`, click the pencil, select everything, copy.
2. Go back to the repository root → **Add file** → **Create new file**.
3. Name it something like `sources.html`.
4. Paste, then replace the middle section — everything between `<main id="main">`
   and `</main>` — with your content.
5. Change the `<title>` and the `<meta name="description">` at the top.
6. Add a link to it in the navigation. The navigation appears in **all four**
   HTML files — add the same line to each, or the new page will only be
   reachable from one place.

---

## Regenerating the figures

The two charts on the scores page are generated from a copy of the scores held
in `tools/make-figures.py`. If you change scores in the table, update the
`SCORES` block in that file to match, then run:

```
python3 tools/make-figures.py
```

This needs Python and matplotlib on your own machine. If that's a hurdle, just
make the charts however you normally would, save them into `assets/img/` under
the same file names, and ignore this script — nothing else depends on it.

**Whichever route you take, do not let the figures and the table disagree.** A
reader who spots a mismatch stops trusting every other number on the page.

---

## Changing the look

Open `assets/style.css`. The first forty lines are a list of colours, fonts and
widths. Change a value there and it changes everywhere consistently. You should
not need to read past that block.

The three axis colours — `--axis-1`, `--axis-2`, `--axis-3` — are used in the
navigation mark, the rubric page, the table, the summary cards and the figures.
If you change them here, change them in `tools/make-figures.py` too.

The site follows the reader's system light/dark setting automatically.

---

## Licence

- **Index, scores, figures and text:** CC BY 4.0 — see [LICENSE-CONTENT.md](LICENSE-CONTENT.md)
- **Site code:** MIT — see [LICENSE](LICENSE)


