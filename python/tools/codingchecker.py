# coding:utf8
'''
Created on Jan 13, 2016

@author: lee
'''
import os
import chardet
import zipfile
import shutil
from datetime import datetime


class CodingChecker(object):

    CHECKED_FILE_EXT = ['.sql', '.zip', '.py']

    def __init__(self, checked_file=None):
        self.checked_file = checked_file
        if self.checked_file ==  None:
            self.checked_file = os.path.abspath('.')
        self.counter = 0
        if os.path.exists(self.checked_file):
            if os.path.isdir(self.checked_file):
                self.checked_file = os.path.abspath(self.checked_file)
                self.tempdir = os.path.join(
                    self.checked_file, datetime.now().strftime('%Y%m%d%H%M%S%f'))
            else:
                self.tempdir = os.path.join(
                    os.path.abspath(
                        os.path.dirname(
                            self.checked_file)),
                    datetime.now().strftime('%Y%m%d%H%M%S%f'))

            logger_file = self.tempdir + '.log'
            if os.path.exists(logger_file):
                os.remove(logger_file)
            self.logger = open(logger_file, 'a')
        else:
            raise BaseException('Param Wrong.')

    def _cur_tempdir(self):
        curpath = os.path.join(self.tempdir, str(self.counter))
        if not os.path.exists(curpath):
            print 'start to make dir %s' % curpath
            os.makedirs(curpath)
        return curpath

    def __del__(self):
        if self.counter > 0:
            for i in range(self.counter + 1):
                if os.path.exists(os.path.join(self.tempdir, str(i))):
                    shutil.rmtree(os.path.join(self.tempdir, str(i)))
            shutil.rmtree(self.tempdir)

    def check(self):
        if not os.path.exists(self.checked_file):
            print 'Error -> path {%s} does not exist.' % self.checked_file
            return
        self._check_file(self.checked_file)
        self.logger.close()

    def _check_zip_file(self, zip_file):
        print 'start to extract zip file -> %s' % zip_file
        self.counter = self.counter + 1
        z = zipfile.ZipFile(zip_file, 'r')
        z.extractall(path=self._cur_tempdir())
        z.close()
        self._check_dir(self._cur_tempdir())

    def _is_need_checked(self, fl):
        return os.path.splitext(fl)[1].lower(
        ) in CodingChecker.CHECKED_FILE_EXT

    def _check_single_file(self, fl):
        print fl
        encoding = chardet.detect(open(fl).read())
        print encoding
        if encoding['encoding'] != 'utf-8':
            self.logger.write(
                '%s\t%s\t%f;' %
                (fl, encoding['encoding'], encoding['confidence']))

    def _check_file(self, fl):
        if os.path.isfile(fl):
            if self._is_need_checked(fl):
                if zipfile.is_zipfile(fl):
                    self._check_zip_file(fl)
                else:
                    self._check_single_file(fl)
            else:
                print 'ignore to check file -> %s' % fl
        elif os.path.isdir(fl):
            self._check_dir(fl)

    def _check_dir(self, dirpath):
        root, dirs, files = os.walk(dirpath).next()
        for sub_file in files:
            self._check_file(os.path.join(root, sub_file))
        for sub_dir in dirs:
            self._check_file(os.path.join(root, sub_dir))

    def _log_result(self, content):
        self.logger.write(content + '\r\n')

if __name__ == '__main__':
    cc = CodingChecker()
    cc.check()
