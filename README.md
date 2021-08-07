# ANTON

Anton is a text sentiment analyser, named after the server farm in Silicon Valley.

## Inspiration

Machine learning is often a topic which many aspiring programmers deliberately avoid, as they think it is extremely complicated and requires a lot of advanced maths. However, I wanted to show everyone that machine learning models are not as difficult as they are often made out to be, starting with a simple text sentiment analyser. 

## What it does

You input a sentence, paragraph, or other text of any length, into the text box in the GUI and click the "Analyze!" button. If the main emotions conveyed through the text are positive, then the background turns green, wheras if the main emotions are negative, the background turns red.

## How I built it

I built this over a period of 2 days using Python and Tkinter. Over the first day, I collected suitable sample data and converted it into a form where it can be used in the classifier. I began to build the classifier and finished it on the second day, after which I used the remaining time to build a simple GUI using Tkinter.

## Challenges I ran into

This was my first move into machine learning,  so most of the time spent on this project was spent researching and reading documentation, blog posts, GitHub code, and drinking coffee. It was extremely important for me to properly understand the concepts behind what I was going to build, and not mindlessly copy someone else's code.

## Accomplishments that I'm proud of

The classifier has an astonishing 86% accuracy rate! I think a large part of this large success rate came down to the quality of the training data, and since I used popular sources, such as Stanford and Kaggle, the training data was representative of a large portion of the testing data. 

## What we learned

This was my first move into machine learning, and so I learned a lot by building this. In particular, I learned how to use Count Vectorizer to vectorize texts and Bernoulli Naive Bayes classifiers as a base for a custom model. 

## What's next for Text Sentiment Analyser

I would like to upgrade it so that it can recognize texts as neutral as well, as the majority of what is said online does not have any discernible strong emotions. Additionally, I would like to experiment with TensorFlow and other ML libraries and see how it changes the effectiveness of my model.
