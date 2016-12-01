# Reputation_Builder

This application will take in a stack exchange question and make a prediction about how many reputation points you would
stand to gain if you gave the top answer.

##Business Understanding

Are you interested in becoming a software developer or a data scientist?  Did you just graduate college or decide to make a career change and are worried about your lack of experience in software development or data analytics?  You could go back to school to get your masters or Ph.D. in machine learning to learn the intricacies of neural networks or in computational complexity to study the P vs NP problem and understand why the halting problem is unsolvable.  But, ain’t nobody got time for that!  There’s life to live, bills to pay, and a job to be had.  However, the question remains:  How can you demonstrate your knowledge, skill, and community spirit to employers?  Well, Stack Overflow and Cross Validated are sites that provide an ample opportunity to boost your reputation by answering questions.  Now, you’re probably asking yourself just how do I know if it is worth my time to answer a particular question?  With The Reputation Builder you’ll never have to wonder about that again.  The Reputation Builder is a predictive data analytics model which will take in a forum question and give you a prediction on how much reputation you stand to gain if you give the top or an average answer.  In no time your reputation will skyrocket and you’ll be hired.

##Data Understanding

To each Stack Overflow question we will collect metadata such as the number of viewcounts, reputation of the poster, number of comments, and of course the question itself.

To calculate the reputation to be gained from an answer we will need to query the number of upvotes, downvotes, and if it has been accepted or not.  The total reputation gain will then be equal to 10 * #upvotes - 2 * #downvotes + (15 if accepted and + 0 if not accepted).

##Data Collection

This predictive analytics problem does have a potential source of data leakage which is illustrated by the following situation.  If a question has a high number of views is it because it is "intrinsically" a good or interesting question or is it because there is a high quality answer which has attracted many of the views?  In order to deal with this source of data leakage we first collect questions with no answers which are two weeks old from a data dump of Stack Overflow questions at data.stackexchange.com.  Then we scrape Stack Overflow in order to collect the current status of the questions including the number of reputation points the top answer received.

##Modeling and Results

An out of the box linear regression and gradient boosting regressor trained on only the metadata yielded a mean absolute error of 25 and 17 respectively.  There are a large number of questions whose answers do not generate any reputation points which explains why linear regression did so poorly.  In order to deal with the large number of zeroes we have decided to model the situation in two steps.  The first step is to train a classifier which will distinguish zero from nonzero responses and the second will be to train a regressor on the nonzero and to combine them by computing the following expected value:

E[rep | X] = 0 * pr(rep = 0) + E[rep | X, rep > 0] * pr(rep > 0)

Combining the metadata and applying Tfidf vectorization to the body of the question our model with a tunned gradient boosted classifier and regressor yields a mean average error of 15 where as only applying a gradient boosted regressor to the metadata with TFidf vectorization yielded a mean average error of 16.  This result suggested that the better we can make our classifier the better mean average error our model will yield.

##Next Steps

Collect more granular data and do some more feature engineering in order to more accurately classify zero and nonzero questions.

Build a web application to give a ranking of the 100 most recent questions and to give a score to any particular question given its url.
