"""
A Toy Spam Filter using the BernoulliNB classifier in Scikit-learn
Template
"""

#1.1 Import the BernoulliNB class from the Scikit-learn package

#1.2. Import Numpy

#1.3 Import the text_adapter



#3. Here is the training data for your classifier
spam_emails=["Hello send your password", "hello please click link", "click link",
"your password here", "send password"]
ham_emails=["hello reset your password", "password email", "warm hello" ]

#4. Prepare your data

#concatenate the training data and assign it to a variable

#make a numpy array of training labels

)
#5. Generate the training data matrix, store it in a variable and print it out


#6. Create a classifier by calling an instance of BernoulliNB

classifier=BernoulliNB()

#7.Train the classifier by calling the fit function


#Now you have a trained classifier!

#8. Test the classifier by calculating the probability that a new email is spam

test_email="hello please send password"
