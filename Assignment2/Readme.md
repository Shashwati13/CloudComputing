Author: 
Shashwati Diware (sdiware@iu.edu)

ECC Assignment 2:
Below Readme file is a guide to the PySpark installation and assignment 2 questions

Tools Used:

PySpark
Jupyter Notebook
Docker
Python 3.x


DataSet Used:

NYC Parking Violations - I have taken 15 Nov 2023 latest dataset.
NBA Shot Logs - I have taken the dataset mentioned in assignment.

Data Processing: 
I have performed some data processing on null values.


Files:

Assignment2_NBA.ipynb - This file has code for NBA logs for question 1 to 2.
Assignment2_NYC.ipynb - This file has code for NYC violation for question 1 to 5.

Packages Used:

import pyspark.sql.functions as psf
from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import VectorAssembler
from pyspark.sql import SparkSession 
from pyspark.sql import SparkSession, SQLContext, Window
from pyspark.sql.functions import when, count, col, sum, regexp_replace
from pyspark import SparkContext
from pyspark.sql.types import IntegerType
import os
import numpy as np
import pandas as pd
import shutil
import pyspark


