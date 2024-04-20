from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SeedCls:
	"""Seed commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("seed", core, parent)

	def set(self, cell_name: str, start_seed: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:FADing:SEED \n
		Snippet: driver.configure.signaling.fading.seed.set(cell_name = 'abc', start_seed = 1) \n
		Sets the start seed for the pseudo-random fading algorithm. \n
			:param cell_name: No help available
			:param start_seed: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('start_seed', start_seed, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:FADing:SEED {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:FADing:SEED \n
		Snippet: value: int = driver.configure.signaling.fading.seed.get(cell_name = 'abc') \n
		Sets the start seed for the pseudo-random fading algorithm. \n
			:param cell_name: No help available
			:return: start_seed: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:FADing:SEED? {param}')
		return Conversions.str_to_int(response)
