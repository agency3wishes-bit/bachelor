#!/usr/bin/env python3
"""Generate thesis/figures/figure1_prisma.png (simplified single-flow diagram, Figure 1 in Ch. 3).

Pure single flow to the 21-study analytical sample, with no intermediate
counts (none are honestly verifiable) and no side branches. Contextual,
methodological, and theoretical sources are explained in the text, not in
the diagram.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(7.0, 7.8))
ax.set_xlim(0, 7.0); ax.set_ylim(1.6, 8.6); ax.axis('off')

def box(x, y, w, h, text, fs=10.5, bold=False):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                       linewidth=1.2, edgecolor='black', facecolor='white')
    ax.add_patch(p)
    ax.text(x+w/2, y+h/2, text, ha='center', va='center', fontsize=fs,
            fontweight='bold' if bold else 'normal')

def arrow(x1, y1, x2, y2):
    a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='-|>', mutation_scale=16,
                        linewidth=1.2, color='black')
    ax.add_patch(a)

box(0.8, 7.35, 5.4, 0.9,
    "Records identified through Google Scholar\n(topic-term searches, backward and forward\ncitation searching, and related-article suggestions)",
    fs=10)
arrow(3.5, 7.35, 3.5, 6.75)

box(0.8, 5.55, 5.4, 1.2,
    "Records screened for eligibility\n(English language, full-text access,\npeer-review status, relevance to manufacturing\nreshoring, and fit with the adopted\nreshoring definition)",
    fs=10)
arrow(3.5, 5.55, 3.5, 4.95)

box(0.8, 3.95, 5.4, 0.9,
    "Full-text studies assessed for inclusion\nin the analytical sample",
    fs=10.5)
arrow(3.5, 3.95, 3.5, 3.35)

box(0.8, 2.2, 5.4, 1.05,
    "Studies included in the analytical sample\nand barrier coding\nn = 21",
    fs=11, bold=True)

plt.tight_layout()
plt.savefig('/home/user/bachelor/thesis/figures/figure1_prisma.png', dpi=200, bbox_inches='tight')
print('figure regenerated (pure single flow, n=21 only)')
