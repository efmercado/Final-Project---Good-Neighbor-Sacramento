# Import libraries necessary for this project
import numpy as np
import pandas as pd

# Import supplementary visualizations code visuals.py
import visuals as vs

from sklearn.model_selection import ShuffleSplit
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import make_scorer
from sklearn.model_selection import GridSearchCV

# Pretty display for notebooks
# get_ipython().run_line_magic('matplotlib', 'inline')
def predict_house_value():

    # Load the Boston housing dataset
    data = pd.read_csv('../Data/real_estate.csv')
    prices = data['price']
    features = data[['beds','baths','square feet']]
        
    # Success
    print("Sacramento housing dataset has {} data points with {} variables each.".format(*data.shape))

    # ## Data Exploration
    # ### Implementation: Calculate Statistics

    np.amin(prices)

    # Minimum price of the data
    minimum_price = np.amin(prices)

    # Maximum price of the data
    maximum_price = np.amax(prices)

    # Mean price of the data
    mean_price = np.mean(prices)

    # Median price of the data
    median_price = np.median(prices)

    # Standard deviation of prices of the data
    std_price = np.std(prices)

    # Show the calculated statistics
    print("Statistics for Boston housing dataset:\n")
    print("Minimum price: ${}".format(minimum_price)) 
    print("Maximum price: ${}".format(maximum_price))
    print("Mean price: ${}".format(mean_price))
    print("Median price ${}".format(median_price))
    print("Standard deviation of prices: ${}".format(std_price))


    # ## Implementation: Define a Performance Metric

    # It is difficult to measure the quality of a given model without quantifying its performance over training and testing. This is typically done using some type of performance metric, whether it is through calculating some type of error, the goodness of fit, or some other useful measurement. For this project, you I ill be calculating the coefficient of determination, R2, to quantify the model's performance. The coefficient of determination for a model is a useful statistic in regression analysis, as it often describes how "good" that model is at making predictions.
    # 
    # The values for R2 range from 0 to 1, which captures the percentage of squared correlation between the predicted and actual values of the target variable. A model with an R2 of 0 is no better than a model that always predicts the mean of the target variable, whereas a model with an R2 of 1 perfectly predicts the target variable. Any value between 0 and 1 indicates what percentage of the target variable, using this model, can be explained by the features. A model can be given a negative R2 as well, which indicates that the model is arbitrarily worse than one that always predicts the mean of the target variable.


    def performance_metric(y_true, y_predict):
        """ Calculates and returns the performance score between 
            true and predicted values based on the metric chosen. """
        
        # TODO: Calculate the performance score between 'y_true' and 'y_predict'
        score = r2_score(y_true, y_predict)
        
        # Return the score
        return score


    # ## Implementation: Shuffle and Split Data
    # For the next implementation it is required to take the Sacramento housing dataset and split the data into training and testing subsets. Typically, the data is also shuffled into a random order when creating the training and testing subsets to remove any bias in the ordering of the dataset.

    # Shuffle and split the data into training and testing subsets
    X_train, X_test, y_train, y_test = train_test_split(features, prices, test_size=0.2, random_state = 42)

    # Success
    print("Training and testing split was successful.")


    # ## Training and Testing

    # ## Analyzing Model Performance
    # In this third section of the project, we'll take a look at several models' learning and testing performances on various subsets of training data. Additionally, we'll investigate one particular algorithm with an increasing 'max_depth' parameter on the full training set to observe how model complexity affects performance. Graphing the model's performance based on varying criteria can be beneficial in the analysis process, such as visualizing behavior that may not have been apparent from the results alone.
    # 
    # ## Learning Curves
    # The following code cell produces four graphs for a decision tree model with different maximum depths. Each graph visualizes the learning curves of the model for both training and testing as the size of the training set is increased. Note that the shaded region of a learning curve denotes the uncertainty of that curve (measured as the standard deviation). The model is scored on both the training and testing sets using R2, the coefficient of determination.

    # Produce learning curves for varying training set sizes and maximum depths
    # vs.ModelLearning(features, prices)


    # ## Learning the Data
    # If we take a close look at the graph with the max depth of 3:
    # 
    # As the number of training points increases, the training score decreases. In contrast, the test score increases.
    # 
    # As both scores (training and testing) tend to converge, from the 300 points treshold, having more training points will not benefit the model.
    # 
    # (Extra question): In general, with more columns for each observation, we'll get more information and the model will be able to learn better from the dataset and therefore, make better predictions.
    # 
    # ## Complexity Curves
    # The following code cell produces a graph for a decision tree model that has been trained and validated on the training data using different maximum depths. The graph produces two complexity curves — one for training and one for validation. Similar to the learning curves, the shaded regions of both the complexity curves denote the uncertainty in those curves, and the model is scored on both the training and validation sets using the performance_metric function.


    # vs.ModelComplexity(X_train, y_train)



    def fit_model(X, y):
        """ Performs grid search over the 'max_depth' parameter for a 
            decision tree regressor trained on the input data [X, y]. """
        
        # Create cross-validation sets from the training data
        cv_sets = ShuffleSplit(n_splits = 10, test_size = 0.20, random_state = 0)

        # Create a decision tree regressor object
        regressor = DecisionTreeRegressor()

        # Create a dictionary for the parameter 'max_depth' with a range from 1 to 10
        params = {'max_depth':[1,2,3,4,5,6,7,8,9,10]}

        # Transform 'performance_metric' into a scoring function using 'make_scorer' 
        scoring_fnc = make_scorer(performance_metric)

        # Create the grid search cv object --> GridSearchCV()
        # Make sure to include the right parameters in the object:
        # (estimator, param_grid, scoring, cv) which have values 'regressor', 'params', 'scoring_fnc', and 'cv_sets' respectively.
        grid = GridSearchCV(estimator=regressor, param_grid=params, scoring=scoring_fnc, cv=cv_sets)

        # Fit the grid search object to the data to compute the optimal model
        grid = grid.fit(X, y)

        # Return the optimal model after fitting the data
        return grid.best_estimator_


    # ### Making Predictions
    # Once a model has been trained on a given set of data, it can now be used to make predictions on new sets of input data. In the case of a decision tree regressor, the model has learned what the best questions to ask about the input data are, and can respond with a prediction for the target variable. We can use these predictions to gain information about data where the value of the target variable is unknown — such as data the model was not trained on.
    # 
    # ### Optimal Model
    #  - What maximum depth does the optimal model have?


    # Fit the training data to the model using grid search
    reg = fit_model(X_train, y_train)

    # Produce the value for 'max_depth'
    print("Parameter 'max_depth' is {} for the optimal model.".format(reg.get_params()['max_depth']))


    # ### Predicting Selling Prices
    # 
    #  - What price would we recommend each client sell his/her home at?
    #  - Do these prices seem reasonable given the values for the respective features?


    # Produce a matrix for client data
    client_data = [[5, 17, 15]]  # Client 3

    # Show predictions
    for i, price in enumerate(reg.predict(client_data)):
        print("Predicted selling price for Client {}'s home: ${:,.2f}".format(i+1, price))

        print("Predicted selling price for Client {}'s home: ${}".format(i+1, price))



    # test = vs.PredictTrials(features, prices, fit_model, client_data)

    return (price)

    




