from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ...........Internal.Types import DataType
from ...........Internal.ArgSingleList import ArgSingleList
from ...........Internal.ArgSingle import ArgSingle
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CrtypeCls:
	"""Crtype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("crtype", core, parent)

	def get(self, cell_name: str, subframe: int, cword=repcap.Cword.Default) -> float:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:DL:CWORd<no>:CRTYpe \n
		Snippet: value: float = driver.configure.signaling.lte.cell.ueScheduling.userDefined.sassignment.downlink.cword.crtype.get(cell_name = 'abc', subframe = 1, cword = repcap.Cword.Default) \n
		Queries the code rate for the DL subframe with the index <Subframe>, code word <no>. \n
			:param cell_name: No help available
			:param subframe: No help available
			:param cword: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cword')
			:return: coderate_type: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('subframe', subframe, DataType.Integer))
		cword_cmd_val = self._cmd_group.get_repcap_cmd_value(cword, repcap.Cword)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:DL:CWORd{cword_cmd_val}:CRTYpe? {param}'.rstrip())
		return Conversions.str_to_float(response)
