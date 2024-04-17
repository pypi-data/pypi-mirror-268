suppressMessages(library(Signac))
suppressMessages(library(Seurat))
suppressMessages(library(magrittr))
suppressMessages(library(readr))
suppressMessages(library(Matrix))
suppressMessages(library(tidyr))
suppressMessages(library(dplyr))
suppressMessages(library(RColorBrewer))
suppressMessages(library(ggplot2))

# Parse command-line arguments
args <- commandArgs(TRUE)

# Check if the correct number of arguments is provided
if (length(args) != 4) {
    stop("Usage: Rscript script.R mex_dir_path fragments singlecellmetadata outdir")
}

# Extract arguments
mex_dir_path <- args[1]
fragments <- args[2]
singlecellmetadata <- args[3]
outdir <- args[4]
PCs <- 2:30

options (warn = -1)
plan("multisession", workers = 4)
options(future.globals.maxSize = 50000 * 1024^2) 

cluster_signac_wrapper = function(mex_dir_path, fragments, singlecellmetadata, outdir, PCs = 2:30){
    ### read peak matrix
    mtx_path <- paste(mex_dir_path, "matrix.mtx.gz", sep = '/')
    feature_path <- paste(mex_dir_path, "peaks.bed.gz", sep = '/')
    barcode_path <- paste(mex_dir_path, "barcodes.tsv.gz", sep = '/')
    
    features <- readr::read_tsv(feature_path, col_names = F) %>% tidyr::unite(feature)
    barcodes <- readr::read_tsv(barcode_path, col_names = F) %>% tidyr::unite(barcode)
    
    mtx <- Matrix::readMM(mtx_path) %>%
    magrittr::set_rownames(features$feature) %>%
    magrittr::set_colnames(barcodes$barcode)


    ### read singlecell metadata
    metadata <- read.csv(
        file = singlecellmetadata,
        header = TRUE,
        row.names = 1
    )
    metadata$log10_uniqueFrags=log10(metadata$fragments)
    metadata$pct_reads_in_peaks <- metadata$peak_region_fragments / metadata$fragments * 100
    metadata$pct_reads_in_tss <- metadata$TSS_region_fragments / metadata$fragments * 100

    chrom_assay <- CreateChromatinAssay(
        counts = mtx,
        sep = c("_", "_"),
        fragments = fragments,
        min.cells = 10,
        min.features = 200
    )

    scATAC <- CreateSeuratObject(
        counts = chrom_assay,
        assay = "peaks",
        meta.data = metadata
    )

    scATAC <- subset(scATAC, subset =log10_uniqueFrags > 3 & pct_reads_in_peaks > 15 & pct_reads_in_tss > 10)
    scATAC <- RunTFIDF(scATAC)
    scATAC <- FindTopFeatures(scATAC, min.cutoff = 'q0')


    if(dim(scATAC)[1] > 50){
        scATAC <- RunSVD(
            object = scATAC,
            assay = 'peaks',
            reduction.key = 'LSI_',
            reduction.name = 'lsi'
        )

        scATAC <- RunUMAP(object = scATAC, reduction = 'lsi', dims = PCs)
        scATAC <- FindNeighbors(object = scATAC, reduction = 'lsi', dims = PCs)
        scATAC <- FindClusters(object = scATAC, verbose = FALSE,algorithm = 3)
        getPalette = colorRampPalette(brewer.pal(9, "Set1"))
        a=getPalette(length(unique(scATAC@meta.data$seurat_clusters)))

        plot4 = DimPlot(object = scATAC, label = TRUE) + NoLegend() +
            scale_color_manual(values = a)

        ggsave(paste0(outdir,"/Cluster_peak.png"), plot = plot4, width = 6, height = 5)
        ggsave(paste0(outdir,"/Cluster_peak.pdf"), plot = plot4, width = 6, height = 5)


        cluster_cor = as.data.frame(Embeddings(object = scATAC,reduction = "umap"))
        cluster_ID = as.data.frame(Idents(object = scATAC))
        coor = cbind(cluster_ID,cluster_cor,scATAC[['log10_uniqueFrags']])
        colnames(coor) = c("Cluster","UMAP_1","UMAP_2","log10_uniqueFrags")
        coor = coor[order(coor$Cluster),]
        counts_cell <- table(coor$Cluster)
        coor$Cluster <- paste(coor$Cluster, counts_cell [match(coor$Cluster, names(counts_cell ))], sep = " CellsNum: ")
        write.csv(coor, file=paste(outdir,"/cluster_cell.stat",sep=""),quote=FALSE)
        saveRDS(scATAC,paste0(outdir,"/saved_clustering.rds"))
        
    }else{
            print("The number of peaks is too low to complete the dimensionality reduction cluster analysis")
            cat(paste("Cluster,UMAP_1,UMAP_2,log10_uniqueFrags","\n",sep=""),file=paste(args$out,"/cluster_cell.stat",sep=""),quote=FALSE)
        }
}

cluster_signac_wrapper(mex_dir_path, fragments, singlecellmetadata, outdir, PCs)