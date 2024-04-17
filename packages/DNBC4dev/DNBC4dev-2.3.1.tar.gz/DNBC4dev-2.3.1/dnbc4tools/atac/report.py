import os
import shutil
from typing import Any

class Report:
    def __init__(self, args: Any) -> None:
        self.name: str = args.name
        self.outdir: str = os.path.abspath(os.path.join(args.outdir, self.name))
        self.species: str = args.species

    def run(self) -> None:
        ### import lib
        from dnbc4tools.tools.utils import str_mkdir, judgeFilexits, get_formatted_time
        from dnbc4tools.__init__ import __root_dir__
        from dnbc4tools.atac.src.generate_report import write_param_to_template

        ### run
        judgeFilexits(
                      f'{self.outdir}/01.data/all.merge.fragments.tsv.gz',
                      f'{self.outdir}/01.data/alignment.fragments.tsv.gz'
                      )
        str_mkdir('%s/04.report/div'%self.outdir)
        str_mkdir('%s/log'%self.outdir)
        str_mkdir('%s/output'%self.outdir)

        print(f'\n{get_formatted_time()}\n'
            f'Statistical analysis and report generation for results.')

        
        report_file, metrics_summary_df = write_param_to_template(
            '%s/config/template/template_scATAC.html'%__root_dir__,
            self.name,
            self.outdir,
            self.species
            )
        htmlFile = open('%s/04.report/%s_scATAC_report.html'%(self.outdir,self.name),'w')
        htmlFile.write(report_file)
        htmlFile.close()
        metrics_summary_df.to_csv('%s/04.report/metrics_summary.xls'%self.outdir,sep='\t',index=None)

        if os.path.exists('%s/04.report/metrics_summary.xls'%self.outdir):
            shutil.copy("%s/04.report/metrics_summary.xls"%self.outdir,'%s/output'%self.outdir)
        if os.path.exists('%s/04.report/%s_scATAC_report.html'%(self.outdir,self.name)):
            shutil.copy("%s/04.report/%s_scATAC_report.html"%(self.outdir,self.name),'%s/output'%self.outdir)
        if os.path.exists('%s/01.data/all.merge.fragments.tsv.gz'%(self.outdir)):
            shutil.copy('%s/01.data/all.merge.fragments.tsv.gz'%(self.outdir),'%s/output/fragments.tsv.gz'%self.outdir)
        if os.path.exists('%s/01.data/all.merge.fragments.tsv.gz.tbi'%(self.outdir)):
            shutil.copy('%s/01.data/all.merge.fragments.tsv.gz.tbi'%(self.outdir),'%s/output/fragments.tsv.gz.tbi'%self.outdir)
        if os.path.exists('%s/02.decon/singlecell.csv'%(self.outdir)):
            shutil.copy('%s/02.decon/singlecell.csv'%(self.outdir),'%s/output'%self.outdir)

        if os.path.exists('%s/01.data/alignment.fragments.sorted.bam'%self.outdir):
            if(os.path.exists("%s/output/alignment.fragments.sorted.bam"%self.outdir)):
                os.remove("%s/output/alignment.fragments.sorted.bam"%self.outdir)
            shutil.move("%s/01.data/alignment.fragments.sorted.bam"%self.outdir,'%s/output'%self.outdir)
        if os.path.exists('%s/01.data/alignment.fragments.sorted.bam.bai'%self.outdir):
            if(os.path.exists("%s/output/alignment.fragments.sorted.bam.bai"%self.outdir)):
                os.remove("%s/output/alignment.fragments.sorted.bam.bai"%self.outdir)
            shutil.move("%s/01.data/alignment.fragments.sorted.bam.bai"%self.outdir,'%s/output'%self.outdir)

        if os.path.exists("%s/02.decon/raw_peak_matrix"%self.outdir):
            if os.path.exists('%s/output/raw_peak_matrix'%self.outdir):
                shutil.rmtree('%s/output/raw_peak_matrix'%self.outdir)
            shutil.copytree("%s/02.decon/raw_peak_matrix"%self.outdir,'%s/output/raw_peak_matrix'%self.outdir,dirs_exist_ok=True)

        if os.path.exists("%s/02.decon/filter_peak_matrix"%self.outdir):
            if os.path.exists('%s/output/filter_peak_matrix'%self.outdir):
                shutil.rmtree('%s/output/filter_peak_matrix'%self.outdir)
            shutil.copytree("%s/02.decon/filter_peak_matrix"%self.outdir,'%s/output/filter_peak_matrix'%self.outdir,dirs_exist_ok=True)

def report(args):
    Report(args).run()


def helpInfo_report(parser):
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
        '--species',
        type=str, 
        metavar='STR',
        help='Species name.',
        required=True
        )
    return parser