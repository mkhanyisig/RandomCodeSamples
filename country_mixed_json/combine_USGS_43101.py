"""
Prospector Geospatial Data
Create GeoJSON object from USGS data

"""


# load libraries
import pandas as pd
import csv
import json
from IPython.display import display
import time




def combine():
    "Combine USGS and 43-101 files into one GeoJSON"

    df_usgs = pd.read_csv('MRDS Data.csv',low_memory=False)
    print("Shape:  ",df_usgs.shape)

    df_mineral = pd.read_csv('mining_reports.csv')
    print("Shape:  ",df_mineral.shape)

    # USGS json
    usgs = df_usgs.to_json(orient="records") #  index labels are not preserved with this encoding
    parsed_usgs = json.loads(usgs)
    #print("JSON :\n")
    #dump_usgs=json.dumps(parsed_usgs, indent=4)
    #print("Object: \n",len(dump_usgs))

    # process 43-101 records

    # lowercase clumn headers
    df_mineral.columns=[x.lower() for x in df_mineral.columns]
    # rename country column & lattitude typo
    df_mineral.rename(columns={"geography":"country"}, inplace=True)
    df_mineral.rename(columns={"lattitude":"latitude"}, inplace=True)

    mineral = df_mineral.to_json(orient="records") #  index labels are not preserved with this encoding
    parsed_mineral = json.loads(mineral)
    #print("JSON :\n")
    #dump_mineral=json.dumps(parsed_mineral, indent=4)
    #print("Object: \n",len(dump_mineral))

    " Merge two Objects into one GeoJSON"

    feature_arr=[]

    # start with USGS
    print("Begin USGS processing\n")
    "USGS"
    i=0
    for obj in parsed_usgs:
        #print("object: ",obj)
        arr_obj={}
        arr_obj.update({"type":"Feature"})
        """
        Create mineral tags
        """

        min1=obj['commod1']
        min2=obj['commod2']
        min3=obj['commod3']

        mineral_tags=set()

        print("\n***\n")
        # first tag
        if min1!=None:
            #print(min1)
            min1=min1.split(",")
            temp=[]
            for el in min1:
                el=el.replace(" ","")
                el=el.lower()
                temp.append(el)
                mineral_tags.add(el)
            #print(temp)
        # second tag
        if min2!=None:
            #print(min2)
            min2=min2.split(",")
            temp=[]
            for el in min2:
                el=el.replace(" ","")
                el=el.lower()
                temp.append(el)
                mineral_tags.add(el)
            #print(temp)
        # second tag
        if min3!=None:
            #print(min3)
            min3=min3.split(",")
            temp=[]
            for el in min3:
                el=el.replace(" ","")
                el=el.lower()
                temp.append(el)
                mineral_tags.add(el)
            #print(temp)

        print("Minerals: ",list(mineral_tags))
        mineral_tags=list(mineral_tags)
        obj.update({"mineral_tags":mineral_tags})
        obj.update({"report_type":"usgs"})

        # update tag
        arr_obj.update({"properties":obj})

        geometry={}
        geometry.update({"type":"Point"})
        geometry.update({"coordinates":[obj.get('longitude'),obj.get('latitude')]}) # needs fixing

        arr_obj.update({"geometry":geometry})

        feature_arr.append(arr_obj)

        print(i," / ",len(parsed_usgs), "  => USGS done")
        i+=1;

    # add 43-101 object
    print("Begin 43-101 processing\n")
    " 43-101"

    i=0
    # process 43-101 minerals
    for obj in parsed_mineral:
        #print("object: ",obj)
        arr_obj={}
        arr_obj.update({"type":"Feature"})
        """
        Create mineral tags
        """

        min1=obj['mineral']


        mineral_tags=set()

        print("\n***\n")
        # first tag
        if min1!=None:
            print(min1)
            min1=min1.split(",")
            temp=[]
            for el in min1:
                el=el.replace(" ","")
                el=el.lower()
                temp.append(el)
                mineral_tags.add(el)
            print(temp)

        print("Minerals: ",list(mineral_tags))
        mineral_tags=list(mineral_tags)
        obj.update({"mineral_tags":mineral_tags})
        obj.update({"report_type":"43101"})

        # update tag
        arr_obj.update({"properties":obj})

        geometry={}
        geometry.update({"type":"Point"})
        geometry.update({"coordinates":[obj.get('longitude'),obj.get('latitude')]}) # needs fixing

        arr_obj.update({"geometry":geometry})
        if(obj.get('latitude')!=None and obj.get('longitude')!=None):
            feature_arr.append(arr_obj)

        print(i," / ",len(parsed_mineral), "  => Mineral done")
        i+=1

    "Build GeoJSON"
    geojson_obj={}
    geojson_obj.update({"type":"FeatureCollection"})
    geojson_obj.update({"features":feature_arr})

    "Export GeoJSON"
    output = open("combined_USGS_43-101.json", 'w')
    output.write(json.dumps(geojson_obj, indent=2))
    output.close()

    print("done")

def countryJSON(country):
    " Using country search key term, build JSON object with country results"
    print("Country JSON: ",country)
    with open('combined_USGS_43-101.json') as f:
      json_obj = json.load(f)
    #print(type(json_obj))
    print("****\nTesting \n****\n")
    print("Total Locations: ",len(json_obj['features']))
    #print("\nGeometry:\n",json_obj['features'][0]['geometry'])

    feature_arr=json_obj['features']

    country_objs=[]
    usgs=0
    mineral=0
    for obj in feature_arr:
        #print(obj["properties"]['country'])
        if(obj["properties"]['country']==country):
            country_objs.append(obj)
            if(obj["properties"]['report_type']=='usgs'):
                usgs+=1
            elif(obj["properties"]['report_type']=='43101'):
                mineral+=1
    print("Result ",len(country_objs))
    print("USGS: ",usgs,"\n43-101: ",mineral)

    # export GeoJSON
    geojson_obj={}
    geojson_obj.update({"type":"FeatureCollection"})
    geojson_obj.update({"features":country_objs})
    #
    output = open(country.lower()+"_mixed.json", 'w')
    output.write(json.dumps(geojson_obj, indent=2))
    output.close()
#
def mineralJSON(min):
    " Using country search key term, build JSON object with country results"
    print("Country JSON: ",country)

    with open('mexico_mixed.json') as f:
      json_obj = json.load(f)
    #print(type(json_obj))
    print("****\nTesting \n****\n")
    print("Total Locations: ",len(json_obj['features']))
    #print("\nGeometry:\n",json_obj['features'][0]['geometry'])

    feature_arr=json_obj['features']

    country_objs=[]
    usgs=0
    mineral=0
    for obj in feature_arr:
        #print(obj["properties"]['country'])
        if(obj["properties"]['mineral_tags'].contains(min)):
            country_objs.append(obj)
            if(obj["properties"]['report_type']=='usgs'):
                usgs+=1
            elif(obj["properties"]['report_type']=='43101'):
                mineral+=1
    print("Result ",len(country_objs))
    print("USGS: ",usgs,"\n43-101: ",mineral)

    # export GeoJSON
    geojson_obj={}
    geojson_obj.update({"type":"FeatureCollection"})
    geojson_obj.update({"features":country_objs})
    #
    output = open(country.lower()+"_mineral.json", 'w')
    output.write(json.dumps(geojson_obj, indent=2))
    output.close()

########### main functions

# Testing
start_time = time.time()
#combine()


countryJSON("Canada")
print("--- Total running time(s): ---" , (time.time() - start_time))
