#!/usr/bin/env python3
"""Generate thesis/figures/figure1_prisma.png (simple single-flow PRISMA-style diagram, Figure 1 in Ch. 3).

The diagram tracks only the path to the 21-study analytical sample used for
barrier coding. Contextual, methodological, and theoretical sources were not
part of this search-and-screening process, so no combined intermediate count
is shown for them (avoids implying they went through the same eligibility
funnel as the reshoring-implementation studies).
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(9.0, 7.6))
ax.set_xlim(0, 9.0); ax.set_ylim(2.2, 8.6); ax.axis('off')

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

# Box 1: identification
box(1.2, 7.35, 5.4, 0.9,
    "Records identified through Google Scholar\n(topic-term searches, citation tracking,\nand related-article suggestions)",
    fs=10.5)
arrow(3.9, 7.35, 3.9, 6.7)

# Box 2: screening
box(1.2, 5.75, 5.4, 0.95,
    "Records screened for eligibility\n(language, full-text access, peer-review\nstatus, and fit with the reshoring definition)",
    fs=10.5)

# Branch: down to full-text assessment, right to exclusions
arrow(3.9, 5.75, 3.9, 5.1)
arrow(4.6, 5.75, 6.55, 5.15)

# Box 3a: excluded (side branch)
box(5.6, 4.3, 2.6, 0.85,
    "Excluded: not genuine\nreshoring, or not relevant\nto implementation barriers",
    fs=9)

# Box 3b: full texts assessed (main flow)
box(1.2, 4.15, 3.9, 0.95,
    "Full texts assessed for the\nanalytical sample",
    fs=10.5)
arrow(3.15, 4.15, 3.15, 3.45)

# Box 4: final included
box(1.2, 2.5, 5.4, 0.95,
    "Included in the analytical sample\nand barrier coding\nn = 21",
    fs=11.5, bold=True)

plt.tight_layout()
plt.savefig('/home/user/bachelor/thesis/figures/figure1_prisma.png', dpi=200, bbox_inches='tight')
print('figure regenerated (simplified, tracks only the 21-study analytical sample)')
