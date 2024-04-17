from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPyCls:
	"""ListPy commands group definition. 23 total commands, 8 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	@property
	def singleCmw(self):
		"""singleCmw commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_singleCmw'):
			from .SingleCmw import SingleCmwCls
			self._singleCmw = SingleCmwCls(self._core, self._cmd_group)
		return self._singleCmw

	@property
	def iqData(self):
		"""iqData commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_iqData'):
			from .IqData import IqDataCls
			self._iqData = IqDataCls(self._core, self._cmd_group)
		return self._iqData

	@property
	def sstop(self):
		"""sstop commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sstop'):
			from .Sstop import SstopCls
			self._sstop = SstopCls(self._core, self._cmd_group)
		return self._sstop

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def envelopePower(self):
		"""envelopePower commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_envelopePower'):
			from .EnvelopePower import EnvelopePowerCls
			self._envelopePower = EnvelopePowerCls(self._core, self._cmd_group)
		return self._envelopePower

	@property
	def retrigger(self):
		"""retrigger commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_retrigger'):
			from .Retrigger import RetriggerCls
			self._retrigger = RetriggerCls(self._core, self._cmd_group)
		return self._retrigger

	@property
	def irepetition(self):
		"""irepetition commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_irepetition'):
			from .Irepetition import IrepetitionCls
			self._irepetition = IrepetitionCls(self._core, self._cmd_group)
		return self._irepetition

	@property
	def parameterSetList(self):
		"""parameterSetList commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_parameterSetList'):
			from .ParameterSetList import ParameterSetListCls
			self._parameterSetList = ParameterSetListCls(self._core, self._cmd_group)
		return self._parameterSetList

	# noinspection PyTypeChecker
	def get_txi_timing(self) -> enums.Timing:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:TXITiming \n
		Snippet: value: enums.Timing = driver.configure.power.listPy.get_txi_timing() \n
		Specifies the timing of the generated 'GPRF Meas<i>:Power' trigger. \n
			:return: timing: STEP | CENTered STEP: Trigger signals are generated between step lengths. CENTered: Trigger signals are generated between measurement lengths.
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:TXITiming?')
		return Conversions.str_to_scalar_enum(response, enums.Timing)

	def set_txi_timing(self, timing: enums.Timing) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:TXITiming \n
		Snippet: driver.configure.power.listPy.set_txi_timing(timing = enums.Timing.CENTered) \n
		Specifies the timing of the generated 'GPRF Meas<i>:Power' trigger. \n
			:param timing: STEP | CENTered STEP: Trigger signals are generated between step lengths. CENTered: Trigger signals are generated between measurement lengths.
		"""
		param = Conversions.enum_scalar_to_str(timing, enums.Timing)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:TXITiming {param}')

	# noinspection PyTypeChecker
	def get_munit(self) -> enums.MagnitudeUnit:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:MUNit \n
		Snippet: value: enums.MagnitudeUnit = driver.configure.power.listPy.get_munit() \n
		No command help available \n
			:return: magnitude_unit: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:MUNit?')
		return Conversions.str_to_scalar_enum(response, enums.MagnitudeUnit)

	def set_munit(self, magnitude_unit: enums.MagnitudeUnit) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:MUNit \n
		Snippet: driver.configure.power.listPy.set_munit(magnitude_unit = enums.MagnitudeUnit.RAW) \n
		No command help available \n
			:param magnitude_unit: No help available
		"""
		param = Conversions.enum_scalar_to_str(magnitude_unit, enums.MagnitudeUnit)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:MUNit {param}')

	def get_count(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:COUNt \n
		Snippet: value: int = driver.configure.power.listPy.get_count() \n
		Queries the total number of segments per sweep, including repetitions. \n
			:return: result_count: decimal Range: 1 to 10000
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:COUNt?')
		return Conversions.str_to_int(response)

	def get_start(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:STARt \n
		Snippet: value: int = driver.configure.power.listPy.get_start() \n
		Selects the first segment to be measured (start of a sweep) . The total number of segments per sweep, including
		repetitions, must not be higher than 10000. \n
			:return: start_index: numeric Range: 0 to StopIndex
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:STARt?')
		return Conversions.str_to_int(response)

	def set_start(self, start_index: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:STARt \n
		Snippet: driver.configure.power.listPy.set_start(start_index = 1) \n
		Selects the first segment to be measured (start of a sweep) . The total number of segments per sweep, including
		repetitions, must not be higher than 10000. \n
			:param start_index: numeric Range: 0 to StopIndex
		"""
		param = Conversions.decimal_value_to_str(start_index)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:STARt {param}')

	def get_stop(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:STOP \n
		Snippet: value: int = driver.configure.power.listPy.get_stop() \n
		Selects the last segment to be measured (end of a sweep) . The total number of segments per sweep, including repetitions,
		must not be higher than 10000. \n
			:return: stop_index: numeric Range: StartIndex to 3999
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:STOP?')
		return Conversions.str_to_int(response)

	def set_stop(self, stop_index: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:STOP \n
		Snippet: driver.configure.power.listPy.set_stop(stop_index = 1) \n
		Selects the last segment to be measured (end of a sweep) . The total number of segments per sweep, including repetitions,
		must not be higher than 10000. \n
			:param stop_index: numeric Range: StartIndex to 3999
		"""
		param = Conversions.decimal_value_to_str(stop_index)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:STOP {param}')

	def get_value(self) -> bool:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST \n
		Snippet: value: bool = driver.configure.power.listPy.get_value() \n
		Enables or disables the list mode for the power measurement. \n
			:return: enable_list_mode: OFF | ON OFF: list mode off ON: list mode on
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST?')
		return Conversions.str_to_bool(response)

	def set_value(self, enable_list_mode: bool) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST \n
		Snippet: driver.configure.power.listPy.set_value(enable_list_mode = False) \n
		Enables or disables the list mode for the power measurement. \n
			:param enable_list_mode: OFF | ON OFF: list mode off ON: list mode on
		"""
		param = Conversions.bool_to_str(enable_list_mode)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST {param}')

	def clone(self) -> 'ListPyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ListPyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
