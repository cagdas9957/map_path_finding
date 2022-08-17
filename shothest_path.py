import osmnx as ox
import networkx as nx
from matplotlib import pyplot as plt
from PIL import Image
import plotly.graph_objects as go




end_lat_long=(29.02256766129032, 41.104720125225995)
img = Image.open("C:/Users/cagda/OneDrive/Masaüstü/teker/map/map.png")

# fig, ax = plt.subplots()
# plt.imshow(img, extent=[0, img.size[0], 0, img.size[1]])


def path():
        max_lat,max_lon=41.10629,29.02639
        min_lat,min_lon=41.10218,29.01785
        
        north=41.1110
        south=41.0985
        east=29.0388
        west=29.0146

        start_latlng=(41.10405, 29.02377)
        # graph=ox.graph.graph_from_bbox(north, south, east, west)
        # ox.save_graph_geopackage(graph,'map.osm')
        graph=ox.load_graphml('./map.osm')
        print(graph)
        orig_node = ox.nearest_nodes(graph, 41.10405, 29.02377)
        dest_node = ox.nearest_nodes(graph, 29.02256, 41.10472)
        path = nx.shortest_path(graph,
                                  orig_node,
                                  dest_node,
                                  weight='length')
        
        # print(path)
        
        fig, ax = ox.plot_graph_route(
        graph, path, route_color='r', route_linewidth=6, node_size=0)
        
        # we will store the longitudes and latitudes in following list 
        # long = [] 
        # lat = []  
        # for i in path:
        #     point = graph.nodes[i]
        #     long.append(point['x'])
        #     lat.append(point['y'])
        
    
        plt.show()



path()