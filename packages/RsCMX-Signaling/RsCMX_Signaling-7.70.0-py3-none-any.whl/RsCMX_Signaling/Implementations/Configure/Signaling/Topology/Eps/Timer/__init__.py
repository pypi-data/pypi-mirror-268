from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TimerCls:
	"""Timer commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("timer", core, parent)

	@property
	def t(self):
		"""t commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_t'):
			from .T import TCls
			self._t = TCls(self._core, self._cmd_group)
		return self._t

	def set(self, name_ta_eps: str, timer: float) -> None:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:EPS:TIMer \n
		Snippet: driver.configure.signaling.topology.eps.timer.set(name_ta_eps = 'abc', timer = 1.0) \n
		No command help available \n
			:param name_ta_eps: No help available
			:param timer: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name_ta_eps', name_ta_eps, DataType.String), ArgSingle('timer', timer, DataType.Float))
		self._core.io.write(f'CONFigure:SIGNaling:TOPology:EPS:TIMer {param}'.rstrip())

	def get(self, name_ta_eps: str) -> float:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:EPS:TIMer \n
		Snippet: value: float = driver.configure.signaling.topology.eps.timer.get(name_ta_eps = 'abc') \n
		No command help available \n
			:param name_ta_eps: No help available
			:return: timer: No help available"""
		param = Conversions.value_to_quoted_str(name_ta_eps)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:TOPology:EPS:TIMer? {param}')
		return Conversions.str_to_float(response)

	def clone(self) -> 'TimerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TimerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
