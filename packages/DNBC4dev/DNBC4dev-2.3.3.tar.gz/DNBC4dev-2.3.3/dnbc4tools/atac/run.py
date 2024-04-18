import os
import argparse
import time
from typing import List, Optional

class Runpipe:
    """
    Initialize the Runpipe class by extracting various parameters from command line arguments.
    
    Args:
        args (argparse.Namespace): Parsed command line arguments containing the following fields:
            name (str): User-defined sample identifier.
            fastq1 (str): Path to the R1 fastq file(s).
            fastq2 (str): Path to the R2 fastq file(s).
            genomeDir (str): Absolute path to the directory containing genome files.
            outdir (str): Output directory; defaults to the current working directory.
            threads (int): Number of threads to use for analysis; defaults to 4.
            darkreaction (Optional[str]): Sequencing dark cycles; 'auto' for automatic detection (default).
            customize (Optional[str]): Custom read structure definition (optional).
            forcecells (Optional[int]): Force the pipeline to use a specified number of cells (optional).
            frags_cutoff (int): Minimum unique fragment count threshold for filtering cells; defaults to 1000.
            tss_cutoff (float): Minimum TSS proportion threshold for filtering cells; defaults to 0.
            jaccard_cutoff (float): Jaccard similarity cutoff for an unspecified purpose (suppressed).
            merge_cutoff (int): Minimum fragment count for merging beads; defaults to 1000.
            skip_barcode_check (bool): Flag to skip barcode check (suppressed).
            process (str): Comma-separated list of analysis steps to execute; defaults to "data,decon,analysis,report".
    """
    def __init__(self, args):
        self.name: str = args.name
        self.fastq1: str = args.fastq1 
        self.fastq2: str = args.fastq2
        self.threads: int = args.threads
        self.darkreaction: Optional[str] = args.darkreaction
        self.customize: Optional[str] = args.customize
        self.outdir: str = os.path.abspath(args.outdir)
        self.genomeDir: str = os.path.abspath(args.genomeDir)
        self.forcecells: int = args.forcecells
        self.filter_frags: int = args.frags_cutoff
        self.filter_tss: float = args.tss_cutoff
        self.filter_jaccard: float = args.jaccard_cutoff
        self.merge_frags: int = args.merge_cutoff
        self.skip_barcode_check = args.skip_barcode_check
        self.process: List[str] = args.process.split(",")
        self.bam = args.bam
        
    def runpipe(self) -> None:
        """
        Execute the complete data processing and analysis pipeline for single-cell ATAC-seq data.

        The pipeline consists of four main stages:
        1. Data preprocessing (`dnbc4atac data`)
        2. Deconvolution (`dnbc4atac decon`)
        3. Analysis (`dnbc4atac analysis`)
        4. Report generation (`dnbc4atac report`)

        Each stage is conditionally executed based on the `process` argument provided during initialization.
        Progress and elapsed time for the entire pipeline are reported upon completion.
        """

        # Import necessary libraries and utility functions
        from dnbc4tools.tools.utils import str_mkdir, judgeFilexits, start_print_cmd, read_json, bin_path
        from dnbc4tools.__init__ import __root_dir__

        # Ensure prerequisite files exist and paths are absolute
        judgeFilexits(self.fastq1, self.fastq2, self.genomeDir)

        # Load reference genome configuration
        genomeDir = os.path.abspath(self.genomeDir)
        indexConfig = read_json('%s/ref.json'%genomeDir)
        refindex = indexConfig['index']
        genome = indexConfig['genome']
        chrmt: str = indexConfig['chrmt']
        chromsizes: str = indexConfig['chromeSize']
        genomesize: str = indexConfig['genomesize']
        tssregion: str = indexConfig['tss']
        species: str = indexConfig['species']
        blacklist: str = indexConfig['blacklist']

        # Construct data preprocessing command
        data_cmd: List[str] = [
            f"{bin_path()}/dnbc4tools atac data",
            f"--fastq1 {self.fastq1} ",
            f"--fastq2 {self.fastq2} ",
            f"--threads {self.threads} ",
            f"--name {self.name} ",
            f"--darkreaction {self.darkreaction} ",
            f"--outdir {self.outdir} ",
            f"--genome {genome} ",
            f"--index {refindex} ",
            f"--chrmt {chrmt}",
            f"--genomesize {genomesize} ",
            f"--chromsizes {chromsizes}",
            f"--bcerror 1 ",
            ]
        
        if self.customize:
            data_cmd += [
                f'--customize {self.customize}'
                ]
        if self.skip_barcode_check:
            data_cmd += [
                f'--skip-barcode-check'
            ]
        if self.merge_frags:
            data_cmd += [
                f'--minmerge {self.merge_frags}'
            ]
        if self.filter_jaccard:
            data_cmd += [
                f'--minjaccard {self.filter_jaccard}'
            ]

        if self.bam:
            data_cmd += [
                f'--bam'
            ]
            
        data_cmd = ' '.join(data_cmd)

        # Construct deconvolution command
        decon_cmd: List[str] = [
            f"{bin_path()}/dnbc4tools atac decon",
            f"--name {self.name} ",
            f"--threads {self.threads}",
            f"--outdir {self.outdir}",
            f"--chrmt {chrmt}",
            f"--tss {tssregion}",
            f"--bl {blacklist}"
        ]
        if self.filter_frags:
            decon_cmd += [
                f'--min_frags_per_cb {self.filter_frags}'
                ]
        if self.filter_tss:
            decon_cmd += [
                f'--min_tss_per_cb {self.filter_tss}'
                ]
        if self.forcecells:
            decon_cmd += [
                f'--forcecells {self.forcecells}'
                ]
        decon_cmd = ' '.join(decon_cmd)

        # Construct analysis command
        analysis_cmd: List[str]  = [
            f"{bin_path()}/dnbc4tools atac analysis",
            f"--name {self.name}",
            f"--outdir {self.outdir}"
            ]
        analysis_cmd = ' '.join(analysis_cmd)
        
        # Construct report generation command
        report_cmd: List[str] = [
            f"{bin_path()}/dnbc4tools atac report",
            f"--name {self.name}",
            f"--outdir {self.outdir}",
            f"--species {species}"
        ]
        report_cmd = ' '.join(report_cmd)

        # Assemble the list of commands to execute based on requested stages
        # Append corresponding commands to cmdlist based on keywords present in `self.process`
        allowed_processes = {'data', 'decon', 'analysis', 'report'}
        if not all(process in allowed_processes for process in self.process):
            raise ValueError("Invalid process name(s) detected. Allowed names are: data, decon, analysis, report.")

        cmdlist: List[str] = []
        if 'data' in self.process:
            cmdlist.append(data_cmd)
        if 'decon' in self.process:
            cmdlist.append(decon_cmd)
        if 'analysis' in self.process:
            cmdlist.append(analysis_cmd)
        if 'report' in self.process:
            cmdlist.append(report_cmd)

        # Start measuring execution time and create log directory
        start_time = time.time()
        str_mkdir('%s/log'%os.path.join(self.outdir,self.name))
        # Execute each pipeline command, logging the output
        for pipecmd in cmdlist:
            start_print_cmd(pipecmd,os.path.join(self.outdir,self.name))
        # Calculate elapsed time after all commands have been executed
        end_time = time.time()
        # Compute total analysis time in hours, minutes, and seconds
        analysis_time = end_time - start_time
        analysis_time_minutes, analysis_time_seconds = divmod(analysis_time, 60)
        analysis_time_hours, analysis_time_minutes = divmod(analysis_time_minutes, 60)
        # Print completion message and elapsed time
        print(f'\nAnalysis Finished')
        print(f'Elapsed Time: {int(analysis_time_hours)} hours {int(analysis_time_minutes)} minutes {int(analysis_time_seconds)} seconds')
            
def run(args):
    """
    Execute the main pipeline using the provided arguments.

    Parameters:
    args (Namespace): Parsed command-line arguments containing configuration settings.
    """
    Runpipe(args).runpipe()


def helpInfo_run(parser):
    """
    Add argument definitions and descriptions to the given argparse parser for the `run` subcommand.

    This function enriches the parser object with command-line options related to various aspects of
    the pipeline, such as sample identification, input/output file paths, genome database location,
    parallel processing parameters, quality control filters, and customizable analysis steps.

    Parameters:
    parser (ArgumentParser): The argparse parser instance to which the arguments will be added.
    """
    parser.add_argument(
        "--name",
        metavar="<SAMPLE_ID>",
        help="User-defined sample ID.",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--fastq1",
        metavar="<FQ1FILES>",
        help="The input R1 fastq files.",
        required=True,
    )
    parser.add_argument(
        "--fastq2",
        metavar="<FQ2FILES>",
        help="The input R2 fastq files.",
        required=True,
    )
    parser.add_argument(
        "--genomeDir",
        type=str,
        metavar="<DATABASE>",
        help="Path to the directory where genome files are stored.",
        required=True,
    )
    parser.add_argument(
        "--outdir",
        metavar="<OUTDIR>",
        help="Output directory. [default: current directory]",
        default=os.getcwd(),
    )
    parser.add_argument(
        "--threads",
        type=int,
        metavar="<CORENUM>",
        default=4,
        help="Number of threads used for analysis. [default: 4]",
    )
    parser.add_argument(
        "--darkreaction",
        metavar="<DARKCYCLE>",
        help="Sequencing dark cycles. Automatic detection is recommended. [default: auto]",
        default="auto",
    )
    parser.add_argument(
        "--customize",
        metavar="<STRUCTURE>",
        help="Customize read structure.",
    )
    parser.add_argument(
        "--forcecells",
        type=int,
        metavar="<CELLNUM>",
        help="Force pipeline to use this number of cells.",
    )
    parser.add_argument(
        "--frags_cutoff",
        type=int,
        metavar="<MIN_FRAGMENTS>",
        help="Filter cells with unique fragments number lower than this value. [default: 1000]",
        default=1000,
    )
    parser.add_argument(
        "--tss_cutoff",
        type=float,
        metavar="<MIN_TSS_RATIO>",
        help="Filter cells with tss proportion lower than this value. [default: 0]",
        default=0.0,
    )
    parser.add_argument(
        "--jaccard_cutoff",
        type=float,
        metavar="<MIN_JACCARD>",
        help=argparse.SUPPRESS,
    )
    parser.add_argument(
        "--merge_cutoff",
        type=int,
        metavar="<MIN_MERGE>",
        help="The lowest number of fragments when merging beads. [default: 1000]",
        default=1000,
    )
    parser.add_argument(
        "--skip-barcode-check",
        action="store_true",
        help=argparse.SUPPRESS,
    )
    parser.add_argument(
        "--process",
        metavar="<ANALYSIS_STEPS>",
        help=(
            "Custom analysis steps enable the skipping of unnecessary steps. "
            "[default: data,decon,analysis,report]"
        ),
        type=str,
        default="data,decon,analysis,report",
    )

    parser.add_argument(
        '--bam',
        action='store_true',
        help='The alignment process generates BAM format files, but this significantly prolongs the analysis time.'
        )
    return parser

    return parser