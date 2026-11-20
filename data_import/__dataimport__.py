from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
def find_num_and_visualize():
    project_path = Path(__file__).resolve().parent.parent
    folder_data = project_path / "data"

    data_test = pd.read_csv(folder_data / 'mnist_test.csv')

    number = int(input('podaj cyfre od 0 do 9: '))

    match = data_test[data_test.iloc[:,0] == number]

    row = match.sample(1).iloc[0, 1:].values

    image = row.reshape(28, 28)
    
    return number, image

