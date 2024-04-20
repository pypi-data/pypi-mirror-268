from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UepLimitCls:
	"""UepLimit commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uepLimit", core, parent)

	def set(self, enable: bool, pcell_nr: enums.PcellNr = None, bwidth_total: enums.BwidthTotal = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:TMODe:UEPLimit \n
		Snippet: driver.configure.signaling.tmode.uepLimit.set(enable = False, pcell_nr = enums.PcellNr.B050, bwidth_total = enums.BwidthTotal.B100) \n
		Enables or disables the UL power limit function (UPLF) test mode at the UE. \n
			:param enable:
				- ON: Send an 'ACTIVATE POWER LIMIT REQUEST' message.
				- OFF: Send a 'DEACTIVATE POWER LIMIT REQUEST' message.
			:param pcell_nr: Value in MHz, configuring the information element 'PCELL NR BANDWIDTH' of the 'ACTIVATE POWER LIMIT
			REQUEST' message.
			:param bwidth_total: Value in MHz, configuring the information element 'TOTAL NR AGGREGATED BANDWIDTH' of the 'ACTIVATE
			POWER LIMIT REQUEST' message."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('pcell_nr', pcell_nr, DataType.Enum, enums.PcellNr, is_optional=True), ArgSingle('bwidth_total', bwidth_total, DataType.Enum, enums.BwidthTotal, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:TMODe:UEPLimit {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Status: enums.LimitStatus: OFF: UPLF is off. DPRogress: Deactivation of UPLF is in progress. ON: UPLF is ON. APRogress: Activation of UPLF is in progress.
			- Pcell_Nr: enums.PcellNr: Value in MHz, configuring the information element 'PCELL NR BANDWIDTH' of the 'ACTIVATE POWER LIMIT REQUEST' message.
			- Bwidth_Total: enums.BwidthTotal: Value in MHz, configuring the information element 'TOTAL NR AGGREGATED BANDWIDTH' of the 'ACTIVATE POWER LIMIT REQUEST' message."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Status', enums.LimitStatus),
			ArgStruct.scalar_enum('Pcell_Nr', enums.PcellNr),
			ArgStruct.scalar_enum('Bwidth_Total', enums.BwidthTotal)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Status: enums.LimitStatus = None
			self.Pcell_Nr: enums.PcellNr = None
			self.Bwidth_Total: enums.BwidthTotal = None

	def get(self) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:TMODe:UEPLimit \n
		Snippet: value: GetStruct = driver.configure.signaling.tmode.uepLimit.get() \n
		Enables or disables the UL power limit function (UPLF) test mode at the UE. \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:SIGNaling:TMODe:UEPLimit?', self.__class__.GetStruct())
