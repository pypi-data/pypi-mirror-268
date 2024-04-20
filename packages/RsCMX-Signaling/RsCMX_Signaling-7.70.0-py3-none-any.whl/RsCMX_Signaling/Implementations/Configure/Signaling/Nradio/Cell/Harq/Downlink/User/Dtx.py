from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DtxCls:
	"""Dtx commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dtx", core, parent)

	def set(self, cell_name: str, dtx: enums.AckOrDtx) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:HARQ:DL:USER:DTX \n
		Snippet: driver.configure.signaling.nradio.cell.harq.downlink.user.dtx.set(cell_name = 'abc', dtx = enums.AckOrDtx.CONTinue) \n
		Defines the reaction to DTX (missing ACKs) , for user-defined DL HARQ, for the initial BWP. \n
			:param cell_name: No help available
			:param dtx: STOP: stop retransmitting CONTinue: continue retransmitting
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('dtx', dtx, DataType.Enum, enums.AckOrDtx))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:HARQ:DL:USER:DTX {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.AckOrDtx:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:HARQ:DL:USER:DTX \n
		Snippet: value: enums.AckOrDtx = driver.configure.signaling.nradio.cell.harq.downlink.user.dtx.get(cell_name = 'abc') \n
		Defines the reaction to DTX (missing ACKs) , for user-defined DL HARQ, for the initial BWP. \n
			:param cell_name: No help available
			:return: dtx: STOP: stop retransmitting CONTinue: continue retransmitting"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:HARQ:DL:USER:DTX? {param}')
		return Conversions.str_to_scalar_enum(response, enums.AckOrDtx)
