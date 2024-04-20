from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LatestCls:
	"""Latest commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("latest", core, parent)

	def fetch(self) -> List[str]:
		"""SCPI: FETCh:SIGNaling:LOG:FILE:LATest \n
		Snippet: value: List[str] = driver.signaling.log.file.latest.fetch() \n
		No command help available \n
			:return: log_files: No help available"""
		response = self._core.io.query_str(f'FETCh:SIGNaling:LOG:FILE:LATest?')
		return Conversions.str_to_str_list(response)
