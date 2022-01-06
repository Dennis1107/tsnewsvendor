:warning: IN DEVELOPMENT for personal usage. No stable version yet.

`tsnewsvendor` is a `python module` that allows to calculate the `newsvendor quantity` from your `facebook prophet forecast`.

# Short intro into the Newsvendor Problem
"The newsvendor (or newsboy or single-period[1] or salvageable) model is a mathematical model in operations management and applied economics used to determine optimal inventory levels. It is (typically) characterized by fixed prices and uncertain demand for a perishable product. If the inventory level is {\displaystyle q}q, each unit of demand above {\displaystyle q}q is lost in potential sales. This model is also known as the newsvendor problem or newsboy problem by analogy with the situation faced by a newspaper vendor who must decide how many copies of the day's paper to stock in the face of uncertain demand and knowing that unsold copies will be worthless at the end of the day." (https://en.wikipedia.org/wiki/Newsvendor_model)

# Why using `tsnewsvendor`
In Time Series Forecasting & Machine Learning most of the focus is on finding an optimal forecast. You often find sales forecasting as one of the most common use cases. `tsnewsvendor` combines the forecasting algorithm `facebook prophet` in order to predict a `newsvendor quantity`.

# What `tsnewsvendor` does

* Using the cross-validation function from facebook prophet in order to derive important statistics for the newsvendor model (note: normally distributed residuals are assumed)
* Can be applied to a new prophet forecast in order to calculate the corresponding newsvendor quantity


# Prerequisites & Installation
* pandas
* prophet

Tested only on windows with anaconda and python 3.8.5
 

# Using `tsnewsvendor` 

## 1. Fit ProphetNewsvendor.fit()
Note: Any parameters of prophets cross-validation function can be used (https://facebook.github.io/prophet/docs/diagnostics.html#cross-validation)
```
tsprophet_fit = ProphetNewsvendor.fit(model=m, initial='365 days', period='365 days', horizon = '180 days')
```

## 2. Predict with Prophet & Apply ProphetNewsvendor.applynewsvendor()
```
forecast = m.predict(future)

forecast['newsvendor_result'] = forecast.apply(lambda row: ProphetNewsvendor.applynewsvendor(
    row['yhat'],
    tsprophet_fit[0],
    tsprophet_fit[1], 
    0.75, 
    0.2
    ), axis = 1)
```
Explanation of parameters:
* mean = row['yhat'] : Demand forecast from prophet
* mean_error = tsprophet_fit[0] : Mean error of our our prophet forecast derived by cross-validation,
* standard devation error = tsprophet_fit[1]: Standard deviation of our our prophet forecast derived by cross-validation, 
* Sales Price = 0.75, 
* Variable Cost = 0.2


**Developers:**

[Dennis Hartel](https://github.com/Dennis1107) 💻
 
