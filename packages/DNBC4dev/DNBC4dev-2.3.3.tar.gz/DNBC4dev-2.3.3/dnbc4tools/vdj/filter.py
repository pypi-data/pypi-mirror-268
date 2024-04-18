import os,argparse
import sys
        
class Filter:
    def __init__(self, args) :
        self.outdir = os.path.abspath(os.path.join(args.outdir, args.name))
        self.repseq = args.repseq
        self.beadstrans = args.beadstrans

    def run(self):
        from dnbc4tools.vdj.src.filter_barcode import BarcodeProcess,cellCalling
        from dnbc4tools.tools.utils import str_mkdir, judgeFilexits, get_formatted_time
        from dnbc4tools.__init__ import __root_dir__
        import pandas as pd
        judgeFilexits(
            f'{self.outdir}/02.assembly/tcrbcr_barcode_report.tsv',
            f'{self.outdir}/02.assembly/tcrbcr_annot.fa',
            f'{self.outdir}/01.data/cell.sequencing.tsv',
            )
        str_mkdir('%s/03.filter'%self.outdir)
        str_mkdir('%s/log'%self.outdir)

        print(f'\n{get_formatted_time()}\n'
            f'Cell calling and generate clonotypes.')
        
        sys.stdout.flush()

        processor = BarcodeProcess(
            f'{self.outdir}/02.assembly/tcrbcr_barcode_report.tsv',
            f'{self.outdir}/02.assembly/tcrbcr_annot.fa', 
            self.repseq,
            f'{self.outdir}/03.filter',
            nofilter = None
            )
        processor.load_barcode_info()
        processor.load_annotation()
        processor.filter_barcodes()

        allanno = pd.read_csv(f'{self.outdir}/03.filter/all_contig_annotations.csv',)

        filterprocess = cellCalling(
            allanno,
            self.beadstrans,
            f'{self.outdir}/03.filter',
            f'{self.outdir}/02.assembly/tcrbcr_annot.fa', 
            f'{self.outdir}/01.data/cell.sequencing.tsv', 
            )
        filterprocess.cell_filter()

def filter(args):
    """
    Run the pipeline using the specified arguments.
    """
    Filter(args).run()

def helpInfo_filter(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    """
    Define the command line arguments for the pipeline.
    """
    parser.add_argument(
        '--name',
        type=str, 
        metavar='STR',
        help='Sample ID'
    )
    parser.add_argument(
        '--outdir', 
        metavar='PATH',
        help='Output directory, [default: current directory].', 
        default=os.getcwd()
    )
    parser.add_argument(
        '--repseq', 
        metavar='STR',
        help='the data is from tcr or bcr.',
        type=str,
        required=True,
        choices=['tcr', 'bcr']
    )
    parser.add_argument(
        '--beadstrans',
        type=str, 
        metavar='PATH',
        help='Beads converted into cells file in scRNA analysis results'
    )
    return parser