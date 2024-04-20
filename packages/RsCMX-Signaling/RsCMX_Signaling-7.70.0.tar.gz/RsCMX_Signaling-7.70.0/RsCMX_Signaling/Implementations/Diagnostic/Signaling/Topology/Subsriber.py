from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SubsriberCls:
	"""Subsriber commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("subsriber", core, parent)

	def get_creation(self) -> bool:
		"""SCPI: DIAGnostic:SIGNaling:TOPology:SUBSriber:CREation \n
		Snippet: value: bool = driver.diagnostic.signaling.topology.subsriber.get_creation() \n
		No command help available \n
			:return: skip: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:SIGNaling:TOPology:SUBSriber:CREation?')
		return Conversions.str_to_bool(response)

	def set_creation(self, skip: bool) -> None:
		"""SCPI: DIAGnostic:SIGNaling:TOPology:SUBSriber:CREation \n
		Snippet: driver.diagnostic.signaling.topology.subsriber.set_creation(skip = False) \n
		No command help available \n
			:param skip: No help available
		"""
		param = Conversions.bool_to_str(skip)
		self._core.io.write(f'DIAGnostic:SIGNaling:TOPology:SUBSriber:CREation {param}')
