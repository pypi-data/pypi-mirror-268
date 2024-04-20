from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FadingCls:
	"""Fading commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fading", core, parent)

	def delete(self, cell_name: str) -> None:
		"""SCPI: DELete:SIGNaling:FADing \n
		Snippet: driver.signaling.fading.delete(cell_name = 'abc') \n
		Forbids any fading and releases the resources reserved for fading. Send this command before switching to live mode. \n
			:param cell_name: No help available
		"""
		param = Conversions.value_to_quoted_str(cell_name)
		self._core.io.write(f'DELete:SIGNaling:FADing {param}')
