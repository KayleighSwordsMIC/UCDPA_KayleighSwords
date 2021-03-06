# -*- coding: utf-8 -*-
"""
Created on Fri May 27 14:33:53 2022

@author: Kayleigh.Swords

create program to replace all the country codes in the World Deaths data file
"""

# import required packages
import pandas as pd


#import data from github csv to dataframe

gitdata = pd.read_csv(r"https://raw.githubusercontent.com/KayleighSwordsMIC/"\
                      r"UCDDataAnalyticsProject/main/Data/World-Deaths.csv")

#check for missing values
#print(data.isna().any())  

#replace missing values with n/a
gitdata.fillna("N/A", inplace=True)

#check again to make sure all missing values are gone
#print(data.isna().any())

#drop duplicates for country and year matches
unique_data = gitdata.drop_duplicates(subset=["Entity", "Year"])

#create list of values
list_of_values = []

def create_codes():    
    #create list of countries as "keys"
    list_of_keys = unique_data["Entity"].to_list()
        
    #characters to be removed
    extra_chars = "()"
        
    #use join() to remove the extra characters
    new_list_of_keys = [''.join(x for x in string if not x in extra_chars) \
                            for string in list_of_keys]
  
    #create holding variable for values
    temp_value = ""
    
    #make new list of codes
    for key in new_list_of_keys:
        temp_value = key.upper()
        
        #if dash and space in country
        if ("-" in temp_value) and (" " not in temp_value):
            list_of_values.append(temp_value[:10])
        
        #if no space in country and the length of its names is less than 7
        elif (" " not in temp_value) and (len(temp_value) > 7):
            list_of_values.append(temp_value[:])
        
        #if there is no space in country
        elif " " not in temp_value:
            list_of_values.append(temp_value[:6])
            
        #if there is a space in the country name        
        elif " " in temp_value:
            temp_value = temp_value.split(" ")
            
            #if there are less than 3 words in the name
            if len(temp_value) < 3:
                list_of_values.append(temp_value[0][:5] + " " + temp_value[1][:6] \
                                      +  " ")
                    
            #if there are 3 words in the name
            elif len(temp_value) == 3:
                list_of_values.append(temp_value[0][:4] + " " + temp_value[1][:5] \
                                      + " " + temp_value[2][:4])
            
            #if there are 4 words in the name
            elif len(temp_value) == 4:
                list_of_values.append(temp_value[0][:4] + " " + temp_value[1][:4] \
                                      + " " + temp_value[2][:4] + " " + temp_value[3][:4])
            
            #if there are 5 words in the name
            elif len(temp_value) == 5:
                list_of_values.append(temp_value[0][:4] + " " + temp_value[1][:4] \
                                      + " " + temp_value[2][:4] + " " + \
                                          temp_value[3][:4] + " " + temp_value[4][:4])
                    
            #if there are 6 words in the name
            elif len(temp_value) == 6:
                list_of_values.append(temp_value[0][:4] + " " + temp_value[1][:4] \
                                      + " " + temp_value[2][:4] + " " + \
                                          temp_value[3][:4] + " " + temp_value[4][:4]\
                                              + " " + temp_value[5][:4])
            
            ##if there are 7 words in the name
            elif len(temp_value) == 7:
                list_of_values.append(temp_value[0][:4] + " " + temp_value[1][:4] \
                                      + " " + temp_value[2][:4] + " " + \
                                          temp_value[3][:4] + " " + temp_value[4][:4]\
                                              + " " + temp_value[5][:4] + " " + \
                                                  temp_value[6][:4])
            
            #if there are 8 words in the name
            elif len(temp_value) == 8:
                list_of_values.append(temp_value[0][:4] + " " + temp_value[1][:4] \
                                      + " " + temp_value[2][:4] + " " + \
                                          temp_value[3][:4] + " " + temp_value[4][:4]\
                                             + " " + temp_value[5][:4] + " " + \
                                                 temp_value[6][:4] +  " " + \
                                                     temp_value[7][:4])
            else:
                print("can't add value")
      
        
    
#replace values in dataframe
def country_codes_replace():
    
    #convert entity column to a list
    entity_column = unique_data["Entity"].to_list()
    
    #make dataframe of entity column and list of values
    new_df = pd.DataFrame()
    
    #add the columns
    new_df["Entity"] = entity_column
    new_df["Code"] = list_of_values
    
    #replace the code column in unique_data
    unique_data.loc[:, ["Code"]] = new_df[["Code"]]
              
    #convert entity column to a list
    entity_column = unique_data["Entity"].to_list()
    
    #make dataframe of entity column and list of values
    new_df = pd.DataFrame()
    
    #add the columns
    new_df["Entity"] = entity_column
    new_df["Code"] = list_of_values
    
    #replace the code column in unique_data
    unique_data.loc[:, ["Code"]] = new_df[["Code"]]
  
    

create_codes()
country_codes_replace()
