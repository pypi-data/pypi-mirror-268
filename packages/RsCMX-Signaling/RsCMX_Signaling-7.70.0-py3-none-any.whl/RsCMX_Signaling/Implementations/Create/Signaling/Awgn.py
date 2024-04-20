from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AwgnCls:
	"""Awgn commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("awgn", core, parent)

	def set_advanced(self, cell_name: str) -> None:
		"""SCPI: CREate:SIGNaling:AWGN:ADVanced \n
		Snippet: driver.create.signaling.awgn.set_advanced(cell_name = 'abc') \n
		No command help available \n
			:param cell_name: No help available
		"""
		param = Conversions.value_to_quoted_str(cell_name)
		self._core.io.write(f'CREate:SIGNaling:AWGN:ADVanced {param}')
