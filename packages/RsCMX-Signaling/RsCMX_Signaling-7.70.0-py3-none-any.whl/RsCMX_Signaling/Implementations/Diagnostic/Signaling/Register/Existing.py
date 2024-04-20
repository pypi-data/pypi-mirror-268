from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ExistingCls:
	"""Existing commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("existing", core, parent)

	def set(self, name_type: enums.NameType = None) -> None:
		"""SCPI: DIAGnostic:SIGNaling:REGister:EXISting \n
		Snippet: driver.diagnostic.signaling.register.existing.set(name_type = enums.NameType.GUI) \n
		No command help available \n
			:param name_type: No help available
		"""
		param = ''
		if name_type:
			param = Conversions.enum_scalar_to_str(name_type, enums.NameType)
		self._core.io.write(f'DIAGnostic:SIGNaling:REGister:EXISting {param}'.strip())
