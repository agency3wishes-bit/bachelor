#!/usr/bin/env python3
"""Generate thesis/figures/figure1_prisma.png (two-arm PRISMA 2020 flow diagram, Figure 1 in Ch. 3)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(10.2, 11.5))
ax.set_xlim(0, 10); ax.set_ylim(0, 12); ax.axis('off')

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

box(0.3, 11.1, 4.4, 0.7, "Identification of studies via databases\n(documented update search, Google Scholar,\n15 July 2026)", fs=10, bold=True)
box(5.3, 11.1, 4.4, 0.7, "Identification of studies via other methods\n(exploratory search, citation searching,\nrelated-article suggestions)", fs=10, bold=True)

box(0.5, 9.5, 4.0, 1.0, "Records identified\n(3 predefined search strings)\nn = 102")
arrow(2.5, 9.5, 2.5, 8.85)
box(0.5, 7.9, 4.0, 0.85, "Duplicates removed\n(already in the review corpus)\nn = 11")
arrow(2.5, 7.9, 2.5, 7.25)
box(0.5, 6.4, 4.0, 0.75, "Records screened\nn = 91")
arrow(2.5, 6.4, 2.5, 5.75)
box(0.5, 4.55, 4.0, 1.1, "Records excluded, with reason: n = 8\n– macro/policy-level, not firm-level: 5\n– nearshoring, not genuine reshoring: 1\n– not peer-reviewed / inaccessible: 2", fs=9.5)
arrow(2.5, 4.55, 2.5, 3.9)
box(0.5, 3.0, 4.0, 0.8, "Records not further assessed\nwithin thesis scope\nn = 83", fs=9.5)
arrow(2.5, 3.0, 2.5, 2.35)
box(0.5, 1.65, 4.0, 0.6, "New studies included from this arm\nn = 0")

box(5.5, 9.5, 4.0, 1.0, "Records identified\nn = not recorded\n(exploratory phase)*")
arrow(7.5, 9.5, 7.5, 8.85)
box(5.5, 7.65, 4.0, 1.1, "Reports assessed at full text\nn = 34\n(21 formal sample + 8 contextual\n+ 5 methodology)", fs=9.5)
arrow(7.5, 7.65, 7.5, 7.0)
box(5.5, 5.35, 4.0, 1.55, "Reports excluded, with reason: n = 4\n– not genuine reshoring (China+1 /\n   re-offshoring pattern): 1\n– full text not openly accessible: 1\n– preprint, not peer-reviewed: 1\n– duplicate of an included source: 1", fs=9.5)
arrow(7.5, 5.35, 7.5, 1.25)

box(1.7, 0.35, 6.6, 0.8, "Studies included in the formal analytical sample\nn = 21", fs=11, bold=True)
arrow(2.5, 1.65, 3.5, 1.2)

ax.text(0.3, 0.02, "* Records identified in the original exploratory phase were not counted prospectively; "
                   "the documented update search provides the reproducible search record.",
        fontsize=8.5, style='italic')

plt.tight_layout()
plt.savefig('/home/user/bachelor/thesis/figures/figure1_prisma.png', dpi=200, bbox_inches='tight')
print('figure regenerated')
