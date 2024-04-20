from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TmodeCls:
	"""Tmode commands group definition. 5 total commands, 3 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tmode", core, parent)

	@property
	def block(self):
		"""block commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_block'):
			from .Block import BlockCls
			self._block = BlockCls(self._core, self._cmd_group)
		return self._block

	@property
	def ssReport(self):
		"""ssReport commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssReport'):
			from .SsReport import SsReportCls
			self._ssReport = SsReportCls(self._core, self._cmd_group)
		return self._ssReport

	@property
	def uepLimit(self):
		"""uepLimit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uepLimit'):
			from .UepLimit import UepLimitCls
			self._uepLimit = UepLimitCls(self._core, self._cmd_group)
		return self._uepLimit

	# noinspection PyTypeChecker
	def get_tloop(self) -> enums.TestLoopState:
		"""SCPI: [CONFigure]:SIGNaling:TMODe:TLOop \n
		Snippet: value: enums.TestLoopState = driver.configure.signaling.tmode.get_tloop() \n
		Opens or closes a test loop mode A at the UE. Prerequisites: Test mode active and UE registered. \n
			:return: test_loop_state: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:TMODe:TLOop?')
		return Conversions.str_to_scalar_enum(response, enums.TestLoopState)

	def set_tloop(self, test_loop_state: enums.TestLoopState) -> None:
		"""SCPI: [CONFigure]:SIGNaling:TMODe:TLOop \n
		Snippet: driver.configure.signaling.tmode.set_tloop(test_loop_state = enums.TestLoopState.CLOSe) \n
		Opens or closes a test loop mode A at the UE. Prerequisites: Test mode active and UE registered. \n
			:param test_loop_state: No help available
		"""
		param = Conversions.enum_scalar_to_str(test_loop_state, enums.TestLoopState)
		self._core.io.write(f'CONFigure:SIGNaling:TMODe:TLOop {param}')

	def get_value(self) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:TMODe \n
		Snippet: value: bool = driver.configure.signaling.tmode.get_value() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:TMODe?')
		return Conversions.str_to_bool(response)

	def set_value(self, enable: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:TMODe \n
		Snippet: driver.configure.signaling.tmode.set_value(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:SIGNaling:TMODe {param}')

	def clone(self) -> 'TmodeCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TmodeCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
