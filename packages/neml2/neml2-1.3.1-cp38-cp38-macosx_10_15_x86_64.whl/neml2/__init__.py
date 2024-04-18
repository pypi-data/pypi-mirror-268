import torch

from .base import HITParser
from .base import Factory
from .models import Model


def load_input(filename, addtional_args=""):
    """
    Load an input file. Two things happen behind the scenes:
    1. A HITParser is used to extract all options from the input file.
    2. The extracted options are sent to the Factory

    Note this method does NOT actually manufacture the objects.
    Objects are manufactured when they are retrieved using the methods below.
    """
    parser = HITParser()
    oc = parser.parse(filename, addtional_args)
    Factory.clear()
    Factory.load(oc)


get_model = Factory.get_model


def load_model(filename, model, additional_args=""):
    """
    Load an input file and return the model with the specified name.
    This is equivalent to calling load_input and then get_model.
    """
    load_input(filename, additional_args)
    return get_model(model)
