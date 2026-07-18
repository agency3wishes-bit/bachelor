#!/usr/bin/env python3
"""Generate thesis/figures/figure1_prisma.png (adapted PRISMA 2020 flow diagram, Figure 1 in Ch. 3).

Adapted PRISMA 2020 layout: four sequential stages (Identification, Screening,
Eligibility, Included) with side stage labels, rectangular boxes, plain arrows,
black and white. No intermediate counts are shown because none were
systematically recorded during the iterative search; n = 21 (the analytical
sample) is the only verifiable stage number. Contextual, methodological, and
theoretical sources are explained in the text, not in the diagram.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

fig, ax = plt.subplots(figsize=(7.6, 8.2))
ax.set_xlim(0, 7.6); ax.set_ylim(1.4, 8.7); ax.axis('off')

BOX_X, BOX_W = 1.55, 5.5

def box(y, h, text, fs=10.5, bold=False):
    p = Rectangle((BOX_X, y), BOX_W, h, linewidth=1.2,
                  edgecolor='black', facecolor='white')
    ax.add_patch(p)
    ax.text(BOX_X + BOX_W/2, y + h/2, text, ha='center', va='center',
            fontsize=fs, fontweight='bold' if bold else 'normal')

def stage_label(y, h, text):
    p = Rectangle((0.35, y), 0.75, h, linewidth=1.2,
                  edgecolor='black', facecolor='white')
    ax.add_patch(p)
    ax.text(0.35 + 0.375, y + h/2, text, ha='center', va='center',
            fontsize=10, rotation=90)

def arrow(y1, y2):
    x = BOX_X + BOX_W/2
    a = FancyArrowPatch((x, y1), (x, y2), arrowstyle='-|>', mutation_scale=16,
                        linewidth=1.2, color='black')
    ax.add_patch(a)

# Identification
stage_label(7.35, 1.0, 'Identification')
box(7.35, 1.0,
    "Records identified through Google Scholar\n(topic-term searches, backward and forward\ncitation searching, and related-article suggestions)",
    fs=10)
arrow(7.35, 6.85)

# Screening
stage_label(5.45, 1.4, 'Screening')
box(5.45, 1.4,
    "Records screened against the eligibility criteria\n(English language, full-text accessibility,\npeer-review status, relevance to manufacturing\nreshoring, and fit with the adopted\nreshoring definition)",
    fs=10)
arrow(5.45, 4.95)

# Eligibility
stage_label(4.05, 0.9, 'Eligibility')
box(4.05, 0.9,
    "Full-text studies assessed against\nthe inclusion criteria",
    fs=10.5)
arrow(4.05, 3.55)

# Included
stage_label(2.5, 1.05, 'Included')
box(2.5, 1.05,
    "Studies included in the analytical sample\nand barrier coding\nn = 21",
    fs=10.5, bold=True)

plt.tight_layout()
plt.savefig('/home/user/bachelor/thesis/figures/figure1_prisma.png', dpi=200, bbox_inches='tight')
print('figure regenerated (adapted PRISMA 2020 layout with stage labels)')
