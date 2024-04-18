import os
import sys
from typing import List, Dict


class Decon:
    def __init__(self, args: Dict):
        """
        Constructor for Decon class.

        Args:
        - args (Dict): A dictionary containing the arguments to configure the Decon object.
        """
        self.name: str = args.name
        self.outdir: str = os.path.abspath(os.path.join(args.outdir, args.name))
        self.threads: str = args.threads
        self.chrmt: str = args.chrmt
        self.tssregion: str = args.tssregion
        self.blacklist: str = args.blacklist
        self.forcecells: int = args.forcecells
        self.min_frags_per_cb: int = args.min_frags_per_cb
        self.min_tss_per_cb: float = args.min_tss_per_cb

    def run(self) -> None:
        """
        Run the Decon algorithm.
        """
        ### import lib
        import numpy as np
        import polars as pl
        from dnbc4tools.tools.utils import str_mkdir,judgeFilexits,\
            logging_call, get_formatted_time
        from dnbc4tools.__init__ import __root_dir__
        from dnbc4tools.tools.cell_calling import cell_calling
        from dnbc4tools.tools.cal_saturation import sub_sample_fragments_atac
        from dnbc4tools.atac.src.filter_qc import generateSummaryCount,pyranger_overlap,get_tss_matrix,tss_enrichment
        from dnbc4tools.tools.plot_draw import enrichment_plot, peak_cellcall_plot, target_fragment_plot, merge_graph, violinatac_plot
        import warnings
        warnings.filterwarnings('ignore')
        MAXCELLNUM = 20000

        # Check if genomeDir exists
        judgeFilexits(
                f'{self.outdir}/01.data/all.merge.fragments.tsv.gz',
                f'{self.outdir}/01.data/cell.id',
                f"{self.outdir}/01.data/filtered_peaks.bed",
                )
        
        # Create output and log directories
        str_mkdir(f"{self.outdir}/02.decon/raw_peak_matrix")
        str_mkdir(f"{self.outdir}/02.decon/images")
        str_mkdir(f"{self.outdir}/02.decon/filter_peak_matrix")
        str_mkdir(f'{self.outdir}/log')
        
        # Change to the output directory
        print(f'\n{get_formatted_time()}\n'
            f'Generating the raw peaks matrix.')
        
        sys.stdout.flush()

        # Construct the Decon command with the provided parameters
        pisacount2_cmd: List[str] = [
            f"{__root_dir__}/software/PISA ",
            f"count2 ",
            f"-bed {self.outdir}/01.data/filtered_peaks.bed ",
            f"-list {self.outdir}/01.data/cell.id ",
            f"-outdir {self.outdir}/02.decon/raw_peak_matrix",
            f"-t {self.threads} ",
            f"{self.outdir}/01.data/all.merge.fragments.tsv.gz"
        ]
        pisacount2_cmd = ' '.join(pisacount2_cmd)
        logging_call(pisacount2_cmd, 'decon', self.outdir)

        ### cell calling by fragments overlapping peaks
        if self.forcecells:
            cell_bc, counts_num = cell_calling(
                f"{self.outdir}/02.decon/raw_peak_matrix/", 
                force_cell_num = self.forcecells, 
                type = "atac",
                logdir=f'{self.outdir}')
            
            singleCellSum = generateSummaryCount(
                f"{self.outdir}/02.decon/raw_peak_matrix/",
                f"{self.outdir}/01.data/all.merge.fragments.tsv.gz",
                f"{self.outdir}/01.data/barcodeTranslate.txt",
                self.chrmt,
                self.tssregion,
                self.blacklist,
                0,
                cell_bc,
                self.forcecells,
                logdir=f'{self.outdir}'
            )

        else:
            ### using high min_umi to only get higher umi solution
            try:
                cell_bc, counts_num = cell_calling(
                    f"{self.outdir}/02.decon/raw_peak_matrix/", 
                    expected_cell_num=3000,
                    method="emptydrops",
                    min_umi=5000000,
                    type="atac",
                    logdir=f'{self.outdir}'
                )
            except Exception as e:
                print(f"Warning: {e}")
                print("Switching to method 'barcoderanks'")
                cell_bc, counts_num = cell_calling(
                    f"{self.outdir}/02.decon/raw_peak_matrix/", 
                    expected_cell_num=3000,
                    method="barcoderanks",
                    min_umi=5000000,
                    type="atac",
                    logdir=f'{self.outdir}'
                )
        
            singleCellSum = generateSummaryCount(
                f"{self.outdir}/02.decon/raw_peak_matrix/",
                f"{self.outdir}/01.data/all.merge.fragments.tsv.gz",
                f"{self.outdir}/01.data/barcodeTranslate.txt",
                self.chrmt,
                self.tssregion,
                self.blacklist,
                self.min_frags_per_cb,
                cell_bc,
                MAXCELLNUM,
                self.min_tss_per_cb,
                logdir=f'{self.outdir}'
            )

        singleCellSum.write_csv(
            f"{self.outdir}/02.decon/singlecell.csv",
            separator=",",
            include_header=True
        )

        ### plot peak knee, peak fragments, tss fragments
        singlecellsummary = singleCellSum.to_pandas()
        peak_cellcall_plot(singlecellsummary, f"{self.outdir}/02.decon/images")
        target_fragment_plot(singlecellsummary, f"{self.outdir}/02.decon/images", selecttype="TSS_region_fragments")
        target_fragment_plot(singlecellsummary, f"{self.outdir}/02.decon/images", selecttype="peak_region_fragments")
        violinatac_plot(singlecellsummary, f"{self.outdir}/02.decon/images")

        ### generate cell calling cellID
        selected_rows = singleCellSum.filter(singleCellSum['is_cell_barcode'] == 1)
        selected_rows[['Cell']].sort('Cell').write_csv(
            f"{self.outdir}/02.decon/beads_barcodes.txt", 
            separator='\t', 
            include_header=False
            )
        
        ### filter peak matrix
        print(f'\n{get_formatted_time()}\n'
            f'Generating the filter peaks matrix.')
        pisacount2filter_cmd: List[str] = [
            f"{__root_dir__}/software/PISA ",
            f"count2 ",
            f"-bed {self.outdir}/01.data/filtered_peaks.bed ",
            f"-list {self.outdir}/02.decon/beads_barcodes.txt ",
            f"-outdir {self.outdir}/02.decon/filter_peak_matrix ",
            f"-t {self.threads} ",
            f"{self.outdir}/01.data/all.merge.fragments.tsv.gz "  
        ]

        pisacount2filter_cmd = ' '.join(pisacount2filter_cmd)
        logging_call(pisacount2filter_cmd, 'decon', self.outdir)

        ### tss enrichment plot
        cell_filter_bc = selected_rows['Cell'].to_numpy().tolist()
        overlap_with_TSS,overlap_with_TSS_dropdup_pl = pyranger_overlap(
            f"{self.outdir}/01.data/all.merge.fragments.tsv.gz",
            self.tssregion,
            1000,
            cell_bc=cell_filter_bc
            )
        tss_matrix = get_tss_matrix(overlap_with_TSS, 1000)
        TSS_counts_div , TSS_enrich = tss_enrichment(tss_matrix, 50, 100, 1000, 2, 0.2)
        enrichment_plot(TSS_counts_div, 1000, f"{self.outdir}/02.decon/images")
        np.savetxt(f"{self.outdir}/02.decon/tss.flankwindow.csv", TSS_counts_div, fmt='%.08f')

        ### plot dup
        merge_graph(
            f"{self.outdir}/02.decon/beads_barcodes.txt", 
            f"{self.outdir}/02.decon/images"
            )

        sub_sample_fragments_atac(
            f"{self.outdir}/01.data/all.merge.fragments.tsv.gz", 
            f"{self.outdir}/02.decon/beads_barcodes.txt", 
            f"{self.outdir}/02.decon/",
            logdir=f'{self.outdir}'
        )

        # bgzip_index(f'{self.outdir}/02.decon/filter.fragments.tsv',str(self.threads))




def decon(args):
    Decon(args).run()

def helpInfo_decon(parser):
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
        help='Output diretory, [default: current directory].', 
        default=os.getcwd()
        )
    parser.add_argument(
        '--forcecells', 
        type=int,
        metavar='INT',
        help='Top N number of cells to be thresholded.'
        )
    parser.add_argument(
        '--threads',
        type=str, 
        metavar='INT',
        default=4,
        help='Number of threads used for the analysis, [default: 4].'
        )
    parser.add_argument(
        '--chrmt',
        type=str, 
        metavar='STR',
        help='Mitochondrial name in genome .',
    )
    parser.add_argument(
        '--tssregion',
        type=str, 
        metavar='PATH',
        help='Loaded transcript start site file.',
    )
    parser.add_argument(
        '--blacklist',
        type=str, 
        metavar='PATH',
        help='User provided blacklist file.',
    )
    parser.add_argument(
        '--min_frags_per_cb',
        type=int,
        default=1000,
        help='Minimum number of fragments needed per CB. [default: 1000].'
    )
    parser.add_argument(
        '--min_tss_per_cb', 
        type=float,
        metavar='FLOAT',
        help='The lowest value of the proportion of fragments located in the tss area. [default: 0].'
        )
    return parser