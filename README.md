# DataToCSV

Many times while searching for datasets, you may come accross some datasets which are in the .data format.
In this it may not have the headers which will cause confusion to understand/explain the dataset.
To overcome this problem use this python code, which will convert your .data file to .csv file.
Also you can add headers in the .csv file as you need.

In this, you need to provide a path of your current .data file and also you need to provide a path where you want your .csv file created.
```
User-Defined Functions used:
To read the .data file:
  def read_data(path)

To add headers to dataset:
  def add_headers(dataset, headers):

To convert .data to .csv:
  def data_file_to_csv()
```

In the "Headers" section provide proper sequence of headers you want.
``` 
Eg: headers = ["Column1", "Column2", "Column3", "Column4"]
```

Run this file:

> python3 data_to_csv.py
        
Your file will be generated.
