
import matplotlib.pyplot as plt
import pandas

from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

data = pandas.read_csv('data.txt', sep='\t', names=['command', 'feedback'])
regr = linear_model.LinearRegression()
regr.fit(data[['command']], data.feedback)
pred = regr.predict(data[['command']])

print("Coefficients: %s, rooted mean sqaured error: %.2f, R^2 score: %.2f" % (regr.coef_,  mean_squared_error(data.feedback, pred)**0.5, 
                                                                             r2_score(data.feedback, pred)))

# Plot outputs
fig, axs = plt.subplots(2)
fig.suptitle('Servo Motor Command vs Feedback (Error: Feedback - Linear Regression Prediction)')

axs[0].scatter(data.command, data.feedback, color="black")
axs[0].plot(data.command, pred, color="blue", linewidth=3)
axs[1].plot(data.feedback - pred, color="red", linewidth=3)
plt.savefig('data.png')
plt.show()

pass



# import pandas
# import matplotlib.pyplot as plt
# import statsmodels.api as sm 
# import statsmodels.formula.api as smf
# from statsmodels.formula.api import ols 
# from statsmodels.datasets import utils as du

# fig = plt.figure(figsize=(8, 6))
# crime_data = sm.datasets.statecrime.load_pandas()
# results = smf.ols('murder ~ hs_grad + urban + poverty + single', data=crime_data.data).fit()
# sm.graphics.plot_regress_exog(results, 'poverty', fig=fig)
# plt.show()

# data = pandas.read_csv('data.txt', sep='\t', names=['command', 'feedback'])
# data['dummy'] = 0
# data = du.process_pandas(data, endog_idx=0, exog_idx=[1,2], index_idx=0)
# # # plt.scatter(data.Command, data.Feedback)
# # plt.plot(data.Command.values, data.Feedback.values, '.')
# # plt.show()


  
# # fit simple linear regression model 
# linear_model = smf.ols('feedback ~ command', data=data.data).fit() 
# # linear_model = sm.OLS(data.Feedback.values, sm.add_constant(data.Command.values)).fit()
# print(linear_model.summary()) 
# # Expected potentiometer ranges 300 degree for value from 0 to 1024, hence slope is 1024/300 = 3.4133. 
# # The test data has a fitted slope of -3.4791 (about 2% difference).
  
# # modify figure size 
# fig = plt.figure(figsize=(14, 8)) 
  
# # creating regression plots 
# fig = sm.graphics.plot_regress_exog(linear_model, 1, fig=fig) 
