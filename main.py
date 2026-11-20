
from data_import.dataimport import find_num_and_visualize
import matplotlib.pyplot as plt

def main():
    number, image = find_num_and_visualize()
    plt.imshow(image, cmap='gray')
    plt.title(f'your number: {number}')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
