from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DshiftCls:
	"""Dshift commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dshift", core, parent)

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import ModeCls
			self._mode = ModeCls(self._core, self._cmd_group)
		return self._mode

	def set(self, cell_name: str, frequency: float) -> None:
		"""SCPI: [CONFigure]:SIGNaling:FADing:DSHift \n
		Snippet: driver.configure.signaling.fading.dshift.set(cell_name = 'abc', frequency = 1.0) \n
		Sets the maximum Doppler frequency for fading.
		A setting is only allowed in USER mode (see [CONFigure:]SIGNaling:FADing:DSHift:MODE) . \n
			:param cell_name: No help available
			:param frequency: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('frequency', frequency, DataType.Float))
		self._core.io.write(f'CONFigure:SIGNaling:FADing:DSHift {param}'.rstrip())

	def get(self, cell_name: str) -> float:
		"""SCPI: [CONFigure]:SIGNaling:FADing:DSHift \n
		Snippet: value: float = driver.configure.signaling.fading.dshift.get(cell_name = 'abc') \n
		Sets the maximum Doppler frequency for fading.
		A setting is only allowed in USER mode (see [CONFigure:]SIGNaling:FADing:DSHift:MODE) . \n
			:param cell_name: No help available
			:return: frequency: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:FADing:DSHift? {param}')
		return Conversions.str_to_float(response)

	def clone(self) -> 'DshiftCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DshiftCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
