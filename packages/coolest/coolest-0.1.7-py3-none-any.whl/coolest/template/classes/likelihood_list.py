__author__ = 'aymgal'

from typing import Tuple

from coolest.template.classes.base import APIBaseObject


SUPPORTED_CHOICES = [
    'imaging_data', 
    'time_delays',
    'magnification_ratios',
    'image_plane_position',
    'source_plane_position',
]


class LikelihoodList(list, APIBaseObject):

    """
    A list all likelihood terms used during lens model parameters optimization. 
    Only applicable in the 'MAP' mode.
    """

    def __init__(self, 
                 *likelihood_types: Tuple[str]) -> None:
        for ll_type in likelihood_types:
            if ll_type not in SUPPORTED_CHOICES:
                raise ValueError(f"Likelihood type '{ll_type}' is not supported.")
        list.__init__(self, likelihood_types)
        APIBaseObject.__init__(self)