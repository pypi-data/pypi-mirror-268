from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SconditionCls:
	"""Scondition commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scondition", core, parent)

	def set(self, stop_condition: enums.StopCondition, value: float = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:BLER:SCONdition \n
		Snippet: driver.configure.signaling.measurement.bler.scondition.set(stop_condition = enums.StopCondition.CONFidence, value = 1.0) \n
		Defines a stop condition for single-shot BLER measurements. \n
			:param stop_condition: SAMPles: number of samples reached for at least one cell TIME: measurement duration reached CONFidence: confidence BLER verdict derived
			:param value: For SAMPles, number of samples. For TIME, measurement duration. For CONFidence, number of samples applied beyond the maximum value defined by 3GPP (2466 without CA, 1003 per CC with CA) .
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('stop_condition', stop_condition, DataType.Enum, enums.StopCondition), ArgSingle('value', value, DataType.Float, None, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:MEASurement:BLER:SCONdition {param}'.rstrip())

	# noinspection PyTypeChecker
	class SconditionStruct(StructBase):
		"""Response structure. Fields: \n
			- Stop_Condition: enums.StopCondition: SAMPles: number of samples reached for at least one cell TIME: measurement duration reached CONFidence: confidence BLER verdict derived
			- Value: float: For SAMPles, number of samples. For TIME, measurement duration. For CONFidence, number of samples applied beyond the maximum value defined by 3GPP (2466 without CA, 1003 per CC with CA) ."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Stop_Condition', enums.StopCondition),
			ArgStruct.scalar_float('Value')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Stop_Condition: enums.StopCondition = None
			self.Value: float = None

	def get(self) -> SconditionStruct:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:BLER:SCONdition \n
		Snippet: value: SconditionStruct = driver.configure.signaling.measurement.bler.scondition.get() \n
		Defines a stop condition for single-shot BLER measurements. \n
			:return: structure: for return value, see the help for SconditionStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:SIGNaling:MEASurement:BLER:SCONdition?', self.__class__.SconditionStruct())
