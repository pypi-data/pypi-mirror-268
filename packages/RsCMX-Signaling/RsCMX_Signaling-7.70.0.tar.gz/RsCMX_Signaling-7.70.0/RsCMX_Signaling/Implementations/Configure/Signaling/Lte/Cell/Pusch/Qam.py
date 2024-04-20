from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class QamCls:
	"""Qam commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: QamOrder, default value after init: QamOrder.Order64"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qam", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_qamOrder_get', 'repcap_qamOrder_set', repcap.QamOrder.Order64)

	def repcap_qamOrder_set(self, qamOrder: repcap.QamOrder) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to QamOrder.Default
		Default value after init: QamOrder.Order64"""
		self._cmd_group.set_repcap_enum_value(qamOrder)

	def repcap_qamOrder_get(self) -> repcap.QamOrder:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, cell_name: str, enable: bool, qamOrder=repcap.QamOrder.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:PUSCh:QAM<nr> \n
		Snippet: driver.configure.signaling.lte.cell.pusch.qam.set(cell_name = 'abc', enable = False, qamOrder = repcap.QamOrder.Default) \n
		No command help available \n
			:param cell_name: No help available
			:param enable: No help available
			:param qamOrder: optional repeated capability selector. Default value: Order64 (settable in the interface 'Qam')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('enable', enable, DataType.Boolean))
		qamOrder_cmd_val = self._cmd_group.get_repcap_cmd_value(qamOrder, repcap.QamOrder)
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:PUSCh:QAM{qamOrder_cmd_val} {param}'.rstrip())

	def get(self, cell_name: str, qamOrder=repcap.QamOrder.Default) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:PUSCh:QAM<nr> \n
		Snippet: value: bool = driver.configure.signaling.lte.cell.pusch.qam.get(cell_name = 'abc', qamOrder = repcap.QamOrder.Default) \n
		No command help available \n
			:param cell_name: No help available
			:param qamOrder: optional repeated capability selector. Default value: Order64 (settable in the interface 'Qam')
			:return: enable: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		qamOrder_cmd_val = self._cmd_group.get_repcap_cmd_value(qamOrder, repcap.QamOrder)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:PUSCh:QAM{qamOrder_cmd_val}? {param}')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'QamCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = QamCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
