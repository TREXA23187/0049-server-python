import json
from sklearn import datasets
import pandas as pd
import pickle
import numpy as np
import os

filename = 'rf.pkl'
current_fonder_path = os.path.split(os.path.realpath(__file__))[0]
model_path = os.path.join(current_fonder_path, "../..", "models", filename)

print(model_path)

iris = datasets.load_iris()


def load_model():
    loaded_model = pickle.load(open(model_path, 'rb'))
    return loaded_model


def get_pred(sepal_length, sepal_width, petal_length, petal_width):
    loaded_model = load_model()
    targets = ['setosa', 'versicolor', 'virginica']

    lst = [sepal_length, sepal_width, petal_length, petal_width]
    input_data = np.array([lst])

    result = loaded_model.predict_proba(input_data)
    # print(result)

    pred_concat = pd.concat([pd.Series(targets), pd.Series(['%.3f' % elem for elem in result[0]])], axis=1)
    predicts = pd.DataFrame(data=pred_concat)
    predicts.columns = ["class", "probability"]
    return predicts.reset_index(drop=True)


def launch_task(sepal_length, sepal_width, petal_length, petal_width):
    pred_model = get_pred(sepal_length, sepal_width, petal_length, petal_width)

    return json.loads(pd.DataFrame(pred_model).to_json(orient='records'))


# def get_task():
#     result = launch_task(request.args.get('sepal_length'), request.args.get('sepal_width'),
#                          request.args.get('petal_length'), request.args.get('petal_width'))
#
#     return make_response(jsonify(result), 200)

if __name__ == '__main__':
    # epal_length = 3.4 & sepal_width = 3.1 & petal_length = 3.4 & petal_width = 1
    result = launch_task(3.4, 3.1, 3.4, 1)
    # m = load_model()
    print(result)
