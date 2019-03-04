# Programming Excercise

**command to run the program**: <br>
<br>
`python run.py <json file>` <br>
example: `python run.py users-1.json`

* This program uses all built-in python libraries

## How streaming is done?

* The program doesn't load all the data into the memory at once. Each line of the input data file is streamed and once a complete json record is read. The json record is sent to calculate the summary statistics but not printed to console yet. Once 1000 records are streamed the summary statistics are printed to console along with the summary statistics for records streamed till now.


## Explaining output

* Mean Balance for current 1000 users: 5230.7289 **(tells the mean balance of current 1000 users)** <br><br>
* Total Mean balance for 50000 users: 5232.066078 **(tells the mean balance of users streamed till now)** <br><br>
* For 1000 users: {"2016": 167, "2017": 173, "2015": 164, "2013": 178, "2012": 156, "2014": 144, "2018": 18} **(tells for the current 1000 records, number of users registered in each year)** <br><br>
* Till Now users registered each year: {"2012": 8229, "2013": 8108, "2017": 8133, "2015": 8022, "2016": 8201, "2014": 8146, "2018": 1161} **(tells number of users registered in each year for all the users streamed till now)**<br><br>
* Median Age for 1000 users: 35.0 **(tell the median age of current 1000 users)** <br><br>
* Median Age for 50000 users: 35.0 **(tells the median age of users streamed till now)** <br><br>
* median num friends for 1000 users: 6.0 **(tells median number of friends for current 1000 users)** <br><br>
* median num friends for 50000 users: 6.0 **(tells the median number of friends for users streamed till now)** <br><br>
* Mean num unread messages for 280 active female users: 49.857142857142854 **(tells mean number of unread messages for current 1000 active female users)** <br><br>
* Mean num unread messages total for 12384 active female users: 49.94081072351421 **(tells mean number of unread messages for users streamed till now)**<br><br>

### Running video of the program is in video.mp4 file<br>

### I have attached the output files as well under output files folder.<br>
* users1_output.txt for users-1.json data<br>
* users2_output.txt for users-2.json data



