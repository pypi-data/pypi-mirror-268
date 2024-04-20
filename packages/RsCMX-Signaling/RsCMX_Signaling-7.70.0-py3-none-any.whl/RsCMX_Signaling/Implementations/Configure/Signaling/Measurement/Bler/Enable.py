from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnableCls:
	"""Enable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enable", core, parent)

	def set(self, dl: bool, ul: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:BLER:ENABle \n
		Snippet: driver.configure.signaling.measurement.bler.enable.set(dl = False, ul = False) \n
		Enables or disables the measurement of DL BLER and UL BLER results. This command affects BLER measurements started via a
		remote command. BLER measurements started via the GUI always deliver DL BLER and UL BLER results. \n
			:param dl: Measure DL BLER results (ON) or not (OFF) .
			:param ul: Measure UL BLER results (ON) or not (OFF) .
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('dl', dl, DataType.Boolean), ArgSingle('ul', ul, DataType.Boolean))
		self._core.io.write(f'CONFigure:SIGNaling:MEASurement:BLER:ENABle {param}'.rstrip())

	# noinspection PyTypeChecker
	class EnableStruct(StructBase):
		"""Response structure. Fields: \n
			- Dl: bool: Measure DL BLER results (ON) or not (OFF) .
			- Ul: bool: Measure UL BLER results (ON) or not (OFF) ."""
		__meta_args_list = [
			ArgStruct.scalar_bool('Dl'),
			ArgStruct.scalar_bool('Ul')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Dl: bool = None
			self.Ul: bool = None

	def get(self) -> EnableStruct:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:BLER:ENABle \n
		Snippet: value: EnableStruct = driver.configure.signaling.measurement.bler.enable.get() \n
		Enables or disables the measurement of DL BLER and UL BLER results. This command affects BLER measurements started via a
		remote command. BLER measurements started via the GUI always deliver DL BLER and UL BLER results. \n
			:return: structure: for return value, see the help for EnableStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:SIGNaling:MEASurement:BLER:ENABle?', self.__class__.EnableStruct())
