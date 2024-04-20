from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TCls:
	"""T commands group definition. 1 total commands, 0 Subgroups, 1 group commands
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

	def set(self, name_ta_5_g: str, factor: int, unit: enums.TimerUnit = None, tnum=repcap.Tnum.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:FGS:TIMer:T<no> \n
		Snippet: driver.configure.signaling.topology.fgs.timer.t.set(name_ta_5_g = 'abc', factor = 1, unit = enums.TimerUnit.DEACtivated, tnum = repcap.Tnum.Default) \n
		Configures the timer T3512 (periodic registration update in a 5GS tracking area) . \n
			:param name_ta_5_g: Name of 5GS tracking area
			:param factor: The timer value is calculated as Factor * Unit.
			:param unit: S2, S30: unit 2 seconds, 30 seconds M1, M10: unit 1 minute, 10 minutes H1, H10, H320: unit 1 hour, 10 hours, 320 hours DEACtivated: timer deactivated
			:param tnum: optional repeated capability selector. Default value: Nr300 (settable in the interface 'T')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name_ta_5_g', name_ta_5_g, DataType.String), ArgSingle('factor', factor, DataType.Integer), ArgSingle('unit', unit, DataType.Enum, enums.TimerUnit, is_optional=True))
		tnum_cmd_val = self._cmd_group.get_repcap_cmd_value(tnum, repcap.Tnum)
		self._core.io.write(f'CONFigure:SIGNaling:TOPology:FGS:TIMer:T{tnum_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Factor: int: The timer value is calculated as Factor * Unit.
			- Unit: enums.TimerUnit: S2, S30: unit 2 seconds, 30 seconds M1, M10: unit 1 minute, 10 minutes H1, H10, H320: unit 1 hour, 10 hours, 320 hours DEACtivated: timer deactivated"""
		__meta_args_list = [
			ArgStruct.scalar_int('Factor'),
			ArgStruct.scalar_enum('Unit', enums.TimerUnit)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Factor: int = None
			self.Unit: enums.TimerUnit = None

	def get(self, name_ta_5_g: str, tnum=repcap.Tnum.Default) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:FGS:TIMer:T<no> \n
		Snippet: value: GetStruct = driver.configure.signaling.topology.fgs.timer.t.get(name_ta_5_g = 'abc', tnum = repcap.Tnum.Default) \n
		Configures the timer T3512 (periodic registration update in a 5GS tracking area) . \n
			:param name_ta_5_g: Name of 5GS tracking area
			:param tnum: optional repeated capability selector. Default value: Nr300 (settable in the interface 'T')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(name_ta_5_g)
		tnum_cmd_val = self._cmd_group.get_repcap_cmd_value(tnum, repcap.Tnum)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:TOPology:FGS:TIMer:T{tnum_cmd_val}? {param}', self.__class__.GetStruct())

	def clone(self) -> 'TCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
