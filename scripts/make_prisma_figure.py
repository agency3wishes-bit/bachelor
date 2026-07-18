#!/usr/bin/env python3
"""Generate thesis/figures/figure1_prisma.png (simple single-flow PRISMA-style diagram, Figure 1 in Ch. 3)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(8.0, 7.4))
ax.set_xlim(0, 8.0); ax.set_ylim(1.9, 8.6); ax.axis('off')

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

box(1.0, 7.35, 5.4, 0.9,
    "Records identified through Google Scholar\n(topic-term searches, citation tracking,\nand related-article suggestions)",
    fs=10.5)
arrow(3.7, 7.35, 3.7, 6.7)

box(1.0, 5.75, 5.4, 0.95,
    "Records screened for eligibility\n(language, full-text availability, peer-review\nstatus, and fit with the reshoring definition)",
    fs=10.5)
arrow(3.7, 5.75, 3.7, 5.1)

box(1.0, 4.15, 5.4, 0.95,
    "Full texts assessed\nn = 33",
    fs=11, bold=True)

arrow(3.7, 4.15, 3.7, 3.5)
arrow(3.7, 3.9, 6.6, 3.15)

box(4.5, 2.7, 3.1, 1.05,
    "Not coded for barrier evidence\n(context or methodology only)\nn = 12",
    fs=9.5)

box(1.0, 2.5, 3.3, 0.95,
    "Included in the\nanalytical sample\nn = 21",
    fs=11, bold=True)

plt.tight_layout()
plt.savefig('/home/user/bachelor/thesis/figures/figure1_prisma.png', dpi=200, bbox_inches='tight')
print('figure regenerated (simple single-flow version)')
