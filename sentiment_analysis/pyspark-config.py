# built from https://github.com/tthustla/setiment_analysis_pyspark/blob/master/Sentiment%20Analysis%20with%20PySpark.ipynb
##
import findspark
findspark.init()
import pyspark as ps
import warnings
from pyspark.sql import SQLContext
##

# create a SparkContext for all available CPUs
try:
    sc = ps.SparkContext('local[4]')
    sqlContext = SQLContext(sc)
    print("Created a SparkContext")
except ValueError:
    warnings.warn("SparkContext already exists in this scope")

##

df = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load('clean_tweet.csv')
##

(train_set, val_set, test_set) = df.randomSplit([0.98, 0.01, 0.01], seed = 2000)

##
from pyspark.ml.feature import HashingTF, IDF, Tokenizer, CountVectorizer
from pyspark.ml.feature import StringIndexer
from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator

##
# Try to fit the model using Pyspark's HashingTF
tokenizer = Tokenizer(inputCol="text", outputCol="words")
hashtf = HashingTF(numFeatures=2**16, inputCol="words", outputCol='tf')
idf = IDF(inputCol='tf', outputCol="features", minDocFreq=5) # minDocFreq removes sparse terms
label_stringIdx = StringIndexer(inputCol="target", outputCol="label")
pipeline = Pipeline(stages = [tokenizer, hashtf, idf, label_stringIdx])

pipelineFit = pipeline.fit(train_set)
train_df = pipelineFit.transform(train_set)
val_df = pipelineFit.transform(val_set)
# train_df.show(5)

##
lr = LogisticRegression(maxIter=100)
lrModel = lr.fit(train_df)
predictions = lrModel.transform(val_df)

##
evaluator = BinaryClassificationEvaluator(rawPredictionCol="rawPrediction")
evaluator.evaluate(predictions)
# 0.85, not bad

##
accuracy = predictions.filter(predictions.label == predictions.prediction).count() / float(val_set.count())
# 0.84

##
# Try to fit the model using Pyspark's CountVectorizer
tokenizer = Tokenizer(inputCol="text", outputCol="words")
cv = CountVectorizer(vocabSize=2**16, inputCol="words", outputCol='cv')
idf = IDF(inputCol='cv', outputCol="features", minDocFreq=5) # minDocFreq removes sparse terms
label_stringIdx = StringIndexer(inputCol="target", outputCol="label")
lr = LogisticRegression(maxIter=100)
pipeline = Pipeline(stages=[tokenizer, cv, idf, label_stringIdx, lr])

train_set2 = train_set
pipelineFit = pipeline.fit(train_set2)
predictions = pipelineFit.transform(val_set)
accuracy = predictions.filter(predictions.label == predictions.prediction).count() / float(val_set.count())
roc_auc = evaluator.evaluate(predictions)

##
