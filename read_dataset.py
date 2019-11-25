import fnmatch
import os
import re


class ReadDataset():
    """
    main dataset read class
    """

    def __init__(self, dataset_dir):
        self.dataset_dir = dataset_dir
        self.totalfile = 32
        self.C = []
        self.W = []
        self.P = []
        self.S = []

    def atoi(self, text):
        """
        Takes a file and checks for integer values in the file name
        :param text: Input file
        :return: Integer values in the file name
        """
        return int(text) if text.isdigit() else text

    def natural_keys(self, text):
        '''
        alist.sort(key=natural_keys) sorts in human order
        http://nedbatchelder.com/blog/200712/human_sorting.html
        (See Toothy's implementation in the comments)
        '''
        return [self.atoi(c) for c in re.split(r'(\d+)', text)]

    def files(self):
        """
        Depending on the number of the files, this function will enter a directory
        and search for similar filenames and append them under different lists.
        :return: Lists
        """
        for i in range(self.totalfile):
            for root, dirnames, filenames in os.walk(self.dataset_dir):
                for filename in fnmatch.filter(filenames, 'p0{}_c.txt'.format(i)):
                    self.C.append(os.path.join(root, filename))
                for filename in fnmatch.filter(filenames, 'p0{}_w.txt'.format(i)):
                    self.W.append(os.path.join(root, filename))
                for filename in fnmatch.filter(filenames, 'p0{}_p.txt'.format(i)):
                    self.P.append(os.path.join(root, filename))
                for filename in fnmatch.filter(filenames, 'p0{}_s.txt'.format(i)):
                    self.S.append(os.path.join(root, filename))
            self.C.sort(key=self.natural_keys)
            self.W.sort(key=self.natural_keys)
            self.P.sort(key=self.natural_keys)
            self.S.sort(key=self.natural_keys)
        return self.C, self.W, self.P, self.S

    def removeWhiteSpace(self, file):
        """
        Removes white spaces in the values
        :param file: List
        :return: White space less values
        """
        length = len(file)
        for i in range(length):
            file[i] = file[i].replace(" ", "")
        return file

    def stringToInt(self, file):
        """
        Converts strings to integers in a list
        :param file: String
        :return: Integers
        """
        length = len(file)
        files = []
        for i in range(length):
            file[i] = int(file[i])
            files.append(file[i])
        return files

    def values(self, index):
        """
        Takes an index and returns the values of different lists.
        :param index: Input index
        :return: Values of the different lists
        """
        c, w, p, s = self.files()
        c_val = int(open(c[index]).read())
        w_val = [line.rstrip('\n') for line in open(w[index])]
        p_val = [line.rstrip('\n') for line in open(p[index])]
        s_val = [line.rstrip('\n') for line in open(s[index])]

        ## Remove White Spaces. Original dataset has white spaces in weight and profit values.

        w_val = self.stringToInt(self.removeWhiteSpace(w_val))
        p_val = self.stringToInt(self.removeWhiteSpace(p_val))
        s_val = self.stringToInt(self.removeWhiteSpace(s_val))
        return c_val, w_val, p_val, s_val
