from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NCls:
	"""N commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Nnum, default value after init: Nnum.Nr310"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("n", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_nnum_get', 'repcap_nnum_set', repcap.Nnum.Nr310)

	def repcap_nnum_set(self, nnum: repcap.Nnum) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Nnum.Default
		Default value after init: Nnum.Nr310"""
		self._cmd_group.set_repcap_enum_value(nnum)

	def repcap_nnum_get(self) -> repcap.Nnum:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, cell_name: str, counter: enums.Counter, nnum=repcap.Nnum.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:TOUT:N<no> \n
		Snippet: driver.configure.signaling.nradio.cell.timeout.n.set(cell_name = 'abc', counter = enums.Counter.N1, nnum = repcap.Nnum.Default) \n
			INTRO_CMD_HELP: Configures one of the following constants: \n
			- N310, for counting out-of-sync indications and starting T310
			- N311, for counting in-sync indications and stopping T310  \n
			:param cell_name: No help available
			:param counter: Value of the constant For N310, the value N5 is not allowed. For N311, the value N20 is not allowed.
			:param nnum: optional repeated capability selector. Default value: Nr310 (settable in the interface 'N')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('counter', counter, DataType.Enum, enums.Counter))
		nnum_cmd_val = self._cmd_group.get_repcap_cmd_value(nnum, repcap.Nnum)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:TOUT:N{nnum_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, nnum=repcap.Nnum.Default) -> enums.Counter:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:TOUT:N<no> \n
		Snippet: value: enums.Counter = driver.configure.signaling.nradio.cell.timeout.n.get(cell_name = 'abc', nnum = repcap.Nnum.Default) \n
			INTRO_CMD_HELP: Configures one of the following constants: \n
			- N310, for counting out-of-sync indications and starting T310
			- N311, for counting in-sync indications and stopping T310  \n
			:param cell_name: No help available
			:param nnum: optional repeated capability selector. Default value: Nr310 (settable in the interface 'N')
			:return: counter: Value of the constant For N310, the value N5 is not allowed. For N311, the value N20 is not allowed."""
		param = Conversions.value_to_quoted_str(cell_name)
		nnum_cmd_val = self._cmd_group.get_repcap_cmd_value(nnum, repcap.Nnum)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:TOUT:N{nnum_cmd_val}? {param}')
		return Conversions.str_to_scalar_enum(response, enums.Counter)

	def clone(self) -> 'NCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
