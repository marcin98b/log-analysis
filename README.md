## Info
Jupyter scripts and notebooks for analyzing the Online Stock Trading System (OSTS).
1) skryptyPrzebiegi (Charts drawing of log data)
- Draw the time waveforms of the APP1 and APP2 parameters, from the acquired data.
- Libraries used: pandas, matplotlib.
- Created notebooks: methodsTime, methodsTimeSet, stockCPU, stockCPUSetArchitecture, stockCPUSetTests, tradingTime, trafficCPU.
2) skryptyKorelacja (Correlation methods)
- The task of this script is to generate heatmaps, correlation coefficients: r-Pearson, rho-Spearman and Tau Kendall for the loaded set.
- Libraries used: matplotlib, pandas, numpy, seaborn.
- Created notepad: correlationMethods.
3) skryptyAR (Associations Rules)
- Implementation of the Apriori algorithm - generation of association rules (AR), in the form of a table for the loaded set.
- Fixed parameters of the script: min_support = 0.25 (minimum support to be shown in the table), n_bins = 2 (number of subsets into which the divided features/attributes).
- Libraries used: matplotlib, numpy, pandas, seaborn, sklearn, mlxtend.
- Notepad created: associationRules.
4) skryptyKlastrowanie (Clustering methods)
- Implementation of clustering methods: hierarchical clustering, k-means and DBSCAN, for the loaded set.
- Fixed KMeans parameters: n_clusters = n (number of clusters), n_init = 10 (number of runs of the algorithm with different centroid draws), max_iter = 500 (maximum number of iterations of the algorithm, for a single run).
- Fixed hierarchical clustering parameters: n_clusters = n (number of clusters), affinity = 'euclidean' (metric for the measure of similarity between features), linkage = 'ward' (linkage criterion).
- DBSCAN parameters established: eps = 0.1 (maximum distance between two points-neighbors), min_samples=5 (min. number of samples in a neighborhood for a point could be considered as key).
- Libraries used: matplotlib, pandas, seaborn, scipy, sklearn.
- Created notepad: clusteringMethods.

## Scripts used in
- Borowiec, M.; Piszko, R.; Rak, T. Knowledge Extraction and Discovery about Web System Based on the Benchmark Application of Online Stock Trading System. Sensors 2023, 23, 2274. https://doi.org/10.3390/s23042274
- Borowiec, M.; Rak, T. Advanced Examination of User Behavior Recognition via Log Dataset Analysis of Web Applications Using Data Mining Techniques. Electronics 2023, 12, 4408. https://doi.org/10.3390/electronics12214408

