import re
from random import shuffle
import json
from nltk import corpus
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
#Some utility methods that I think maybe useful in the future
class Utils:

    #removes html tags from the body of the question text
    @staticmethod
    def strip_html_tags(text):
        tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
        no_tags_text = tag_re.sub('',text)
        return no_tags_text

    #converts to utf format
    @staticmethod
    def convert_to_utf(input):
        if isinstance(input, dict):
            temp_dict = {}
            for key,value in input.iteritems():
                temp_dict[Utils.convert_to_utf(key)] = Utils.convert_to_utf(value)
            return temp_dict
            #return {self.convert_to_utf(key): self.convert_to_utf(value) for key, value in input.iteritems()}
        elif isinstance(input, list):
            temp_list = []
            for element in input:
                temp_list.append(Utils.convert_to_utf(element))
            return temp_list
            #return [self.convert_to_utf(element) for element in input]
        elif isinstance(input, unicode):
            return input.encode('utf-8')
        else:
            return input

    #file io for json
    @staticmethod
    def write_to_file_json(filename, data, indent_value=4):
       #Converts to json and dumps the contents to a file
       with open(filename, 'w') as outfile:
           json.dump(data, outfile, indent=indent_value)
       outfile.close()

    @staticmethod
    def read_file_json(filename):
       #Converts to json and dumps the contents to a file
       with open(filename, 'r') as infile:
          data = json.load(infile)
       infile.close()
       return data

    @staticmethod
    def write_to_file(filename, data):
       outfile =  open(filename, 'w')
       outfile.write(data)
       outfile.close()


    @staticmethod
    def shuffle_in_unison(list1, list2):
        list1_shuf = []
        list2_shuf = []
        index_shuf = range(len(list1))
        shuffle(index_shuf)
        for i in index_shuf:
            list1_shuf.append(list1[i])
            list2_shuf.append(list2[i])
        del list1,list2
        return (list1_shuf,list2_shuf)
