from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CgroupCls:
	"""Cgroup commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cgroup", core, parent)

	def set(self, mcg: bool, scg: bool = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:BLER:CMEasure:CGRoup \n
		Snippet: driver.configure.signaling.measurement.bler.cmeasure.cgroup.set(mcg = False, scg = False) \n
		Selects the cell groups to be evaluated by the BLER measurement. \n
			:param mcg: No help available
			:param scg: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('mcg', mcg, DataType.Boolean), ArgSingle('scg', scg, DataType.Boolean, None, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:MEASurement:BLER:CMEasure:CGRoup {param}'.rstrip())

	# noinspection PyTypeChecker
	class CgroupStruct(StructBase):
		"""Response structure. Fields: \n
			- Mcg: bool: No parameter help available
			- Scg: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Mcg'),
			ArgStruct.scalar_bool('Scg')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Mcg: bool = None
			self.Scg: bool = None

	def get(self) -> CgroupStruct:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:BLER:CMEasure:CGRoup \n
		Snippet: value: CgroupStruct = driver.configure.signaling.measurement.bler.cmeasure.cgroup.get() \n
		Selects the cell groups to be evaluated by the BLER measurement. \n
			:return: structure: for return value, see the help for CgroupStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:SIGNaling:MEASurement:BLER:CMEasure:CGRoup?', self.__class__.CgroupStruct())
