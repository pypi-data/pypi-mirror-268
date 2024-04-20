from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ExtendedCls:
	"""Extended commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("extended", core, parent)

	def set(self, name_ta_eps: str, enable: bool, factor: int = None, unit: enums.TimerUnit = None, tnum=repcap.Tnum.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:EPS:TIMer:T<no>:EXTended \n
		Snippet: driver.configure.signaling.topology.eps.timer.t.extended.set(name_ta_eps = 'abc', enable = False, factor = 1, unit = enums.TimerUnit.DEACtivated, tnum = repcap.Tnum.Default) \n
		Configures the extended timer T3412. \n
			:param name_ta_eps: Name of EPS tracking area
			:param enable: ON: Send the timer value to the UE. OFF: Do not send a timer value.
			:param factor: The timer value is calculated as Factor * Unit.
			:param unit: S2, S30: unit 2 seconds, 30 seconds M1, M10: unit 1 minute, 10 minutes H1, H10, H320: unit 1 hour, 10 hours, 320 hours DEACtivated: timer deactivated
			:param tnum: optional repeated capability selector. Default value: Nr300 (settable in the interface 'T')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name_ta_eps', name_ta_eps, DataType.String), ArgSingle('enable', enable, DataType.Boolean), ArgSingle('factor', factor, DataType.Integer, None, is_optional=True), ArgSingle('unit', unit, DataType.Enum, enums.TimerUnit, is_optional=True))
		tnum_cmd_val = self._cmd_group.get_repcap_cmd_value(tnum, repcap.Tnum)
		self._core.io.write(f'CONFigure:SIGNaling:TOPology:EPS:TIMer:T{tnum_cmd_val}:EXTended {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: ON: Send the timer value to the UE. OFF: Do not send a timer value.
			- Factor: int: The timer value is calculated as Factor * Unit.
			- Unit: enums.TimerUnit: S2, S30: unit 2 seconds, 30 seconds M1, M10: unit 1 minute, 10 minutes H1, H10, H320: unit 1 hour, 10 hours, 320 hours DEACtivated: timer deactivated"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_int('Factor'),
			ArgStruct.scalar_enum('Unit', enums.TimerUnit)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Factor: int = None
			self.Unit: enums.TimerUnit = None

	def get(self, name_ta_eps: str, tnum=repcap.Tnum.Default) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:EPS:TIMer:T<no>:EXTended \n
		Snippet: value: GetStruct = driver.configure.signaling.topology.eps.timer.t.extended.get(name_ta_eps = 'abc', tnum = repcap.Tnum.Default) \n
		Configures the extended timer T3412. \n
			:param name_ta_eps: Name of EPS tracking area
			:param tnum: optional repeated capability selector. Default value: Nr300 (settable in the interface 'T')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(name_ta_eps)
		tnum_cmd_val = self._cmd_group.get_repcap_cmd_value(tnum, repcap.Tnum)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:TOPology:EPS:TIMer:T{tnum_cmd_val}:EXTended? {param}', self.__class__.GetStruct())
