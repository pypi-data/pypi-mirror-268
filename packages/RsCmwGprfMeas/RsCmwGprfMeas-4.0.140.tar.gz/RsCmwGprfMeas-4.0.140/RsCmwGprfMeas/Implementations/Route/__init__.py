from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RouteCls:
	"""Route commands group definition. 7 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("route", core, parent)

	@property
	def scenario(self):
		"""scenario commands group. 4 Sub-classes, 2 commands."""
		if not hasattr(self, '_scenario'):
			from .Scenario import ScenarioCls
			self._scenario = ScenarioCls(self._core, self._cmd_group)
		return self._scenario

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Scenario: enums.Scenario: SALone | CSPath SALone: standalone (non-signaling) scenario CSPath: combined signal path scenario
			- Master: str: string Controlling application for scenario CSPath
			- Rf_Connector: enums.RfConnector: RF connector for the input path
			- Rf_Converter: enums.RxConverter: RX module for the input path"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Scenario', enums.Scenario),
			ArgStruct.scalar_str('Master'),
			ArgStruct.scalar_enum('Rf_Connector', enums.RfConnector),
			ArgStruct.scalar_enum('Rf_Converter', enums.RxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Scenario: enums.Scenario = None
			self.Master: str = None
			self.Rf_Connector: enums.RfConnector = None
			self.Rf_Converter: enums.RxConverter = None

	def get_value(self) -> ValueStruct:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance> \n
		Snippet: value: ValueStruct = driver.route.get_value() \n
		Returns the configured routing settings. For possible connector and converter values, see 'Values for RF path selection'. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:GPRF:MEASurement<Instance>?', self.__class__.ValueStruct())

	def clone(self) -> 'RouteCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RouteCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
