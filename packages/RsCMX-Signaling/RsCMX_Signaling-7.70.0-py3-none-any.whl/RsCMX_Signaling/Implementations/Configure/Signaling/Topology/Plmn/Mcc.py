from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.Utilities import trim_str_response
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MccCls:
	"""Mcc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcc", core, parent)

	def set(self, name_plmn: str, mcc: str) -> None:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:PLMN:MCC \n
		Snippet: driver.configure.signaling.topology.plmn.mcc.set(name_plmn = 'abc', mcc = 'abc') \n
		Configures the mobile country code (MCC) of a PLMN. \n
			:param name_plmn: No help available
			:param mcc: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name_plmn', name_plmn, DataType.String), ArgSingle('mcc', mcc, DataType.String))
		self._core.io.write(f'CONFigure:SIGNaling:TOPology:PLMN:MCC {param}'.rstrip())

	def get(self, name_plmn: str) -> str:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:PLMN:MCC \n
		Snippet: value: str = driver.configure.signaling.topology.plmn.mcc.get(name_plmn = 'abc') \n
		Configures the mobile country code (MCC) of a PLMN. \n
			:param name_plmn: No help available
			:return: mcc: No help available"""
		param = Conversions.value_to_quoted_str(name_plmn)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:TOPology:PLMN:MCC? {param}')
		return trim_str_response(response)
