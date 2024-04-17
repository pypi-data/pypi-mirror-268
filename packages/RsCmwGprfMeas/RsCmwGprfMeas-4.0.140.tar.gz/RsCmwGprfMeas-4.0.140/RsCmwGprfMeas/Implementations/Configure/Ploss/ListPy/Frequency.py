from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrequencyCls:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, connector: enums.CmwsConnector, num_entries: int, frequency: List[float]) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:PLOSs:LIST:FREQuency \n
		Snippet: driver.configure.ploss.listPy.frequency.set(connector = enums.CmwsConnector.R11, num_entries = 1, frequency = [1.1, 2.2, 3.3]) \n
		No command help available \n
			:param connector: No help available
			:param num_entries: No help available
			:param frequency: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('connector', connector, DataType.Enum, enums.CmwsConnector), ArgSingle('num_entries', num_entries, DataType.Integer), ArgSingle.as_open_list('frequency', frequency, DataType.FloatList, None))
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:PLOSs:LIST:FREQuency {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Num_Entries: int: No parameter help available
			- Frequency: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Num_Entries'),
			ArgStruct('Frequency', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Num_Entries: int = None
			self.Frequency: List[float] = None

	def get(self, connector: enums.CmwsConnector) -> GetStruct:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:PLOSs:LIST:FREQuency \n
		Snippet: value: GetStruct = driver.configure.ploss.listPy.frequency.get(connector = enums.CmwsConnector.R11) \n
		No command help available \n
			:param connector: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.enum_scalar_to_str(connector, enums.CmwsConnector)
		return self._core.io.query_struct(f'CONFigure:GPRF:MEASurement<Instance>:PLOSs:LIST:FREQuency? {param}', self.__class__.GetStruct())
