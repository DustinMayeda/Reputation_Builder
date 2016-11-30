# Reputation_Builder

This application will take in a stack exchange question and make a prediction about how many reputation points you would
stand to gain if you gave the top answer.

##Business Understanding

Are you interested in becoming a software developer or a data scientist?  Did you just graduate college or decide to make a career change and are worried about your lack of experience in software development or data analytics?  You could go back to school to get your masters or Ph.D. in machine learning to learn the intricacies of neural networks or in computational complexity to study the P vs NP problem and understand why the halting problem is unsolvable.  But, ain’t nobody got time for that!  There’s life to live, bills to pay, and a job to be had.  However, the question remains:  How can you demonstrate your knowledge, skill, and community spirit to employers?  Well, Stack Overflow and Cross Validated are sites that provide an ample opportunity to boost your reputation by answering questions.  Now, you’re probably asking yourself just how do I know if it is worth my time to answer a particular question?  With The Reputation Builder you’ll never have to wonder about that again.  The Reputation Builder is a predictive data analytics model which will take in a forum question and give you a prediction on how much reputation you stand to gain if you give the top or an average answer.  In no time your reputation will skyrocket and you’ll be hired.

##Data Understanding

To each Stack Overflow question we will collect metadata such as the number of viewcounts, reputation of the poster, number of comments, and of course the question itself.

To calculate the reputation to be gained from an answer we will need to query the number of upvotes, downvotes, and if it has been accepted or not.  The total reputation gain will then be equal to 10 * #upvotes - 2 * #downvotes + (15 if accepted and + 0 if not accepted).

##Data Collection

This predictive analytics problem does have a potential source of data leakage which is illustrated by the following situation.  If a question has a high number of views is it because it is "intrinsically" a good or interesting questions or is it because there is a high quality answer which has attracted many of the views?  In order to deal with this source of data leakage we first collect two week old questions with no answers from a data dump of Stack Overflow questions at data.stackexchange.com.  Then we scrape Stack Overflow in order to collect the current status of the questions including the number of reputation points the top answer received.

##Modeling

We will be using regression algorithms since the number of reputation points can take on a fairly large number of values.  To do the regression analysis we will use linear regression, ridge regression, decision tree, random forest, and boosted decision trees.  In order to compensate for the sensitivity of linear regression to outliers we will use ridge regression to reduce the variance.

Time permitting I would like to do a time series analysis of the lifecycle of a question.  This would give us more information on how the reputation points for the top answer and average answer change.  Trends in this change would inform the user about how fast and when to post an answer. 


Evaluation

Since we will have a large data set we can make a hold out test set along with a training and validation set on which to train and to tune the parameters of the ridge regression, random forest, and boosted decision tree.

Given that we are most concerned with accuracy we will evaluate the above models using the mean squared error.  However, if the scores do not differ very much we will prefer linear regression, decision tree, and ridge regression due to their interpretability which will allow for more targeted questioning.


Deployment

The model will be deployed in a flask app in which the user will first enter a site.  Then enter either a url to a question for which predictions will be given or tags for which a collection of recent questions will be evaluated and presented to the user in order of highest projected point value.  If there is continued interest in using the model weekly datasets could be collected in order to evaluate the model to see if it has gone stale as indicated by a large change in the mean squared error.  Given more of these tests we could start to figure out what a reasonable level of accuracy is for predicting expected reputation point gain of a question.



