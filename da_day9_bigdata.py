# -*- coding: utf-8 -*-
"""DA_Day9_BigData.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MbHIKUER8Av7bM11GAQQ5x2b2nwZ1OnE

Pyspark
"""

#Install Apache spark 3.0.3 with Hadoop 2.7
!pip install pyspark==3.0.3

#import sparksession from spyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

#create a sparksession #job
spark = SparkSession.builder \
        .appName("DistributedComputingExample") \
        .getOrCreate()

#Load data from CSV file
file_path='/content/diabetcsv.csv'
df=spark.read.csv(file_path,header=True,inferSchema=True)
    #loading file
#Show the DataFrame
df.show()

#Calculate mean mass per age group
mean_mass_per_age_group=df.groupBy("insu").agg(avg("mass").alias("Mean_Mass"))
#Show the mean mass per age group
mean_mass_per_age_group.show()
df.show()
#Stop the SparkSession
spark.stop()