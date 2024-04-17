from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Result_State_Open: enums.PathLossState: No parameter help available
			- Result_State_Short: enums.PathLossState: No parameter help available
			- Result_State_Eval: enums.PathLossState: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Result_State_Open', enums.PathLossState),
			ArgStruct.scalar_enum('Result_State_Short', enums.PathLossState),
			ArgStruct.scalar_enum('Result_State_Eval', enums.PathLossState)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Result_State_Open: enums.PathLossState = None
			self.Result_State_Short: enums.PathLossState = None
			self.Result_State_Eval: enums.PathLossState = None

	def fetch(self, connector: enums.CmwsConnector, path_index: enums.PathIndex = None) -> FetchStruct:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:PLOSs:EVAL:STATe \n
		Snippet: value: FetchStruct = driver.ploss.eval.state.fetch(connector = enums.CmwsConnector.R11, path_index = enums.PathIndex.P1) \n
		No command help available \n
			:param connector: No help available
			:param path_index: No help available
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('connector', connector, DataType.Enum, enums.CmwsConnector), ArgSingle('path_index', path_index, DataType.Enum, enums.PathIndex, is_optional=True))
		return self._core.io.query_struct(f'FETCh:GPRF:MEASurement<Instance>:PLOSs:EVAL:STATe? {param}'.rstrip(), self.__class__.FetchStruct())
