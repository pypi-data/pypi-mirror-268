# Median housing value prediction

The housing data can be downloaded from https://raw.githubusercontent.com/ageron/handson-ml/master/. The script has codes to download the data. We have modelled the median house value on given housing data.

The following techniques have been used:

 - Linear regression
 - Decision Tree
 - Random Forest

## Steps performed

1. **Data Preparation**: The housing data is cleaned and prepared. Missing values are checked and imputed.

2. **Feature Engineering**: Features are generated, and variables are checked for correlation.

3. **Modeling**: Multiple sampling techniques are evaluated. The dataset is split into training and testing sets. Various modeling techniques, including linear regression, decision trees, and random forest, are tried and evaluated. The mean squared error (MSE) is used as the evaluation metric.


## How to Run the Code

Follow these steps to run the code:

### Environment Setup

1. **Create Environment**:

    ```bash```
    ```conda env create -f env.yml```

2. **Activate Environment**:

    ```bash```
    ```conda activate mle-dev```

3. **To excute the script**:
```python3 nonstandardcode.py```

4. **Flake 8 command**:
```flake8 nonstandardcode.py```

## How to Run the Code

Follow these steps to run the code:
1. create the environment
    ```conda env create --name mle-dev --file env.yml```

2. Activate the Conda environment:

   ```bash```
   ```conda activate mle-dev```
3. Install dependencies using the environment configuration file:
```conda env create -f env.yml```

or manually install the dependencies

```conda install numpy pandas matplotlib  scikit-learn```

## Execute the Scripts
### Run the following scripts sequentially:
````python ingest_data.py```
```python train.py train.csv```
```python score.py test.csv```

## Run Tests
### Run the unit tests and functional tests:
```python test_ingest_data.py```
```python test_train.py train.csv```
```python test_score.py test.csv```
```pytest```


## Code Formatting
### Use black, isort, and flake8 for code formatting:

Fix some errors by adding this to black:
```black --fast nonstandardcode.py #remove extra lines from the code```

Fix some errors by adding this to isort:
```isort --float-to-top nonstandardcode.py     #gets all the imports to the top of the file```

Fix some errors by adding this to flake8:
```flake8 --ignore=F401 --max-line-length=120```
nonstandardcode.py F401 are imports that are not required and increase max line to 120 words

## Generating Data and Models
### To generate training, testing, housing_prepared, and housing_labels files, run:
```bash```
```python ingest_data.py --log-level DEBUG --log-path ../logs/ingest_data.log```

--log-level DEBUG - USED FOR DEBUG MODE FOR STORING THE LOGS
--log--path - USED FOR STORING THE LOG DATA IN THE FILE SPECIFIED
--no-console-log -NOT TO PRINT THE LOG IN CONSOLE
THEN THE NEXT COMMAND LINE ARGUMENT IS THE 4 FILES THAT ARE GOING TO BE GENRATED

### To train machine learning models and generate pickle files, run:
Now to run the second train.py file so as to generate the pickle files for the data they are not uploaded since they are very large and github has limitations of 100mb
```python train.py --file-name train.csv --log-path ../logs/train.log --log-level DEBUG--log-level```
DEBUG - USED FOR DEBUG MODE FOR STORING THE LOGS
--log--path - USED FOR STORING THE LOG DATA IN THE FILE SPECIFIED
--no-console-log -NOT TO PRINT THE LOG IN CONSOLE
THEN THE NEXT COMMAND LINE ARGUMENT IS THE 4 FILES THAT ARE GOING TO BE GENRATED

### To score all four models based on RMSE values, run:
Now to score all the four models based on rmse values
```python score.py --file-name test.csv --log-path ../logs/score.log  --log-level```
DEBUG--log-level DEBUG - USED FOR DEBUG MODE FOR STORING THE LOGS
--log--path - USED FOR STORING THE LOG DATA IN THE FILE SPECIFIED
--no-console-log -NOT TO PRINT THE LOG IN CONSOLE
the answer will be printed in the console

## To install and configure the setup.py files we use the following line of code this will make all three of our files into packages and we can use them in testing
```pip install --upgrade setuptools```
```pip install --upgrade build```
```python -m build```
give all the dependencies in the setup.py files

### Documentation Generation
To generate Sphinx documentation:
Then to run functional test to see if all the files has been created correctly
python -m functional_test

### To generate the sphinx files for documentation
```pip install sphinx```
```sphinx-quickstart```
```sphinx-build -M html source source```
```sphinx-apidoc -o source .\src\house_price_prediction\```
```make html```
After running sphinx-quickstart, make necessary changes in the conf.py file and add modules inside the index.rst file, then run the last two lines.


This README provides detailed instructions for setting up the environment, running the code, formatting the code, generating data and models, installing and configuring packages, and generating documentation. Adjust paths and commands as needed based on your project setup.
