from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PeriodicityCls:
	"""Periodicity commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("periodicity", core, parent)

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.PeriodicityCqiReport:
		"""SCPI: SENSe:SIGNaling:NRADio:CELL:CQIReporting:REPort:PERiodicity \n
		Snippet: value: enums.PeriodicityCqiReport = driver.sense.signaling.nradio.cell.cqiReporting.report.periodicity.get(cell_name = 'abc') \n
		Queries the periodicity of CSI reports,
		configured indirectly via [CONFigure:]SIGNaling:NRADio:CELL:CQIReporting:PERiodicity, for the initial BWP. \n
			:param cell_name: No help available
			:return: periodicity: Periodicity in slots"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'SENSe:SIGNaling:NRADio:CELL:CQIReporting:REPort:PERiodicity? {param}')
		return Conversions.str_to_scalar_enum(response, enums.PeriodicityCqiReport)
