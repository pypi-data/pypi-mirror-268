from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ImeiCls:
	"""Imei commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("imei", core, parent)

	def fetch(self) -> str:
		"""SCPI: FETCh:SIGNaling:UE:IMEI \n
		Snippet: value: str = driver.signaling.ue.imei.fetch() \n
		No command help available \n
			:return: imei: No help available"""
		response = self._core.io.query_str(f'FETCh:SIGNaling:UE:IMEI?')
		return trim_str_response(response)
