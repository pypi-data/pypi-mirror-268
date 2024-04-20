from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SubsetCls:
	"""Subset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("subset", core, parent)

	def set(self, cell_name: str, subset: enums.CodebookSubset) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:PUSCh:TSCHema:CODebook:SUBSet \n
		Snippet: driver.configure.signaling.nradio.cell.pusch.tschema.codebook.subset.set(cell_name = 'abc', subset = enums.CodebookSubset.AUTO) \n
		Selects the codebook subset for codebook-based transmission (signaled 'codebookSubset') , for the initial BWP. \n
			:param cell_name: No help available
			:param subset: AUTO: signaled value selected via reported UE capabilities FPNC: signaled value 'fullyAndPartialAndNonCoherent' PNC: signaled value 'partialAndNonCoherent', currently not supported NC: signaled value 'nonCoherent'
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('subset', subset, DataType.Enum, enums.CodebookSubset))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:PUSCh:TSCHema:CODebook:SUBSet {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.CodebookSubset:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:PUSCh:TSCHema:CODebook:SUBSet \n
		Snippet: value: enums.CodebookSubset = driver.configure.signaling.nradio.cell.pusch.tschema.codebook.subset.get(cell_name = 'abc') \n
		Selects the codebook subset for codebook-based transmission (signaled 'codebookSubset') , for the initial BWP. \n
			:param cell_name: No help available
			:return: subset: AUTO: signaled value selected via reported UE capabilities FPNC: signaled value 'fullyAndPartialAndNonCoherent' PNC: signaled value 'partialAndNonCoherent', currently not supported NC: signaled value 'nonCoherent'"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:PUSCh:TSCHema:CODebook:SUBSet? {param}')
		return Conversions.str_to_scalar_enum(response, enums.CodebookSubset)
