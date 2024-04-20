from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TCls:
	"""T commands group definition. 2 total commands, 1 Subgroups, 1 group commands
	Repeated Capability: Tnum, default value after init: Tnum.Nr300"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("t", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_tnum_get', 'repcap_tnum_set', repcap.Tnum.Nr300)

	def repcap_tnum_set(self, tnum: repcap.Tnum) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Tnum.Default
		Default value after init: Tnum.Nr300"""
		self._cmd_group.set_repcap_enum_value(tnum)

	def repcap_tnum_get(self) -> repcap.Tnum:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def extended(self):
		"""extended commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_extended'):
			from .Extended import ExtendedCls
			self._extended = ExtendedCls(self._core, self._cmd_group)
		return self._extended

	def set(self, name_ta_eps: str, factor: int, unit: enums.TimerUnitB = None, tnum=repcap.Tnum.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:EPS:TIMer:T<no> \n
		Snippet: driver.configure.signaling.topology.eps.timer.t.set(name_ta_eps = 'abc', factor = 1, unit = enums.TimerUnitB.DEACtivated, tnum = repcap.Tnum.Default) \n
		Configures the timer T3412 (periodic EPS tracking area update) . \n
			:param name_ta_eps: Name of EPS tracking area
			:param factor: The timer value is calculated as Factor * Unit.
			:param unit: S2: unit 2 seconds M1: unit 1 minute M6: unit 6 minutes DEACtivated: timer deactivated
			:param tnum: optional repeated capability selector. Default value: Nr300 (settable in the interface 'T')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name_ta_eps', name_ta_eps, DataType.String), ArgSingle('factor', factor, DataType.Integer), ArgSingle('unit', unit, DataType.Enum, enums.TimerUnitB, is_optional=True))
		tnum_cmd_val = self._cmd_group.get_repcap_cmd_value(tnum, repcap.Tnum)
		self._core.io.write(f'CONFigure:SIGNaling:TOPology:EPS:TIMer:T{tnum_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Factor: int: The timer value is calculated as Factor * Unit.
			- Unit: enums.TimerUnitB: S2: unit 2 seconds M1: unit 1 minute M6: unit 6 minutes DEACtivated: timer deactivated"""
		__meta_args_list = [
			ArgStruct.scalar_int('Factor'),
			ArgStruct.scalar_enum('Unit', enums.TimerUnitB)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Factor: int = None
			self.Unit: enums.TimerUnitB = None

	def get(self, name_ta_eps: str, tnum=repcap.Tnum.Default) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:EPS:TIMer:T<no> \n
		Snippet: value: GetStruct = driver.configure.signaling.topology.eps.timer.t.get(name_ta_eps = 'abc', tnum = repcap.Tnum.Default) \n
		Configures the timer T3412 (periodic EPS tracking area update) . \n
			:param name_ta_eps: Name of EPS tracking area
			:param tnum: optional repeated capability selector. Default value: Nr300 (settable in the interface 'T')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(name_ta_eps)
		tnum_cmd_val = self._cmd_group.get_repcap_cmd_value(tnum, repcap.Tnum)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:TOPology:EPS:TIMer:T{tnum_cmd_val}? {param}', self.__class__.GetStruct())

	def clone(self) -> 'TCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
