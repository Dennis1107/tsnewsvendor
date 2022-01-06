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
 

# Using `Jupybricks` 

Jupybricks is a command line tool can be used. More information with:
```
jupybricks --help
```

## For single file conversion:

Transforming databricks .py file to jupyter .ipynb:
```
jupybricks databricks-to-jupyter --input-filename <example_files/databricks_example.py> --output-filename <example_files/jupyter_example.ipynb>
```
Transforming jupyter .ipynb file to databricks .py file
```
jupybricks jupyter-to-databricks --input-filename <example_files/jupyter_example.ipynb> --output-filename <example_files/databricks_example.py>
```

## For multiple files:
:warning: it is necessary to have a file named convert_list.json in your root folder from where you call jupybricks. Jupybricks uses this file in order to know which files are used for mapping .py files with the corresponding .ipynb files.
As an example. 
```
{
    "example_files/jupyter_example.ipynb" : "example_files/databricks_example.py"    
}
```

If you have the convert_list.json properly set up then you can run the cli commands without paramets:
```
jupybricks databricks-to-jupyter
```
```
jupybricks jupyter-to-databricks
```

# Next Steps
Feel free to reach out to give advice or feature requests.
Planned next steps:
- [ ] adding unit tests
- [ ] adding mkdocs documentation
- [ ] testing on different OS
- [ ] heavy testing on different kind of databricks formats
- [ ] Github Actions & pre commit hooks
- [ ] installable version over pip

**Developers:**

[Dennis Hartel](https://github.com/Dennis1107) 💻
 
