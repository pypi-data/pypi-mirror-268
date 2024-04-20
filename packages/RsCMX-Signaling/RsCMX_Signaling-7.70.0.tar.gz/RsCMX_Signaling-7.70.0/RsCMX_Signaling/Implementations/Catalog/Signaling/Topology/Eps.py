from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EpsCls:
	"""Eps commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eps", core, parent)

	def get_ue(self) -> List[str]:
		"""SCPI: CATalog:SIGNaling:TOPology:EPS:UE \n
		Snippet: value: List[str] = driver.catalog.signaling.topology.eps.get_ue() \n
		No command help available \n
			:return: ui_id: No help available
		"""
		response = self._core.io.query_str('CATalog:SIGNaling:TOPology:EPS:UE?')
		return Conversions.str_to_str_list(response)

	def get(self, name_plmn: str = None) -> List[str]:
		"""SCPI: CATalog:SIGNaling:TOPology:EPS \n
		Snippet: value: List[str] = driver.catalog.signaling.topology.eps.get(name_plmn = 'abc') \n
		Queries a list of all EPS tracking areas. You can restrict the query to a selected PLMN. \n
			:param name_plmn: No help available
			:return: name_ta_eps: Comma-separated list of tracking area names, one string per tracking area."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name_plmn', name_plmn, DataType.String, None, is_optional=True))
		response = self._core.io.query_str(f'CATalog:SIGNaling:TOPology:EPS? {param}'.rstrip())
		return Conversions.str_to_str_list(response)
