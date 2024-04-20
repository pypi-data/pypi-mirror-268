from pathlib import Path

import matplotlib as mpl
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.patches import Rectangle

import mpl_fontkit as fk
import marsilea as ma
from marsilea.layers import Rect, Marker, FrameRect, RightTri
from marsilea.plotter import (SizedMesh, MarkerMesh, Numbers,
                              Violin, Labels, Chunk, ColorMesh)
from sklearn.preprocessing import normalize

SAVE_PATH = Path(__file__).parent.parent.parent / 'img' / 'publication'
SAVE_PATH.mkdir(exist_ok=True)
fk.install('Lato')

mpl.rcParams['font.size'] = 8

pbmc3k = ma.load_data("pbmc3k")
exp = pbmc3k['exp']
pct_cells = pbmc3k['pct_cells']
count = pbmc3k['count']

matrix = normalize(exp.to_numpy(), axis=0)

cell_cat = ['Lymphoid', 'Myeloid', 'Lymphoid', 'Lymphoid',
            'Lymphoid', 'Myeloid', 'Myeloid', 'Myeloid']

if __name__ == "__main__":

    # All plotters
    size_mesh = SizedMesh(
        pct_cells, size_norm=Normalize(vmin=0, vmax=100),
        color="none", edgecolor="#6E75A4",
        size_legend_kws=dict(
            title="% of cells", show_at=[.3, .5, .8, 1]
        ))
    marker_mesh = MarkerMesh(matrix > 0.7, color="#DB4D6D", label="High")

    bar = Numbers(count['Value'], color="#fac858", label="Cell Count")
    violin = Violin(exp, label="Expression", linewidth=0, color="#ee6666")

    cell_labels = Labels(exp.index, align="center")
    gene_names = Labels(exp.columns, padding=10)
    cat_labels = Chunk(['Lymphoid', 'Myeloid'], fill_colors=["#33A6B8", "#B481BB"],
                       color="white", padding=20)

    # Step 1a
    h = ma.Heatmap(
        matrix, cmap="Greens", label="Normalized\nExpression",
        width=3, height=3.5)
    h.save(SAVE_PATH / 'layout-step-1a.png', dpi=300)

    # Step 1b
    h.add_layer(size_mesh)
    h.add_layer(marker_mesh)
    h.save(SAVE_PATH / 'layout-step-1b.png', dpi=300)

    # Step 2
    h.add_right(bar, pad=.1, size=.7)
    h.add_top(violin, pad=.1, size=.75)
    h.save(SAVE_PATH / 'layout-step-2.png', dpi=300)

    # Step 3
    h.add_left(cell_labels)
    h.add_bottom(gene_names)
    h.hsplit(labels=cell_cat, order=['Lymphoid', 'Myeloid'])
    h.add_left(cat_labels, pad=.05)
    h.save(SAVE_PATH / 'layout-step-3.png', dpi=300)

    # Step 4
    h.add_dendrogram("left", colors=["#33A6B8", "#B481BB"])
    h.add_dendrogram("bottom")
    h.add_legends(pad=.1)
    h.save(SAVE_PATH / 'layout-step-4.png', dpi=300)

    # Show layout adjustment
    mapper = {0: Rect(color="#454545"), 1: Marker("*", color="#D14D72"),
              2: FrameRect(color="#89375F"), 3: RightTri(color="#CE5959"),
              4: RightTri(color="#BACDDB", right_angle="upper right")}
    rng = np.random.default_rng(0)
    data = rng.choice([0, 1, 2, 3, 4], (10, 10))
    data1d = rng.choice(np.arange(100), 10)
    data2d = rng.standard_normal((10, 10))
    bar = Numbers(data1d, color="#52D3D8")
    violin = Violin(data2d, color="#52D3D8")

    # Basic layout
    h = ma.Layers(data=data, pieces=mapper, shrink=(.8, .8))
    h.add_right(bar, size=1)
    h.save(SAVE_PATH / 'layout-basic.png', dpi=300)

    # Show change plotter size
    h = ma.Layers(data=data, pieces=mapper, shrink=(.8, .8), width=8)
    h.add_right(bar, size=1)
    h.save(SAVE_PATH / 'layout-basic-change-canvas-size.png', dpi=300)

    # Show change plotter size
    h = ma.Layers(data=data, pieces=mapper, shrink=(.8, .8))
    h.add_right(bar, size=3)
    h.save(SAVE_PATH / 'layout-basic-change-plotter-size.png', dpi=300)

    # Show change pad
    h = ma.Layers(data=data, pieces=mapper, shrink=(.8, .8))
    h.add_right(bar, size=1, pad=2)
    h.save(SAVE_PATH / 'layout-basic-change-pad.png', dpi=300)

    # Show change location
    h = ma.Layers(data=data, pieces=mapper, shrink=(.8, .8))
    h.add_left(bar, size=1)
    h.save(SAVE_PATH / 'layout-basic-change-location.png', dpi=300)

    # Show change plotter type
    h = ma.Layers(data=data, pieces=mapper, shrink=(.8, .8))
    h.add_right(violin, size=1)
    h.save(SAVE_PATH / 'layout-basic-change-plotter-type.png', dpi=300)

