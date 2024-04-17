import os,argparse
import sys
        
class Report:

    def __init__(self, args) :
        self.name = args.name
        self.species = args.species
        self.outdir = os.path.abspath(os.path.join(args.outdir, args.name))
        self.repseq = args.repseq

    def run(self):
        from dnbc4tools.vdj.src.generate_report import generate_report_summary
        from dnbc4tools.tools.utils import str_mkdir, judgeFilexits, get_formatted_time
        from dnbc4tools.__init__ import __root_dir__

        judgeFilexits(
            f'{self.outdir}/01.data/sequencing_report.csv',
            f'{self.outdir}/01.data/tcrbcr_bc.fa',
            f'{self.outdir}/02.assembly/tcrbcr_assembled_reads.fa',
            f'{self.outdir}/01.data/cell.sequencing.tsv',
            f'{self.outdir}/03.filter/all_contig_annotations.csv',
            f'{self.outdir}/03.filter/filtered_contig_annotations.csv',
            f'{self.outdir}/02.assembly/tcrbcr_annot.fa',
            f'{self.outdir}/03.filter/clonotypes.csv',
            )
        str_mkdir('%s/04.report/div'%self.outdir)
        str_mkdir('%s/04.report/table'%self.outdir)
        str_mkdir('%s/log'%self.outdir)

        print(f'\n{get_formatted_time()}\n'
            f'Generate report.')
        
        sys.stdout.flush()

        generate_report_summary(
            self.name,
            self.species,
            self.outdir,
            self.repseq,
            f'{__root_dir__}/config/template/',
        )

        

def report(args):
    """
    Run the pipeline using the specified arguments.
    """
    Report(args).run()

def helpInfo_report(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    """
    Define the command line arguments for the pipeline.
    """
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
        '--species',
        type=str, 
        metavar='STR',
        help='Species name'
    )
    parser.add_argument(
        '--name',
        type=str, 
        metavar='STR',
        help='Sample ID'
    )
    return parser