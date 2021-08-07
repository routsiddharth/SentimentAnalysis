from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB

def preprocessing_step(datasets: list) -> list:

    filepath = "/Users/siddharthrout/Desktop/Important/SentimentAnalysis/Analyzer/"

    def process_dataSet1() -> list:

        # Getting Data From File

        with open(f"{filepath}DataSet1/reviews.txt", "r") as text_file:
            data = text_file.read().split('\n')

        # Converting "REVIEW \t SCORE" to ["REVIEW", "SCORE"]

        processed_data = []

        for single_data in data:
            if len(single_data.split("\t")) == 2 and single_data.split("\t")[1] != "":
                processed_data.append(single_data.split("\t"))

        return processed_data


    def process_dataSet2() -> list:

        # Getting Data in File

        processed_data = []

        with open(f"{filepath}DataSet2/text.txt", "r") as text_file:
            text = text_file.read().split('\n')

        with open(f"{filepath}DataSet2/scores.txt", "r") as text_file:
            scores = text_file.read().split()

        # Forming ["REVIEW", "SCORE"]

        for i in range(len(text)):
            t = text[i].split(",")[1]

            # Getting Avg of Scores

            s = [int(num) for num in scores[i].split(",")[1:4]]
            s = (sum(s)/len(s) - 1)/24
            s = str(round(s, 2))

            processed_data.append([t, s])

        return processed_data

    def process_dataSet3() -> list:

        processed_data = []

        with open(f"{filepath}DataSet3/text.txt", "r") as text_file:
            text = text_file.read().split("\n")

        for i in range(len(text)):
            try:
                values = text[i].split(",")

                t = values[1][1:-1]
                s = "0" if values[0][1:-1] == "1" else "1"

                processed_data.append([t, s])

            except:
                pass

        return processed_data

    def process_dataSet4() -> list:

        with open(f"{filepath}DataSet4/scores.txt", "r") as f:
            lines = f.read().split("\n")

        lines = [line.split(",") for line in lines]

        processed_data = []

        for line in lines:
            try:
                processed_data.append([line[4], "1" if line[1] == '"positive"' else "0"])

            except:
                pass

        return processed_data

    rawData = [[], process_dataSet1(), process_dataSet2(), process_dataSet3(), process_dataSet4()]
    data = []

    for i in datasets:
        data.extend(rawData[i])

    return data

def training_step(data, vectorizer):

    training_text = []
    training_result = []

    for text, result in data:
        training_text.append(text)
        training_result.append(result)

    training_text = vectorizer.fit_transform(training_text)

    return BernoulliNB().fit(training_text, training_result)

def analyse_text(classifier, vectorizer, text):
    return classifier.predict(vectorizer.transform([text]))

def main(text, datasets: list = [1, 2, 4]):

    acceptableDatasets = [1, 2, 3, 4]

    if not all([i in acceptableDatasets for i in datasets]):
        datasets = [1, 2, 3, 4]
    else:
        datasets = datasets

    training_data = preprocessing_step(datasets)
    vectorizer = CountVectorizer(binary='true')
    classifier = training_step(training_data, vectorizer)

    if type(text) == list:

        scores = []

        for i in range(len(text)):
            if type(text[i]) == str:
                score = analyse_text(classifier, vectorizer, text[i])
                scores.append(str(score[0]))

        return scores

    elif type(text) == str:
        score = analyse_text(classifier, vectorizer, text)
        return str(score[0])

    else:
        raise Exception("Type Error: Parameter \"text\" must be type str or list")