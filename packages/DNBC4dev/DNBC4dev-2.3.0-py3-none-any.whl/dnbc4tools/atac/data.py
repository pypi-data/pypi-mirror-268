import os,argparse
import sys
from typing import List


def filter_chrM(peak, new_peak, chrM):
    filtered_peaks = []
    with open(peak, 'r') as input_file:
        for line in input_file:
            if not line.startswith('#'):
                fields = line.strip().split('\t')
                if fields[0] != chrM:
                    filtered_peaks.append('\t'.join(fields[:4]))

    with open(new_peak, 'w') as output_file:
        output_file.write('\n'.join(filtered_peaks))

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
        self.genome = args.genome
        self.refindex = args.index
        self.chrmt = args.chrmt
        self.genomesize = args.genomesize
        self.chromsizes = args.chromsizes
        self.filter_jaccard = args.minjaccard
        self.filter_frags = args.minmerge
        self.bcerror = args.bcerror
        self.skip_barcode_check = args.skip_barcode_check
        self.bam = args.bam

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
            type = 'atac',
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
            rm_temp, get_formatted_time, bgzip_index, bin_path, logging_call, create_index
        from dnbc4tools.atac.src.calculate_jaccardindex import calculate_jaccard_index_cbs, barcard_otsu_filter, generate_merge_frags
        from dnbc4tools.tools.combineBeads import similarity_droplet_file,barcodeTranslatefile
        from dnbc4tools.__init__ import __root_dir__

        # Check if the input files and genomeDir exists
        judgeFilexits(
            self.fastq1,
            self.fastq2,
            self.genome
            )
        str_mkdir(f"{self.outdir}/01.data")
        str_mkdir('%s/log/.temp'%self.outdir)
        # bin_command = bin_path()
        barcodeconfig = self.seqStructure()
        
        print(f'\n{get_formatted_time()}\n'
            f'Conduct quality control for raw data, perform alignment.')
        
        sys.stdout.flush()

        # Run Chromap to perform barcode processing and alignment
        chromap_cmd: List[str] = [
            f"{__root_dir__}/software/chromap ",
            f"--preset atac ",
            f"--bc-error-threshold {self.bcerror} ",
            f"--trim-adapters ",
            f"-x {self.refindex} ",
            f"-r {self.genome} ",
            f"-1 {self.fastq1} ",
            f"-2 {self.fastq2} ",
            #f"-o {self.outdir}/01.data/alignment.fragments.tsv ",
            f"--barcode {self.fastq1} ",
            f"--barcode-whitelist {f'{__root_dir__}/config/atac/whitelist_atac.txt.gz'} ",
            f"--read-format {barcodeconfig} ",
            f"-t {self.threads} "
            #f"2> {self.outdir}/01.data/alignment_report.tsv"
        ]

        if self.bam:
            chromap_cmd += [f"-o {self.outdir}/01.data/alignment.fragments.sam --SAM "]
        else:
            chromap_cmd += [f"-o {self.outdir}/01.data/alignment.fragments.tsv "]
        
        if self.skip_barcode_check:
            chromap_cmd += ['--skip-barcode-check']
        chromap_cmd += [f'2> {self.outdir}/01.data/alignment.report.tsv']
        chromap_cmd = ' '.join(chromap_cmd)
        
        ### chromap generate aligment.fragments.tsv
        logging_call(chromap_cmd,'data',self.outdir)

        ### generate bam file
        if self.bam:
            sambam_sort_cmd = [
                f"{__root_dir__}/software/samtools",
                "view",
                f"--threads {self.threads}",
                "-bS",
                f"{self.outdir}/01.data/alignment.fragments.sam",
                "|",
                f"{__root_dir__}/software/samtools",
                "sort",
                f"--threads {self.threads}",
                f"-o {self.outdir}/01.data/alignment.fragments.sorted.bam -"
            ]
            sambam_sort_cmd = ' '.join(sambam_sort_cmd)

            pisaBamFra_cmd: List[str] = [
                f"{__root_dir__}/software/PISA ",
                f"bam2frag",
                f"-cb CB -isize 2000 ",
                f"-@ {self.threads} ",
                f"-o {self.outdir}/01.data/alignment.fragments.tsv.gz ",
                f"{self.outdir}/01.data/alignment.fragments.sorted.bam"  
            ]
            pisaBamFra_cmd = ' '.join(pisaBamFra_cmd)

            logging_call(sambam_sort_cmd,'data',self.outdir)
            create_index(self.threads,f'{self.outdir}/01.data/alignment.fragments.sorted.bam',self.outdir)
            logging_call(pisaBamFra_cmd,'data',self.outdir)
            
            rm_temp(
            f'{self.outdir}/01.data/alignment.fragments.sam',
            )
        else:
            bgzip_index(f'{self.outdir}/01.data/alignment.fragments.tsv',str(self.threads))
        
        ### filter min frags, using jaccard index merge
        char_set = {row.split('\t')[0] for row in open(self.chromsizes, 'r').readlines()}
        
        ### jaccard index for cell barocde

        print(f'\n{get_formatted_time()}\n'
            f'Calculating bead similarity and merging beads within the same droplet.')
        calculate_jaccard_index_cbs(
            fragments_tsv_filename = f'{self.outdir}/01.data/alignment.fragments.tsv.gz' ,
            output = f'{self.outdir}/01.data',
            min_frags_per_CB = self.filter_frags,
            chromosomes = char_set,
            logdir=f'{self.outdir}'
        )
        
        ### otsu filter cb merge
        barcard_otsu_filter(
            f'{self.outdir}/01.data/cb.jaccard.index.tsv',
            f'{self.outdir}/01.data',
            self.filter_jaccard,
            logdir=f'{self.outdir}'
        )
        ### merge beads filter and trans beads all

        similarity_droplet_file('%s/01.data/barcard.overlap.filtered.tsv'%self.outdir,
                                '%s/01.data/beads.min.frags.tsv'%self.outdir,
                                '%s/01.data/combined.list.tsv'%self.outdir,
                                0.02,9,
                                logdir=f'{self.outdir}')
        
        barcodeTranslatefile('%s/01.data/combined.list.tsv'%self.outdir,
                         '%s/01.data/alignment.count.tsv'%self.outdir, 
                         '%s/01.data/barcodeTranslate.txt'%self.outdir, 
                         '%s/01.data/cell.id'%self.outdir, 
                         logdir=f'{self.outdir}'
                         )
        
        ### generate merge fragments
        generate_merge_frags(
            f'{self.outdir}/01.data/alignment.fragments.tsv.gz',
            f'{self.outdir}/01.data/barcodeTranslate.txt',
            f'{self.outdir}/01.data/combined.list.tsv',
            f'{self.outdir}/01.data',
            chromosomes = char_set,
            logdir=f'{self.outdir}'
            )

        bgzip_index(f'{self.outdir}/01.data/all.merge.fragments.tsv',str(self.threads))
        bgzip_index(f'{self.outdir}/01.data/filter.merge.fragments.tsv',str(self.threads))

        ### call peak
        print(f'\n{get_formatted_time()}\n'
            f'Analyze fragments for peak calling.')
        str_mkdir(f"{self.outdir}/01.data/callpeak")
        macs2_cmd: List[str] = [
            f"{bin_path()}/macs2 ",
            f"callpeak ",
            f"--treatment {self.outdir}/01.data/filter.merge.fragments.tsv.gz ",
            f"--name {self.name} ",
            f"-B ",
            f"--outdir {self.outdir}/01.data/callpeak ",
            f"--format BED ",
            f"--gsize {self.genomesize} ",
            f"-q 0.01 ",
            f"--nomodel ",
            #f"--call-summits --keep-dup all ",
            f"--shift -75 --extsize 150 ",
            f"--tempdir {self.outdir}/log/.temp/ "
        ]
        macs2_cmd = ' '.join(macs2_cmd)
        logging_call(macs2_cmd, 'data', self.outdir)

        ### raw peak matrix
        filter_chrM(
            f'{self.outdir}/01.data/callpeak/{self.name}_peaks.narrowPeak', 
            f'{self.outdir}/01.data/filtered_peaks.bed', 
            self.chrmt
            )
        
        rm_temp(
            f'{self.outdir}/01.data/filter.merge.fragments.tsv.gz',
            f'{self.outdir}/01.data/filter.merge.fragments.tsv.gz.tbi',
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
        '--genome',
        type=str, 
        metavar='PATH',
        help='Path of reference genome.',
    )
    parser.add_argument(
        '--index',
        type=str, 
        metavar='PATH',
        help='Path to the directory containing reference database.',
    )
    parser.add_argument(
        '--chrmt',
        type=str, 
        metavar='STR',
        help='Mitochondrial name in genome .',
    )
    parser.add_argument(
        '--genomesize',
        help='The genome size required when macs2 calls peak',
    )
    parser.add_argument(
        '--chromsizes',
        help='The length of chromosomes',
    )
    parser.add_argument(
        '--minjaccard',
        type=float,
        metavar='FLOAT',
        default=0.02,
        help='The lowest jaccard index value when merging cell barcode. [default: 0.02].'
    )
    parser.add_argument(
        '--minmerge',
        type=int,
        metavar='PATH',
        default=1000,
        help='Minimum number of fragments needed per CB. [default: 1000].'
    )
    parser.add_argument(
        '--bcerror',
        type=int,
        metavar='INT',
        default=1,
        help='Set the error tolerance for cell barcodes.'
    )
    parser.add_argument(
        '--skip-barcode-check',
        action='store_true',
        help=argparse.SUPPRESS
        )
    parser.add_argument(
        '--bam',
        action='store_true',
        help='The alignment process generates BAM format files, but this significantly prolongs the analysis time.'
        )
    return parser