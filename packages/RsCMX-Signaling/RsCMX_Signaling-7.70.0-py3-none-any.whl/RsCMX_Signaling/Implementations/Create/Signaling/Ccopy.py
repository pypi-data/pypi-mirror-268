from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CcopyCls:
	"""Ccopy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ccopy", core, parent)

	def set(self, cell_name: str, no_copies: int, continuous: bool) -> None:
		"""SCPI: CREate:SIGNaling:CCOPy \n
		Snippet: driver.create.signaling.ccopy.set(cell_name = 'abc', no_copies = 1, continuous = False) \n
		Copies a cell. \n
			:param cell_name: Name of the source cell.
			:param no_copies: Number of cell copies to be created.
			:param continuous:
				- ON: Places the cell copies above the source cell in the same frequency band. Configures the frequencies of the cell copies for intraband contiguous carrier aggregation.
				- OFF: Copies the frequency settings of the source cell."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('no_copies', no_copies, DataType.Integer), ArgSingle('continuous', continuous, DataType.Boolean))
		self._core.io.write(f'CREate:SIGNaling:CCOPy {param}'.rstrip())
