from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerCls:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal See 'Reliability indicator'
			- Avg: float: float Average power of all samples Unit: dBm
			- Max_Py: float: float Maximum power of all samples Unit: dBm
			- Par: float: float Peak to average ratio Unit: dB
			- Index_Avg_Power: int: decimal Index of the average power 'bin'"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Avg'),
			ArgStruct.scalar_float('Max_Py'),
			ArgStruct.scalar_float('Par'),
			ArgStruct.scalar_int('Index_Avg_Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Avg: float = None
			self.Max_Py: float = None
			self.Par: float = None
			self.Index_Avg_Power: int = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:POWer:CCDF:POWer \n
		Snippet: value: FetchStruct = driver.power.cumulativeDistribFnc.power.fetch() \n
		Returns some statistic results for the power samples. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:GPRF:MEASurement<Instance>:POWer:CCDF:POWer?', self.__class__.FetchStruct())
