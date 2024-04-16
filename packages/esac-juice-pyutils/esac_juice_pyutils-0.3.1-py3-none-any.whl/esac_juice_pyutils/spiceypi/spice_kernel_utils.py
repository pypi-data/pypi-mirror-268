"""
Created on April, 2021

@author: Claudio Munoz Crego

Python module including Spice kernel utils
"""

import os
import sys
import shutil
import logging
import urllib
import wget

import spiceypy as spi


def print_kernel_info():
    """
    Include the list of kernel loaded

    """
    kernel_info = get_kernel_loaded_info()
    for ele in kernel_info[1:]:
        logging.debug('\t{:^6}:{}'.format(ele[1], ele[0]))


def get_kernel_loaded_info():
    """
    Returns the current list of kernel loaded in spice

    """
    kernel_info = []
    kcount = spi.ktotal('All')
    kernel_info.append(kcount)
    for i in range(kcount):
        kernel_info.append(spi.kdata(i, 'All', 256, 256, 256))

    return kernel_info


def update_path_val_in_mk_file(path_to_metakernel, kernel_root_dir):
    """
    Update PATH_VALUES within a given mk file

    :param path_to_metakernel: metakernel file path
    :param kernel_root_dir: path to the spice kernel base directory (local copy)
    :return des: the path of the updated kernel file
    """

    if not os.path.exists(path_to_metakernel):
        logging.error('metakernel file does not exist: {}'.format(path_to_metakernel))
        sys.exit()

    if not os.path.exists(kernel_root_dir):
        logging.error('directory does not exist: {}'.format(kernel_root_dir))
        sys.exit()

    fi = open(path_to_metakernel, 'r')
    lines = fi.readlines()
    fi.close()

    fo = open(path_to_metakernel, 'w')
    for line in lines:

        if 'PATH_VALUES' in line:

            line_without_space = line.replace(' ', '').replace('\t', '')

            if line_without_space.startswith('PATH_VALUES'):
                s = line.split("'")
                line = "'".join([s[0], kernel_root_dir, s[2]])

        fo.write(line)

    fo.close()

    logging.info('PATH_VALUES set to "{}" in metakernel file copy: {}'.format(kernel_root_dir, path_to_metakernel))


def get_copy_spice_metakernel(path_to_metakernel, kernel_root_dir, output_dir, new_kernel_file_name=None):
    """
    Copy metakernel file, and  reset "PATH_VALUES" to spice kernel root directory

    :param path_to_metakernel: metakernel file path
    :param kernel_root_dir: path to the spice kernel base directory (local copy)
    :param new_kernel_file_name: allows to specify new file
    :param output_dir: destination directory
    :return: des: new_kernel_file_name path of the metakernel file copy
    """

    kernel_root_dir = os.path.abspath(kernel_root_dir)

    if not os.path.exists(path_to_metakernel):
        logging.error('"metakernel file path" does not exists; {}'.format(path_to_metakernel))
        sys.exit()

    if not os.path.exists(kernel_root_dir):
        logging.error('"kernel_root_dir" does not exists; {}'.format(kernel_root_dir))
        sys.exit()

    file_name = os.path.basename(path_to_metakernel)
    if new_kernel_file_name:
        file_name = new_kernel_file_name

    dest = os.path.join(output_dir, file_name)

    shutil.copy(path_to_metakernel, dest)
    logging.info('metakernel file copy create: {}'.format(dest))

    if kernel_root_dir is not None and kernel_root_dir != '':

        update_path_val_in_mk_file(dest, kernel_root_dir)

    return dest


def read_files_in_mk_file(path_to_metakernel):
    """
    Read files within a given mk file

    :param path_to_metakernel: metakernel file path
    :return kernel_to_load: dictionary {pathvalue:[list of kernels]}
    """

    if not os.path.exists(path_to_metakernel):
        logging.error('metakernel file does not exist: {}'.format(path_to_metakernel))
        sys.exit()

    fi = open(path_to_metakernel, 'r')
    lines = fi.readlines()

    for line in lines:

        line = line.lstrip()

        if line.startswith('PATH_SYMBOLS'):

            list_path_symbols = line.split('(')[1].split(')')[0]
            list_path_symbols = list_path_symbols.strip().replace(' ', '').replace("'", "").split(',')

        if line.startswith('PATH_VALUES'):
            list_path_values = line.split('(')[1].split(')')[0]
            list_path_values = list_path_values.strip().replace(' ', '').replace("'", "").split(',')

    fi.close()

    if len(list_path_values) != len(list_path_symbols):

        logging.error('nb PATH_VALUES != nb PATH_SYMBOLS in {}'.format(path_to_metakernel))
        sys.exit()

    path_values_dico = {}
    for i in range(len(list_path_values)):

        path_values_dico[list_path_symbols[i]] = list_path_values[i]

    kernel_to_load = {}
    for line in lines:

        my_line = line.lstrip()

        if my_line.startswith("'$"):

            for p_val in list_path_symbols:

                p_val_var = "$" + p_val

                if p_val_var in line:

                    fi = line.split("'")[1].replace(p_val_var, '')
                    if fi.startswith('/'):
                        fi = fi[1:]

                    p_val_abs_path = path_values_dico[p_val]

                    if p_val_abs_path not in kernel_to_load.keys():

                        kernel_to_load[p_val_abs_path] = [fi]

                    else:

                        kernel_to_load[p_val_abs_path].append(fi)

    return kernel_to_load


def download_url(url, root, filename=None):
    """
    Download a file from a url and place it in root.

    :param url: URL to download file from
    :param root: Directory to place downloaded file in
    :param filename: Name to save the file under. If None, use the basename of the URL
    """

    root = os.path.expanduser(root)

    if not filename:
        filename = os.path.basename(url)
    file_path = os.path.join(root, filename)

    os.makedirs(root, exist_ok=True)

    try:

        logging.info('Downloading {} to {}'.format(url, file_path))
        urllib.request.urlretrieve(url, file_path)

    except (urllib.error.URLError, IOError) as e:

        if url[:5] == 'https':

            url = url.replace('https:', 'http:')
            logging.warning('Failed download. Trying https -> http instead')
            logging.info('Downloading {} to {}'.format(url, file_path))
            urllib.request.urlretrieve(url, file_path)


def download_spice_file(url, list_of_files, local_dir='./'):
    """
    Download file from spice kernel if needed (not in local copy)

    :param url: URL to download file from
    :param list_of_files:
    :param local_dir:
    :return:
    """

    here = os.getcwd()
    os.chdir(local_dir)

    for f in list_of_files:

        f_local_copy = os.path.join(local_dir, f)
        f_url = os.path.join(url, f)

        if not os.path.exists(f_local_copy):

            dir_name = os.path.dirname(f_local_copy)

            os.makedirs(dir_name, exist_ok=True)

            logging.info('requesting file from {}'.format(f_url))
            wget.download(f_url, dir_name)
            logging.info('new file copied to {}'.format(f_local_copy))

    os.chdir(here)


def update_local_kernel_copy(kernel_to_load, url='ftp://spiftp.esac.esa.int/data/SPICE/JUICE/kernels/'):
    """
    Update local kernel directory

    :param url: URL to download file from
    :param kernel_to_load: dictionary {pathvalue:[list of kernels]}
    """

    for k, v in kernel_to_load.items():

        if not os.path.exists(k):

            logging.warning('local kernels directory does not exist!')
            os.mkdir(k)
            logging.info('local kernel directory created: {}'.format(k))

        download_spice_file(url, v, k)


def get_copy_spice_metakernel_dico(kernel_parameters, working_dir='./'):
    """
    Copy metakernel file, and optionally reset "PATH_VALUES" to spice kernel

    1) set kernel local dir path
    2) set metakernel_path and copy to local directory
    3) update kernel local dir path in metakernel local copy if needed

    :param kernel_parameters: kernel parameters
    :param working_dir: working directory; ./ by default
    :return: des: the path of the metakernel file copy
    """

    kernel_root_dir = None

    if 'local_root_dir' in kernel_parameters:

        logging.info('kernel local_root_dir: '.format(kernel_parameters['local_root_dir']))
        kernel_root_dir = os.path.expandvars(kernel_parameters['local_root_dir'])
        kernel_root_dir = os.path.abspath(kernel_root_dir)

        if not os.path.exists(kernel_root_dir):
            logging.warning('"kernel_root_dir" does not exists; {}'.format(kernel_root_dir))
            sys.exit()

    elif 'update' in kernel_parameters:

        if kernel_parameters['update']:

            kernel_root_dir = os.path.abspath('./kernels')
            if not os.path.exists(kernel_root_dir):
                os.mkdir(kernel_root_dir)

            logging.info('kernel local_root_dir set to local default: '.format(kernel_root_dir))

    if 'meta_kernel' in kernel_parameters:

        path_to_metakernel = os.path.expandvars(kernel_parameters['meta_kernel'])

        if not os.path.exists(path_to_metakernel):
            logging.warning('"meta_kernel" path does not exists; {}'.format(path_to_metakernel))
            sys.exit()

        elif not os.path.isfile(path_to_metakernel):
                logging.warning('meta_kernel is not a file: "{}"'.format(path_to_metakernel))

    file_name = os.path.basename(path_to_metakernel)
    metakernel_file_path = os.path.join(working_dir, file_name)

    shutil.copy(path_to_metakernel, metakernel_file_path)
    logging.info('metakernel file copy create: {}'.format(metakernel_file_path))

    if kernel_root_dir is not None and kernel_root_dir != '':

        update_path_val_in_mk_file(metakernel_file_path, kernel_root_dir)

    if 'update' in kernel_parameters:

        if kernel_parameters['update']:

            kernel_to_load = read_files_in_mk_file(metakernel_file_path)

            if 'remote_url' in kernel_parameters:
                update_local_kernel_copy(kernel_to_load, kernel_parameters['remote_url'])
            else:
                update_local_kernel_copy(kernel_to_load)

    logging.info('kernel update: {}'.format(kernel_parameters['update']))
    logging.info('kernel remote_url: {}'.format(kernel_parameters['remote_url']))

    return metakernel_file_path


def get_copy_spice_metakernel(kernel_parameters, working_dir='./'):
    """
    Copy metakernel file, and optionally reset "PATH_VALUES" to spice kernel

    1) set kernel local dir path
    2) set metakernel_path and copy to local directory
    3) update kernel local dir path in metakernel local copy if needed

    :param kernel_parameters: kernel parameters
    :param working_dir: working directory; ./ by default
    :return: des: the path of the metakernel file copy
    """

    kernel_root_dir = None

    if hasattr(kernel_parameters ,'local_root_dir'):

        logging.info('kernel local_root_dir: '.format(kernel_parameters.local_root_dir))
        kernel_root_dir = os.path.expandvars(kernel_parameters.local_root_dir)
        kernel_root_dir = os.path.abspath(kernel_root_dir)

        if not os.path.exists(kernel_root_dir):
            logging.warning('"kernel_root_dir" does not exists; {}'.format(kernel_root_dir))
            sys.exit()

    elif hasattr(kernel_parameters.kernel, 'update'):

        if kernel_parameters.update:

            kernel_root_dir = os.path.abspath('./kernels')
            if not os.path.exists(kernel_root_dir):
                os.mkdir(kernel_root_dir)

            logging.info('kernel local_root_dir set to local default: '.format(kernel_root_dir))

    if hasattr(kernel_parameters, 'meta_kernel'):

        path_to_metakernel = os.path.expandvars(kernel_parameters.meta_kernel)

        if not os.path.exists(path_to_metakernel):
            logging.warning('"meta_kernel" path does not exists; {}'.format(path_to_metakernel))
            sys.exit()

        elif not os.path.isfile(path_to_metakernel):
                logging.warning('meta_kernel is not a file: "{}"'.format(path_to_metakernel))

    file_name = os.path.basename(path_to_metakernel)
    metakernel_file_path = os.path.join(working_dir, file_name)

    shutil.copy(path_to_metakernel, metakernel_file_path)
    logging.info('metakernel file copy create: {}'.format(metakernel_file_path))

    if kernel_root_dir is not None and kernel_root_dir != '':

        update_path_val_in_mk_file(metakernel_file_path, kernel_root_dir)

    if hasattr(kernel_parameters, 'update'):

        if kernel_parameters.update:

            kernel_to_load = read_files_in_mk_file(metakernel_file_path)

            if 'remote_url' in kernel_parameters:
                update_local_kernel_copy(kernel_to_load, kernel_parameters.remote_url)
            else:
                update_local_kernel_copy(kernel_to_load)

    logging.info('kernel remote_url: {}'.format(kernel_parameters.remote_url))
    logging.info('kernel update: {}'.format(kernel_parameters.update))

    return metakernel_file_path