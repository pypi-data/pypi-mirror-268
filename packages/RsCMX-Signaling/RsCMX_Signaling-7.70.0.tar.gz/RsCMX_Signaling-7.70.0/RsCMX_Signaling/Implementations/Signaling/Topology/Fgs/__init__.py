from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FgsCls:
	"""Fgs commands group definition. 4 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fgs", core, parent)

	@property
	def ue(self):
		"""ue commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ue'):
			from .Ue import UeCls
			self._ue = UeCls(self._core, self._cmd_group)
		return self._ue

	def delete(self, name_ta_5_g: str) -> None:
		"""SCPI: DELete:SIGNaling:TOPology:FGS \n
		Snippet: driver.signaling.topology.fgs.delete(name_ta_5_g = 'abc') \n
		Deletes a 5GS tracking area. \n
			:param name_ta_5_g: No help available
		"""
		param = Conversions.value_to_quoted_str(name_ta_5_g)
		self._core.io.write(f'DELete:SIGNaling:TOPology:FGS {param}')

	def clone(self) -> 'FgsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FgsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
