from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NulPowerCls:
	"""NulPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nulPower", core, parent)

	def set(self, cell_name: str, behavior: enums.AckOrDtx) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:HARQ:UL:BEHavior:NULPower \n
		Snippet: driver.configure.signaling.nradio.cell.harq.uplink.behavior.nulPower.set(cell_name = 'abc', behavior = enums.AckOrDtx.CONTinue) \n
		Defines the behavior when detecting no UL power: stop or continue requesting retransmissions from the UE, for the initial
		BWP. \n
			:param cell_name: No help available
			:param behavior: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('behavior', behavior, DataType.Enum, enums.AckOrDtx))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:HARQ:UL:BEHavior:NULPower {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.AckOrDtx:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:HARQ:UL:BEHavior:NULPower \n
		Snippet: value: enums.AckOrDtx = driver.configure.signaling.nradio.cell.harq.uplink.behavior.nulPower.get(cell_name = 'abc') \n
		Defines the behavior when detecting no UL power: stop or continue requesting retransmissions from the UE, for the initial
		BWP. \n
			:param cell_name: No help available
			:return: behavior: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:HARQ:UL:BEHavior:NULPower? {param}')
		return Conversions.str_to_scalar_enum(response, enums.AckOrDtx)
