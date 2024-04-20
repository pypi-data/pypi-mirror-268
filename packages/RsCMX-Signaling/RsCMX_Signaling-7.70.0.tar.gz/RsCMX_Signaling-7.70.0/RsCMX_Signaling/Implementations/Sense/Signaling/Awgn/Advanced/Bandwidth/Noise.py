from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NoiseCls:
	"""Noise commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("noise", core, parent)

	def get(self, cell_name: str) -> float:
		"""SCPI: SENSe:SIGNaling:AWGN:ADVanced:BWIDth:NOISe \n
		Snippet: value: float = driver.sense.signaling.awgn.advanced.bandwidth.noise.get(cell_name = 'abc') \n
		Queries the noise bandwidth. \n
			:param cell_name: No help available
			:return: noise_bandwidth: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'SENSe:SIGNaling:AWGN:ADVanced:BWIDth:NOISe? {param}')
		return Conversions.str_to_float(response)
