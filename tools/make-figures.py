#!/usr/bin/env python3
"""
Regenerate the figures on the scores page.

You only need this if you want to rebuild the charts yourself. Edit the SCORES
dictionary below so it matches the table in frameworks.html, then run:

    python3 tools/make-figures.py

It writes three files into assets/img/ :
    figure-axis-comparison.png
    figure-indicator-heatmap.png
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
PAPER = "#FBFAF7"
INK = "#17171B"
INK_SOFT = "#55555F"
INK_FAINT = "#86868F"
RULE = "#E2DFD6"
AXIS = ["#2F4B7C", "#9A4636", "#6A7A38"]

FRAMEWORKS = ["OECD\nPrinciples", "EU AI Act", "UN\ninstruments",
              "AU\ninstruments", "ASEAN\nGuide"]

INDICATORS = [
    ("1.1 Centralisation of decision-making", 0),
    ("1.2 Bindingness", 0),
    ("1.3 Enforcement power", 0),
    ("1.4 Exclusivity of agenda-setting", 0),
    ("1.5 Supranationality", 0),
    ("2.1 Amendment rigidity", 1),
    ("2.2 Permanence of rules", 1),
    ("2.3 Rigidity of technical updating", 1),
    ("2.4 Exit cost", 1),
    ("2.5 Insulation from legal challenge", 1),
    ("3.1 Adoption lag", 2),
    ("3.2 Deadline unworkability", 2),
    ("3.3 Implementation support gap", 2),
    ("3.4 Coordination cost", 2),
    ("3.5 Adaptive rigidity", 2),
]

# Rows in the same order as INDICATORS; columns in the order of FRAMEWORKS.
# KEEP THIS IN STEP WITH THE TABLE IN frameworks.html.
SCORES = np.array([
    [25, 100,  25,  50,   0],
    [ 0, 100,  25,  50,   0],
    [ 0, 100,   0,  33,   0],
    [75,  50,  25,  50,  50],
    [ 0, 100,   0,  25,   0],
    [25,  50,  75, 100,   0],
    [50,  25,  75, 100, 100],
    [25,   0,  75, 100,  50],
    [ 0, 100,   0,  50,   0],
    [100,  0, 100,  50, 100],
    [25,  75,  50,  50,  25],
    [100, 50, 100, 100, 100],
    [50,   0,  50,  75,  50],
    [100, 50, 100, 100, 100],
    [25,   0,  75, 100,  50],
], dtype=float)

AXIS_NAMES = ["Power Concentration", "Entrenchment", "Implementation Friction"]

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "figure.facecolor": PAPER,
    "axes.facecolor": PAPER,
    "savefig.facecolor": PAPER,
    "text.color": INK,
    "axes.labelcolor": INK_SOFT,
    "xtick.color": INK_SOFT,
    "ytick.color": INK_SOFT,
})


def axis_means():
    return np.array([SCORES[0:5].mean(axis=0),
                     SCORES[5:10].mean(axis=0),
                     SCORES[10:15].mean(axis=0)])


# --- Figure 1: grouped bars --------------------------------------------------
def figure_axis_comparison():
    means = axis_means()
    fig, ax = plt.subplots(figsize=(9, 5), dpi=200)

    x = np.arange(len(FRAMEWORKS))
    width = 0.26

    for i in range(3):
        bars = ax.bar(x + (i - 1) * width, means[i], width,
                      label=AXIS_NAMES[i], color=AXIS[i],
                      edgecolor="none", zorder=3)
        ax.bar_label(bars, fmt="%.0f", padding=3, fontsize=8,
                     color=INK_SOFT, zorder=4)

    ax.set_xticks(x)
    ax.set_xticklabels(FRAMEWORKS, fontsize=9.5)
    ax.set_ylim(0, 108)
    ax.set_yticks([0, 25, 50, 75, 100])
    ax.set_ylabel("Axis score  (0–100)", fontsize=9.5, labelpad=10)
    ax.yaxis.grid(True, color=RULE, linewidth=0.9, zorder=0)
    ax.set_axisbelow(True)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(RULE)
    ax.tick_params(length=0)

    ax.set_title("Axis averages across five AI governance frameworks",
                 fontsize=12.5, loc="left", pad=26, color=INK)
    ax.text(0, 1.045, "Higher always means more of the property named. "
                      "Placeholder data.",
            transform=ax.transAxes, fontsize=9, color=INK_FAINT)

    ax.legend(frameon=False, fontsize=9, ncols=3, loc="upper center",
              bbox_to_anchor=(0.5, -0.13))

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "figure-axis-comparison.png"),
                bbox_inches="tight", pad_inches=0.35)
    plt.close(fig)


# --- Figure 2: heatmap -------------------------------------------------------
def figure_heatmap():
    fig, ax = plt.subplots(figsize=(9, 7), dpi=200)

    cmap = LinearSegmentedColormap.from_list(
        "ink", [PAPER, "#C9CFD8", "#5B6B84", "#22303F"])

    im = ax.imshow(SCORES, cmap=cmap, vmin=0, vmax=100, aspect="auto")

    ax.set_xticks(np.arange(len(FRAMEWORKS)))
    ax.set_xticklabels([f.replace("\n", " ") for f in FRAMEWORKS],
                       fontsize=9, rotation=22, ha="left")
    ax.xaxis.set_ticks_position("top")
    ax.set_yticks(np.arange(len(INDICATORS)))
    ax.set_yticklabels([n for n, _ in INDICATORS], fontsize=8.5)

    for i, (_, axis_i) in enumerate(INDICATORS):
        ax.get_yticklabels()[i].set_color(AXIS[axis_i])

    for i in range(SCORES.shape[0]):
        for j in range(SCORES.shape[1]):
            v = SCORES[i, j]
            ax.text(j, i, f"{v:.0f}", ha="center", va="center", fontsize=8.5,
                    color="#FFFFFF" if v >= 55 else INK_SOFT)

    ax.set_xticks(np.arange(-0.5, len(FRAMEWORKS), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(INDICATORS), 1), minor=True)
    ax.grid(which="minor", color=PAPER, linewidth=2.5)
    ax.tick_params(which="both", length=0)
    for side in ("top", "right", "left", "bottom"):
        ax.spines[side].set_visible(False)

    for start, end, colour in ((0, 5, AXIS[0]), (5, 10, AXIS[1]), (10, 15, AXIS[2])):
        ax.plot([-0.72, -0.72], [start - 0.35, end - 0.65],
                color=colour, linewidth=3, clip_on=False,
                solid_capstyle="butt")

    fig.colorbar(im, ax=ax, shrink=0.4, pad=0.03,
                 label="Score (0–100)").outline.set_visible(False)

    fig.text(0.02, 0.045, "Placeholder data. Colour bars at left mark the three axes: "
                          "power concentration, entrenchment, implementation friction.",
             fontsize=8.5, color=INK_FAINT)

    fig.tight_layout(rect=(0, 0.05, 1, 1))
    fig.savefig(os.path.join(OUT, "figure-indicator-heatmap.png"),
                bbox_inches="tight", pad_inches=0.35)
    plt.close(fig)


# --- Social sharing card -----------------------------------------------------
def social_card():
    fig = plt.figure(figsize=(6, 3.15), dpi=200)
    fig.patch.set_facecolor(PAPER)

    for i, w in enumerate([0.62, 0.42, 0.24]):
        fig.add_artist(plt.Rectangle((0.075, 0.735 - i * 0.062), w * 0.5, 0.038,
                                     facecolor=AXIS[i], edgecolor="none",
                                     transform=fig.transFigure))

    fig.text(0.075, 0.44, "AI Governance\nDesign Index", fontsize=27,
             color=INK, linespacing=1.15, va="center", weight="medium")
    fig.text(0.075, 0.16,
             "How international AI frameworks concentrate power,\n"
             "entrench their rules, and cost to implement.",
             fontsize=10.5, color=INK_SOFT, linespacing=1.5, va="center")

    fig.savefig(os.path.join(OUT, "social-card.png"), facecolor=PAPER)
    plt.close(fig)


if __name__ == "__main__":
    figure_axis_comparison()
    figure_heatmap()
    social_card()
    means = axis_means()
    print("Axis averages (rounded), columns in framework order:")
    for name, row in zip(AXIS_NAMES, means):
        print(f"  {name:26s} {[round(v) for v in row]}")
    print("Figures written to assets/img/")
