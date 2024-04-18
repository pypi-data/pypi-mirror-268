import os,argparse
import sys
        
class Assembly:
    def __init__(self, args) :
        self.name = args.name
        self.threads = args.threads
        self.outdir = os.path.abspath(os.path.join(args.outdir, args.name))
        self.coordinate = args.coordinate
        self.IMGT = args.IMGT
        self.pairedreads = args.pairedreads

    def run(self):
        """
        Runs Chromap to perform barcode processing and alignment.
        """
        ### import lib
        from dnbc4tools.vdj.src.split_assembly_anno import trust4_pipe, N_CHUNKS
        from dnbc4tools.tools.utils import str_mkdir, judgeFilexits, \
            get_formatted_time,  rm_temp
        from dnbc4tools.__init__ import __root_dir__

        # Check if the input files and genomeDir exists
        judgeFilexits(
            f'{self.outdir}/01.data/tcrbcr_umi.fa',
            f'{self.outdir}/01.data/tcrbcr_bc.fa',
            f'{self.outdir}/01.data/cell.sequencing.tsv',
            )
        str_mkdir('%s/02.assembly/temp'%self.outdir)
        str_mkdir('%s/log'%self.outdir)

        # Get the absolute path of the genomeDir and the read_format from the Data class
        #genomeDir = os.path.abspath(self.genomeDir)
        
        print(f'\n{get_formatted_time()}\n'
            f'VDJ assembly.')
        
        sys.stdout.flush()


        # Run Chromap to perform barcode processing and alignment
        if self.pairedreads:
            trust4_pipe(
                f'{self.outdir}',
                self.threads,
                self.coordinate,
                self.IMGT,
                __root_dir__,
                N_CHUNKS,
                self.pairedreads,
                logdir=f'{self.outdir}'
            )
        else:
            trust4_pipe(
                f'{self.outdir}',
                self.threads,
                self.coordinate,
                self.IMGT,
                __root_dir__,
                N_CHUNKS,
                logdir=f'{self.outdir}'
            )

        rm_temp(
            f"{self.outdir}/02.assembly/temp",
        )

def assembly(args):
    """
    Run the pipeline using the specified arguments.
    """
    Assembly(args).run()

def helpInfo_assembly(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    """
    Define the command line arguments for the pipeline.
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
    parser.add_argument(
        '--threads',
        type=int, 
        metavar='INT',
        default=4,
        help='Number of threads used for the analysis, [default: 4].'
    )
    parser.add_argument(
        '--coordinate',
        type=str, 
        metavar='PATH',
        help='coordinate file in vdj database.',
        required=True
    )
    
    parser.add_argument(
        '--IMGT',
        type=str, 
        metavar='PATH',
        help='IMGT file in vdj database.',
        required=True
    )

    parser.add_argument(
        '--pairedreads',
        action='store_true',
        help='Assemble using paired-end data.'
    )

    return parser