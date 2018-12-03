# BA Job Analysis and Visualization
IEOR 4501: Tools for Analytics

## Group Information
+ Group name: LuckySeven
+ Group members: Yilun Cheng, Fangyuan Chen, Yanqi Zhang, Quenu Cheng

## Objective
Our team wants to establish a database that contains the Business Analyst (BA) opportunities in thirty largest states in the United States for users. The data we get is scraped mainly from Glassdoor. Users can get more vivid information about the position descriptions, salary ranges and average salaries through bar chart, state map and WordCloud. Moreover, users are able to find their desired position based on our filter system. Our job will make job-haunting process more convenient for users.

## Python Package Requirement
+	Pandas
+	Numpy
+	Plotly
+	Bokeh
+	WordCloud
+	nltk

install instrucions:
```
pip install Pandas
pip install Numpy
pip install Plotly
pip install Bokeh
pip install WordCloud
pip install nltk
```

## Run Instructions
We merged all out functions into a command line tool `main.py`.

Run 
```
python main.py -h
```
for help scripts, which is like:
![GitHub](https://github.com/fangyuanc7/LuckySeven/blob/master/examples/parameters.png)
We can use different parameters to get different functions.

### Web Scarping ###
The `-d` `-f` arguments help our team to grab different jobs in different cities in the US from Glassdoor. We get the Business Analyst positions posted on Glassdoor for the 30 largest states in the United States. It generates 30 raw datasets, which are used as the raw data for this project and the raw datasets are all saved in the raw_data directory.

We can use these functions as follows:
```sh
# fetch business analyst job in New Orleans without description
python main.py -f 0 "business analyst" "new orleans"

python main.py -d "https://www.glassdoor.com/partner/jobListing.htm?pos=101&ao=338372&s=149&guid=000001676640cf86a6ec12245a32bf41&src=GD_JOB_AD&t=SRFJ&extid=4&exst=OL&ist=&ast=OL&vt=w&slr=true&rtp=0&cs=1_2efff88d&cb=1543608783262&jobListingId=3028474751"
```

### Data Cleaning ###
The `-m` `-c` arguments are used to clean datas. `-m` helps us merge all the datasets in raw_data directory and `-c` helps us to clean the merged dataset.
```
python main.py -m
python main.py -c
```

### Data Visualization ###
After merging and cleaning the raw dataset, we are able to use three functions get one state map and two bar charts that could help users to get more intuitive information about our dataset. 
```
python main.py -s
python main.py -b
python main.py -q
```
for example:
![GitHub](https://github.com/fangyuanc7/LuckySeven/blob/master/examples/average_salary_bar_example.png)
![GitHub](https://github.com/fangyuanc7/LuckySeven/blob/master/examples/map_result_example.png)
![GitHub](https://github.com/fangyuanc7/LuckySeven/blob/master/examples/salary_range_bar_example.png)

### Filter System ###
The filter system we established allows the user to get a list of the desired BA positions based on certain requirements. The requirements including city, keywords, minimum salary and company. Users can also scroll down the list and get more information about job description.
```
python main.py -l
```
![GitHub](https://github.com/fangyuanc7/LuckySeven/blob/master/examples/filters_result_example.png)

### Word Cloud ###
The wordcloud we established provides users a graph that contains heterogeneous words with different sizes. The more a specific word appears in the job description for each cities, the bigger and bolder it appears in the word cloud.
```
python main.py -w "new orleans"
```
![GitHub](https://github.com/fangyuanc7/LuckySeven/blob/master/examples/words_cloud_example.png)
