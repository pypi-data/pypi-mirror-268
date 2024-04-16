
import os
import sys
import filecmp
import logging

def same_folders(dcmp):
    if dcmp.diff_files:
        return False
    for sub_dcmp in dcmp.subdirs.values():
        return same_folders(sub_dcmp)
    return True


class my_dircmp(filecmp.dircmp):

    def __init__(self, dir_a, dir_b):
        pass

class MyComparisonReport(filecmp.dircmp):

    def __init__(self, dir_a, dir_b):
        pass


    def rec(self):

        self.my_report = {}

        self.dir_a_name
        self.dir_b_name

        self.dir_a = []
        self.dir_b = []
        self.summary = {}

def populate(self):
    """

    :return:
    """

    for my_dir in [self.dir_a_name, self.dir_b_name]:
        if not os.path.isdir(self.dir_a_name):
            logging.error(''.format(my_dir))
            sys.exit()

    comparison = filecmp.dircmp(dir_1, dir_2)


class Compare(filecmp.dircmp):

    def __init__(self, dir_a, dir_b):

        self.dir_a_name
        self.dir_b_name

        self.dir_a = []
        self.dir_b = []
        self.summary = {}

        for my_dir in [self.dir_a_name, self.dir_b_name]:
            if not os.path.isdir(self.dir_a_name):
                logging.error(''.format(my_dir))
                sys.exit()

    def populate(self):
        pass


def get_all_files(root_dir):

    all_files = []
    for path, subdirs, files in os.walk(root_dir):
        for name in files:
            print('\t', path , name)
            all_files.append(os.path.join(path, name))

    return all_files


if __name__ == '__main__':

    # Ref Data
    base_dir = os.path.expandvars('$HOME/JUICE_SO_new/MAPPS/REGRESSION_TEST')
    dir_2 = os.path.join(base_dir, 'REF_DATA/Europa_flyby_CDR_crema_3_1_2018')
    # dir_2 = os.path.expandvars('$HOME/JUICE_SO_new/MAPPS/REGRESSION_TEST/REF_DATA/Ganymede_500k_2018')
    # dir_2 = os.path.expandvars('$HOME/JUICE_SO_new/MAPPS/REGRESSION_TEST/REF_DATA/jupiter')

    dir_1 = os.path.join(base_dir, 'TEST_DATA_SET/Jupiter_perijove_2018/eps_output')

    print(os.listdir(dir_1))
    print(os.listdir(dir_2))

    get_all_files(dir_1)

    print('\n ################ Comparison 1')
    comparison = filecmp.dircmp(dir_1, dir_2)
    # comparison.report_full_closure()
    print('file only in {}:\n{}'.format(dir_2, comparison.left_only))
    print('file only in {}:\n{}'.format(dir_1, comparison.right_only))
    print('same files: {}'.format(comparison.common_files))
    print('different file: {} '.format(comparison.same_files))


    # print('\nComparison 2')
    # comparison = filecmp.dircmp(os.path.dirname(dir_1), os.path.dirname(dir_2))
    # comparison.report_full_closure()
    #
    # print('End Comparison 2\n')

    # print ('File only in new output: {}'.format(comparison.left_only))
    # print ('File not in new output: Only in ref data {}'.format(comparison.right_only))
    #
    # print comparison.common_dirs
    # print comparison.common_files
    # print comparison.same_files
    # print 'diff ', comparison.diff_files

    # for f in comparison.subdirs.keys():
    #     element = comparison.subdirs[f]
    #     print element.common_dirs
    #     print element.common_files
    #     print element.same_files
    #     print 'diff ', element.diff_files

    # print('\nFile Comparison')
    # file_1 = os.path.join(dir_2, 'data_rate_avg.out')
    # file_2 = os.path.join(dir_1, 'data_rate_avg.out')
    # print filecmp.cmp(file_1, file_1)
    # print filecmp.cmp(file_1, file_2)
    #
    # base_dir = os.path.dirname(dir_2)
    # print '\n## REF DATA root directory: {}\n'.format(base_dir)
    # for f in get_all_files(base_dir):
    #     print f.replace(base_dir, '')


