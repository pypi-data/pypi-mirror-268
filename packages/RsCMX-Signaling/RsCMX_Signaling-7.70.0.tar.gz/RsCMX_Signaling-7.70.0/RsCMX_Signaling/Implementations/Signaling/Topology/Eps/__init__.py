from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EpsCls:
	"""Eps commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eps", core, parent)

	@property
	def ue(self):
		"""ue commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ue'):
			from .Ue import UeCls
			self._ue = UeCls(self._core, self._cmd_group)
		return self._ue

	@property
	def bearer(self):
		"""bearer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bearer'):
			from .Bearer import BearerCls
			self._bearer = BearerCls(self._core, self._cmd_group)
		return self._bearer

	def delete(self, name_ta_eps: str) -> None:
		"""SCPI: DELete:SIGNaling:TOPology:EPS \n
		Snippet: driver.signaling.topology.eps.delete(name_ta_eps = 'abc') \n
		Deletes an EPS tracking area. \n
			:param name_ta_eps: No help available
		"""
		param = Conversions.value_to_quoted_str(name_ta_eps)
		self._core.io.write(f'DELete:SIGNaling:TOPology:EPS {param}')

	def clone(self) -> 'EpsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EpsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
