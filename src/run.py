# Importing necessary libraries
import sys
import json
import statistics
import re

from re import sub
from decimal import Decimal


def conv_balance(bal):
    '''
    function that returns processed balance for a give balance
    '''
    value = Decimal(sub(r'[^\d.]', '', bal))
    return value


def get_year(yr):
    '''
    extracts year from given string and returns it
    '''
    return yr.split('-')[0]


class parse_json():
    bal_amt = 0
    total_count = 0
    temp_count = 0
    total_amt = 0
    temp_age = list()
    total_age = list()
    temp_num_friends = list()
    total_num_friends = list()
    temp_unread_messages = 0
    total_unread_messages = 0
    temp_unread_count = 0
    total_unread_count = 0


    temp_user_year = {}
    total_user_year = {}


    def __init__(self):
        pass


    def process_json(self, data):
        '''
        method to call print_all_stats for every 1000
        '''
        self.temp_count += 1
        self.total_count += 1
        self.add_balance(data)
        self.add_user_year(data)
        self.add_age(data)
        self.add_num_friends(data)
        self.add_unread_messages(data)
        if self.temp_count == 1000:
            self.print_all_stats()

    def print_all_stats(self):
        '''
        main method to call methods to print the summary stats

        '''
        if self.temp_count == 0:
            return
        self.get_balance()
        self.get_user_year()
        self.get_median_age()
        self.get_num_friends()
        self.get_unread_messages()
        self.temp_count = 0
        print("################################################################################################")


    def add_user_year(self, data):
        '''
        adds user registered in an particular year
        '''
        year = get_year(data['registered'])
        name = data['name']
        temp_value = 1
        if year in self.temp_user_year:
            temp_value = self.temp_user_year[year] + 1

        total_value = 1
        if year in self.total_user_year:
            total_value = self.total_user_year[year] + 1

        self.temp_user_year[year] = temp_value
        self.total_user_year[year] = total_value


    def get_user_year(self):
        '''
        prints number of users registered each year for 1000 records as well as for the number of records streamed till now
        '''
        print("For " + str(self.temp_count) + " users: " + json.dumps(self.temp_user_year))
        print("Till Now users registered each year: " + json.dumps(self.total_user_year))
        self.temp_user_year.clear()


    def get_balance(self):
        '''
        prints mean balance of users for 1000 records as well as the mean balance for number of records streamed till now
        '''
        bal_amt_1000 = self.bal_amt / self.temp_count
        self.total_amt = self.total_amt + self.bal_amt
        print("Mean Balance for current " + str(self.temp_count) + " users: " + str(bal_amt_1000))
        print("Total Mean balance for " + str(self.total_count)+" users: "+str(self.total_amt / self.total_count))
        self.bal_amt = 0


    def add_balance(self, data):
        '''
        adds balance for a particular user
        '''
        self.bal_amt = self.bal_amt + conv_balance(data['balance'])


    def add_age(self, data):
        '''
        adds age for a particular user
        '''
        self.temp_age.append(data['age'])


    def get_median_age(self):
        '''
        calculates and prints the median age for 1000 users and as well as for the users streamed till now
        '''
        self.total_age.extend(self.temp_age)
        print("Median Age for " + str(self.temp_count) + " users: " + str(statistics.median(self.temp_age)))
        print("Median Age for " +str(self.total_count)+ " users: " +str(statistics.median(self.total_age)))
        self.temp_age.clear()


    def add_num_friends(self, data):
        '''
        adds number of friends for each user
        '''
        self.temp_num_friends.append(len(data['friends']))


    def get_num_friends(self):
        '''
        prints median number of friends for 1000 users as well as for the users streamed till now
        '''
        self.total_num_friends.extend(self.temp_num_friends)
        print("median num friends for " + str(self.temp_count) + " users: " + str(statistics.median(self.temp_num_friends)))
        print("median num friends for " +str(self.total_count)+ " users: " +str(statistics.median(self.total_num_friends)))
        self.temp_num_friends.clear()


    def add_unread_messages(self, data):
        '''
        adds number of unread messages for each user
        '''
        if data['gender'] == 'female' and data['isActive'] is True:
            self.temp_unread_count += 1
            self.temp_unread_messages = self.temp_unread_messages + int(re.findall('\d+', data['greeting'])[0])


    def get_unread_messages(self):
        '''
        prints mean of number of unread messages for 1000 users as well as the users streamed till now
        '''
        self.total_unread_count = self.total_unread_count + self.temp_unread_count
        self.total_unread_messages = self.total_unread_messages + self.temp_unread_messages
        print("Mean num unread messages for "+ str(self.temp_unread_count) + " active female users: " + str(
        self.temp_unread_messages / self.temp_unread_count))
        print("Mean num unread messages total for " + str(self.total_unread_count) + " active female users: " + str(
        self.total_unread_messages / self.total_unread_count))
        self.temp_unread_count = 0
        self.temp_unread_messages = 0


def main(filepath):
    '''
    main method to stream the json file
    '''
    obj = parse_json()
    with open(filepath) as fp:
        stack_ptr = 0
        one_json = ""
        json_count = 0
        for cnt, line in enumerate(fp):
            data = line.strip()

            if stack_ptr == 0 and data in ('[', ']'):
                continue

            if data == '{':
                stack_ptr = stack_ptr + 1
                one_json = one_json + data
            elif data in ('},', '}'):
                stack_ptr = stack_ptr - 1
                if stack_ptr == 0:
                    one_json = one_json + '}'
                else:
                    one_json = one_json + data
            else:
                one_json = one_json + data
            if stack_ptr == 0:
                json_count = json_count + 1
                tmp_json = json.loads(one_json)
                one_json = ""
                obj.process_json(tmp_json)

    # this call is for, if there are less than 1000 records at the end of the file while streaming, calling this
    # methods prints the summary statistics for remaining records
    obj.print_all_stats()


if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
        main(filepath)
    except (IndexError):
        print ("command format to run the code: python run.py users-1.json")
