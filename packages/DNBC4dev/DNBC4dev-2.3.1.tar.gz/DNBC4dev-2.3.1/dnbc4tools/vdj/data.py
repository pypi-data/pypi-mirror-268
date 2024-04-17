import os,argparse
import sys
from typing import List
        
class Data:
    """
    Initializes a Data object with the provided arguments.

    Attributes:
        name (str): Sample name.
        fastq1 (str): Path to the R1 fastq file.
        fastq2 (str): Path to the R2 fastq file.
        threads (int): Number of threads to use.
        darkreaction (str): Type of dark reaction.
        customize (str): Custom reaction format.
        outdir (str): Output directory path.
        genomeDir (str): Path to the genome directory.
        bcerror (float): Barcode error threshold.
    """

    def __init__(self, args) :
        self.name = args.name
        self.fastq1 = args.fastq1 
        self.fastq2 = args.fastq2
        self.threads = args.threads
        self.darkreaction = args.darkreaction
        self.customize = args.customize
        self.outdir = os.path.abspath(os.path.join(args.outdir, args.name))
        self.coordinate = args.coordinate
        self.beadstrans = args.beadstrans
        self.splitreads = args.splitreads
        self.pairedreads = args.pairedreads

    def seqStructure(self) -> str:
        """
        Determines the sequence structure based on the input fastq files and the provided arguments.

        Returns:
            str: The sequence structure string.
        """
        ### import lib
        from dnbc4tools.tools.chemistydark import designated_chem_dark
        ### run
        return designated_chem_dark(
            type = 'vdj',
            fastqR1list = self.fastq1, 
            fastqR2list = self.fastq2, 
            customize = self.customize, 
            darkreaction = self.darkreaction,
            chemistry = "auto"
            )

    def run(self):
        """
        Runs Chromap to perform barcode processing and alignment.
        """
        ### import lib
        from dnbc4tools.tools.utils import str_mkdir, judgeFilexits, \
            logging_call, get_formatted_time, bin_path, rm_temp
        from dnbc4tools.__init__ import __root_dir__
        from dnbc4tools.vdj.src.cut_fastq_cbub import extract_crur_fastq, cell_summary
        import pandas as pd

        # Check if the input files and genomeDir exists
        judgeFilexits(self.fastq1,self.fastq2)
        str_mkdir('%s/01.data'%self.outdir)
        str_mkdir('%s/log'%self.outdir)

        # Get the absolute path of the genomeDir and the read_format from the Data class
        #genomeDir = os.path.abspath(self.genomeDir)
        
        
        if self.customize:
            barcodeconfig = self.seqStructure()
        elif self.pairedreads:
            barcodeconfig = self.seqStructure()[0]
        else:
            barcodeconfig = self.seqStructure()[1]

        print(f'\n{get_formatted_time()}\n'
            f'Barcode Processing, Alignment.')
        sys.stdout.flush()

        # combine list file 
        combine_list = pd.read_csv(self.beadstrans)
        combine_list = combine_list[["CELL","BARCODE"]]
        combine_list['BARCODE'] = combine_list['BARCODE'].str.split(';')
        combine_list = combine_list.explode('BARCODE').reset_index(drop=True)
        combine_list.to_csv(f'{self.outdir}/01.data/barcodeTranslate.txt',sep='\t',header=None,index=None)
        combine_list['BARCODE'].to_csv(f'{self.outdir}/01.data/barcodeWhitelist.list',sep='\t',header=None,index=None)

        # Run Chromap to perform barcode processing and alignment
        PISAparse_cmd: List[str] = [
            f"{__root_dir__}/software/PISA parse ",
            f"-q 20 ",
            f"-t {self.threads} ",
            f"-config {barcodeconfig} ",
            f"-report {self.outdir}/01.data/sequencing_report.csv "
        ]

        vdjextractor_cmd: List[str] = [
            f"{__root_dir__}/software/TRUST4/fastq-extractor ",
            f"-t {self.threads} ",
            f"-f {self.coordinate} ",
            f"-o {self.outdir}/01.data/tcrbcr ",
            f"--barcode {self.outdir}/01.data/cb_cut.fastq ",
            f"--UMI {self.outdir}/01.data/ub_cut.fastq ",
            f"--barcodeTranslate {self.outdir}/01.data/barcodeTranslate.txt ",
            f"--barcodeWhitelist {self.outdir}/01.data/barcodeWhitelist.list ",
        ]

        cutadapt_cmd: List[str] = [
            f"{bin_path()}/cutadapt ",
            f"-j {self.threads} ",
            "--report minimal ",
        ]
        
        if self.pairedreads:
            PISAparse_cmd += [
                f'-1 {self.outdir}/01.data/clean_R1.fastq -2 {self.outdir}/01.data/clean_R2.fastq {self.fastq1} {self.fastq2}'
                ]
            PISAparse_cmd = ' '.join(PISAparse_cmd)
            logging_call(PISAparse_cmd,'data',self.outdir)

            extract_crur_fastq.extract_cr_ur_fqpaired_pysam(
                f"{self.outdir}/01.data", 
                f"{self.outdir}/01.data", 
                self.splitreads
                )
            
            vdjextractor_cmd += [
                f'-1 {self.outdir}/01.data/fq1_cut.fastq -2 {self.outdir}/01.data/fq2_cut.fastq'
            ]
            vdjextractor_cmd = ' '.join(vdjextractor_cmd)
            logging_call(vdjextractor_cmd,'data',self.outdir)

            # cutadapt_cmd += [
            #     "-G AAGCAGTGGTATCAACGCAGAGT{20} ",
            #     f'-o {self.outdir}/01.data/tcrbcr_cut_1.fq ',
            #     f'-p {self.outdir}/01.data/tcrbcr_cut_2.fq ',
            #     f'{self.outdir}/01.data/tcrbcr_1.fq ',
            #     f'{self.outdir}/01.data/tcrbcr_2.fq '
            # ]
            # cutadapt_cmd = ' '.join(cutadapt_cmd)
            # logging_call(cutadapt_cmd,'data',self.outdir)

            rm_temp(
                f"{self.outdir}/01.data/clean_R1.fastq",
                f"{self.outdir}/01.data/clean_R2.fastq",
                f"{self.outdir}/01.data/fq1_cut.fastq",
                f"{self.outdir}/01.data/fq2_cut.fastq",
                f"{self.outdir}/01.data/ub_cut.fastq",
                f"{self.outdir}/01.data/cb_cut.fastq",
                # f'{self.outdir}/01.data/tcrbcr_1.fq',
                # f'{self.outdir}/01.data/tcrbcr_2.fq'
            )

        else:
            PISAparse_cmd += [
                f'-1 {self.outdir}/01.data/clean.fastq {self.fastq1} {self.fastq2}'
                ]
            PISAparse_cmd = ' '.join(PISAparse_cmd)
            logging_call(PISAparse_cmd,'data',self.outdir)
            extract_crur_fastq.extract_cr_ur_fqsingle_pysam(
                f"{self.outdir}/01.data", 
                f"{self.outdir}/01.data", 
                self.splitreads
                 )
            vdjextractor_cmd += [
                f'-u {self.outdir}/01.data/fq_cut.fastq '
            ]
            vdjextractor_cmd = ' '.join(vdjextractor_cmd)
            logging_call(vdjextractor_cmd,'data',self.outdir)

            # cutadapt_cmd += [
            #     "-g AAGCAGTGGTATCAACGCAGAGT{20} ",
            #     f'-o {self.outdir}/01.data/tcrbcr_cut_1.fq ',
            #     f'{self.outdir}/01.data/tcrbcr.fq ',
            # ]
            # cutadapt_cmd = ' '.join(cutadapt_cmd)
            # logging_call(cutadapt_cmd,'data',self.outdir)

            rm_temp(
                f"{self.outdir}/01.data/clean.fastq",
                f"{self.outdir}/01.data/fq_cut.fastq",
                f"{self.outdir}/01.data/ub_cut.fastq",
                f"{self.outdir}/01.data/cb_cut.fastq",
                # f'{self.outdir}/01.data/tcrbcr.fq'
            )

        cell_summary(
            f"{self.outdir}/01.data/tcrbcr_bc.fa",
            f"{self.outdir}/01.data/tcrbcr_umi.fa",
            f"{self.outdir}/01.data/cell.sequencing.tsv", 
        )

def data(args):
    """
    Run the pipeline using the specified arguments.
    """
    Data(args).run()

def helpInfo_data(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
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
        '--fastq1', 
        metavar='FASTQ',
        help='The input R1 fastq files.', 
        required=True
    )
    parser.add_argument(
        '--fastq2', 
        metavar='FASTQ',
        help='The input R2 fastq files.', 
        required=True
    )
    parser.add_argument(
        '--darkreaction',
        metavar='STR',
        help='Sequencing dark cycles. Automatic detection is recommended, [default: auto].', 
        default='auto'
    )
    parser.add_argument(
        '--customize',
        metavar='STR',
        help='Customize read structure.'
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
        '--beadstrans',
        type=str, 
        metavar='PATH',
        help='Beads converted into cells file in scRNA analysis results'
    )
    parser.add_argument(
        '--pairedreads',
        action='store_true',
        help='Assemble using paired-end data.'
    )
    parser.add_argument(
        '--splitreads',
        metavar='INT',
        default=None,
        help='Extracting a subset of reads for analysis.'
    )

    return parser