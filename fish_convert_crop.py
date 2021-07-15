import numpy as np
from matplotlib import pyplot as plt

def get_planes_review(aimg):
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(2, 3)

    plane_0 = int(len(aimg)*0.5)
    plane_1 = int(aimg.shape[1]*0.5)
    plane_2 = int(aimg.shape[2]*0.5)


    ax1 = fig.add_subplot(gs[:, 0])
    ax1.imshow(aimg.take(plane_0, 0), cmap='gray')
    ax1.axhline(plane_1, color='g')
    ax1.axvline(plane_2, color='b')
    plt.setp(ax1.spines.values(), color='r', linewidth=2)
    ax1.set_xticks([])
    ax1.set_yticks([])

    ax2 = fig.add_subplot(gs[0, 1:])
    plt.setp(ax2.spines.values(), color='g', linewidth=2)
    ax2.axvline(plane_0, color='r')
    ax2.axhline(plane_2, color='b')
    ax2.imshow(aimg.take(plane_1, 1).T, cmap='gray')
    ax2.set_xticks([])
    ax2.set_yticks([])

    ax3 = fig.add_subplot(gs[1, 1:])
    plt.setp(ax3.spines.values(), color='b', linewidth=2)
    ax3.axvline(plane_0, color='r')
    ax3.axhline(plane_1, color='g')
    ax3.imshow(aimg.take(plane_2, 2).T, cmap='gray')
    ax3.set_xticks([])
    ax3.set_yticks([])

    plt.tight_layout()
    return fig

def get_bbox_review(aimg):
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(30, 10))

    axes[0][0].imshow(aimg.take(0, 1).T, cmap='gray')
    axes[0][0].set_title(f'axis=1;slice=0')
    axes[0][0].set_xticks([])
    axes[0][0].set_yticks([])

    axes[0][1].imshow(aimg.take(0, 0), cmap='gray')
    axes[0][1].set_title(f'axis=0;slice=0')
    axes[0][1].set_xticks([])
    axes[0][1].set_yticks([])

    axes[0][2].imshow(aimg.take(-1, 1).T, cmap='gray')
    axes[0][2].set_title(f'axis=1;slice=-1')
    axes[0][2].set_xticks([])
    axes[0][2].set_yticks([])

    axes[1][0].imshow(aimg.take(0, 2).T, cmap='gray')
    axes[1][0].set_title(f'axis=2;slice=0')
    axes[1][0].set_xticks([])
    axes[1][0].set_yticks([])

    axes[1][1].imshow(aimg.take(-1, 0), cmap='gray')
    axes[1][1].set_title(f'axis=0;slice=-1')
    axes[1][1].set_xticks([])
    axes[1][1].set_yticks([])

    axes[1][2].imshow(aimg.take(-1, 2).T, cmap='gray')
    axes[1][2].set_title(f'axis=2;slice=-1')
    axes[1][2].set_xticks([])
    axes[1][2].set_yticks([])

    plt.tight_layout()
    return fig

def get_slices_review(aimg):
    slice_ids = np.linspace(0, aimg.shape[0]-1, 12, dtype=np.uint)

    fig, axes = plt.subplots(nrows=3, ncols=4, figsize=(16, 12))
    for i, j in enumerate(slice_ids):
        ca = axes[i//4][i%4]
        ca.imshow(aimg[j], cmap='gray')
        ca.set_xticks([])
        ca.set_yticks([])
    plt.tight_layout()
    return fig

