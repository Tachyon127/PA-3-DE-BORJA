# PA-3-DE-BORJA

Problem #1
- **Car Data Frame (Display)** 

1. A .csv file corresponding to cars is loaded into a data frame using pandas ```cars.csv```
2. To display the first and last five rows of the resulting cars, ```.head()```
and ```.tail()``` is utilized to return n rows of the car dataframe.

```
import pandas as pd

##Load the corresponding .csv file for the dataframe
cars = pd.read_csv('cars.csv') 

##Used to display the first five rows, leaving the () empty defaults to five rows.
cars.head()

##Used to display the last five rows, leaving the () empty defaults to five rows.
cars.tail()
```

Problem #2
- **Subsetting, Slicing, and Indexing**

Using the dataframe cars in problem 1, the following information are extracted using; 
1. ```.iloc[:5, ::2]``` This displays the first 5 rows of the dataframe while slicing the columns in segments of 2 to display the odd-numbered columns
2. ```cars['Model']=='Mazda RX4'``` returns a bool that is true where the model "Mazda RX4" is. ```.loc[]``` is then used to return the full row where that condition is true.
4. A similar method is utilized to display the model "Camaro Z28" while filtering the data to only display the number of cylinders by including  ```['cyl']```
5. Three car models are stored in the variable ```cars_model```. ```.isin()``` is then utilized to filter the rows
where the column value (stored in the variable) is in the list ```cars.loc[cars['Model'].isin(cars_model), ['cyl', 'gear']]```

```
import pandas as pd
cars = pd.read_csv('cars.csv')

cars.iloc[:5, ::2]

cars.loc[cars['Model']=='Mazda RX4']

cars.loc[cars['Model']=='Camaro Z28', ['cyl']]

cars_model = ['Mazda RX4', 'Ford Pantera L', 'Honda Civic']
cars.loc[cars['Model'].isin(cars_model), ['cyl', 'gear']]
```
