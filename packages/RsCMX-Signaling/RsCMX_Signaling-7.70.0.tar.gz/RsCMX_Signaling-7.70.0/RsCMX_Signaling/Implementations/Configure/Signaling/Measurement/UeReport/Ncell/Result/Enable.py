from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnableCls:
	"""Enable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enable", core, parent)

	def set(self, rsrp: bool, rsrq: bool, rssi_nr: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:UEReport:NCELl:RESult:ENABle \n
		Snippet: driver.configure.signaling.measurement.ueReport.ncell.result.enable.set(rsrp = False, rsrq = False, rssi_nr = False) \n
		Selects the quantities to be reported by the UE for neighbor cell measurements. Applies only to <Type> = CNETwork, see
		[CONFigure:]SIGNaling:MEASurement:UEReport:NCELl:RESult:TYPE \n
			:param rsrp: No help available
			:param rsrq: No help available
			:param rssi_nr: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('rsrp', rsrp, DataType.Boolean), ArgSingle('rsrq', rsrq, DataType.Boolean), ArgSingle('rssi_nr', rssi_nr, DataType.Boolean))
		self._core.io.write(f'CONFigure:SIGNaling:MEASurement:UEReport:NCELl:RESult:ENABle {param}'.rstrip())

	# noinspection PyTypeChecker
	class EnableStruct(StructBase):
		"""Response structure. Fields: \n
			- Rsrp: bool: No parameter help available
			- Rsrq: bool: No parameter help available
			- Rssi_Nr: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Rsrp'),
			ArgStruct.scalar_bool('Rsrq'),
			ArgStruct.scalar_bool('Rssi_Nr')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rsrp: bool = None
			self.Rsrq: bool = None
			self.Rssi_Nr: bool = None

	def get(self) -> EnableStruct:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:UEReport:NCELl:RESult:ENABle \n
		Snippet: value: EnableStruct = driver.configure.signaling.measurement.ueReport.ncell.result.enable.get() \n
		Selects the quantities to be reported by the UE for neighbor cell measurements. Applies only to <Type> = CNETwork, see
		[CONFigure:]SIGNaling:MEASurement:UEReport:NCELl:RESult:TYPE \n
			:return: structure: for return value, see the help for EnableStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:SIGNaling:MEASurement:UEReport:NCELl:RESult:ENABle?', self.__class__.EnableStruct())
