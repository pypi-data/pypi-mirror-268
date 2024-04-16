"""
Created on October, 2017

@author: Claudio Munoz Crego (ESAC)

This file ...
"""

import os
import sys
import shutil
import logging
import subprocess
import datetime

heading_character = {0: '#', 1: '*', 2: '=', 3: '-', 4: '^', 5: '"'}


class RstHandler(object):
    """

    """

    def __init__(self, output_path, out=sys.stdout,
                 start=datetime.datetime.now(), end=datetime.datetime.now()):
        """
        :param out: unit where to write report summary
        """

        self.output_path = output_path
        self.out = self.reset_out(out)
        self.start = start
        self.end = end

    def reset_out(self, out):
        """
        Reset the output stream

        :param out: unit where to write report summary
        :return: unit where to write report summary
        """

        if out == "rst":
            self.rst_file_name = os.path.join(self.output_path, 'report.rst')
            out = open(os.path.join(self.output_path, 'report.rst'), 'w')

        return out

    def write_text(self, text):
        """
        write normal text

        :param text:
        :return:
        """

        self.out.write(text)

    def write_heading(self, level='=', text='heading'):
        """
        Write heading

            # with overline, for parts
            * with overline, for chapters
            =, for sections
            -, for subsections
            ^, for subsubsections
            ", for paragraphs
        :param text:
        :param level:
        :return:
        """

        title_size = len(text)
        self.out.write('\n{}\n'.format(level * title_size))
        self.out.write(text)
        self.out.write('\n{}\n'.format(level * title_size))

    def write_head(self, nlevel=0, text=''):

        """
        Write heading

            0: # with overline, for parts
            1: * with overline, for chapters
            2: =, for sections
            3: -, for subsections
            4: ^, for subsubsections
            5: ", for paragraphs
        :param text: heading text
        :param nlevel: a number
        """

        title_size = len(text)
        self.out.write('\n{}\n'.format(heading_character[nlevel] * title_size))
        self.out.write(text)
        self.out.write('\n{}\n'.format(heading_character[nlevel] * title_size))

    def write_head_part(self, text):
        """
        Write head chapter
        :param text:
        :return:
            """
        self.write_heading('#', text)

    def write_head_chapter(self, text):
        """
        Write head chapter
        :param text:
        :return:
            """
        self.write_heading('*', text)

    def write_head_section(self, text):
        """
        Write head section
        :param text:
        :return:
            """

        self.out.write('\n')
        self.insert_page_break()
        self.write_heading('=', text)

    def write_head_subsection(self, text):
        """
        Write head subsection
        :param text:
        :return:
        """
        self.out.write('\n')
        self.write_heading('-', text)

    def write_head_subsubsection(self, text):
        """
        Write head subsubsection
        :param text:
        :return:
        """
        self.write_heading('^', text)

    def write_h6(self, text):
        """
        Write head h6
        :param text:
        :return:
        """
        self.write_heading('"', text)

       # def reST_to_html_fragment(self, a_str):
    #
    #     from docutils import core
    #     parts = core.publish_parts(
    #         source=a_str,
    #         writer_name='html')
    #     return parts['body_pre_docinfo'] + parts['fragment']
    #
    # def reST_to_html_file(self, rst_path_file=''):
    #
    #     f = open(os.path.join(self.output_path, 'report_metrics_summary.rst'), 'r')
    #
    #     a_str = '\n'.join(f.readlines())
    #
    #     html_str = self.reST_to_html_fragment(a_str)
    #
    #     f = open(os.path.join(self.output_path, 'report_metrics_summary.html'), 'w')

    def print_introduction(self):
        """
        Print intro
        """
        total_duration = self.end - self.start

        intro = ("\n"
                 ".. |date| date::\n"
                 ".. |time| date:: %H:%M:%S\n"
                 "\n"
                 "This document was automatically generated by Simu Dust Particle Tool on |date| at |time|.\n\n"
                 "Scenario start: {0}\n"
                 "Scenario end: {1}\n"
                 "Scenario Duration: {2}\n"
                 "\n").format(self.start, self.end, total_duration)

        self.out.write(intro)

    def print_rst_csv_table(self, metrics, title=""):
        """
        Generate (print) a table in rst format
        work for html version but not rst2pdf

        :param title:
        :param metrics:
        :return:
        """

        to_print = [' .. csv-table:: {}'.format(title)]

        header = '\n\t:header: ' + ', '.join(['"{}"'.format(v) for v in metrics[0]])
        to_print.append(header)

        to_print.append("\n")
        for i in range(1, len(metrics)):
            to_print.append('\n\t' + ', '.join(['"{}"'.format(v) for v in metrics[i]]))

        for l in to_print:
            self.out.write(l)

        self.out.write('\n')

    def print_rst_table(self, metrics, title=True):
        """
        Generate (print) a table in rst format

        :param title: flag which specify if the table have a title line or not.
        :param metrics: list of table lines, if title=True, the title must be in metrics[0]
        :param out: unit where to write report summary
        :return:
        """

        # convert all elements to strings
        for i in range(len(metrics)):
            metrics[i] = [str(ele) for ele in metrics[i]]

        d = []
        table_title_format = '|'
        table_line_format = '|'

        for i in range(len(metrics[0])):
            # print 'i = ', i, len(metrics[0])
            d.append(len(max([str(ele[i]) for ele in metrics], key=len)))
            table_title_format += ' {' + str(i) + ':' + str(d[i]) + 's} |'
            table_line_format += ' {' + str(i) + ':' + str(d[i]) + 's} |'
        table_title_format += '\n'
        table_line_format += '\n'

        table_line = ''
        table_line_title = ''
        for i in range(len(d)):
            table_line += '+{}'.format('-' * (d[i] + 2))
            table_line_title += '+{}'.format('=' * (d[i] + 2))

        table_line += '+\n'
        table_line_title += '+\n'

        if title:
            self.out.write(table_line)
            self.out.write(table_title_format.format(*metrics[0]))
            self.out.write(table_line_title)
            metrics.pop(0)
        else:
            self.out.write(table_line)

        for ele in metrics:
            self.out.write(table_line_format.format(*ele))
            self.out.write(table_line)

        self.out.write('\n')

    def print_rst_metrics_summary_table(self, metrics):
        """
        Generate summary metric table

        :param metrics list of table lines
        :param out: unit where to write report summary
        """

        metrics.insert(0,['Metric', 'Value', 'Unit'])
        self.print_rst_table(metrics)

    def insert_literal(self, file_name):
        """
        Insert file contents as is (literally)

        :param file_name:
        :return:
        """

        self.out.write('\n' + '.. include:: ' + file_name + '\n  :literal:\n')

    def insert_page_break(self):
        """
        Insert file contents as is (literally)

        :param file_name:
        :return:
        """

        self.out.write('\n' + '.. raw:: pdf' + '\n\n   PageBreak \n')

    def rst_insert_figure(self, fig_path, title, text=[]):
        """
        Write rst instructions to include a figure
        :param out: unit where to write report summary
        :param fig_path: path of figure file
        :param title: figure title
        :param text: some text
        :return:
        """

        if text != '':
            text = "   This figure includes {}\n".format(text)
        fig = ("\n"
               " .. figure:: {0}\n"
               "   :width: 100%\n"
               "   :alt: {0}\n"
               "   :align: center\n"
               "\n"
               "   {1}\n"
               "\n{2}"
               ).format(fig_path, title, text)

        self.out.write(fig)

    def rst_to_html(self):

        f_in = os.path.join(self.output_path, 'report.rst')
        f_out = os.path.join(self.output_path, 'report.html')

        self.replace_string_within_file(f_in, to_parce={'DL_ ': 'DL  ', 'DL_"': 'DL "'})

        command = 'rst2html5.py {} {} '.format(f_in, f_out)

        logging.info('running os command "{}'.format(command))
        # os.system(command)

        try:
            p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

            while True:
                line = p.stdout.readline()
                if not line: break
                print('{}'.format(line))
            p.wait()

            if p.returncode != 0:
                p.terminate()

            logging.info('file {} generated '.format(f_out))

        except Exception:
            logging.error('command failed:  {} '.format(command))
            logging.warning('file {} cannot be generated '.format(f_out))

    # def rst2pdf(self, style_file=None):
    #     """
    #     Convert rst to pdf file using rst2pdf tool and optionally a style file
    #     :return:
    #     """
    #
    #     f_in = os.path.join(self.output_path, 'report.rst')
    #     f_out = os.path.join(self.output_path, 'report.pdf')
    #     command = 'rst2pdf {} {} '.format(f_in, f_out)
    #     if style_file:
    #         command = 'rst2pdf {} -s {} {} '.format(f_in, style_file, f_out)
    #
    #     logging.info('running os command "{}'.format(command))
    #     # os.system(command)
    #
    #     try:
    #         p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    #
    #         while True:
    #             line = p.stdout.readline()
    #             if not line: break
    #             print('{}'.format(line))
    #         p.wait()
    #
    #         if p.returncode != 0:
    #             p.terminate()
    #
    #         logging.info('file {} generated '.format(f_out))
    #
    #     except Exception:
    #         logging.error('command failed:  {} '.format(command))
    #         logging.warning('file {} cannot be generated '.format(f_out))

    def rename_report(self, report_name, just_rename=True):
        """
        Rename report name; default is 'report'
        """

        extensions = ['rst', 'pdf', 'html', 'docx']

        for val in extensions:

            src = os.path.join(self.output_path, 'report.' + val)
            dest = os.path.join(self.output_path, report_name + '.' + val)

            if os.path.exists(src):

                if just_rename:
                    shutil.move(src, dest)
                    logging.info('report file renamed: {}'.format(dest))
                else:
                    shutil.copy(src, dest)
                    logging.info('report file copied: {}'.format(dest))

    def html_to_pdf(self):
        """

        Requires
        linux: sudo apt-get install wkhtmltopdf
        mac os: brew install Caskroom/cask/wkhtmltopdf
        pip install wkhtmltopdf
        pip install pdfkit
        :return:
        """

        f_in = os.path.join(self.output_path, 'report.html')
        f_out = os.path.join(self.output_path, 'report.pdf')

        import pdfkit

        options = {
                'page-size': 'A4',
                'margin-top': '0.75in',
                'margin-right': '0.75in',
                'margin-bottom': '0.75in',
                'margin-left': '0.75in',
                'dpi':400,
                }

        try:
            pdfkit.from_file([f_in], f_out, options=options)
            logging.info('file {} generated '.format(f_out))
        except: # catch *all* exceptions
            e = sys.exc_info()
            print(e[0])
            for ele in e[1]:
                print('{}'.format(ele))
            logging.error('file {} generated '.format(f_out))

    def pandoc_docx_to_rst(self, input_path_file, output_path_file=''):

        if output_path_file == '':
            output_path_file = input_path_file.replace('.docx', '.rst')
        self.pandoc_convert(input_path_file, output_path_file)

    def pandoc_rst_to_docx(self, input_path_file='', output_path_file=''):

        if input_path_file == '':
            input_path_file = self.rst_file_name

        if output_path_file == '':
            output_path_file = input_path_file.replace('.rst', '.docx')
        self.pandoc_convert(input_path_file, output_path_file)

    def pandoc_rst_to_pdf(self, input_path_file, output_path_file=''):
        """

        Note : by command line
        pandoc -s my_file.docx -t rst -o my_file.rst
        :param input_path_file:
        :param output_path_file:
        :return:
        """

        if output_path_file == '':
            output_path_file = input_path_file.replace('.rst', '.pdf')
        self.pandoc_convert(input_path_file, output_path_file)

    def pandoc_convert(self, input_path_file, output_path_file, args=()):
        """
        Requires:

        brew install pandoc
        brew cask install basictex (to support pdf)
        pip install pypandoc


        :param input_path_file:
        :param output_path_file:
        :return:
        """
        import pypandoc

        output_type = os.path.basename(output_path_file).split('.')[1]
        pypandoc.convert_file(input_path_file, output_type, extra_args=args, outputfile=output_path_file)

    def pandoc_html_to_docx(self, input_path_file='', output_path_file='', docx_style_file=None):
        """
        Translate html to docx

        Note : by command line
        pandoc -f html -t docx my_file.html -o my_file.docx
        :param docx_style_file: docx templates
        :param args: list of extra arguments (i.e. --reference-doc custom-reference.docx)
        :param input_path_file:
        :param output_path_file

        """

        from shutil import which
        if which('pandoc'):

            if input_path_file == '':
                input_path_file = os.path.join(self.output_path, 'report.html')
            if output_path_file == '':
                output_path_file = input_path_file.replace('.html', '.docx')

            # self.pandoc_convert(input_path_file, output_path_file, args=args)
            # logging.info('file {} generated '.format(output_path_file))

            here = os.getcwd()
            os.chdir(self.output_path)

            command = 'pandoc -f html -t docx {} -o {}'.format(input_path_file, output_path_file)
            if docx_style_file:
                command += ' --reference-doc {}'.format(docx_style_file)

            logging.info('running os command "{}'.format(command))
            # os.system(command)

            try:
                p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

                while True:
                    line = p.stdout.readline()
                    if not line: break
                    print('{}'.format(line))
                p.wait()

                if p.returncode != 0:
                    p.terminate()

                logging.info('file {} generated '.format(output_path_file))

            except Exception:
                logging.error('command failed:  {} '.format(command))
                logging.warning('file {} cannot be generated '.format(output_path_file))

            os.chdir(here)

        else:

            logging.warning('pandoc is not available; cannot convert html to docx')

    def replace_string_within_file(self, input_file, to_parce={'DL_ ': 'DL '}):
        """
        Replace string in file

        :param input_file:
        :param to_parce:
        :return:
        """
        import shutil

        old_file = input_file + '.save'
        shutil.copy(input_file, old_file)

        destination = open(input_file, "w")
        source = open(old_file, "r")
        for line in source:

            for k, v in to_parce.items():

                line = line.replace(k, v)

            destination.write(line)

        source.close()
        destination.close()

        os.remove(old_file)
