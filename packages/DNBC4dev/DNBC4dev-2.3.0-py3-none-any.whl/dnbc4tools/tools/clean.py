import os
import argparse
from typing import Dict, List, Optional
import glob
import shutil

from dnbc4tools.__init__ import __root_dir__


def sample_name(
    indir: str, 
    samplename: Optional[str] = None
    ) -> Dict[str, List[str]]:
    """Get a dictionary of sample names categorized by data type.

    Args:
        indir: Directory path where the samples are stored.
        samplename: Optional, a comma-separated string of sample names to search for.
    
    Returns:
        A dictionary with keys 'scRNA' and 'scATAC' and lists of sample names as values.
    """
    all_sample: Dict[str, List[str]] = {
        'scRNA': [],
        'scATAC': []
    }
    if samplename:
        for name in samplename.split(','):
            if os.path.exists(f"{indir}/{name}/04.report/{name}_scRNA_report.html"):
                all_sample['scRNA'].append(name)
            elif os.path.exists(f"{indir}/{name}/04.report/{name}_scATAC_report.html"):
                all_sample['scATAC'].append(name)
            else:
                print(f"The sample of {name} was not found")
                pass
    else:
        html_list = glob.glob(f"{indir}/*/04.report/*.html")
        for html in html_list:
            if 'scRNA' in html:
                sample = html.split('/')[-1].split('_scRNA_')[0]
                all_sample['scRNA'].append(sample)
            elif 'scATAC' in html:
                sample = html.split('/')[-1].split('_scATAC_')[0]
                all_sample['scATAC'].append(sample)
            else:
                pass
    return all_sample


def remove_file(path: str):
    """Remove a file if it exists.

    Args:
        file: Path to the file to be removed.
    """
    if os.path.exists(path):
        if os.path.isfile(path):
            os.remove(path)
            print(f"{path} has been deleted.")
        elif os.path.isdir(path):
            shutil.rmtree(path)
            print(f"{path} directory has been deleted.")
    else:
        print(f"{path} does not exist.")


def remove_RNAfile(scRNAlist: List[str], indir: str):
    """Remove RNA-seq files for each sample in the list.

    Args:
        scRNAlist: List of sample names for RNA-seq data.
        indir: Directory path where the samples are stored.
    """
    print("\033[0;32;40mStart Running Analysis\033[0m")
    print("scRNA file: ", scRNAlist)

    for sample in scRNAlist:
        # 01.data
        remove_file(f"{indir}/{sample}/01.data/oligo.reads.fq.gz")
        remove_file(f"{indir}/{sample}/01.data/cDNA.barcode.counts.txt")
        remove_file(f"{indir}/{sample}/01.data/final_sorted.bam")
        remove_file(f"{indir}/{sample}/01.data/SJ.out.tab")
        remove_file(f"{indir}/{sample}/01.data/oligo.barcode.counts.txt")
        remove_file(f"{indir}/{sample}/01.data/CB_UB_count.txt")
        remove_file(f"{indir}/{sample}/01.data/beads_stat.txt")
        # 02.count
        remove_file(f"{indir}/{sample}/02.count/raw_matrix")
        remove_file(f"{indir}/{sample}/02.count/filter_matrix")
        # 03.analysis
        remove_file(f"{indir}/{sample}/03.analysis/QC_Clutser.h5ad")
        remove_file(f"{indir}/{sample}/03.analysis/filter_feature.h5ad")
    print("\033[0;32;40mComplete\033[0m")

def remove_ATACfile(scATAClist: List[str], indir: str):
    """
    Removes unnecessary files generated during scATAC-seq analysis from a list of samples.

    Args:
    - scATAClist: A list of sample names.
    - indir: The path to the input directory containing the analysis results.
    """
    print("\033[0;32;40mStart Running Analysis\033[0m")
    print('scATAC file: ',scATAClist)

    for sample in scATAClist:
        # 01.data
        #remove_file(f"{indir}/{sample}/01.data/aln.bam")
        remove_file(f"{indir}/{sample}/01.data/alignment.fragments.tsv.gz")
        remove_file(f"{indir}/{sample}/01.data/alignment.count.tsv")
        remove_file(f"{indir}/{sample}/01.data/all.merge.fragments.tsv.gz")
        remove_file(f"{indir}/{sample}/01.data/cb.jaccard.index.tsv")
        remove_file(f"{indir}/{sample}/01.data/cell.id")
        remove_file(f"{indir}/{sample}/01.data/callpeak/{sample}_control_lambda.bdg")
        remove_file(f"{indir}/{sample}/01.data/callpeak/{sample}_treat_pileup.bdg")
        # 02.decon
        remove_file(f"{indir}/{sample}/02.decon/singlecell.csv")
        remove_file(f"{indir}/{sample}/02.decon/raw_peak_matrix")
        remove_file(f"{indir}/{sample}/02.decon/filter_peak_matrix")
        # 03.analysis

    print("\033[0;32;40mComplete\033[0m")

class Clean:
    def __init__(self, args: argparse.Namespace):
        """Initialize the Clean class.

        Args:
            args (argparse.Namespace): The command line arguments.
        """
        self.name = args.name
        self.indir = os.path.abspath(args.indir)

    def run(self) -> None:
        """Run the Clean class."""
        sampleDict = sample_name(self.indir,self.name)
        if len(sampleDict['scRNA']) > 0 :
            remove_RNAfile(sampleDict['scRNA'],self.indir)
        if len(sampleDict['scATAC']) > 0 :
            remove_ATACfile(sampleDict['scATAC'],self.indir)
    
def clean(args: argparse.Namespace):
    """Clean up the output files generated by scRNA and scATAC analysis.

    Args:
        args (argparse.Namespace): The command line arguments.
    """
    Clean(args).run()

def helpInfo_clean(parser: argparse.ArgumentParser):
    """Add command line arguments for the clean function.

    Args:
        parser (argparse.ArgumentParser): The parser for the command line arguments.
    """
    parser.add_argument(
        '--name',
        metavar='NAME',
        default=None,
        help='Sample name, [default is all sample in input directory]'
    )
    parser.add_argument(
        '--indir',
        metavar='DIR',
        help='The dir for cleaned up.'
        #help='The dir for cleaned up, [default: current directory].', 
        #default=os.getcwd()
    )