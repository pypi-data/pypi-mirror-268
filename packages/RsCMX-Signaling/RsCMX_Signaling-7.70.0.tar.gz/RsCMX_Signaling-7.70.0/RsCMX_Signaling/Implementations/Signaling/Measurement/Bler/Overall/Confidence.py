from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConfidenceCls:
	"""Confidence commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("confidence", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> enums.BlerState:
		"""SCPI: FETCh:SIGNaling:MEASurement:BLER:OVERall:CONFidence \n
		Snippet: value: enums.BlerState = driver.signaling.measurement.bler.overall.confidence.fetch() \n
		Returns the overall results of a confidence BLER measurement. \n
		Suppressed linked return values: reliability \n
			:return: state: PENDing: measurement still running, no verdict yet PASS, FAIL: verdict of the measurement"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:SIGNaling:MEASurement:BLER:OVERall:CONFidence?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.BlerState)
