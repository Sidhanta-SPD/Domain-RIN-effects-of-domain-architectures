import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


adj_mat1=pd.read_csv('2fbo_dom_1.adj_mat',sep=' ',index_col=0)
adj_mat2=pd.read_csv('2fbo_dom_2.adj_mat',sep=' ',index_col=0)
G=nx.from_pandas_adjacency(adj_mat1)
G2=nx.from_pandas_adjacency(adj_mat2)
G.degree()
clust=nx.clustering(G)#clustering coefficients
clust2=nx.clustering(G2)
print(np.mean(list(clust.values())))#mean of clustering coefficients of all nodes.
#or nx.average_clustering(G)

#global clustering coefficient
nx.transitivity(G)
nx.transitivity(G2)

#density of network
nx.density(G)
nx.density(G2)

#average shortest pathlength
nx.average_shortest_path_length(G)
nx.average_shortest_path_length(G2)
#network diameter
nx.diameter(G)
nx.diameter(G2)

#degree assortivity coefficient
nx.degree_assortativity_coefficient(G)
nx.degree_assortativity_coefficient(G2)

#network modularity
#nx.modularity(G)
#plotting the network
plt.subplot(2,1,1)
Gcc1 = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
pos1 = nx.spring_layout(Gcc1, seed=10396953)
nx.draw_networkx_nodes(Gcc1, pos1, node_size=199)
nx.draw_networkx_edges(Gcc1, pos1, alpha=0.4)

plt.subplot(2,1,2)
Gcc2 = G2.subgraph(sorted(nx.connected_components(G2), key=len, reverse=True)[0])
pos2 = nx.spring_layout(Gcc2, seed=10396953)
nx.draw_networkx_nodes(Gcc2, pos2, node_size=145)
nx.draw_networkx_edges(Gcc2, pos2, alpha=0.4)

#----------------
#plotting communities
communities = list(nx.community.girvan_newman(G2))

# Modularity -> measures the strength of division of a network into modules
modularity_df = pd.DataFrame(
    [
        [k + 2, nx.community.modularity(G2, communities[k])]
        for k in range(len(communities))
    ],
    columns=["k", "modularity"],
)


# function to create node colour list
def create_community_node_colors(graph, communities):
    number_of_colors = len(communities)
    #colors = ["#D4FCB1", "#CDC5FC", "#FFC2C4", "#F2D140", "red"][:number_of_colors]
    colors = ['#000000','#FFFFFF','#FF0000','#00FF00','#0000FF','#FFFF00',
              '#00FFFF','#FF00FF','#808080','#800000'][:number_of_colors]
    node_colors = []
    for node in graph:
        current_community_index = 0
        for community in communities:
            if node in community:
                node_colors.append(colors[current_community_index])
                break
            current_community_index += 1
    return node_colors

#bet1={key.split("_")[1]:round(values,3) for key,values in nx.betweenness_centrality(G).items()}
#https://networkx.org/documentation/stable/auto_examples/algorithms/plot_girvan_newman.html
# function to plot graph with node colouring based on communities
def visualize_communities(graph, communities):#add i if plotting subplots. refer the link
    node_colors = create_community_node_colors(graph, communities)
    modularity = round(nx.community.modularity(graph, communities), 6)
    title = f"Community Visualization of {len(communities)} communities with modularity of {modularity}"
    pos = nx.spring_layout(graph, k=0.3, iterations=50, seed=2)
    #plt.subplot(2, 1, i)
    fig=plt.figure(figsize=(8, 6))
    plt.title(title)
    nx.draw(
        graph,
        pos=pos,
        node_size=100,
        node_color=node_colors,
        with_labels=True,
        font_size=5,
        font_color="black",
    )
    fig.set_facecolor('lightgray')

#sns.set_style('darkgrid')
#fig, ax = plt.subplots(2, figsize=(15, 20))

# Plot graph with colouring based on communities
#visualize_communities(G, communities[0], 1)#remove 1, This is for subplot
#visualize_communities(G, communities[3], 2)#number of communities has max modularity. The position in communnities is n-2.
#correct way for drawing only the community is:
visualize_communities(G2, communities[6]) #for 8 communities

# Plot change in modularity as the important edges are removed
modularity_df.plot.bar(
    x="k",
    #ax=ax[1],
    color="#F2D140",
    title="Modularity Trend for Girvan-Newman Community Detection",
)
plt.show()


#-----------------betweenness centrality
aligned_res=pd.read_csv("aligned_res",sep=' ',header=None,names=("resn1","ch1","res1","resn2","ch2","res2"))
aligned_res["RES1"] = aligned_res[["ch1","res1", "resn1"]].apply(lambda x: "_".join(x.astype(str)), axis =1)
aligned_res["RES2"] = aligned_res[["res2", "resn2"]].apply(lambda x: "B_"+"_".join(x.astype(str)), axis =1)
aligned_res=aligned_res.drop(columns=["ch1","res1", "resn1","ch2","res2", "resn2"])
#aligned_res=aligned_res.drop(index=(183))#the last residue pair is not in network
aligned_res["idx"]=np.arange(1,len(aligned_res)+1)
aligned_res["bet1"]=[round(nx.betweenness_centrality(G)[aligned_res["RES1"][i]],3) if aligned_res["RES1"][i] in adj_mat1.columns else np.nan for i in range(len(aligned_res))]
aligned_res["bet2"]=[round(nx.betweenness_centrality(G2)[aligned_res["RES2"][i]],3) 
                     if aligned_res["RES2"][i] in adj_mat2.columns
                     else np.nan
                     for i in range(len(aligned_res))]
aligned_res["cls1"]=[round(nx.closeness_centrality(G)[aligned_res["RES1"][i]],3) if aligned_res["RES1"][i] in adj_mat1.columns else np.nan for i in range(len(aligned_res))]
aligned_res["cls2"]=[round(nx.closeness_centrality(G2)[aligned_res["RES2"][i]],3) if aligned_res["RES2"][i] in adj_mat2.columns else np.nan for i in range(len(aligned_res))]
aligned_res["deg1"]=[round(nx.degree(G)[aligned_res["RES1"][i]],3) if aligned_res["RES1"][i] in adj_mat1.columns else np.nan for i in range(len(aligned_res))]
aligned_res["deg2"]=[round(nx.degree(G2)[aligned_res["RES2"][i]],3) if aligned_res["RES2"][i] in adj_mat2.columns else np.nan for i in range(len(aligned_res))]

aligned_res.dropna(subset=["bet1","bet2","cls1","cls2","deg1","deg2"], inplace=True)
aligned_res.reset_index(drop=True, inplace=True)

f, ax = plt.subplots(3, 1, figsize=(18, 18))
#plt.figure(figsize=(18,3))
sns.set_style('darkgrid')
#betweenness
sns.lineplot(data=aligned_res,x=aligned_res.idx,y=aligned_res.bet1,ax=ax[0])
sns.lineplot(data=aligned_res,x=aligned_res.idx,y=aligned_res.bet2,ax=ax[0])
ax[0].set_xticks(np.arange(0,115,5))
ax[0].set_yticks(np.arange(0,0.14,0.02)) #for betweenness
ax[0].set_ylabel('Betweenness')
ax[0].set_xlabel('')
#closeness
sns.lineplot(data=aligned_res,x=aligned_res.idx,y=aligned_res.cls1,ax=ax[1])
sns.lineplot(data=aligned_res,x=aligned_res.idx,y=aligned_res.cls2,ax=ax[1])
ax[1].set_xticks(np.arange(0,115,5))
ax[1].set_yticks(np.arange(0.18,0.44,0.05)) 
ax[1].set_ylabel('Closeness')
ax[1].set_xlabel('')
#degree
sns.lineplot(data=aligned_res,x=aligned_res.idx,y=aligned_res.deg1,ax=ax[2])
sns.lineplot(data=aligned_res,x=aligned_res.idx,y=aligned_res.deg2,ax=ax[2])
ax[2].set_xticks(np.arange(0,115,5))
ax[2].set_yticks(np.arange(0,17,2)) 
ax[2].set_ylabel('Degree')
ax[2].set_xlabel('Topological equivalence residue index')


#mean absolute error(MAE)
np.mean(aligned_res.bet1-aligned_res.bet2)

"""
#main parameters for comparing with scientific reports paper. https://www.nature.com/articles/s41598-021-92201-3#Sec8
G1_pars=pd.DataFrame({"Res":nx.betweenness_centrality(G).keys(),"Btw":nx.betweenness_centrality(G).values(),"Deg":dict(nx.degree(G)).values(),"Cls":nx.closeness_centrality(G).values()})
G2_pars=pd.DataFrame({"Res":nx.betweenness_centrality(G2).keys(),"Btw":nx.betweenness_centrality(G2).values(), "Deg":dict(nx.degree(G2)).values(),"Cls":nx.closeness_centrality(G2).values()})
#super-critical residues
G1_pars[(G1_pars["Btw"]>=max(G1_pars.Btw)*0.8) & (G1_pars["Deg"]>=max(G1_pars.Deg)*0.8) & (G1_pars["Cls"] >= max(G1_pars.Cls)*0.8)]

#HDHB=High degree and high betweenness
HDHB=G1_pars[(G1_pars["Btw"]>=max(G1_pars.Btw)*0.8) & (G1_pars["Deg"]>=max(G1_pars.Deg)*0.8)]
#LDHB
LDHB=G1_pars[(G1_pars["Btw"]>=max(G1_pars.Btw)*0.8) & (G1_pars["Deg"]<max(G1_pars.Deg)*0.2)]
#LDLB
LDLB=G1_pars[(G1_pars["Btw"]<max(G1_pars.Btw)*0.2) & (G1_pars["Deg"]<max(G1_pars.Deg)*0.2)]

ress=HDHB["Res"].str.extract(r'(\d+)')[0].to_list()
pymol_res='+'.join(ress)
"""
#=====================================the above code is Not used====
