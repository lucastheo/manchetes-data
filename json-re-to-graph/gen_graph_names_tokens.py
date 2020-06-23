import sys
import networkx as nx
sys.path.append('../libs')
import lib_json_graph_file

if __name__ == "__main__":
    json_graph = lib_json_graph_file.load_json_edge_names_token_graph()
    objDG = nx.DiGraph()
    labels = set()

    i = 0
    for token in json_graph.keys():
        i += 1
        objDG.add_node( token , id = i , type = 'token')

        for name in json_graph[ token ]:
            if name not in json_graph.keys():
                i += 1
                objDG.add_node( name , id = i , type = 'name')
    
    for token in json_graph:
        for name in json_graph[ token ]:
            for url in json_graph[ token ][ name ][ lib_json_graph_file.KEY_FREQUENCY_URL_DATA ]:
                for data in json_graph[ token ][ name ][ lib_json_graph_file.KEY_FREQUENCY_URL_DATA ][ url ]:
                    objDG.add_edge(token, name , data = data , url = url )
    
    nx.write_gexf( objDG , "../data/gexf/graph_token_name.gexf")