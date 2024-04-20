from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.Utilities import trim_str_response
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MncCls:
	"""Mnc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mnc", core, parent)

	def set(self, name_plmn: str, mnc: str) -> None:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:PLMN:MNC \n
		Snippet: driver.configure.signaling.topology.plmn.mnc.set(name_plmn = 'abc', mnc = 'abc') \n
		Configures the mobile network code (MNC) of a PLMN. \n
			:param name_plmn: No help available
			:param mnc: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name_plmn', name_plmn, DataType.String), ArgSingle('mnc', mnc, DataType.String))
		self._core.io.write(f'CONFigure:SIGNaling:TOPology:PLMN:MNC {param}'.rstrip())

	def get(self, name_plmn: str) -> str:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:PLMN:MNC \n
		Snippet: value: str = driver.configure.signaling.topology.plmn.mnc.get(name_plmn = 'abc') \n
		Configures the mobile network code (MNC) of a PLMN. \n
			:param name_plmn: No help available
			:return: mnc: No help available"""
		param = Conversions.value_to_quoted_str(name_plmn)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:TOPology:PLMN:MNC? {param}')
		return trim_str_response(response)
