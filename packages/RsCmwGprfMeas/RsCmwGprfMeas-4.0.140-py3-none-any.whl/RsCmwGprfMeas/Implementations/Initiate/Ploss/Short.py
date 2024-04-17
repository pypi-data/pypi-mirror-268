from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ShortCls:
	"""Short commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("short", core, parent)

	def set(self, connector: enums.CmwsConnector, path_index: enums.PathIndex = None) -> None:
		"""SCPI: INITiate:GPRF:MEASurement<Instance>:PLOSs:SHORt \n
		Snippet: driver.initiate.ploss.short.set(connector = enums.CmwsConnector.R11, path_index = enums.PathIndex.P1) \n
		No command help available \n
			:param connector: No help available
			:param path_index: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('connector', connector, DataType.Enum, enums.CmwsConnector), ArgSingle('path_index', path_index, DataType.Enum, enums.PathIndex, is_optional=True))
		self._core.io.write(f'INITiate:GPRF:MEASurement<Instance>:PLOSs:SHORt {param}'.rstrip())

	# noinspection PyTypeChecker
	class ShortStruct(StructBase):
		"""Response structure. Fields: \n
			- Connector: enums.CmwsConnector: No parameter help available
			- Path_Index: enums.PathIndex: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Connector', enums.CmwsConnector),
			ArgStruct.scalar_enum('Path_Index', enums.PathIndex)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Connector: enums.CmwsConnector = None
			self.Path_Index: enums.PathIndex = None

	def get(self) -> ShortStruct:
		"""SCPI: INITiate:GPRF:MEASurement<Instance>:PLOSs:SHORt \n
		Snippet: value: ShortStruct = driver.initiate.ploss.short.get() \n
		No command help available \n
			:return: structure: for return value, see the help for ShortStruct structure arguments."""
		return self._core.io.query_struct(f'INITiate:GPRF:MEASurement<Instance>:PLOSs:SHORt?', self.__class__.ShortStruct())
