import nltk
nltk.download('stopwords')
nltk.download('wordnet')

#We use sklearn library for machine learning based analysis. Sklearn support many machine learning approaches such as SVM, nearest neighbour, random forest, k-means and many more. You can find more information about sklearn in this webpage: https://scikit-learn.org/stable/

# Importing libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import re
import numpy as np
from collections import Counter

def predict_text(input_text):

    stop = set(stopwords.words('english'))
    exclude = set(string.punctuation)
    lemma = WordNetLemmatizer()

    #Yup, when you work with text, text cleaning is a crucial task! This simple function allows you to clean doc. You can modify this function to fit your text cleaning processes."""

    # Cleaning the text sentences so that punctuation marks, stop words & digits are removed
    def clean(doc):
        stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
        punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
        normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
        processed = re.sub(r"\d+","",normalized)
        y = processed.split()
        return y

    #Document Representations used in this example is Tf-Idf. You already learn this method last 2 weeks.
    #Term frequency and inverse document frequency (tf-idf) is a word weighing scheme. The tf-idf value increases as the number of times a word appears in a document. So, it helps to reflect the importance of a word in a corpus.

    import pandas as pd

    #"""Let's read our data!"""

    # read traning dataset
    dataset = pd.read_csv('combined_file_cleaned_final.csv')
    print("Data\n",dataset)

    train_clean_sentences = []

    #"""Text Preprocessing - for each document in our dataset, we will give it to clean function above. The document can be found in dataset['Text'] <- inside column 'Text'"""

    for line in dataset["cleaned"]:
        line = line.strip()
        cleaned = clean(line)
        cleaned = ' '.join(cleaned)
        train_clean_sentences.append(cleaned)

    #"""Output after text preprocessing"""

    #print(train_clean_sentences)

    #"""Text representation by using TFIDF"""

    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(train_clean_sentences)

    #"""Let's split the data into training our model. For easy understanding, we will label our dataset to 0, 1 & 2."""

    # Creating true labels for 30 training sentences
    y_train = dataset["target"]

    #"""Training the Classification (K-NN) & Clustering (K-Means) models.
    #Output for k-NN classification is category membership. Texts are assigned to class that is most common among their k nearest neighbours.
    #Clustering determines the grouping of a set of data.In K-Means clustering, the 'K' cluster centers are the centroid of data points of a cluster.


    # Classification the document with KNN classifier
    modelknn = KNeighborsClassifier(n_neighbors=5)
    modelknn.fit(X,y_train)

    #"""Testing on Unseen Texts.
    #This is to test the trained model. It is tested using 3 text sentences.

    # Predicting it on test data : Testing Phase
    test_sentences = ["""I feel so sad because i can't be happy, and that makes me more unhappy  """, """I went to church with my mom and a huge chunk of the sermon was basically if youre  its because your faith is weak and . this is why I dont go to church or tell my mom Im on antidepressants ?"""]

    test_clean_sentence = []
    for test in test_sentences:
      cleaned_test = clean(test)
      cleaned = ' '.join(cleaned_test)
      cleaned = re.sub(r"\d+","",cleaned)
      test_clean_sentence.append(cleaned)

    Test = vectorizer.transform(test_clean_sentence)

    true_test_labels = ['non-depressed','depressed']
    #classification
    predicted_labels_knn = modelknn.predict(Test)
    #clustering
    predicted_labels_kmeans = modelkmeans.predict(Test)

    st.inputText()

    print ("\nBelow 3 sentences will be predicted against the learned nieghbourhood and learned clusters:\n1. ",\
    test_sentences[0],"\n2. ",test_sentences[1],"\n3. ")
    print ("\n-------------------------------PREDICTIONS BY KNN------------------------------------------")
    print ("\n",test_sentences[0],":",true_test_labels[np.int(predicted_labels_knn[0])],\
    "\n",test_sentences[1],":",true_test_labels[np.int(predicted_labels_knn[1])])

"""From the output above, we can see that all of the 3 sentences tested are correctly clustered and classified into categories."""
