from matplotlib import pyplot as plt
from PIL import Image
import osmnx as ox
import networkx as nx


class plotter:
    def __init__(self):
        
        self.end_latlng=None
        self.img = Image.open("C:/Users/cagda/OneDrive/Masaüstü/teker/map/map.png")
    
        loc_x,loc_y=self.location( 41.10269, 29.02162)
        print(loc_x,loc_y)

        
        fig, ax = plt.subplots()
        plt.imshow(self.img, extent=[0, self.img.size[0], 0, self.img.size[1]])
        plt.scatter(loc_x,loc_y,c='r',s=40)
        
        # plt.savefig('C:/Users/cagda/OneDrive/Masaüstü/teker/map/plotted_map.png')

        self.dest_x=0.0
        self.dest_y=0.0

        cid = fig.canvas.mpl_connect('button_press_event', self.onclick)
        plt.show()

    def onclick(self,event):
            max_lat,max_lon=41.10629,29.02639
            min_lat,min_lon=41.10218,29.01785
            #GET CLİCKED LOCATİON
            self.dest_x=event.xdata
            self.dest_y=event.ydata
            
            #CONVERT TO LAT LON
            self.dest_lon=min_lon+((max_lon-min_lon)*self.dest_x)/self.img.size[0]
            self.dest_lat=min_lat+((max_lat-min_lat)*self.dest_y)/self.img.size[1]
            print(self.dest_lon,self.dest_lat)

            self.end_latlng=(self.dest_lon,self.dest_lat)
            
            plt.clf()
            plt.imshow(self.img, extent=[0, self.img.size[0], 0, self.img.size[1]])
            plt.scatter([self.dest_x], [self.dest_y],c='r',s=40); #inform matplotlib of the new data
            plt.draw() 


    def location(self,lat,lon):
          
            max_lat,max_lon=41.10629,29.02639
            min_lat,min_lon=41.10218,29.01785
            # max_lat,max_lon=41.10536,29.02797
            # min_lat,min_lon=41.10110,29.01973

            lat=lat-min_lat
            lon=lon-min_lon
            
            loc_y=(lat*self.img.size[1])/(max_lat-min_lat)
            loc_x=(lon*self.img.size[0])/(max_lon-min_lon)
            
            return loc_x,loc_y
    
    def path(self,end_latlng):
        north=41.1110
        south=41.0985
        east=29.0388
        west=29.0146

        start_latlng=41.10405, 29.02377
        graph=ox.graph.graph_from_bbox(north, south, east, west)
        orig_node = ox.get_nearest_node(graph, start_latlng)
        dest_node = ox.get_nearest_node(graph, end_latlng)
        shortest_route = nx.shortest_path(graph,
                                  orig_node,
                                  dest_node,
                                  weight='time')

run=plotter()



