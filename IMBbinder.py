#!/usr/bin/env python
# coding: utf-8
''' IMBdownloader : download all Internet Magazine Back Number Archives'''
import glob
from PyPDF2 import PdfFileWriter, PdfFileReader

magName = 'InternetMag'
dirs = glob.glob('*/')  # directory list, it’s OK??
for dir in dirs:
    pdfName = magName+dir[:-1]+'.pdf'  # ex) InternetMag194410.pdf
    outPdf = PdfFileWriter()  # make empty pdf
    files = glob.glob(dir+'*.pdf')
    for file in files:
        inPdf = PdfFileReader(open(file, "rb"))
        if inPdf.isEncrypted:  # some pdf were encripted
            inPdf.decrypt("")  # ? why empty password ?
        pageNum = inPdf.getNumPages()-1  # delete last page, !!
        for p in range(0, pageNum):  # !! getNumPages(0) gets page1
            page = inPdf.getPage(p)
            outPdf.addPage(page)
    outPdf.write(open(pdfName, "wb"))
    print pdfName
