import time

from Knapsack import Knapsack
from read_dataset import ReadDataset


def main(dataset_dir,index):
    readvalues = ReadDataset(dataset_dir)
    totalIteration = 25000
    number_of_genes = 100
    C, weights, profits, opt = readvalues.values(index)
    a_knapsack = Knapsack(weights, profits, opt, number_of_genes, C, totalIteration)
    gene1 = a_knapsack.main_function()
    return gene1


if __name__ == '__main__':
    start_time1 = time.time()
    dataset_path = 'dataset'
    dataset_num = 8
    print("_______________________________")
    print("____Solving Knapsack Problem___")
    print('\n')
    for i in range(dataset_num):
        print("___________________________")
        print("__Working on P0{} Dataset__".format(i + 1))
        start_time = time.time()
        main(dataset_path, i)
        print("__________________________")
        print("P0{} Dataset Done!".format(i + 1))
        print("__________________________")
        print("Execution Time: %s seconds" % (time.time() - start_time))
        print('\n')
    print("________________________________")
    print("Total Execution Time: %s seconds" % (time.time() - start_time1))

