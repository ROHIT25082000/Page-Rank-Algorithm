# Page-Rank-Algorithm
# An implementation of Page-rank-algorithm using map-reduce on a very large web-graph.
<i>
Directed graph (each unordered pair of nodes is saved once): web-Google.txt
Webgraph from the Google programming contest, 2002
Nodes: 875713 Edges: 5105039</i>

format of the file 
FromNodeId    ToNodeId

Ensure you have Hadoop v2 up and running 
store the file in hdfs 
run the script it will run take around 45 min to compute the pagerank 
have patience . 

You can also do this computation in memory by using Spark with python or scala that would lightening fast !
but I have done using 2 mappers and 2 reducers . 
