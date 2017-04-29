# Measures-of-Vector-Similarity
Measures of Vector Similarity Between Word Co-Occurrance vectors V and W: Cosine, Jaccard, and Dice

vectorSimilarityFunctions.py contains three functions that are used to measure the vector similarity: Cosine, Jaccard, and Dice. The functions come from "Speech and Language Processing: A introduction to natural language processing" by Jurafsky and Martin. It only contains the 

similarityText.py is a small script that has 3 different pairs of vectors and it runs those pairs on all 3 of the similarity measures. It will display the results up to the nearest thousandth. The two functions in the file are helper functions. One rounds the result passed to the nearest thousandth and the other makes it easier to run all the measures on a pair of vectors.

If you wish to run the tests, make sure to have both of the files in the same directory. Then run the test only since the vectorSimilarityFunctions.py only contains the functions and no runnable code.

------------------------------------------------------------------------------------------------------------------------------------------
MORE INFO:

The formaulas can be found here on page 763: http://stp.lingfil.uu.se/~santinim/ml/2014/JurafskyMartinSpeechAndLanguageProcessing2ed_draft%202007.pdf

You can find information for each measure below:

Cosine Similarity: https://en.wikipedia.org/wiki/Cosine_similarity

Jaccard Similarity: https://en.wikipedia.org/wiki/Jaccard_index#Generalized_Jaccard_similarity_and_distance

Dice Similarity: https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient
