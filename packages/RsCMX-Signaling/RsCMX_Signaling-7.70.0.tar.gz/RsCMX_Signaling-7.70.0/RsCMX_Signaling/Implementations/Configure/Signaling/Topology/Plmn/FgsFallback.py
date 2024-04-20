from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FgsFallbackCls:
	"""FgsFallback commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fgsFallback", core, parent)

	def set(self, name_plmn: str, n_26_support: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:PLMN:FGSFallback \n
		Snippet: driver.configure.signaling.topology.plmn.fgsFallback.set(name_plmn = 'abc', n_26_support = False) \n
		Selects whether the 5G AMF behind NR cells has an N26 interface to a 4G MME. \n
			:param name_plmn: No help available
			:param n_26_support: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name_plmn', name_plmn, DataType.String), ArgSingle('n_26_support', n_26_support, DataType.Boolean))
		self._core.io.write(f'CONFigure:SIGNaling:TOPology:PLMN:FGSFallback {param}'.rstrip())

	def get(self, name_plmn: str) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:PLMN:FGSFallback \n
		Snippet: value: bool = driver.configure.signaling.topology.plmn.fgsFallback.get(name_plmn = 'abc') \n
		Selects whether the 5G AMF behind NR cells has an N26 interface to a 4G MME. \n
			:param name_plmn: No help available
			:return: n_26_support: No help available"""
		param = Conversions.value_to_quoted_str(name_plmn)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:TOPology:PLMN:FGSFallback? {param}')
		return Conversions.str_to_bool(response)
