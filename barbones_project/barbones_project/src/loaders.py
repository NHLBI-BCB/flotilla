__author__ = 'lovci'

""" loads pre-made pickle files """

import sys
import os

import pandas as pd
from .utils import data_dir


def load_descriptors(sample_descriptors_pickle=None, gene_descriptors_pickle=None, event_descriptors_pickle=None):
    study_data_dir = data_dir()
    descrip = {'sample':None,
               'gene':None,
               'event':None}
    try:
        if sample_descriptors_pickle is not None:
            descrip['sample'] = pd.read_pickle(sample_descriptors_pickle)
        if event_descriptors_pickle is not None:
            descrip['event'] = pd.read_pickle(event_descriptors_pickle)
        if gene_descriptors_pickle is not None:
            descrip['gene'] = pd.read_pickle(gene_descriptors_pickle)

    except Exception as E:
        sys.stderr.write("error loading descriptors: %s, \n\n .... entering pdb ... \n\n" % E)
        import pdb
        pdb.set_trace()
        raise
    return descrip['sample'], descrip['gene'], descrip['event']


def load_transcriptome_data(expression_data_dump, splicing_data_dump):
    try:
        splicing = pd.read_pickle(splicing_data_dump)
        expression = pd.read_pickle(expression_data_dump)

    except Exception as E:
        sys.stderr.write("error loading transcriptome data: %s, \n\n .... entering pdb ... \n\n" % E)
        import pdb
        pdb.set_trace()
        raise

    return (splicing, expression)