#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   plot_draw
@Time    :   2023/12/17
@Author  :   lishuangshuang
@Version :   1.0
@Contact :   lishuangshuang3@mgi-tech.com
'''
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math, os
from typing import List, Dict
from matplotlib.patches import Patch
from scipy.stats import gaussian_kde, norm
from matplotlib.ticker import MaxNLocator
import matplotlib.ticker as ticker
from scipy.interpolate import make_interp_spline
import warnings
warnings.filterwarnings("ignore")

def enrichment_plot(TSS_counts_div, flank_window, outdir):
    fig, ax = plt.subplots(1,1,figsize=(8, 6))
    ax.plot(
        range(-flank_window - 1, flank_window), TSS_counts_div, color= None
    )
    plt.xlim(-flank_window, flank_window)
    plt.xlabel("Position from TSS", fontsize=10)
    plt.ylabel("Normalized enrichment", fontsize=10)

    plt.savefig(
            f"{outdir}/tss.enrichment.png",
            dpi=300,
            facecolor="white",
        )
    

def peak_cellcall_plot(singlecellsummary, outdir):
    singlecellsummary = singlecellsummary.sort_values(by = 'peak_region_fragments', ascending=False)
    filtered_df = singlecellsummary[singlecellsummary['is_cell_barcode'] == 1]
    last_row = filtered_df.iloc[-1]
    peak_region_fragments_value = last_row['peak_region_fragments']
    row_number = len(filtered_df)

    f, ax = plt.subplots(1, 1,figsize=(8, 6))
    sns.lineplot(data=singlecellsummary, x=range(len(singlecellsummary)), y="peak_region_fragments", ax=ax)
    ax.axhline(y=peak_region_fragments_value, xmin=0)
    ax.axvline(x=row_number)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_title(
        f"threshold {peak_region_fragments_value}, {row_number} cells capture"
    )

    plt.savefig(
            f"{outdir}/peak.kneeplot.png",
            dpi=300,
            facecolor="white",
        )


def target_fragment_plot(singlecellsummary, outdir, selecttype="TSS_region_fragments"):
    singlecellsummary = singlecellsummary.sort_values(by = selecttype, ascending=False)
    singlecellsummary['y_value'] = (singlecellsummary[selecttype] / singlecellsummary['fragments']).round(4)
    df2 = singlecellsummary[['fragments', 'y_value', 'is_cell_barcode']].drop_duplicates()
    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        x='fragments',
        y='y_value',
        hue='is_cell_barcode',
        data=df2,
        palette={True: 'blue', False: 'red'},
        s=2
    )

    plt.xscale('log')
    plt.xlabel('fragments')
    plt.legend(title='is_cell_barcode')
    plt.ylim(0, 1)
    if selecttype == "TSS_region_fragments":
        plt.ylabel('Fraction fragments overlapping tss region')
        plt.savefig(
            f"{outdir}/tss.fragments.png",
            dpi=300,
            facecolor="white",
        )
    elif selecttype == "peak_region_fragments":
        plt.ylabel('Fraction fragments overlapping peaks')
        plt.savefig(
            f"{outdir}/peak.fragments.png",
            dpi=300,
            facecolor="white",
        )
    else:
        raise Exception('Unrecognized type!')
        

def merge_graph(selectbarcode_file: str, outdir: str) -> None:
    selectbarcode = pd.read_table(selectbarcode_file, sep='\t', header=None)
    selectbarcode['Count'] = selectbarcode[0].str.split('_N', expand=True)[1]
    figtable = selectbarcode.Count.value_counts()
    figtable = figtable.reset_index(level=None, drop=False, inplace=False)
    #figtable['index'] = figtable['index'].astype(int)
    #figtable['Count'] = figtable.apply(lambda x: round(x['frequence'] / x['index']), axis=1)
    figtable.columns = ['Num', 'Count']
    figtable['Num'] = figtable['Num'].astype(str)
    cellnum = figtable['Count'].sum()
    figtable['num_count'] = figtable["Num"].map(str) +'  '+figtable["Count"].map(str)
    figtable = figtable.sort_values("Num")

    params: Dict[str, object] = {
        'figure.figsize': (7.65, 5.72),
        'axes.labelsize': 'larger',
        'figure.dpi': 100,
        'axes.titlelocation': 'left',
        'axes.spines.top': False,
        'axes.spines.right': False,
        'legend.handlelength': 1.2,
        'legend.handleheight': 1.2,
        'xtick.labelsize': 'medium',
        'ytick.labelsize': 'medium'
    }
    plt.rcParams.update(params)
    set2_colors: List[str] = sns.color_palette('Set2', n_colors=len(figtable))
    # Plot bar graph
    ax = sns.barplot(x='Num', y='Count', data=figtable, palette=set2_colors, saturation=1, width=0.9)
    # Add legend
    legend_labels: List[str] = []
    for i in range(len(figtable)):
        label = figtable.iloc[i]['Num'] + " " + str(figtable.iloc[i]['Count'])
        legend_labels.append(label)
    handles: List[Patch] = [
        Patch(facecolor=set2_colors[i], edgecolor='none', label=legend_labels[i])
        for i in range(len(figtable))
    ]
    ax.legend(handles=handles, loc='upper right', frameon=False, labelspacing=1)
    # Set axis labels and title
    ax.set(xlabel='Number of beads per droplet', ylabel='CellCount',
           title='Total cell number %s' % cellnum)
    # Save plot as png and pdf files
    plt.savefig(
        '%s/cellNumber.merge.png' % outdir,
        dpi=300,
        facecolor="white"
        )
    

def insert_length_plot(fragments_bc_pl, outdir):
    fragments_bc = fragments_bc_pl.to_pandas()
    fragments_bc["Width"] = abs(fragments_bc['End'].values - fragments_bc['Start'].values)
    FPW_DF = (
                fragments_bc.groupby(["Width"])
                .agg({"FragmentCount": np.sum})
                .rename_axis(None)
                .reset_index()
                .rename(columns={"index": "Width", "FragmentCount": "Nr_frag"})
            )
    FPW_DF["Ratio_frag"] = FPW_DF["Nr_frag"].values / np.sum(FPW_DF["Nr_frag"])
    FPW_DF = FPW_DF.sort_values(by=["Width"], ascending=False)
    W = FPW_DF.loc[:, "Width"]
    pF = FPW_DF.loc[:, "Nr_frag"]
    fig, ax = plt.subplots(1, 1,figsize=(8, 6))
    color =None
    ax.plot(W, pF, color=color)
    plt.xlabel("Fragment size", fontsize=10)
    plt.ylabel("Fragments ratio", fontsize=10)
    plt.xlim(0, 800)
    plt.ticklabel_format(style='sci', scilimits=(6, 6), axis='y')
    
    plt.savefig(
        '%s/InterSize.png' % outdir,
        dpi=300,
        facecolor="white"
        )
    FPW_DF.to_csv(
        '%s/fraglength.ratio.csv' % outdir,
        index=False
        )


def dup_plot(fragments_bc_pl, outdir):
    fragments_bc = fragments_bc_pl.to_pandas()
    FPB_dup = (
            fragments_bc.groupby(["CellBarcode"], observed=True, sort=False)
            .agg({"FragmentCount": np.sum})
            .rename_axis(None)
        )
    FPB_dup.columns = ["Total_nr_frag"]

    FPB_nodup = (
        fragments_bc.groupby(["CellBarcode"], sort=False, observed=True)
        .size()
        .to_frame(name="Unique_nr_frag")
        .rename_axis(None)
    )

    FPB = pd.concat([FPB_dup, FPB_nodup], axis=1)
    FPB["Dupl_nr_frag"] = FPB["Total_nr_frag"] - FPB["Unique_nr_frag"]
    FPB["Dupl_rate"] = FPB["Dupl_nr_frag"] / FPB["Total_nr_frag"]

    x = FPB["Unique_nr_frag"]
    y = FPB["Dupl_rate"]

    cmap = None
    fig = plt.figure(figsize=(8, 6))
    xy = np.vstack([np.log(x), y])
    z = gaussian_kde(xy)(xy)
    idx = z.argsort()
    x, y, z = x[idx], y[idx], z[idx]
    plt.scatter(x, y, c=z, s=2, edgecolor=None, cmap=cmap)
    plt.ylim(0, 1)
    plt.xscale("log")
    plt.xlabel("Number of (unique) fragments", fontsize=10)
    plt.ylabel("Duplication rate", fontsize=10)
    plt.colorbar().set_label("Density")

    plt.savefig(
        '%s/dup.percent.png' % outdir,
        dpi=300,
        facecolor="white"
        )
    
### violin plot for rna
def set_plot_params():
    params = {'figure.figsize': (5, 5),
              'axes.labelsize': 'medium',
              'figure.dpi': 150,
              'axes.spines.top': False,
              'axes.spines.right': False,
              'xtick.labelsize': 'medium',
              'ytick.labelsize': 'x-small'}
    plt.rcParams.update(params)


def add_boxplot_violinplot(ax, data, y_col, color):
    boxprops = dict(linewidth=1, edgecolor='black', zorder=1)
    whiskerprops = dict(linewidth=1, color='black')
    medianprops = dict(linewidth=1, color='black')
    
    sns.violinplot(y=y_col, data=data, color=color, inner=None, bw=.2, saturation=1, scale="width", ax=ax, cut=0, linewidth=0.5)
    sns.boxplot(y=y_col, data=data, ax=ax, width=0.2, color="white", fliersize=0, showfliers=False,
                boxprops=boxprops, whiskerprops=whiskerprops, medianprops=medianprops, showcaps=False)
    ax.set_ylabel('')
    ax.set_xlabel(y_col)


def violinrnac_plot(adata):
    set_plot_params()
    
    meta = adata.obs
    if meta.empty:
        print("Error: Input data is empty.")
        return
    
    fig, axes = plt.subplots(1, max(3, meta['pct_counts_mt'].sum() > 0))
    
    threshold1 = np.ceil(meta['pct_counts_mt'].quantile(0.995))
    threshold2 = np.ceil(meta['n_genes_by_counts'].quantile(0.995))
    threshold3 = np.ceil(meta['total_counts'].quantile(0.995))
    meta_threshold1 = meta[meta['pct_counts_mt'] <= threshold1]
    meta_threshold2 = meta[meta['n_genes_by_counts'] <= threshold2]
    meta_threshold3 = meta[meta['total_counts'] <= threshold3]
    
    if meta['pct_counts_mt'].sum() > 0:
        ax = axes[2]
        add_boxplot_violinplot(ax, meta_threshold1, "pct_counts_mt", "#7570B3")
        ax.set_xlabel('mito.percent')
    
    ax = axes[0]
    add_boxplot_violinplot(ax, meta_threshold2, "n_genes_by_counts", "#1B9E77")
    ax.set_xlabel('genes')

    ax = axes[1]
    add_boxplot_violinplot(ax, meta_threshold3, "total_counts", "#D95F02")
    ax.set_xlabel('counts')

    fig.tight_layout()
    return fig


def violinatac_plot(singlecellsummary, outdir):
    set_plot_params()
    
    if singlecellsummary.empty:
        print("Error: Input data is empty.")
        return
    
    meta = singlecellsummary[singlecellsummary['is_cell_barcode'] == 1].copy()

    meta.loc[:, 'TSS_Proportion'] = meta['TSS_region_fragments'] / meta['fragments']
    meta.loc[:, 'FRIP'] = meta['peak_region_fragments'] / meta['fragments']
    meta.loc[:, 'Fragmentslog'] = np.log10(meta['fragments'] + 1)
    
    fig, axes = plt.subplots(1, 3)
    
    add_boxplot_violinplot(axes[0], meta, "Fragmentslog", "#7570B3")
    axes[0].set_xlabel('fragments(Log10)')

    add_boxplot_violinplot(axes[1], meta, "TSS_Proportion", "#1B9E77")
    axes[1].set_xlabel('TSS_Proportion')

    add_boxplot_violinplot(axes[2], meta, "FRIP", "#D95F02")
    axes[2].set_xlabel('FRIP')

    fig.tight_layout()
    plt.savefig(f'{outdir}/summary.violin.png', dpi=300, facecolor="white")


### cDNA saturation
def to_percent(temp: float, position: int) -> str:
    """
    Convert a number to a percentage string with 'k' added to the end if over 1000.

    Returns:
    The percentage string with 'k' added if necessary.
    """
    return '%d'%(temp/1000) + 'k'

def rna_umi_saturation(ax: plt.axes, table: pd.DataFrame):
    """
    Plot the UMI sequencing saturation curve.

    Args:
    ax: The plot axes to draw the curve on.
    table: The data table with columns 'Mean Reads per Cell' and 'Sequencing Saturation'.
    """
    xnew = np.linspace(table['sampling_fraction'].min(),table['sampling_fraction'].max(),20)
    smooth = make_interp_spline(table['sampling_fraction'],table['Sequencing Saturation']/100)(xnew)
    ax.set_xlim([0, table['sampling_fraction'].max()])
    ax.set_ylim([0, 0.9999])
    #ax.xaxis.set_major_formatter(ticker.FuncFormatter(to_percent))
    ax.yaxis.set_major_locator(MaxNLocator(5))
    ax.xaxis.set_major_locator(MaxNLocator(5))
    ax.spines['right'].set_visible(False) 
    ax.spines['top'].set_visible(False)
    ax.grid(linestyle='--')
    ax.plot(xnew,smooth,linewidth=3.0)
    ax.axhline(y=0.9,ls="--",c="black",linewidth=2.0)
    ax.set(xlabel='Sampling Fraction', ylabel='Sequencing Saturation',title='Sequencing Saturation')

def rna_gene_saturation(ax: plt.axes, table: pd.DataFrame):
    """
    Plot the gene expression saturation curve.

    Args:
    ax: The plot axes to draw the curve on.
    table: The data table with columns 'Mean Reads per Cell' and 'Median Genes per Cell'.
    """
    xnew = np.linspace(table['sampling_fraction'].min(),table['sampling_fraction'].max(),20)
    smooth = make_interp_spline(table['sampling_fraction'],table['Median Genes per Cell'])(xnew)
    ax.set_xlim([0, table['sampling_fraction'].max()])
    ax.set_ylim([0, table['Median Genes per Cell'].max()])
    #ax.xaxis.set_major_formatter(ticker.FuncFormatter(to_percent))
    ax.yaxis.set_major_locator(MaxNLocator(4))
    ax.xaxis.set_major_locator(MaxNLocator(5))
    ax.spines['right'].set_visible(False) 
    ax.spines['top'].set_visible(False)
    ax.grid(linestyle='--')
    ax.plot(xnew,smooth,linewidth=3.0)
    ax.set(xlabel='Sampling Fraction', ylabel='Median Gene per Cell',title='Median Gene per Cell')

def plot_rna_saturation(outdir):
    """
    Generate and save the UMI and gene expression saturation plots.
    """
    for_plot = pd.read_table(os.path.join(outdir,'saturation_cDNA.xls'),sep='\t')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), tight_layout=True)
    arts = rna_umi_saturation(ax1,for_plot)
    arts = rna_gene_saturation(ax2,for_plot)
    fig.savefig(os.path.join(outdir,'saturation_cDNA.png'),facecolor='white',transparent=False,dpi=400)
    plt.close(fig)


### plot oligo saturation
def oligo_sequence_saturation(ax: plt.axes, table: pd.DataFrame):
    xnew = np.linspace(table['sampling_fraction'].min(),table['sampling_fraction'].max(),20)
    smooth = make_interp_spline(table['sampling_fraction'],table['Sequencing Saturation']/100)(xnew)
    ax.set_xlim([0, table['sampling_fraction'].max()])
    ax.set_ylim([0, 0.9999])
    ax.yaxis.set_major_locator(MaxNLocator(5))
    ax.xaxis.set_major_locator(MaxNLocator(5))
    ax.spines['right'].set_visible(False) 
    ax.spines['top'].set_visible(False)
    ax.grid(linestyle='--')
    ax.plot(xnew,smooth,linewidth=3.0)
    ax.axhline(y=0.9,ls="--",c="black",linewidth=2.0)
    ax.set(xlabel='sampling_fraction', ylabel='Sequencing Saturation',title='Sequencing Saturation')

def oligo_umi_saturation(ax: plt.axes, table: pd.DataFrame):
    xnew = np.linspace(table['sampling_fraction'].min(),table['sampling_fraction'].max(),20)
    smooth = make_interp_spline(table['sampling_fraction'],table['UMI Saturation']/100)(xnew)
    ax.set_xlim([0, table['sampling_fraction'].max()])
    ax.set_ylim([0, 0.9999])
    ax.yaxis.set_major_locator(MaxNLocator(5))
    ax.xaxis.set_major_locator(MaxNLocator(5))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.grid(linestyle='--')
    ax.plot(xnew,smooth,linewidth=3.0)
    ax.axhline(y=0.9,ls="--",c="black",linewidth=2.0)
    ax.set(xlabel='sampling_fraction', ylabel='UMI Saturation',title='UMI Saturation')

def plot_oligo_saturation(outdir):
    for_plot = pd.read_table(os.path.join(outdir,'saturation_oligo.xls'),sep='\t')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), tight_layout=True)
    arts = oligo_sequence_saturation(ax1,for_plot)
    arts = oligo_umi_saturation(ax2,for_plot)
    fig.savefig(os.path.join(outdir,'saturation_oligo.png'),facecolor='white',transparent=False,dpi=400)
    plt.close(fig)

### saturation atac plot
def atac_sequence_saturation(ax: plt.axes, table: pd.DataFrame):
    xnew = np.linspace(table['sampling_fraction'].min(),table['sampling_fraction'].max(),20)
    smooth = make_interp_spline(table['sampling_fraction'],table['Sequencing Saturation'])(xnew)
    ax.set_xlim([0, table['sampling_fraction'].max()])
    ax.set_ylim([0, 0.9999])
    ax.yaxis.set_major_locator(MaxNLocator(5))
    ax.xaxis.set_major_locator(MaxNLocator(5))
    ax.spines['right'].set_visible(False) 
    ax.spines['top'].set_visible(False)
    ax.grid(linestyle='--')
    ax.plot(xnew,smooth,linewidth=3.0)
    ax.axhline(y=0.9,ls="--",c="black",linewidth=2.0)
    ax.set(xlabel='sampling_fraction', ylabel='Sequencing Saturation',title='Sequencing Saturation')

def atac_frag_saturation(ax: plt.axes, table: pd.DataFrame):
    xnew = np.linspace(table['Mean Reads Pair Per Cell'].min(),table['Mean Reads Pair Per Cell'].max(),20)
    smooth = make_interp_spline(table['Mean Reads Pair Per Cell'],table['median_uniq_frag_per_bc'])(xnew)
    ax.set_xlim([0, table['Mean Reads Pair Per Cell'].max()])
    ax.set_ylim([0, table['median_uniq_frag_per_bc'].max()])
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(to_percent))
    ax.yaxis.set_major_locator(MaxNLocator(4))
    ax.xaxis.set_major_locator(MaxNLocator(5))
    ax.spines['right'].set_visible(False) 
    ax.spines['top'].set_visible(False)
    ax.grid(linestyle='--')
    ax.plot(xnew,smooth,linewidth=3.0)
    ax.set(xlabel='Mean Reads Pair Per Cell', ylabel='Median Unique Fragments Per Cell',title='Median Unique Fragments per Cell')

def plot_atac_saturation(outdir):
    for_plot = pd.read_table(os.path.join(outdir,'sampling.stats.xls'),sep='\t')
    for_plot['Sequencing Saturation'] = 1- for_plot['total_unique_frag_count']/for_plot['total_frag_count']
    for_plot['Mean Reads Pair Per Cell'] = for_plot['total_frag_count']/for_plot['cell_barcode_count']
    for_plot.fillna(0, inplace=True)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), tight_layout=True)
    arts = atac_sequence_saturation(ax1,for_plot)
    arts = atac_frag_saturation(ax2,for_plot)
    fig.savefig(os.path.join(outdir,'saturation_atac.png'),facecolor='white',transparent=False,dpi=400)
    plt.close(fig)