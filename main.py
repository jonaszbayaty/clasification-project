
from data_import.dataimport import find_num_and_visualize
import matplotlib.pyplot as plt

def main():
    number, image = find_num_and_visualize()
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
