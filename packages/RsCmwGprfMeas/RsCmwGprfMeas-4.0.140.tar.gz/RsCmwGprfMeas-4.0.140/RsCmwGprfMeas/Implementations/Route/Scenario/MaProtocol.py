from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaProtocolCls:
	"""MaProtocol commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maProtocol", core, parent)

	def set(self, controler: str = None, converter: enums.RxConverter = None) -> None:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance>:SCENario:MAPRotocol \n
		Snippet: driver.route.scenario.maProtocol.set(controler = 'abc', converter = enums.RxConverter.IRX1) \n
		No command help available \n
			:param controler: No help available
			:param converter: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('controler', controler, DataType.String, None, is_optional=True), ArgSingle('converter', converter, DataType.Enum, enums.RxConverter, is_optional=True))
		self._core.io.write(f'ROUTe:GPRF:MEASurement<Instance>:SCENario:MAPRotocol {param}'.rstrip())
