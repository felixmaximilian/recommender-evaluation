# recommender-evaluation

# About
A couple of performance measures for recommender systems.
# How to use it in your Pyspark Code

You can import the module directly from S3 using the
[addPyFile method of your spark context](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.SparkContext.addPyFile):

```python
sc.addPyFile("s3://is24-data-science-infrastructure/emr/python/lib/latest/recommender_evaluation.zip")
```

```python
sc.addPyFile("s3://is24-data-science-infrastructure/emr/python/lib/v1.0-21/recommender_evaluation.zip")
```

Afterwards you can import from this module as you would from every other module:

```python
from recommender_kpi.evaluation import novelty_metric
```


# How to contribute

Feel free to clone this repository and commit your own functions. Every new
commit triggers a TeamCity
[build](http://teamcity.rz.is/viewType.html?buildTypeId=DataScience_recommender-evaluation)
which packages a new version out of the sources found at src/main/python and
loads it into S3. However, you have to make sure that your source code is
covered with unit tests at src/unittest/python. Every failed test as well as a
source code coverage of less than 70% cause the build to fail. The automated
build and tests are performed with python 2.7.


# How to build locally

If you like to test your changes prior to committing you can setup a local build
environment easily:

```bash
virtualenv -p python2.7 venv
source venv/bin/activate
pip install pybuilder
```

Afterwards you can package (incl. running the tests and checking the code
coverage) locally:

```bash
pyb -X
```
