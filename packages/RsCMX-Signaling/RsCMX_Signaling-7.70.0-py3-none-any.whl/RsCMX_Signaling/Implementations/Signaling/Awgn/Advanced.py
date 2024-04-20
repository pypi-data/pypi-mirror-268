from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AdvancedCls:
	"""Advanced commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("advanced", core, parent)

	def delete(self, cell_name: str) -> None:
		"""SCPI: DELete:SIGNaling:AWGN:ADVanced \n
		Snippet: driver.signaling.awgn.advanced.delete(cell_name = 'abc') \n
		No command help available \n
			:param cell_name: No help available
		"""
		param = Conversions.value_to_quoted_str(cell_name)
		self._core.io.write(f'DELete:SIGNaling:AWGN:ADVanced {param}')
