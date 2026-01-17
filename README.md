# Word Count - MapReduce Project

## Overview
This is a Hadoop MapReduce word count application that processes text files to count the frequency of each word. It demonstrates the fundamental concepts of distributed data processing using the MapReduce programming model.

## Project Structure
```
wordcount/
├── README.md              # This file
├── mapper.py              # Mapper script - emits words with count 1
├── reducer.py             # Reducer script - aggregates word counts
├── input/                 # Input data directory
│   └── file.txt          # Sample input file
└── DOCKER-and-HADOOP.ppsx # Presentation slides
```

## Files Description

### mapper.py
The mapper reads input text and emits key-value pairs in the format: `word\t1`
- Reads text from stdin
- Splits text into words
- Outputs each word with an initial count of 1

### reducer.py
The reducer aggregates counts for each word received from the mapper
- Reads sorted key-value pairs from mapper output
- Accumulates counts for identical words
- Outputs final word counts in format: `word\tcount`

### input/file.txt
Sample input file containing text to be processed for word counting

## Prerequisites
- Hadoop installed and configured
- Python 3.x
- Docker (optional, for containerized execution)

## How to Run

### With Hadoop
```bash
# Set up input
hadoop fs -put input/file.txt /user/hadoop/input/

# Run MapReduce job
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input /user/hadoop/input/ \
  -output /user/hadoop/output/ \
  -mapper mapper.py \
  -reducer reducer.py

# View results
hadoop fs -cat /user/hadoop/output/part-00000
```

### Local Testing (Without Hadoop)
```bash
# Test mapper
cat input/file.txt | python mapper.py | sort | python reducer.py
```

## Output Format
The output consists of one line per unique word:
```
word1    count1
word2    count2
word3    count3
```

## Notes
- The mapper and reducer scripts are designed to work with Hadoop Streaming
- Words are case-sensitive (modify mapper.py if case-insensitive counting is needed)
- The reducer expects input to be sorted by word (automatically handled by Hadoop)
