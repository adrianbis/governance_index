#!/usr/bin/env python3
"""
Regenerate the figures on the scores page.

Edit SCORES below so it matches the table in frameworks.html, then run:

    python3 tools/make-figures.py

While only one framework is coded it writes a single-framework profile chart.
Once two or more frameworks have scores it also writes the comparison chart and
the heatmap automatically.

Outputs into assets/img/ :
    figure-eu-profile.png          (always)
    figure-axis-comparison.png     (when 2+ frameworks are coded)
    figure-indicator-heatmap.png   (when 2+ frameworks are coded)
    social-card.png
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "assets", "img")
os.makedirs(OUT, exist_ok=True)

# --- Palette, matching assets/style.css -------------------------------------
PAPER, INK, INK_SOFT, INK_FAINT, RULE = "#FBFAF7", "#17171B", "#55555F", "#86868F", "#E2DFD6"
AXIS = ["#2F4B7C", "#9A4636", "#6A7A38"]
AXIS_NAMES = ["Power concentration", "Reversibility", "Efficiency"]

FRAMEWORKS = ["OECD\nPrinciples", "EU AI Act", "UNESCO\nRec.",
              "AU\nStrategy", "ASEAN\nGuide"]

# (label, axis index, reverse-coded?)
FEATURES = [
    ("1.1 Decision-making concentration", 0, False),
    ("1.2 Agenda-setting concentration",  0, False),
    ("1.3 Resource concentration",        0, False),
    ("1.4 Technical concentration",       0, False),
    ("2.1 Exit possibility",              1, False),
    ("2.2 Amendment difficulty",          1, True),
    ("2.3 Sunset mechanisms",             1, False),
    ("2.4 Path dependency",               1, True),
    ("3.1 Deliberation speed",            2, False),
    ("3.2 Binding implementation",        2, False),
    ("3.3 Optimised coordination",        2, False),
    ("3.4 Compliance verification",       2, False),
]

# RAW scores as coded, rows in FEATURES order, columns in FRAMEWORKS order.
# Use np.nan for a framework that has not been coded yet.
# KEEP THIS IN STEP WITH THE TABLE IN frameworks.html.
n = np.nan
SCORES = np.array([
    [n, 75, n, n, n],
    [n, 90, n, n, n],
    [n, 70, n, n, n],
    [n, 80, n, n, n],
    [n,  0, n, n, n],
    [n, 45, n, n, n],   # reverse-coded
    [n, 50, n, n, n],
    [n, 90, n, n, n],   # reverse-coded
    [n, 45, n, n, n],
    [n, 75, n, n, n],
    [n, 50, n, n, n],
    [n, 70, n, n, n],
], dtype=float)

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "figure.facecolor": PAPER, "axes.facecolor": PAPER, "savefig.facecolor": PAPER,
    "text.color": INK, "axes.labelcolor": INK_SOFT,
    "xtick.color": INK_SOFT, "ytick.color": INK_SOFT,
})


def contributions():
    """Scores as they enter the axis means — reverse-coded rows inverted."""
    out = SCORES.copy()
    for i, (_, _, rev) in enumerate(FEATURES):
        if rev:
            out[i] = 100.0 - out[i]
    return out


def axis_means():
    c = contributions()
    # Uncoded frameworks are all-NaN columns; nanmean warns on those, which is
    # expected here, not a problem. Silence it so the output stays readable.
    with np.errstate(invalid="ignore"):
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)
            return np.array([np.nanmean(c[0:4], axis=0),
                             np.nanmean(c[4:8], axis=0),
                             np.nanmean(c[8:12], axis=0)])


def coded_columns():
    return [j for j in range(SCORES.shape[1]) if not np.all(np.isnan(SCORES[:, j]))]


# --- Single-framework profile ------------------------------------------------
def figure_profile(col=1, filename="figure-eu-profile.png"):
    c = contributions()[:, col]
    raw = SCORES[:, col]
    means = axis_means()[:, col]

    labels, values, colours, notes = [], [], [], []
    for grp in range(3):
        idx = range(grp * 4, grp * 4 + 4)
        for i in idx:
            name, ax_i, rev = FEATURES[i]
            labels.append(name)
            values.append(c[i])
            colours.append(AXIS[ax_i])
            notes.append(f"raw {raw[i]:.0f}" if rev else "")
        labels.append(f"{AXIS_NAMES[grp]} average")
        values.append(means[grp])
        colours.append(AXIS[grp])
        notes.append("MEAN")

    y = np.arange(len(labels))[::-1]
    fig, ax = plt.subplots(figsize=(9, 6.15), dpi=200)

    for yi, v, colour, note in zip(y, values, colours, notes):
        is_mean = note == "MEAN"
        ax.barh(yi, v, height=0.62 if is_mean else 0.5, color=colour,
                alpha=1.0 if is_mean else 0.55, zorder=3)
        label = f"{v:.0f}"
        ax.text(v + 1.5, yi, label, va="center", fontsize=8.5,
                fontweight="bold" if is_mean else "normal",
                color=INK if is_mean else INK_SOFT)
        # The raw score for reverse-coded features sits after the plotted value,
        # never inside the bar — a short bar would push it onto the background
        # and render it invisible.
        if note and not is_mean:
            ax.text(v + 1.5 + 4.6 * len(label), yi, f"({note})", va="center",
                    fontsize=7.4, color=INK_FAINT, style="italic")

    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=8.8)
    for tick, note, colour in zip(ax.get_yticklabels(), notes, colours):
        tick.set_color(colour)
        if note == "MEAN":
            tick.set_fontweight("bold")

    ax.set_xlim(0, 108)
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_xlabel("Score (0–100) as it enters the axis average", fontsize=9, labelpad=9)
    ax.xaxis.grid(True, color=RULE, linewidth=0.9, zorder=0)
    ax.set_axisbelow(True)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(RULE)
    ax.tick_params(length=0)

    title = FRAMEWORKS[col].replace("\n", " ")
    ax.set_title(f"{title} (as adopted): the twelve features", fontsize=12.5, loc="left", pad=26)
    ax.text(0, 1.035,
            "Reverse-coded features (2.2, 2.4) are shown as they enter the average, "
            "with the raw score in brackets.",
            transform=ax.transAxes, fontsize=8.6, color=INK_FAINT)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, filename), bbox_inches="tight", pad_inches=0.35)
    plt.close(fig)


# --- Comparison chart, once 2+ frameworks are coded --------------------------
def figure_axis_comparison():
    cols = coded_columns()
    if len(cols) < 2:
        return False
    means = axis_means()[:, cols]
    names = [FRAMEWORKS[j] for j in cols]

    fig, ax = plt.subplots(figsize=(9, 5), dpi=200)
    x, width = np.arange(len(names)), 0.26
    for i in range(3):
        bars = ax.bar(x + (i - 1) * width, means[i], width, label=AXIS_NAMES[i],
                      color=AXIS[i], edgecolor="none", zorder=3)
        ax.bar_label(bars, fmt="%.0f", padding=3, fontsize=8, color=INK_SOFT)

    ax.set_xticks(x); ax.set_xticklabels(names, fontsize=9.5)
    ax.set_ylim(0, 108); ax.set_yticks([0, 25, 50, 75, 100])
    ax.set_ylabel("Axis score  (0–100)", fontsize=9.5, labelpad=10)
    ax.yaxis.grid(True, color=RULE, linewidth=0.9, zorder=0); ax.set_axisbelow(True)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(RULE); ax.tick_params(length=0)
    ax.set_title("Axis averages across the coded frameworks", fontsize=12.5, loc="left", pad=26)
    ax.text(0, 1.045, "Higher always means more of the property named.",
            transform=ax.transAxes, fontsize=9, color=INK_FAINT)
    ax.legend(frameon=False, fontsize=9, ncols=3, loc="upper center",
              bbox_to_anchor=(0.5, -0.13))
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "figure-axis-comparison.png"),
                bbox_inches="tight", pad_inches=0.35)
    plt.close(fig)
    return True


# --- Heatmap, once 2+ frameworks are coded -----------------------------------
def figure_heatmap():
    cols = coded_columns()
    if len(cols) < 2:
        return False
    data = contributions()[:, cols]
    names = [FRAMEWORKS[j].replace("\n", " ") for j in cols]

    fig, ax = plt.subplots(figsize=(9, 6.2), dpi=200)
    cmap = LinearSegmentedColormap.from_list("ink", [PAPER, "#C9CFD8", "#5B6B84", "#22303F"])
    im = ax.imshow(data, cmap=cmap, vmin=0, vmax=100, aspect="auto")

    ax.set_xticks(np.arange(len(names)))
    ax.set_xticklabels(names, fontsize=9, rotation=22, ha="left")
    ax.xaxis.set_ticks_position("top")
    ax.set_yticks(np.arange(len(FEATURES)))
    ax.set_yticklabels([f[0] for f in FEATURES], fontsize=8.5)
    for i, (_, ax_i, _) in enumerate(FEATURES):
        ax.get_yticklabels()[i].set_color(AXIS[ax_i])

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            v = data[i, j]
            if np.isnan(v):
                continue
            ax.text(j, i, f"{v:.0f}", ha="center", va="center", fontsize=8.5,
                    color="#FFFFFF" if v >= 55 else INK_SOFT)

    ax.set_xticks(np.arange(-0.5, len(names), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(FEATURES), 1), minor=True)
    ax.grid(which="minor", color=PAPER, linewidth=2.5)
    ax.tick_params(which="both", length=0)
    for side in ("top", "right", "left", "bottom"):
        ax.spines[side].set_visible(False)
    for start, end, colour in ((0, 4, AXIS[0]), (4, 8, AXIS[1]), (8, 12, AXIS[2])):
        ax.plot([-0.72, -0.72], [start - 0.35, end - 0.65], color=colour,
                linewidth=3, clip_on=False, solid_capstyle="butt")

    fig.colorbar(im, ax=ax, shrink=0.42, pad=0.03,
                 label="Score (0–100)").outline.set_visible(False)
    fig.text(0.02, 0.045, "Values shown as they enter the axis averages; "
                          "reverse-coded features already inverted.",
             fontsize=8.5, color=INK_FAINT)
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    fig.savefig(os.path.join(OUT, "figure-indicator-heatmap.png"),
                bbox_inches="tight", pad_inches=0.35)
    plt.close(fig)
    return True


# --- Social sharing card -----------------------------------------------------
def social_card():
    fig = plt.figure(figsize=(6, 3.15), dpi=200)
    fig.patch.set_facecolor(PAPER)
    for i, w in enumerate([0.62, 0.42, 0.24]):
        fig.add_artist(plt.Rectangle((0.075, 0.735 - i * 0.062), w * 0.5, 0.038,
                                     facecolor=AXIS[i], edgecolor="none",
                                     transform=fig.transFigure))
    fig.text(0.075, 0.44, "AI Governance\nDesign Index", fontsize=27, color=INK,
             linespacing=1.15, va="center", weight="medium")
    fig.text(0.075, 0.16,
             "How international AI frameworks concentrate power,\n"
             "how reversible they are, and how efficiently they work.",
             fontsize=10.5, color=INK_SOFT, linespacing=1.5, va="center")
    fig.savefig(os.path.join(OUT, "social-card.png"), facecolor=PAPER)
    plt.close(fig)


if __name__ == "__main__":
    cols = coded_columns()
    for j in cols:
        figure_profile(j, "figure-eu-profile.png" if j == 1
                          else f"figure-profile-{j}.png")
    made_comparison = figure_axis_comparison()
    made_heatmap = figure_heatmap()
    social_card()

    means = axis_means()
    print(f"Coded frameworks: {[FRAMEWORKS[j].replace(chr(10),' ') for j in cols]}")
    print("Axis averages (rounded), columns in framework order:")
    for name, row in zip(AXIS_NAMES, means):
        print(f"  {name:22s} "
              f"{['—' if np.isnan(v) else round(v) for v in row]}")
    print(f"Comparison chart: {'written' if made_comparison else 'skipped (needs 2+ frameworks)'}")
    print(f"Heatmap:          {'written' if made_heatmap else 'skipped (needs 2+ frameworks)'}")
    print("Figures written to assets/img/")
