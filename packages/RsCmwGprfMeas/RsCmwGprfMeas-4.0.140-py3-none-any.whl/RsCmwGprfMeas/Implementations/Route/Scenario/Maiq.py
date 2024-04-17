from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaiqCls:
	"""Maiq commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maiq", core, parent)

	def set(self, rx_connector: enums.RfConnector, rf_converter: enums.RxConverter) -> None:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance>:SCENario:MAIQ \n
		Snippet: driver.route.scenario.maiq.set(rx_connector = enums.RfConnector.I11I, rf_converter = enums.RxConverter.IRX1) \n
		No command help available \n
			:param rx_connector: No help available
			:param rf_converter: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('rx_connector', rx_connector, DataType.Enum, enums.RfConnector), ArgSingle('rf_converter', rf_converter, DataType.Enum, enums.RxConverter))
		self._core.io.write(f'ROUTe:GPRF:MEASurement<Instance>:SCENario:MAIQ {param}'.rstrip())

	# noinspection PyTypeChecker
	class MaiqStruct(StructBase):
		"""Response structure. Fields: \n
			- Rx_Connector: enums.RfConnector: No parameter help available
			- Rf_Converter: enums.RxConverter: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Rx_Connector', enums.RfConnector),
			ArgStruct.scalar_enum('Rf_Converter', enums.RxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx_Connector: enums.RfConnector = None
			self.Rf_Converter: enums.RxConverter = None

	def get(self) -> MaiqStruct:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance>:SCENario:MAIQ \n
		Snippet: value: MaiqStruct = driver.route.scenario.maiq.get() \n
		No command help available \n
			:return: structure: for return value, see the help for MaiqStruct structure arguments."""
		return self._core.io.query_struct(f'ROUTe:GPRF:MEASurement<Instance>:SCENario:MAIQ?', self.__class__.MaiqStruct())
