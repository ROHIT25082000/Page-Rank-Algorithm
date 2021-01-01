# Page-Rank-Algorithm
# An implementation of Page-rank-algorithm using map-reduce on a very large web-graph.
<i>
Directed graph (each unordered pair of nodes is saved once): web-Google.txt<br>
Webgraph from the Google programming contest, 2002<br>
Nodes: 875713 Edges: 5105039</i>
<br>
format of the file<br> 
# FromNodeId    ToNodeId
link for the data set <a href="https://www.kaggle.com/pappukrjha/google-web-graph">link to dataset/a>
Ensure you have Hadoop v2 up and running 
store the file in hdfs 
run the script it will run take around 45 min to compute the pagerank 
have patience . 

You can also do this computation in memory by using Spark with python or scala that would be lightening fast !
but I have done using 2 mappers and 2 reducers in map-reduce code. 
