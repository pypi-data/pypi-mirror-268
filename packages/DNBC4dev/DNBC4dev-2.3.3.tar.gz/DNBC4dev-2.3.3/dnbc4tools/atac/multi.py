import os
from dnbc4tools.__init__ import __root_dir__

# Determine the current execution environment, whether running within Docker or Singularity container
def get_current_environment():
    if os.path.exists('/.dockerenv'):
        return 'Docker'
    elif 'SINGULARITY_CONTAINER' in os.environ:
        return 'Singularity'
    else:
        return 'Non-container'
# Convert relative paths to absolute paths
def get_abspath(paths):
    relative_paths = paths.split(",")
    absolute_paths = [os.path.abspath(path) for path in relative_paths]
    result = ",".join(absolute_paths)
    return result

# Write command line to a shell script
def write_to_shell_script( cmd_line: str, script_path: str) -> None:
    with open(script_path, 'w') as shelllist:
        shelllist.write(cmd_line + '\n')

class MultiList:
    def __init__(self, args):
        """
        Initialize the MultiList class.

        :param args: An object containing the list file path, genome directory, output directory, and thread count.
        """
        self.list = args.list
        self.genomeDir = os.path.abspath(args.genomeDir)
        self.outdir = args.outdir
        self.threads = args.threads

    def _build_cmd_line(self, name: str, fastqr1: str, fastqr2: str) -> str:
        """
        Construct a command-line string.

        :param name: Sample name.
        :param fastqr1: Path to the first FASTQ file.
        :param fastqr2: Path to the second FASTQ file.
        :return: Constructed command-line string.
        """
        cmd_line = []
        current_environment = get_current_environment()

        # Build the command line based on the runtime environment
        if current_environment == 'Singularity':
            fastqr1_dir = {os.path.dirname(os.path.realpath(item)) for item in fastqr1.split(",")}
            fastqr2_dir = {os.path.dirname(os.path.realpath(item)) for item in fastqr2.split(",")}

            data_dir = ','.join(set.union(fastqr1_dir, fastqr2_dir))
            genome_dir = os.path.dirname(os.path.realpath(self.genomeDir))
            out_dir = os.path.dirname(os.path.realpath(self.outdir)) if self.outdir else os.path.dirname(os.path.realpath(os.getcwd()))

            cmd_line.append('export SINGULARITY_BIND=%s,%s,%s\n' % (data_dir, genome_dir, out_dir))
            sif_or_sandbox_path = os.environ.get('SINGULARITY_CONTAINER')

            cmd_line.append('singularity exec %s dnbc4tools atac run --name %s --fastq1 %s --fastq2 %s --genomeDir %s'
                            % (sif_or_sandbox_path, name, fastqr1, fastqr2, self.genomeDir))
            
        else:
            path = '/'.join(str(__root_dir__).split('/')[0:-4])+ '/bin'
            cmd = '%s/dnbc4tools atac run --name %s --fastq1 %s --fastq2 %s --genomeDir %s' % (path, name, fastqr1, fastqr2, self.genomeDir)
            cmd_line.append(cmd)

        # Add thread count and output directory parameters
        if self.threads:
            cmd_line.append('--threads %s' % self.threads)
        if self.outdir:
            self.outdir = os.path.abspath(self.outdir)
            cmd_line.append('--outdir %s' % self.outdir)
        
        return ' '.join(cmd_line)
    
    def run(self) -> None:
        """
        Execute the main function for processing a sample list.

        Attempts to open the specified sample list file and processes each line, ignoring lines starting with '#'.
        For non-comment lines, it extracts the sample name and corresponding FASTQ file paths (supporting multiple paths separated by semicolons),
        generating a Shell script containing the specified analysis command for each sample.

        Raises:
            FileNotFoundError: If the input sample list file does not exist.
            Exception: For any other unexpected exceptions.
        """
        try:
            with open(self.list, 'r') as samplelist:
                for idx, line in enumerate(samplelist):
                    if line.strip().startswith('#'):
                        continue
                    lst = line.strip().split('\t')
                    name = lst[0]
                    fastqr1 = get_abspath(lst[1].split(';')[0])
                    fastqr2 = get_abspath(lst[1].split(';')[-1])
                    shell_script_path = '%s.sh' % name
                    cmd_line = self._build_cmd_line(name, fastqr1, fastqr2)
                    write_to_shell_script(cmd_line, shell_script_path) # Write the command line to the Shell script
        except FileNotFoundError as e:
            print(f"Error: {e}. Please check the input file path.")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
    
def multi(args):
    """
    Launch the multi-list processing workflow.

    Parameters:
        args: An object containing command-line arguments, which must at least have an 'list' attribute specifying the sample list path.

    Returns:
        None
    """
    MultiList(args).run()

def helpInfo_multi(parser):
    """
    Add command-line arguments for the multi-list processing workflow.

    Parameters:
        parser: The ArgumentParser object to add arguments to.

    Returns:
        The modified ArgumentParser object.
    """
    parser.add_argument(
        '--list', 
        metavar='<LIST>',
        help='sample list.', 
        type=str,
        required=True
        )
    parser.add_argument(
        '--outdir', 
        metavar='<OUTDIR>',
        help='Output diretory, [default: current directory].', 
        )
    parser.add_argument(
        '--threads',
        type=int, 
        metavar='<CORENUM>',
        default=4,
        help='Number of threads used for analysis, [default: 4].'
        )
    parser.add_argument(
        '--genomeDir',
        type=str, 
        metavar='<DATABASE>',
        help='Path to the directory where genome files are stored.',
        required=True
        )
    return parser