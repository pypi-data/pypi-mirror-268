"""
Distribution
------------

Matched distribution utils

"""

from torch import Tensor
from torch.distributions.multivariate_normal import MultivariateNormal

def normal(mean:Tensor,
           emittance:Tensor,
           wolski:Tensor) -> MultivariateNormal:
    """
    Create a multivariate normal distribution

    Parameters
    ----------
    mean: Tensor
        mean vector
    emittance: Tensor
        emittance vector
    wolski: Tensor
        wolski twiss matrices

    Returns
    -------
    MultivariateNormal

    Note
    ----
    Use sample method for generation

    Examples
    --------
    >>> from math import pi
    >>> import torch
    >>> from twiss.matrix import rotation
    >>> from twiss.normal import cs_normal
    >>> from twiss.wolski import twiss
    >>> n = cs_normal(torch.tensor([0.1, 5.0, -0.1, 10.0]))
    >>> m = n @ rotation(*2*pi*torch.tensor([0.12, 0.21])) @ n.inverse()
    >>> *_, ws = twiss(m)
    >>> es = torch.tensor([1.0E-6, 1.0E-8])
    >>> ms = torch.zeros(4)
    >>> db = normal(ms, es, ws)
    >>> ex, ey = es
    >>> wx, wy = ws
    >>> torch.allclose(db.covariance_matrix, ex*wx + ey*wy)
    True
    >>> torch.allclose(db.sample((2**20, )).T.cov(), db.covariance_matrix)
    True

    """
    for _ in wolski:
        emittance = emittance.unsqueeze(-1)
    covariance_matrix = (emittance*wolski).sum(0)
    return MultivariateNormal(mean, covariance_matrix)
