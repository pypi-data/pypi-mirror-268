from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SubsetCls:
	"""Subset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("subset", core, parent)

	def set(self, cell_name: str, subset: enums.CodebookSubset, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bpwid>:PUSCh:TSCHema:CODebook:SUBSet \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.pusch.tschema.codebook.subset.set(cell_name = 'abc', subset = enums.CodebookSubset.AUTO, bwParts = repcap.BwParts.Default) \n
		Selects the codebook subset for codebook-based transmission (signaled 'codebookSubset') , for BWP <bb>. \n
			:param cell_name: No help available
			:param subset: AUTO: signaled value selected via reported UE capabilities FPNC: signaled value 'fullyAndPartialAndNonCoherent' PNC: signaled value 'partialAndNonCoherent', currently not supported NC: signaled value 'nonCoherent'
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('subset', subset, DataType.Enum, enums.CodebookSubset))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:PUSCh:TSCHema:CODebook:SUBSet {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> enums.CodebookSubset:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bpwid>:PUSCh:TSCHema:CODebook:SUBSet \n
		Snippet: value: enums.CodebookSubset = driver.configure.signaling.nradio.cell.bwp.pusch.tschema.codebook.subset.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Selects the codebook subset for codebook-based transmission (signaled 'codebookSubset') , for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: subset: AUTO: signaled value selected via reported UE capabilities FPNC: signaled value 'fullyAndPartialAndNonCoherent' PNC: signaled value 'partialAndNonCoherent', currently not supported NC: signaled value 'nonCoherent'"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:PUSCh:TSCHema:CODebook:SUBSet? {param}')
		return Conversions.str_to_scalar_enum(response, enums.CodebookSubset)
