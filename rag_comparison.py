# from . import code2nl
# from . import code2latent

from code2nl import rag as code2nl_rag
from code2latent import rag as code2lat_rag

from random_functions import test_functions

query = """
  take a list and return the number of items in that list that are greater than 0  
"""

code2nl_rag.get_n_highest_similar_to(
    query, test_functions, 5, c2e_model_name="gemma", e2l_model_name="jina")

# TODO: do this
# code2lat_rag.get_n_highest_similar_to(
#     "heakdjwajdaw", test_functions, 5, "codet5p")
#
