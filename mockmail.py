"""
Building a Naive Bayes Spam filter with scikit-learn
"""
from sklearn.naive_bayes import MultinomialNB
import numpy as np


spam_email1="hello world I am a spam email. so spam.much wow"
spam_email2="hello again, I am a spam email."
spam_email3="hello world. it is time to spam you inbox.Like. spam it a lot."

ham_email1="this is your bank receipt."
ham_email2="some random totally unrelated work email"
ham_email3="someone has favorited your fanfiction. hooray!"

spam_emails=[spam_email1, spam_email2, spam_email3]
ham_emails=[ham_email1, ham_email2, ham_email3]

all_emails=spam_emails+ham_emails

def tokenizer(list_of_strings):
    email_dictionary=[]
    for email in list_of_strings:
        email_word=email.split()
        for word in email_word:
            if word not in email_dictionary:
                email_dictionary.append(word)
            else:
                pass
    return email_dictionary

feature_dictionary=tokenizer(all_emails)

def make_word_count_list(dictionary, email):
    """
    Outputs a matrix where each row represents one sample and each column one
    feature
    """
    #1. output a sample list
    sample=[]
    sample_dictionary={}
    email_words=email.split()
    for word in dictionary:
        sample_dictionary[word]=0
    for word in email_words:
        if word in sample_dictionary.keys():
            sample_dictionary[word]+=1
        else:
            pass
    #iterate over sample_dictionary and assign values to the list
    for word in sample_dictionary.keys():
        sample.append(sample_dictionary[word])
    return sample

matrix=[]
for email in all_emails:
    matrix.append(make_word_count_list(feature_dictionary, email))

print matrix

print np.array(matrix)
#make a label vector
#how many samples do you have
labels=[1,1,1]+[0,0,0]
labels_array=np.array(labels)
#adjust the matrix for the zero count problem
clf = MultinomialNB()
#fit the array using the data you have
clf.fit(np.array(matrix),labels_array)

new_email="hello beautiful. buy medication at www.buymeds.com"
word_count_new_email=make_word_count_list(feature_dictionary,new_email)
print word_count_new_email
print clf.predict_proba(word_count_new_email)



"""
Make a numpy matrix with all word counts
"""

email_box={}
email_box['inbox']=[]
email_box['sent']=[]
email_box['spam']=[]

def auto_populate_email_box():
    message1={'from':'random.mail@somemail.com',
               'to': 'jane@mockmail.com',
               'subject': 'coffee today?',
                'message': 'Hi Jane, meet at Gherkin for coffee?'}
    message2={'from':'bob.the.builder@awesomemail.com',
               'to': 'jane@mockmail.com',
               'subject': 'your folder',
                'message': 'Hello, you forgot your folder'}
    message3={'from':'banker@randombank.com',
               'to': 'jane@mockmail.com',
               'subject': 'Your bank statement',
                'message': 'Your bank statement for this month is available at '}
    email_box['inbox'].append(message1)
    email_box['inbox'].append(message2)
    email_box['inbox'].append(message3)


def print_message(email):
    """
    Prints out a pretty version of the email dict
    """
    print "From: " + email['from']
    print "To: " + email['to']
    print "Subject: " + email['subject']
    print "Message: " + email['message']

def print_inbox(email_box):
    print "*****INBOX*****"
    inbox_emails=email_box['inbox']
    for message in inbox_emails:
        print "*****************"
        print_message(message)

def calculate_stats(email_box):
    stats={}
    stats['inbox']=0
    stats['sent']=0
    stats['spam']=0
    for key in email_box.keys():
        stats[key]=len(email_box[key])
    return stats
def print_stats(stats):
    print "Your currently have:"
    for key in stats.keys():
        print "%d messages in your " + key



command_help={}
command_help['inbox']="Type 'inbox' to view recent incoming messages"
command_help['sent']="Type 'sent' to view sent messages'"
command_help['spam']="Type 'spam' to view recent spam messages"
command_help['manual']="Type 'manual' to manually send an email to your inbox"
command_help['help']="Type 'help' to print this help message"
command_help['quit']="Type 'quit' to exit MockMail"


def print_help():
    print "Welcome to your MockMail - your friendly command line based email client!"
    print "*************************************************************************"
    email_stats=calculate_stats(email_box)
    print_stats(email_stats)
    print "You can interact with MockMail using the following commands"
    for key in command_help.keys():
        print command_help[key]
#populate the email box
auto_populate_email_box()

def manual():
    """
    A method which allows the user to manually type an email to test the mail box spam filter
    """
    manual_message={}
    print "\n \n"
    print "************MANUAL EMAIL COMPOSITION***************"
    print "Welcome to manual email composition!"
    print "This functionality allows you to send an email to yourself to test the functionality of your spam filter"
    print "Please fill out the following fields to send your email"
    print "Message: "
    message = raw_input()
    while len(message)==0:
        print "Your message cannot be empty"
        message=raw_input()
    print "The message you typed is: "
    print message



def main():
    print_help()
    while True:
        print "Please enter a command:"
        command=raw_input()
        if command=="quit":
            print "See you soon!"
            break
        elif command=="inbox":
            print_inbox(email_box)
        elif command == "manual":
            manual()
        else:
            print "Sorry, I did not recognize the command"
            print "**************************************"
            print_help()


if __name__:main()
