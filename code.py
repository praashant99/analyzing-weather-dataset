# --------------
#Importing the modules
import pandas as pd
import numpy as np
from scipy.stats import mode 

weather=pd.read_csv(path)

#Code for categorical variable
def categorical(df):
   category=df.select_dtypes(include=['object'])
   return category
cat=categorical(weather)
print(cat[:5])
 


#Code for numerical variable
def numerical(df):
    number=df.select_dtypes(include=['int64','float64'])
    return number
numb=numerical(weather)
print(numb[:5])


#code to check distribution of variable
def clear(df,col,val):
    v=df[col].value_counts()[val]
    return v
vals=clear(weather,'Weather','Fog')


   



#Code to check instances based on the condition
def instances_based_condition(df,col1,val1,col2,val2):
    con=df[(df[col1]>val1)&(df[col2]==val2)]
    return con
wind_speed_35_vis_25=instances_based_condition(weather,'Wind Spd (km/h)',35,'Visibility (km)',25)
""" Instances based on the condition
    
    This function accepts a dataframe, 2 columns(feature) and 2 values which returns the dataframe
    based on the condition.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    col1 - First feature of the dataframe on which you want to apply the filter
    val1 - Value to be filtered on the first feature
    col2 - Second feature of the dataframe on which you want to apply the filter
    val2 - Value to be filtered on second feature
    
    Returns:
    instance - Generated dataframe
"""
    
    



# Code to calculate different aggreagted values according to month

def agg_values_ina_month(df,date_col,agg_col, agg):
    df[date_col]=pd.to_datetime(df[date_col])
    aggg=pd.pivot_table(df,columns=agg_col,aggfunc=agg)
    return aggg

ag1=agg_values_ina_month(weather,'Date/Time','Temp (C)','mean')
"""  Aggregate values according to month
    
    This function accepts a dataframe, 2 columns(feature) and aggregated funcion(agg) which returns the Pivot 
    table with different aggregated value of the feature with an index of the month.
     
    Keyword arguments:
    df - Pandas dataframe which has the data.
    date_col - Date feature of the dataframe on which you want to apply to_datetime conversion
    agg_col - Feature of the dataframe on which values will be aggregated.
    agg - Dictionary of aggregate functions with feature as the key and func as the value
    
    Returns:
    aggregated_value - Generated pivot table
"""



# Code to group values based on the feature
def group_values(df,col1,agg1):
    f= df.groupby([col1]).agg(agg1)
    return f

mean_weather=group_values(weather,'Weather','mean')
""" Agrregate values by grouping
    
    This function accepts a dataframe, 1 column(feature) and aggregated function(agg1) which groupby the 
    datframe based on the column.
   
   Keyword arguments:
    df - Pandas dataframe which has the data.
    col1 - Feature of the dataframe on which values will be aggregated.
    agg1 - Dictionary of aggregate functions with feature as the key and func as the value
    
    Returns:
    grouping - Dataframe with all columns on which it is grouped on.
"""
    



# function for conversion 
def convert(df,celsius):
    df['Fahrenhei']=(df[celsius]*1.8+32)
    return df['Fahrenhei']
con=convert(weather,'Temp (C)')
print(con)
""" Convert temperatures from celsius to fahrenhheit
    
    This function accepts a dataframe, 1 column(feature) which returns the dataframe with converted values from 
    celsius to fahrenhheit.
         
    Keyword arguments:
    df - Pandas dataframe which has the data.
    celsius - Temperature feature of the dataframe which you want to convert to fahrenhheit
    
    Returns:
    converted_temp - Generated dataframe with Fahrenhheit temp.
    
"""
    


# Load the weather_2012 data csv file and store it in weather variable. The path of the dataset has been stored in the variable `path` for you.



# As you have now loaded the weather data you might want to check the categorical and numerical variables. You can check it by calling categorical and numerical function. 




#You might be interested in checking the distribution of a specific value like the number of times the weather was exactly Cloudy in the given column. Feel free to check on other values.
#You can check it by calling the function clear with respective parameters.
#By using index of the value or name of the value you can check the number of count




# Now suppose you want to check some instances based on a specific condition like when the wind speed was above 35 and visibility was 25. You can dicretly check it by calling the function instances_based_condition with respective parameters.




#You have temperature data and want to calculate the mean temperature recorded by month.You can generate a pivot table which contains the aggregated values(like mean, max ,min, sum, len) recoreded by month. 
#You can call the function agg_values_ina_month with respective parameters. 



# To groupby based on a column like you want to groupby on Weather column and then aggregate the mean values of each column for different types of weather using mean. You can call the function group_values.
# Feel free to try on diffrent aggregated functions like max, min, sum, len



# You have a temperature data and wanted to convert celsius temperature into fahrehheit temperatures you can call the function convert.


