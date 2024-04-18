import os,argparse
import sys

class Analysis:
    def __init__(self, args: argparse.Namespace) -> None:
        """
        Initialize the Analysis class.

        Args:
        - args (argparse.Namespace): parsed command-line arguments
        """
        self.name = args.name
        self.outdir = os.path.abspath(os.path.join(args.outdir, args.name))

    def run(self) -> None:
        """
        Run the analysis.
        """
        ### import lib
        from dnbc4tools.tools.utils import str_mkdir,judgeFilexits, \
            get_formatted_time, setup_logging
        from dnbc4tools.tools.io import read_data_atac
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        import scanpy as sc
        import pandas as pd
        from contextlib import redirect_stdout
        from dnbc4tools.__init__ import __root_dir__
        from dnbc4tools.atac.src.scanpy_cluster import CellDataAnalyzer,get_cluster
        import warnings
        warnings.filterwarnings('ignore')

        ### run
        judgeFilexits(
            f'{self.outdir}/01.data/all.merge.fragments.tsv.gz',
            f'{self.outdir}/02.decon/filter_peak_matrix',
            f'{self.outdir}/02.decon/singlecell.csv',
            )
        
        str_mkdir(f'{self.outdir}/03.analysis')
        str_mkdir(f'{self.outdir}/log/.temp')

        os.environ[ 'MPLCONFIGDIR' ] = os.path.join(self.outdir, 'log', '.temp')
        os.environ[ 'NUMBA_CACHE_DIR' ] = os.path.join(self.outdir, 'log', '.temp')


        print(f'\n{get_formatted_time()}\n'
            f'Conducting dimensionality reduction and clustering.')
        sys.stdout.flush()

        adata = read_data_atac(
            f'{self.outdir}/02.decon/filter_peak_matrix/'
            )
        scanpy_object = CellDataAnalyzer(adata)
        scanpy_object._pp_qc()
        scanpy_object.adata.obs.to_csv(
            f"{self.outdir}/03.analysis/raw_qc.xls",index=True,sep='\t'
            )
        scanpy_object._pp_basicfilter()
        
        if len(scanpy_object.adata.obs.index) > 100:
            logger = setup_logging('analysis', self.outdir)
            with open(logger.handlers[0].baseFilename, "a") as log_file:
                with redirect_stdout(log_file):
                    scanpy_object._pp_scanpy_doubletdetect()
        scanpy_object._pp_hvgs()
        scanpy_object._pp_reduce()
        scanpy_object._pp_cluster()
        sc.pl.umap(
                    scanpy_object.adata, 
                    color = ['leiden'], 
                    legend_loc = 'on data'
                    )
        plt.savefig(f"{self.outdir}/03.analysis/cluster.png")


        singlecell = pd.read_csv(f"{self.outdir}//02.decon/singlecell.csv",index_col=0)
        cluster_table = get_cluster(scanpy_object.adata, singlecell)
        cluster_table.to_csv(
            f"{self.outdir}/03.analysis/cluster.csv",
            index=True
            )
        # scanpy_object.adata.write(f"{self.outdir}/03.analysis/QC_Clutser.h5ad")

def analysis(args: argparse.Namespace) -> None:
    """
    Run the analysis.

    Args:
    - args (argparse.Namespace): parsed command-line arguments
    """
    Analysis(args).run()


def helpInfo_analysis(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    """
    Add command-line arguments for the analysis subcommand.

    Args:
    - parser (argparse.ArgumentParser): argparse parser

    Returns:
    - argparse.ArgumentParser: argparse parser
    """
    parser.add_argument(
        '--name', 
        metavar='NAME',
        help='Sample name.', 
        type=str,
        required=True
    )
    parser.add_argument(
        '--outdir', 
        metavar='PATH',
        help='Output directory, [default: current directory].', 
        default=os.getcwd()
    )

    return parser