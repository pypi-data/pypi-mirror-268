from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPyCls:
	"""ListPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	def get(self, target: enums.Target) -> List[str]:
		"""SCPI: DIAGnostic:SIGNaling:REGistration:LIST \n
		Snippet: value: List[str] = driver.diagnostic.signaling.registration.listPy.get(target = enums.Target.ALL) \n
		No command help available \n
			:param target: No help available
			:return: item: No help available"""
		param = Conversions.enum_scalar_to_str(target, enums.Target)
		response = self._core.io.query_str(f'DIAGnostic:SIGNaling:REGistration:LIST? {param}')
		return Conversions.str_to_str_list(response)
