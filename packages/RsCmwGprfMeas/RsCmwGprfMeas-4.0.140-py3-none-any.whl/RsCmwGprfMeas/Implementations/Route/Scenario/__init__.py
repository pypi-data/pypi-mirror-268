from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScenarioCls:
	"""Scenario commands group definition. 6 total commands, 4 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scenario", core, parent)

	@property
	def maProtocol(self):
		"""maProtocol commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maProtocol'):
			from .MaProtocol import MaProtocolCls
			self._maProtocol = MaProtocolCls(self._core, self._cmd_group)
		return self._maProtocol

	@property
	def salone(self):
		"""salone commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_salone'):
			from .Salone import SaloneCls
			self._salone = SaloneCls(self._core, self._cmd_group)
		return self._salone

	@property
	def maiq(self):
		"""maiq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maiq'):
			from .Maiq import MaiqCls
			self._maiq = MaiqCls(self._core, self._cmd_group)
		return self._maiq

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import CatalogCls
			self._catalog = CatalogCls(self._core, self._cmd_group)
		return self._catalog

	def get_cspath(self) -> str:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance>:SCENario:CSPath \n
		Snippet: value: str = driver.route.scenario.get_cspath() \n
		Activates the combined signal path scenario and selects a controlling firmware application for the GPRF measurements. The
		selected application controls the signal routing settings and analyzer settings while the combined signal path scenario
		is active. To query a list of possible <Controller> values, see method RsCmwGprfMeas.Route.Scenario.Catalog.cspath. \n
			:return: master: No help available
		"""
		response = self._core.io.query_str('ROUTe:GPRF:MEASurement<Instance>:SCENario:CSPath?')
		return trim_str_response(response)

	def set_cspath(self, master: str) -> None:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance>:SCENario:CSPath \n
		Snippet: driver.route.scenario.set_cspath(master = 'abc') \n
		Activates the combined signal path scenario and selects a controlling firmware application for the GPRF measurements. The
		selected application controls the signal routing settings and analyzer settings while the combined signal path scenario
		is active. To query a list of possible <Controller> values, see method RsCmwGprfMeas.Route.Scenario.Catalog.cspath. \n
			:param master: string Example: 'LTE Sig1'
		"""
		param = Conversions.value_to_quoted_str(master)
		self._core.io.write(f'ROUTe:GPRF:MEASurement<Instance>:SCENario:CSPath {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.Scenario:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance>:SCENario \n
		Snippet: value: enums.Scenario = driver.route.scenario.get_value() \n
		Queries the active scenario. \n
			:return: scenario: SALone | CSPath SALone: standalone (non-signaling) scenario CSPath: combined signal path scenario
		"""
		response = self._core.io.query_str('ROUTe:GPRF:MEASurement<Instance>:SCENario?')
		return Conversions.str_to_scalar_enum(response, enums.Scenario)

	def clone(self) -> 'ScenarioCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ScenarioCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
