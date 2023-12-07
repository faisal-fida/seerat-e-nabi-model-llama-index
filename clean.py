with open("data/dataset.txt", "r") as f:
    data = f.readlines()

data = [x.strip() for x in data]

# preprocess data
import re

# remove all non-alphanumeric characters
data = [re.sub(r"\W+", " ", x) for x in data]
# remove all empty lines
data = [x for x in data if x != ""]
# remove all lines with less than 3 words
data = [x for x in data if len(x.split()) >= 3]

# save preprocessed data
with open("data/dataset_preprocessed.txt", "w") as f:
    f.write("\n".join(data))
