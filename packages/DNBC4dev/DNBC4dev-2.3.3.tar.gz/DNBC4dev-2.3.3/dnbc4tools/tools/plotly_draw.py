#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   plotly_draw
@Time    :   2023/12/15
@Author  :   lishuangshuang
@Version :   1.0
@Contact :   lishuangshuang3@mgi-tech.com
'''

import plotly.express as px
import pandas as pd
import plotly as py
import plotly.graph_objs as go
from plotly.io import *
from plotly.subplots import make_subplots
import collections,math
import numpy as np
from scipy.interpolate import make_interp_spline
from six import ensure_str, iteritems, itervalues
from scipy import stats, spatial as spatial

PLOTLYCONFIG = {
    'modeBarButtonsToRemove': [
        "autoScale2d",
        "hoverClosestCartesian", 
        "hoverCompareCartesian", 
        "lasso2d",
        "zoomIn2d", 
        "zoomOut2d", 
        "sendDataToCloud",
        "toggleSpikelines" ,
        "logo"
        ],
    'displaylogo': False,
    }

# save plot
def draw_and_save_plot(figures, filenames, div_filenames, outdir):
    for fig, filename, div_filename in zip(figures, filenames, div_filenames):
        py.offline.plot(
            fig,
            filename=outdir + '/' + filename,
            auto_open=False,
            config=PLOTLYCONFIG
        )
        figplot = py.offline.plot(
            fig,
            include_plotlyjs=False,
            show_link=False,
            output_type='div',
            config=PLOTLYCONFIG
        )
        with open(outdir + '/' + div_filename, 'w') as fw:
            fw.write(figplot)


# barcoderanks plot density
def segment_log_plot(y_data, x_start, x_end):
    log_max_x = np.log(len(y_data))
    log_max_y = np.log(max(y_data))
    segment_len = 0.0
    segment_idx = [x_start]
    for i in range(x_start, x_end):
        last_i = max(x_start, i-1)
        dx = (np.log(i) - np.log(last_i)) / log_max_x
        dy = (np.log(y_data[i]) - np.log(y_data[last_i])) / log_max_y
        segment_len += np.linalg.norm([dx, dy])
        if segment_len >= 0.02 and i > (segment_idx[-1] + 20):
            segment_idx.append(i+1)
            segment_len = 0.0
    if segment_idx[-1] != x_end:
        segment_idx.append(x_end)
    return segment_idx

# barcoderanks plot density
def plot_cmap(density):
    plot_colors =  [
        "#DDDDDD","#D6D9DC","#CFD6DB","#C8D3DA","#C1D0D9",
        "#BACDD9","#B3C9D8","#ACC6D7","#A5C3D6","#9EC0D6",
        "#97BDD5","#90BAD4","#89B6D3","#82B3D3","#7BB0D2",
        "#74ADD1","#6DAAD0","#66A6CF","#5FA3CF","#58A0CE",
        "#539DCC","#4F99CA","#4C95C8","#4992C6","#458EC3",
        "#428AC1","#3F87BF","#3B83BD","#3880BA","#347CB8",
        "#3178B6","#2E75B4","#2A71B1","#276DAF","#236AAD",
        "#2066AB","#1D62A8","#195FA6","#165BA4","#1358A2"
        ]
    levels = len(plot_colors)
    ind = min(levels - 1, int(math.floor(levels * density)))
    return plot_colors[ind]

def downsample_scatterplot_by_density(points_df, npoints, dim1, dim2):
    if len(points_df) <= npoints:
        return points_df
    dim1_log2 = np.log2(points_df[dim1] + 1)
    dim1_z = stats.zscore(dim1_log2)
    dim2_log2 = np.log2(points_df[dim2] + 1)
    dim2_z = stats.zscore(dim2_log2)
    round_df = pd.DataFrame(
        {"z1": np.round(dim1_z, 2), "z2": np.round(dim2_z, 2)}, index=points_df.index
    )
    np.random.seed(0)
    is_dup = round_df.duplicated()
    ind_unique = round_df.index[is_dup == False]
    ind_dup = round_df.index[is_dup]
    if len(ind_unique) <= npoints:
        samp_dups = np.random.choice(ind_dup, size=npoints - len(ind_unique), replace=False)
        return pd.concat([points_df.loc[ind_unique], points_df.loc[samp_dups]])
    tree = spatial.KDTree(round_df.loc[ind_unique])
    radius = 0.1
    neighbors = tree.query_ball_tree(tree, radius)
    frequency = np.array([len(x) for x in neighbors])
    inv_density = radius ** 2 / frequency

    samp_index = np.random.choice(
        round_df.loc[ind_unique].index,
        size=npoints,
        replace=False,
        p=inv_density / sum(inv_density),
    )
    return points_df.loc[samp_index]


# plotly all
class plotly_summary:

    @staticmethod
    # df : barcode,UMI,iscell
    def _plot_barcoderanks_rna(dataframe_df, width, height):
        dataframe_df = dataframe_df.sort_values(by="UMI" , ascending=False)
        dataframe_df = dataframe_df.reset_index(drop=True)
        dataframe_df['New']=dataframe_df.index
        cell_bc = np.array(dataframe_df[dataframe_df['is_cell_barcode'] == 1].index)
        sorted_bc = np.array(dataframe_df.index)
        sorted_counts = np.array(dataframe_df['UMI'])
        total_bc = len(sorted_bc)
        ix1 = dataframe_df.drop_duplicates('is_cell_barcode',keep='first').index[1]-1
        ix2 = dataframe_df.drop_duplicates('is_cell_barcode',keep='last').index[0]
        plot_segments = []
        barcodeSegment = collections.namedtuple(
            'barcodeSegment', 
            ['start', 'end', 'density', 'legend']
            )

        plot_segments.append(barcodeSegment(
            start=0, end=ix1, density=1.0, legend=True))
        plot_segments.append(barcodeSegment(
            start=ix2+1, end=total_bc, density=0.0, legend=True))

        mixed_segments = segment_log_plot(
            sorted_counts, ix1, ix2
            )
        for i in range(len(mixed_segments) - 1):
            num_cells = sum(
                [1 for i in range(mixed_segments[i], mixed_segments[i + 1]) if sorted_bc[i] in cell_bc])
            
            density = float(num_cells)/float(mixed_segments[i + 1]-mixed_segments[i])
            plot_segments.append(barcodeSegment(
                    start=mixed_segments[i], end = mixed_segments[i + 1], density=density, legend=False))

        plot_data = []
        for plot_segment in plot_segments:
            start = max(0, plot_segment.start - 1)
            end = plot_segment.end
            selct_count = dataframe_df[start:end]
            dp_first = set(selct_count[selct_count[["UMI"]].duplicated(keep="first")].index)
            dp_last = set(selct_count[selct_count[["UMI"]].duplicated(keep="last")].index)
            dp_inter = dp_first & dp_last
            selct_count=selct_count.drop(list(dp_inter),axis=0)
            x = list(selct_count['New'])
            y = list(selct_count['UMI'])
            name = 'TRUE' if plot_segment.density > 0 else 'NOISE'
            if plot_segment.density > 0:
                n_barcodes = plot_segment.end - plot_segment.start
                n_cells = int(round(plot_segment.density * n_barcodes))
                hover = "{:.0f}% Cell<br>({}/{})".format(100 * plot_segment.density, n_cells, n_barcodes)
            else:
                hover = "NOISE"

            data_dict = {
                "x": x,"y": y,"name": name, "hoverinfo": "text",
                "text": hover,"type": "scattergl","mode": "lines",
                "line": {
                    "width": 3,
                    "color": plot_cmap(plot_segment.density),
                    },
                "showlegend": plot_segment.legend,
                }
            plot_data.append(data_dict)

        plotly_data = [
            go.Scatter(
                x=dat['x'], y=dat['y'], name=dat['name'], mode=dat['mode'], 
                showlegend=dat['showlegend'],
                marker={
                    'color': dat['line']['color']
                    }, 
                line=dat['line'], text=dat['text']
                ) for dat in plot_data
                ]
        layout = go.Layout(
            xaxis = dict(
                type="log", gridcolor="lightgrey", title="Barcode in Rank-descending Order",
                color="black", showline=True, zeroline=True, linewidth=1, fixedrange= True,
                linecolor="black"),
            yaxis = dict(
                type="log", title="UMI counts", gridcolor="lightgrey",
                linewidth=1, fixedrange= True, color="black", linecolor="black"
                ),
            height= height, width= width,
            plot_bgcolor='rgba(0,0,0,0)',hovermode='closest',paper_bgcolor='white',
            legend = dict(
                x=1,y=1,traceorder="normal",
                font = dict(
                    family="Arial",size=12,color="black"
                    ),
                bordercolor="Black",borderwidth=0),
            margin = dict(l=0,r=0,b=0,t=0,pad=1),
            font = dict(size=10))
        fig = go.Figure(
            data=plotly_data, layout=layout
            )
        return fig
    

    @staticmethod
    def _plot_cluster(cluster_df, width, height, type="Cluster"):
        if type == "Cluster":
            cluster_df[['Cluster']] = cluster_df[['Cluster']].astype('str')
            fig = px.scatter(
                cluster_df, 
                x=cluster_df.UMAP_1, 
                y=cluster_df.UMAP_2, 
                color= cluster_df['Cluster'],
                color_discrete_sequence=px.colors.qualitative.G10
                )
            
            fig.update_layout(
                autosize=False,
                width=width,
                height=height,
                legend_title=dict(font=dict(size=13),text='Cluster',),
                legend=dict(font=dict(size=10,family='Arial'),itemsizing='constant'),
                plot_bgcolor='rgba(0,0,0,0)',
                xaxis=dict(gridcolor='lightgray',),
                yaxis=dict(gridcolor='lightgray',)
                )
            
        elif type == "nUMI":
            fig = px.scatter(
                cluster_df, 
                x=cluster_df.UMAP_1, 
                y=cluster_df.UMAP_2, 
                color= cluster_df['nUMI'],
                )
            
            fig.update_layout(
                autosize=False,
                width=width,
                height=height,
                legend_title=dict(font=dict(size=13),text='nUMI',),
                legend=dict(font=dict(size=10,family='Arial'),),
                plot_bgcolor='rgba(0,0,0,0)',
                xaxis=dict(gridcolor='lightgray',),
                yaxis=dict(gridcolor='lightgray',)
                )
        
        elif type == "anno":
            cluster_df = cluster_df.sort_values(by=['Predict_number','Cluster'],ascending=False)
            fig = px.scatter(
                cluster_df, 
                x=cluster_df.UMAP_1, 
                y=cluster_df.UMAP_2, 
                color= cluster_df['Predicted cell type'],
                color_discrete_sequence=px.colors.qualitative.G10
                )
            
            fig.update_layout(
                autosize=False,
                width=width,
                height=height,
                legend_title=dict(font=dict(size=16),text='Predicted cell type: cell number',),
                legend=dict(x=1.2,y=0.5,font=dict(size=10,family='Arial'),itemsizing='constant'),
                plot_bgcolor='rgba(0,0,0,0)',
                xaxis=dict(gridcolor='lightgray',),
                yaxis=dict(gridcolor='lightgray',)
            )

        elif type == "uniqueFrags":
            fig = px.scatter(
                cluster_df, 
                x=cluster_df.UMAP_1, 
                y=cluster_df.UMAP_2, 
                color= cluster_df['log10_uniqueFrags'],
                color_continuous_scale=px.colors.sequential.Viridis
                )
            
            fig.update_layout(
                autosize=False,
                width=width,
                height=height,
                legend_title=dict(font=dict(size=13),text='Fragments(log)',),
                legend=dict(font=dict(size=10,family='Arial'),),
                plot_bgcolor='rgba(0,0,0,0)',
                xaxis=dict(gridcolor='lightgray',),
                yaxis=dict(gridcolor='lightgray',)
                )
        else:
            raise Exception('Unrecognized.')
        
        fig.update_traces(
            marker={'size': 3}
            )
        fig.update_xaxes(
            zeroline=True, zerolinewidth=1, zerolinecolor='gray'
            )
        fig.update_yaxes(
            zeroline=True, zerolinewidth=1, zerolinecolor='gray'
            )
        
        return fig

    @staticmethod
    def _plot_saturation(saturantion_df, width, height, type, mean_reads= None):
        if type == "rna_sequence":
            x=saturantion_df['sampling_fraction']* int(mean_reads)
            y=saturantion_df['Sequencing Saturation']
            if len(saturantion_df) > 2:
                xnew = np.linspace(x.min(),x.max(),50)
                ynew = make_interp_spline(x,y)(xnew)
            else:
                xnew = x
                ynew = y
            fig = px.line(saturantion_df, x=xnew, y=ynew )
            fig.update_layout(
                autosize=False,
                width=width,
                height=height,
                plot_bgcolor='rgba(0,0,0,0)',
                xaxis=dict(gridcolor='lightgray',title="Mean Reads per Cell"),
                yaxis=dict(gridcolor='lightgray',title="Sequencing Saturation"),
                yaxis_range=[0,100]
            )

        elif type == "rna_gene":
            x=saturantion_df['sampling_fraction']* int(mean_reads)
            y=saturantion_df['Median Genes per Cell']
            if len(saturantion_df) > 2:
                xnew = np.linspace(x.min(),x.max(),50)
                ynew = make_interp_spline(x,y)(xnew)
            else:
                xnew = x
                ynew = y
            fig = px.line(saturantion_df, x=xnew, y=ynew )
            fig.update_layout(
                autosize=False,
                width=width,
                height=height,
                plot_bgcolor='rgba(0,0,0,0)',
                xaxis=dict(gridcolor='lightgray',title="Mean Reads per Cell"),
                yaxis=dict(gridcolor='lightgray',title="Median Genes per Cell")
            )

        elif type == "atac_dup":
            y=saturantion_df['median_uniq_frag_per_bc']
            x=saturantion_df['sampling_fraction']* int(mean_reads)
            fig = px.line(saturantion_df, x=x, y=y)

            fig.update_layout(
                autosize=False,
                width=width,
                height=height,
                plot_bgcolor='rgba(0,0,0,0)',
                yaxis=dict(gridcolor='lightgray',title="Median Unique Fragments Per Cell"),
                xaxis=dict(gridcolor='lightgray',title="Mean Read Pairs Per Cell"),
            )
        
        else:
            raise Exception('Unrecognized.')

        fig.update_xaxes(
            zeroline=True, zerolinewidth=1, zerolinecolor='gray'
            )
        fig.update_yaxes(
            zeroline=True, zerolinewidth=1, zerolinecolor='gray'
            )
        fig.update_traces(
            line=dict(color="#337ab7", width=3)
            )
        
        return fig

    
    @staticmethod
    def _plot_clonotype(clonotype_df, width, height):
        if len(clonotype_df) < 10:
            missing_rows = 10 - len(clonotype_df)
            for _ in range(missing_rows):
                clonotype_df = clonotype_df.append({'clonotype_id': f'clonotype{_}', 'proportion': 0}, ignore_index=True)

        clonotypes = clonotype_df.head(10).copy()
        x = clonotypes['clonotype_id'].str.replace("clonotype", "")
        y = clonotypes['proportion']
        fig = px.bar(clonotypes, x=x, y=y)
        fig.update_layout(
            autosize=False,
            width=width,
            height=height,
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(gridcolor='lightgray', title="Clonotype ID"),
            yaxis=dict(gridcolor='lightgray', title="Fraction of Cells"),
            title_text='<b>Top 10 Clonotype Frequencies</b>'
        )
        fig.update_xaxes(
            zeroline=True, zerolinewidth=1, zerolinecolor='gray', showgrid=False
        )
        fig.update_yaxes(
            zeroline=True, zerolinewidth=1, zerolinecolor='gray'
        )
        fig.update_traces(
            marker_color='#337ab7'
        )
        fig.update_traces(hovertemplate='Clonotype ID: %{x}<br>Fraction of Cells: %{y}')
        return fig





    @staticmethod
    def _plot_barcoderanks_atac(dataframe_df, width, height):
        dataframe_df = dataframe_df.sort_values(by="peak_region_fragments" , ascending=False)
        dataframe_df = dataframe_df.reset_index(drop=True)
        dataframe_df['New'] = dataframe_df.index
        cell_bc = np.array(dataframe_df[dataframe_df['is_cell_barcode'] == 1].index)
        sorted_bc = np.array(dataframe_df.index)
        sorted_counts = np.array(dataframe_df['peak_region_fragments'])
        total_bc = len(sorted_bc)
        ix1 = dataframe_df.drop_duplicates('is_cell_barcode',keep='first').index[1]-1
        ix2 = dataframe_df.drop_duplicates('is_cell_barcode',keep='last').index[0]
        plot_segments = []
        barcodeSegment = collections.namedtuple(
            'barcodeSegment', 
            ['start', 'end', 'density', 'legend']
            )

        plot_segments.append(barcodeSegment(
            start=0, end=ix1, density=1.0, legend=True))
        plot_segments.append(barcodeSegment(
            start=ix2+1, end=total_bc, density=0.0, legend=True))

        mixed_segments = segment_log_plot(
            sorted_counts, ix1, ix2
            )
        for i in range(len(mixed_segments) - 1):
            num_cells = sum(
                [1 for i in range(mixed_segments[i], mixed_segments[i + 1]) if sorted_bc[i] in cell_bc])
            
            density = float(num_cells)/float(mixed_segments[i + 1]-mixed_segments[i])
            plot_segments.append(barcodeSegment(
                    start=mixed_segments[i], end = mixed_segments[i + 1], density=density, legend=False))

        plot_data = []
        for plot_segment in plot_segments:
            start = max(0, plot_segment.start - 1)
            end = plot_segment.end
            selct_count = dataframe_df[start:end]
            dp_first = set(selct_count[selct_count[["peak_region_fragments"]].duplicated(keep="first")].index)
            dp_last = set(selct_count[selct_count[["peak_region_fragments"]].duplicated(keep="last")].index)
            dp_inter = dp_first & dp_last
            selct_count=selct_count.drop(list(dp_inter),axis=0)
            x = list(selct_count['New'])
            y = list(selct_count['peak_region_fragments'])
            name = 'TRUE' if plot_segment.density > 0 else 'NOISE'
            if plot_segment.density > 0:
                n_barcodes = plot_segment.end - plot_segment.start
                n_cells = int(round(plot_segment.density * n_barcodes))
                hover = "{:.0f}% Cell<br>({}/{})".format(100 * plot_segment.density, n_cells, n_barcodes)
            else:
                hover = "NOISE"

            data_dict = {
                "x": x,"y": y,"name": name, "hoverinfo": "text",
                "text": hover,"type": "scattergl","mode": "lines",
                "line": {
                    "width": 3,
                    "color": plot_cmap(plot_segment.density),
                    },
                "showlegend": plot_segment.legend,
                }
            plot_data.append(data_dict)

        plotly_data = [
            go.Scatter(
                x=dat['x'], y=dat['y'], name=dat['name'], mode=dat['mode'], 
                showlegend=dat['showlegend'],
                marker={
                    'color': dat['line']['color']
                    }, 
                line=dat['line'], text=dat['text']
                ) for dat in plot_data
                ]
        layout = go.Layout(
            xaxis = dict(
                type="log", gridcolor="lightgrey", title="Barcode in Rank-descending Order",
                color="black", showline=True, zeroline=True, linewidth=1, fixedrange= True,
                linecolor="black"),
            yaxis = dict(
                type="log", title="Fragments Overlapping Peaks", gridcolor="lightgrey",
                linewidth=1, fixedrange= True, color="black", linecolor="black"
                ),
            height= height, width= width,
            plot_bgcolor='rgba(0,0,0,0)',hovermode='closest',paper_bgcolor='white',
            legend = dict(
                x=1,y=1,traceorder="normal",
                font = dict(
                    family="Arial",size=12,color="black"
                    ),
                bordercolor="Black",borderwidth=0),
            margin = dict(l=0,r=0,b=0,t=0,pad=1),
            font = dict(size=10))
        fig = go.Figure(
            data=plotly_data, layout=layout
            )
        return fig


    @staticmethod
    def _plot_atac_fragjaccard(dataframe_df, point, width, height):
        dataframe_df = dataframe_df.round({"jaccard":4})
        dp_first = set(dataframe_df[dataframe_df[["jaccard"]].duplicated(keep="first")].index)
        dp_last = set(dataframe_df[dataframe_df[["jaccard"]].duplicated(keep="last")].index)
        dp_inter = dp_first & dp_last
        dataframe_df = dataframe_df.drop(list(dp_inter),axis=0)
        df_True = dataframe_df[(dataframe_df['jaccard'] >= point)]
        df_False = dataframe_df[(dataframe_df['jaccard'] < point)]
        trace0_x = list(df_True['jaccard_rank'])
        trace0_y = list(df_True['jaccard'])
        trace1_x = list(df_False['jaccard_rank'])
        trace1_y = list(df_False['jaccard'])
        blue_line = list(zip(trace0_x, trace0_y))
        blue_line = [list(i) for i in blue_line]
        black_line = list(zip(trace1_x, trace1_y))
        black_line = [list(i) for i in black_line] 
        trace0 = go.Scatter(
            x = trace0_x, y = trace0_y, mode="lines", name="TRUE", line=dict(color="#005bac",width=3)
        )
        trace1 = go.Scatter(
            x = trace1_x, y = trace1_y, mode="lines", name="FALSE", line=dict(color="grey",width=3)
        )
        layout = go.Layout(
            xaxis = dict(type="log", gridcolor="lightgrey", title="Bead Pairs in Rank-descending Order",
                    color="black", showline=True, zeroline=True, linewidth=1, fixedrange= True, linecolor="black"
                ),
            yaxis = dict(type="log", gridcolor="lightgrey", title="Jaccard Index",
                    linewidth=1,fixedrange= True, color="black", linecolor="black"
                    ),
            height=height, width=width, plot_bgcolor='rgba(0,0,0,0)', hovermode='closest', paper_bgcolor='white',
            legend = dict(x=1, y=1, traceorder="normal",font=dict(
                family="Arial",size=12,color="black"),
                bordercolor="Black",borderwidth=0),
            margin = dict(l=0, r=0, b=0, t=0, pad=1 ),
            font = dict(size=10)
            )             

        data = [trace0, trace1]
        fig = go.Figure(data=data, layout=layout)
        return fig
    

    @staticmethod
    def _plot_merge_beads(dataframe_df, width, height):
        dataframe_df['Count'] = dataframe_df[0].str.split('_N', expand=True)[1]
        figtable = dataframe_df.Count.value_counts()
        figtable = figtable.reset_index(level=None, drop=False, inplace=False)
        #figtable['index'] = figtable['index'].astype(int)
        figtable.columns = ['Num', 'Count']
        figtable['Num'] = figtable['Num'].astype(str)
        cellnum = figtable['Count'].sum()
        figtable['num_count'] = figtable["Num"].map(str) +' '+figtable["Count"].map(str)
        figtable = figtable.sort_values("Num")

        missing_nums = [str(i) for i in range(1, 10) if str(i) not in figtable['Num'].tolist()]
        missing_rows = pd.DataFrame({'Num': missing_nums, 'Count': 0, 'num_count': [f'{num}  0' for num in missing_nums]})
        figtable = pd.concat([figtable, missing_rows], ignore_index=True)
        figtable = figtable.sort_values('Num').head(9)

        x = figtable['Num']
        y = figtable['Count']
        fig = px.bar(figtable, x=x, y=y, color='num_count', color_discrete_sequence=px.colors.qualitative.Set2)
        fig.update_layout(
            autosize=False,
            width=width,
            height=height,
            margin = dict(l=0,r=0,t=50,b=0),
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(gridcolor='lightgray', title="Number of beads per droplet",title_font_size=12,title_standoff = 10),
            yaxis=dict(gridcolor='lightgray', title="Count",title_font_size=13,title_standoff = 10), 
            title=dict(
                text="Total cell number %s"%cellnum,
                font=dict(
                    family="Arial",
                    size=18,
                    color="black"
                ),
                x=0.05,
                y=0.95,
            ),
            legend=dict(
                x=0.8,
                y=1,
                font=dict(size=10,family='Arial'),
                #itemsizing='constant',
                title=None
            ),
        )
        fig.update_xaxes(
            zeroline=True, zerolinewidth=1, zerolinecolor='gray', showgrid=False
        )
        fig.update_yaxes(
            zeroline=True, zerolinewidth=1, zerolinecolor='gray', showgrid=False
        )
        fig.update_traces(
            hovertemplate='Merge Beads Num: %{x}<br>Count: %{y}', 
            width=0.9
            )
        return fig

    @staticmethod
    def _plot_tss_enrichment(dataframe_df, width, height):
        data = {
            "layout": {
                "xaxis": {
                    "gridcolor": 'lightgray',
                    "type": "linear",
                    "title": "Relative Position (bp from TSS)",
                    "showline": True,
                    "zeroline": False,
                    #"title_font_size": 12,
                    #"title_standoff": 10
                },
                "yaxis": {
                    "gridcolor": 'lightgray',
                    "type": "linear",
                    "title": "Relative Enrichment",
                    "showline": True,
                    "zeroline": False,
                    #"title_font_size": 13,
                    #"title_standoff": 5
                },
                "title": "Enrichment around TSS",
            },
            "data": [
            ],
        }

        ref_dict = {
            "name": "tss",
            "x": list(list(range(-1000, 1001))),
            "y": list(dataframe_df[0]),
            "type": "scatter",
            "mode": "lines",
            "marker": {"opacity": 0.7, "color": "#005bac", "size": 4},
        }
        data["data"].append(ref_dict)

        fig = go.Figure(data=data)
        fig.update_layout(
            autosize=False,
            width=width,
            height=height,
            margin = dict(l=0,r=0,t=50,b=0),
            plot_bgcolor='rgba(0,0,0,0)',
            title=dict(
                text="Enrichment around TSS",
                font=dict(
                    family="Arial",
                    size=15,
                    color="black"
                ),
                x=0.05,
                y=0.95,
            ),
        )
        fig.update_xaxes(
            zeroline=False, zerolinewidth=1, zerolinecolor='lightgrey', showgrid=True , fixedrange= True, gridcolor = 'lightgrey'
        )
        fig.update_yaxes(
            zeroline=True, zerolinewidth=1, zerolinecolor='lightgrey', showgrid=True, fixedrange= True, gridcolor = 'lightgrey'
        )

        return fig
    

    @staticmethod
    def _plot_insert_size(dataframe_df, width, height):
        data = {
            "layout": {
                "xaxis": {
                    "gridcolor": 'lightgray',
                    "type": "linear",
                    "title": "Insert Size",
                    "showline": True,
                    "zeroline": False,
                    #"title_font_size": 12,
                    #"title_standoff": 10,
                    'range': [0, 800]
                },
                "yaxis": {
                    "gridcolor": 'lightgray',
                    "type": "linear",
                    "title": "Fragment Count",
                    "showline": True,
                    "zeroline": False,
                    #"title_font_size": 13,
                    #"title_standoff": 5
                },
                "title": "Enrichment around TSS",
            },
            "data": [
                {
                    "name": "Cells",
                    "x": list(dataframe_df['Width']),
                    "y": list(dataframe_df['Nr_frag']),
                    "type": "scatter",
                    "mode": "lines",
                    "line": {"color": "#005bac"},
                }

            ],
        }

        fig = go.Figure(data=data)
        fig.update_layout(
            autosize=False,
            width=width,
            height=height,
            margin = dict(l=0,r=0,t=50,b=0),
            plot_bgcolor='rgba(0,0,0,0)',
            title=dict(
                text="Insert Size Distribution",
                font=dict(
                    family="Arial",
                    size=15,
                    color="black"
                ),
                x=0.05,
                y=0.95,
            ),
        )
        fig.update_xaxes(
            zeroline=True, zerolinewidth=1, zerolinecolor='lightgrey', showgrid=True , fixedrange= True, gridcolor = 'lightgrey', 
        )
        fig.update_yaxes(
            zeroline=True, zerolinewidth=1, zerolinecolor='lightgrey', showgrid=True, fixedrange= True, gridcolor = 'lightgrey',
        )

        return fig

    @staticmethod
    def _plot_atac_target_plot(dataframe_df, target, width, height, excluded_barcodes = None):
        labels = ["Non-cells", "Cells"]
        are_cells = [dataframe_df["is_cell_barcode"] == 1]
        colors = ["grey", "#005bac", "g", "r", "m"]

        is_not_cell_valid = (dataframe_df["Cell"] != ensure_str(b"NO_BARCODE")) & (sum(are_cells) == 0)
        masks = [is_not_cell_valid] + are_cells
        total = dataframe_df["fragments"]
        target_map = {
            "TSS": "TSS_region_fragments",
            "Peaks": "peak_region_fragments"
        }

        if excluded_barcodes is not None:
            exclusions_by_type = {}
            for barcode_data in itervalues(excluded_barcodes):
                for barcode in barcode_data:
                    reason = barcode_data[barcode][0]
                    if reason not in exclusions_by_type:
                        exclusions_by_type[reason] = set()
                    exclusions_by_type[reason].add(barcode)
            for reason, barcode_set in iteritems(exclusions_by_type):
                labels.append(reason)
                exclude_mask = np.array([bc in barcode_set for bc in dataframe_df["CB"]])
                masks.append(exclude_mask)
                # Remove these from the "Non-cells" category as well
                masks[0][exclude_mask] = False

        no_dups_dfs = []
        for label, mask in zip(labels, masks):
            dups_df = pd.DataFrame(
                {"total": total[mask], "subtype": dataframe_df[target_map[target]][mask]}
            )
            dups_df.drop_duplicates(inplace=True)
            no_dups_dfs.append(dups_df)
        if sum(map(len, no_dups_dfs)) > 2000:
            downsampled_dfs = []
            for dataframe in no_dups_dfs:
                downsampled_dfs.append(
                    downsample_scatterplot_by_density(dataframe, 2000, "total", "subtype")
                )
            no_dups_dfs = downsampled_dfs

        data = []
        for label, points_df, color in zip(labels, no_dups_dfs, colors):
            xvals = points_df["total"]
            yvals = points_df["subtype"] / points_df["total"]
            data.append(
                {
                    "name": label,
                    "x": list(xvals),
                    "y": list(yvals),
                    "type": "scatter",
                    "mode": "markers",
                    "marker": {"opacity": 0.7, "color": color, "size": 3},
                }
            )
            
        data_plot =  {
            "layout": {
                "xaxis": {
                    "type": "log",
                    "title": "Fragments per Barcode",
                    "showline": True,
                    "zeroline": False,
                },
                "yaxis": {
                    "type": "linear",
                    "title": "Fraction Fragments Overlapping {}".format(target),
                    "showline": True,
                    "zeroline": False,
                },
                #"title": "{} Targeting".format(target),
            },
            "data": data,
        }

        fig = go.Figure(data=data_plot)
        fig.update_layout(
            autosize=False,
            width=width,
            height=height,
            margin = dict(l=0,r=0,t=20,b=0),
            plot_bgcolor='rgba(0,0,0,0)',
            title=dict(
                text="{} Targeting".format(target),
                font=dict(
                    family="Arial",
                    size=15,
                    color="black"
                ),
                x=0.05,
                y=0.95,
            ),
        )
        fig.update_xaxes(
            zeroline=False, zerolinewidth=1, zerolinecolor='lightgrey', showgrid=True , fixedrange= True, gridcolor = 'lightgrey', 
        )
        fig.update_yaxes(
            zeroline=False, zerolinewidth=1, zerolinecolor='lightgrey', showgrid=True, fixedrange= True, gridcolor = 'lightgrey',
        )

        return fig

    @staticmethod
    def _plot_atacviolin_plot(dataframe_df, width, height):
        meta = dataframe_df[dataframe_df['is_cell_barcode'] == 1].copy()
        meta.loc[:, 'TSS_Proportion'] = meta['TSS_region_fragments'] / meta['fragments']
        meta.loc[:, 'FRIP'] = meta['peak_region_fragments'] / meta['fragments']
        meta.loc[:, 'Fragmentslog'] = np.log10(meta['fragments'] + 1)
        fig = make_subplots(rows=1, cols=3, vertical_spacing=0.1, horizontal_spacing=0.1)
        fig.add_trace(
            go.Violin(y=meta['TSS_Proportion'], box_visible=True, line_color='black', line_width=2,
                        box_fillcolor = "white",points=False,spanmode = "hard",
                        meanline_visible=True, fillcolor='#005bac', opacity=0.8,
                        x0='TSS Proportion'),row=1, col=2
        )

        fig.add_trace(
            go.Violin(y=meta['FRIP'], box_visible=True, line_color='black', line_width=2,
                        box_fillcolor = "white",points=False,spanmode = "hard",
                        meanline_visible=True, fillcolor='#005bac', opacity=0.8,
                        x0='FRIP'),row=1, col=3
        )

        fig.add_trace(
            go.Violin(y=meta['Fragmentslog'], box_visible=True, line_color='black', line_width=2,
                        box_fillcolor = "white",points=False,spanmode = "hard",
                        meanline_visible=True, fillcolor='#005bac', opacity=0.8,
                        x0='Fragments(log)'),row=1, col=1
        )

        fig.update_layout(
            autosize=False,
            width=width,
            height=height,
            font_size=13,
            margin = dict(l=0,r=0,t=0,b=0),
            plot_bgcolor='#F9F9F9',
            title=dict(
                #text="Violin Summary",
                font=dict(
                    family="Arial",
                    size=15,
                    color="black"
                ),
                x=0.15,
                y=0.90,
            ),
            showlegend=False
        )
        fig.update_xaxes(
            zeroline=False, zerolinewidth=1, zerolinecolor='lightgrey', showgrid=False , fixedrange= True, gridcolor = 'lightgrey', 
        )
        fig.update_yaxes(
            zeroline=False, zerolinewidth=1, zerolinecolor='lightgrey', showgrid=False, fixedrange= True, gridcolor = 'lightgrey',
        )

        return fig


    @staticmethod
    def _plot_rnaviolin_plot(dataframe_df, width, height):
        meta = dataframe_df.copy()
        if 'pct_counts_mt' not in meta.columns:
            meta['pct_counts_mt'] = 0
        fig = make_subplots(rows=1, cols=3, vertical_spacing=0.1, horizontal_spacing=0.1)
        fig.add_trace(
            go.Violin(y=meta['n_genes_by_counts'], box_visible=True, line_color='black', line_width=2,
                        box_fillcolor = "white",points=False,spanmode = "hard",
                        meanline_visible=True, fillcolor='#005bac', opacity=0.8,
                        x0='genes'),row=1, col=1
        )

        fig.add_trace(
            go.Violin(y=meta['total_counts'], box_visible=True, line_color='black', line_width=2,
                        box_fillcolor = "white",points=False,spanmode = "hard",
                        meanline_visible=True, fillcolor='#005bac', opacity=0.8,
                        x0='counts'),row=1, col=2
        )

        fig.add_trace(
            go.Violin(y=meta['pct_counts_mt'], box_visible=True, line_color='black', line_width=2,
                        box_fillcolor = "white",points=False,spanmode = "hard",
                        meanline_visible=True, fillcolor='#005bac', opacity=0.8,
                        x0='mito.percent'),row=1, col=3
        )

        fig.update_layout(
            autosize=False,
            width=width,
            height=height,
            font_size=13,
            margin = dict(l=0,r=0,t=0,b=0),
            plot_bgcolor='#F9F9F9',
            title=dict(
                #text="Violin Summary",
                font=dict(
                    family="Arial",
                    size=15,
                    color="black"
                ),
                x=0.15,
                y=0.90,
            ),
            showlegend=False
        )
        fig.update_xaxes(
            zeroline=False, zerolinewidth=1, zerolinecolor='lightgrey', showgrid=False , fixedrange= True, gridcolor = 'lightgrey', 
        )
        fig.update_yaxes(
            zeroline=False, zerolinewidth=1, zerolinecolor='lightgrey', showgrid=False, fixedrange= True, gridcolor = 'lightgrey',
        )

        return fig






    
    


