# Popularity Prediction using Inbuilt-Dictionary

- Dict.txt contains the dictionary of all the positive and negative words used. There are 104 positive and 104 negative words in the dictionary in such a way that words 0 - 103 are positive words and adding 104 to a positive words gives it's counter (negative) word.
- get_features.py uses the Dict.txt to generate features from comments of a particular movie trailer. It requires the path to an excel file where each row contains a comment about a movie trailer in English Language.
- Output.py is then used to train and test on the generated movie features. It requires the path to the combined features.xlsx file which will be made by get_features.py.
