# Python_Assign_Agnitha
This Would be my Assign for the backend exercise for the internship Exercise for Agnitha

This Code is organized in Three parts Main, Fetch Details and Save to CSV

The function Main Has a Arg Parser which takes two params which can be Default : query defualt to Physics and file name default to output
with help of these args it calls the fetch details and save to CSV Function

Fetch Details take use of the pubmed api with all the params necessary and get the ids of documents that are related to querry than it 
search for all the papers and the details of the papers which are assosiated with these ids.

Save to CSV just take the file name and create a csv file for the data


This project required me to use poetry as i had not used any package that need not to be install seperately if we require than we can use

poetry init 
poetry add (package names)
poetry install


