import xml.etree.cElementTree as etree
from pprint import pprint as pp
from utils import *
'''
    function parses the xml file and returns a list of dictionaries.
    Each dict is of the following format
    {'AcceptedAnswerId': '13',
     'AnswerCount': '2',
     'Body': '<p>This is a common question by those who have just rooted their phones.  What apps, ROMs, benefits, etc. do I get from rooting?  What should I be doing now?</p>\n',
     'CommentCount': '0',
     'CommunityOwnedDate': '2011-01-25T08:44:10.820',
     'CreationDate': '2010-09-13T19:16:26.763',
     'FavoriteCount': '119',
     'Id': '1',
     'LastActivityDate': '2013-09-03T05:57:21.440',
     'LastEditDate': '2013-04-05T15:50:48.133',
     'LastEditorUserId': '16575',
     'OwnerUserId': '10',
     'PostTypeId': '1',
     'Score': '172',
     'Tags': '<rooting><root>',
     'Title': "I've rooted my phone.  Now what?  What do I gain from rooting?",
     'ViewCount': '207478'
     }
     Import this file into your code and use it directly
'''
def parse_xml_file(filename):
    infile = open(filename, 'r')
    context = etree.iterparse(infile)
    parsed_rows = []
    for event,elem in context:
        parsed_row = dict(elem.attrib)
        parsed_row['body'] = Utils.strip_html_tags(parsed_row['body'])
        parsed_rows.append(parsed_row)
        elem.clear()
    infile.close()
    return parsed_rows

def parse_xml_and_separate_labels(filename):
    infile = open(filename, 'r')
    context = etree.iterparse(infile)
    parsed_rows = []
    labels=[]
    for event,elem in context:
        parsed_row = dict(elem.attrib)
        if "PostTypeId" in parsed_row.keys() and parsed_row['PostTypeId'] == '1':
            if 'Body' in parsed_row:
                parsed_row['Body'] = Utils.strip_html_tags(parsed_row['Body'])
            else:
                parsed_row['Body'] = ''
            parsed_rows.append(parsed_row)
            if 'AcceptedAnswerId' in parsed_row and parsed_row['AcceptedAnswerId'] is not None:
                labels.append(1)
            else:
                labels.append(0)

        elem.clear()
    infile.close()
    return (parsed_rows, labels)



'''
def main():
    rows = parse_xml_file("../data/Posts.xml")

if __name__ == "__main__":
    main()
'''
