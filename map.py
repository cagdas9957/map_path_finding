from io import BytesIO
from PIL import Image
import requests
import math

class Map:

    def __init__(self):
        
        # osm api which get our map tiles z=zoom,x=tile number from start point (horizantal),y=tile number from start point (vertical)
        self.URL = "https://tile.openstreetmap.org/{z}/{x}/{y}.png".format
        
        # pixel size of the edge of the one tile
        self.TILE_SIZE = 256
        
        # gps coordinates of the area we want 
        self.lon_1,self.lat_1=29.01785,41.10629 #top left 
        self.lon_2,self.lat_2=29.02639,41.10218 #bottom right

        # zoom constant 
        self.zoom=18

        
        self.x_1,self.y_1=self.point_to_pixels(self.lon_1,self.lat_1,self.zoom)
        self.x_1_tile,self.y_1_tile=int(self.x_1/self.TILE_SIZE),int(self.y_1/self.TILE_SIZE)

        self.x_2,self.y_2=self.point_to_pixels(self.lon_2,self.lat_2,self.zoom)
        self.x_2_tile,self.y_2_tile=math.ceil(self.x_2/self.TILE_SIZE),math.ceil(self.y_2/self.TILE_SIZE)

        # full size image we'll add tiles to
        self.img = Image.new('RGB', (
            (self.x_2_tile - self.x_1_tile) * self.TILE_SIZE,
            (self.y_2_tile - self.y_1_tile) * self.TILE_SIZE))
        
        # request from api 
        for j in range(self.y_1_tile,self.y_2_tile):
            for k in range(self.x_1_tile,self.x_2_tile):
                
                # download each grid of matrix and assign to a variable
                tile_img=self.request(k,j,self.zoom)

                # add each tile to the full size image
                self.img.paste(
                    im=tile_img,
                    box=((k - self.x_1_tile) * self.TILE_SIZE, (j - self.y_1_tile) * self.TILE_SIZE))
        
        print(self.img.size[0],self.img.size[1])

        # crop the image the coordinates we want
        self.img=self.crop(self.img)

        # save the image we get in png format
        self.img.save('map.png')
        
        # plt.imshow(self.img)
        # plt.show()

        # x_ticks,y_ticks=self.adjust_ticks()
        
    

    # algorithm which turns gps coordinates to mercator projection pixels
    def point_to_pixels(self,lon, lat, zoom):
        """convert gps coordinates to web mercator"""
        r = math.pow(2, zoom) * self.TILE_SIZE
        lat = math.radians(lat)

        x = int((lon + 180.0) / 360.0 * r)
        y = int((1.0 - math.log(math.tan(lat) + (1.0 / math.cos(lat))) / math.pi) / 2.0 * r)

        return x, y


    # make request to api
    def request(self,x_tiles,y_tiles,zoom):
        # format the url
        url = self.URL(x=x_tiles, y=y_tiles, z=zoom)

        # make the request
        with requests.get(url) as resp:
            img = Image.open(BytesIO(resp.content))
        return img

    def crop(self,img):
        left=self.x_1-(self.x_1_tile*self.TILE_SIZE)
        top=self.y_1-(self.y_1_tile*self.TILE_SIZE)
        right=self.x_2-(self.x_2_tile*self.TILE_SIZE)+img.size[0]
        bottom=self.y_2-(self.y_2_tile*self.TILE_SIZE)+self.img.size[1]

        print(left,top,right,bottom)
        
        img = img.crop((
            int(left),  # left
            int(top),  # top
            int(right),  # right
            int(bottom))) # bottom
        
        return img
        
        

map=Map()


    




    