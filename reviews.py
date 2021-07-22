import numpy as np
from matplotlib import pyplot as plt
import argparse
from flexpand import Expander, add_args
from tqdm.auto import tqdm
from skimage import io
import os

class getView:

    def __call__(self, aimg, view_type):
        if view_type == "planes":
            fig = self.get_planes_review(aimg)
        elif view_type == "bbox":
            fig = self.get_bbox_review(aimg)
        elif view_type == "slices":
            fig = self.get_slices_review(aimg)
        return fig
    
    def get_planes_review(self, aimg):
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

    def get_bbox_review(self, aimg):
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

    def get_slices_review(self, aimg):
        slice_ids = np.linspace(0, aimg.shape[0]-1, 12, dtype=np.uint)

        fig, axes = plt.subplots(nrows=3, ncols=4, figsize=(16, 12))
        for i, j in enumerate(slice_ids):
            ca = axes[i//4][i%4]
            ca.imshow(aimg[j], cmap='gray')
            ca.set_xticks([])
            ca.set_yticks([])
        plt.tight_layout()
        return fig


def save_plots(input_files, output_folder, views, omit):
    x = getView()
    for file in tqdm(input_files):
        first_read = True   # flag to check if img if being read first time
        for view in views:
            fname = view + '_' + os.path.split(file)[1]
            if output_folder is None:
                fig_name = os.path.join(os.path.split(file)[0], fname)
            elif os.path.exists(output_folder) and os.path.isdir(output_folder):
                fig_name = os.path.join(output_folder, fname)
            if not omit or not os.path.exists(fig_name):
                if first_read:
                    aimg = io.imread(file)
                    first_read = False
                fig = x(aimg, view)
                fig.savefig(fig_name)
                fig.clf()


def main():
    parser = argparse.ArgumentParser(description = 'get views for 3d TIFF volumes')
    input_group = parser.add_argument_group('Input files to be processed with this util')
    add_args(input_group)

    parser.add_argument('--view-types', nargs='+', choices=["planes","bbox","slices"], help='one or more views to be saved')
    parser.add_argument('--output-files', default=None, help='Files to output the result of processing. If folder is provided will be saved with the same name as input files. If nothing provided will be saved with prefix alongside with input files.')
    parser.add_argument('--omit', default=False, const=True, action='store_const', help='If file with the same name found it will be overwrited. By default this file will not be processed.')
    args = parser.parse_args()
    
    # get input file space
    fle = Expander(verbosity=True)
    input_files = fle(args=args)
    save_plots(input_files, args.output_files, args.view_types, args.omit)


if __name__ == "__main__":
    main()