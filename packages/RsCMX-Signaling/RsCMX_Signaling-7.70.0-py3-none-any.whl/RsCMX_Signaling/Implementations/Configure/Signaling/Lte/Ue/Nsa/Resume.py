from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResumeCls:
	"""Resume commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("resume", core, parent)

	def set(self, ue_id: str = None, bearer_id: List[int] = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:UE:NSA:RESume \n
		Snippet: driver.configure.signaling.lte.ue.nsa.resume.set(ue_id = 'abc', bearer_id = [1, 2, 3]) \n
		Resumes the EN-DC mode after an error resulting in a suspended EN-DC mode. \n
			:param ue_id: For future use. Enter any value if you want to use optional parameters.
			:param bearer_id: ID of the dedicated bearer. To get a list of all dedicated bearer IDs, see method RsCMX_Signaling.Catalog.Signaling.Lte.Ue.Dbearer.get_.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ue_id', ue_id, DataType.String, None, is_optional=True), ArgSingle('bearer_id', bearer_id, DataType.IntegerList, None, True, True, 1))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:UE:NSA:RESume {param}'.rstrip())
