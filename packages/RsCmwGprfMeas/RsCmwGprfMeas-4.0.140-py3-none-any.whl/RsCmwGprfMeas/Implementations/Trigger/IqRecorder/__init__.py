from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqRecorderCls:
	"""IqRecorder commands group definition. 9 total commands, 1 Subgroups, 8 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqRecorder", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import CatalogCls
			self._catalog = CatalogCls(self._core, self._cmd_group)
		return self._catalog

	def get_source(self) -> str:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:SOURce \n
		Snippet: value: str = driver.trigger.iqRecorder.get_source() \n
		Selects the source of the trigger events. Some values are always available. They are listed below. Depending on the
		installed options, additional values are available. You can query a list of all supported values via TRIGger:...
		:CATalog:SOURce?. \n
			:return: source: string 'IF Power': IF power trigger 'Free Run': free run (untriggered)
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:IQRecorder:SOURce?')
		return trim_str_response(response)

	def set_source(self, source: str) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:SOURce \n
		Snippet: driver.trigger.iqRecorder.set_source(source = 'abc') \n
		Selects the source of the trigger events. Some values are always available. They are listed below. Depending on the
		installed options, additional values are available. You can query a list of all supported values via TRIGger:...
		:CATalog:SOURce?. \n
			:param source: string 'IF Power': IF power trigger 'Free Run': free run (untriggered)
		"""
		param = Conversions.value_to_quoted_str(source)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:IQRecorder:SOURce {param}')

	def get_offset(self) -> int:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:OFFSet \n
		Snippet: value: int = driver.trigger.iqRecorder.get_offset() \n
		Defines a delay time for triggered measurements. The trigger offset delays the start of the measurement relative to the
		trigger event. \n
			:return: trigger_offset: numeric Trigger offset in samples. Range: 0 to 64E+6
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:IQRecorder:OFFSet?')
		return Conversions.str_to_int(response)

	def set_offset(self, trigger_offset: int) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:OFFSet \n
		Snippet: driver.trigger.iqRecorder.set_offset(trigger_offset = 1) \n
		Defines a delay time for triggered measurements. The trigger offset delays the start of the measurement relative to the
		trigger event. \n
			:param trigger_offset: numeric Trigger offset in samples. Range: 0 to 64E+6
		"""
		param = Conversions.decimal_value_to_str(trigger_offset)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:IQRecorder:OFFSet {param}')

	def get_mgap(self) -> float:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:MGAP \n
		Snippet: value: float = driver.trigger.iqRecorder.get_mgap() \n
		Sets a minimum time during which the IF signal must be below the trigger threshold before the trigger is armed so that an
		IF power trigger event can be generated. The I/Q recorder runs always in single-shot mode. Therefore it is controlled by
		a single trigger event. The minimum trigger gap condition is valid between the start of the measurement and the first
		trigger event. \n
			:return: minimum_gap: numeric Range: 0 s to 0.01 s, Unit: s
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:IQRecorder:MGAP?')
		return Conversions.str_to_float(response)

	def set_mgap(self, minimum_gap: float) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:MGAP \n
		Snippet: driver.trigger.iqRecorder.set_mgap(minimum_gap = 1.0) \n
		Sets a minimum time during which the IF signal must be below the trigger threshold before the trigger is armed so that an
		IF power trigger event can be generated. The I/Q recorder runs always in single-shot mode. Therefore it is controlled by
		a single trigger event. The minimum trigger gap condition is valid between the start of the measurement and the first
		trigger event. \n
			:param minimum_gap: numeric Range: 0 s to 0.01 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(minimum_gap)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:IQRecorder:MGAP {param}')

	def get_timeout(self) -> float or bool:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:TOUT \n
		Snippet: value: float or bool = driver.trigger.iqRecorder.get_timeout() \n
		Selects the maximum time that the measurement waits for a trigger event before it stops in remote control mode or
		indicates a trigger timeout in manual operation mode. This setting has no influence on 'Free Run' measurements. \n
			:return: timeout: (float or boolean) numeric | ON | OFF Range: 0.01 s to 300 s, Unit: s ON | OFF enables or disables the timeout check.
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:IQRecorder:TOUT?')
		return Conversions.str_to_float_or_bool(response)

	def set_timeout(self, timeout: float or bool) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:TOUT \n
		Snippet: driver.trigger.iqRecorder.set_timeout(timeout = 1.0) \n
		Selects the maximum time that the measurement waits for a trigger event before it stops in remote control mode or
		indicates a trigger timeout in manual operation mode. This setting has no influence on 'Free Run' measurements. \n
			:param timeout: (float or boolean) numeric | ON | OFF Range: 0.01 s to 300 s, Unit: s ON | OFF enables or disables the timeout check.
		"""
		param = Conversions.decimal_or_bool_value_to_str(timeout)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:IQRecorder:TOUT {param}')

	def get_threshold(self) -> float:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:THReshold \n
		Snippet: value: float = driver.trigger.iqRecorder.get_threshold() \n
		Defines the trigger threshold for power trigger sources. \n
			:return: threshold: numeric Range: -50 dB to 0 dB, Unit: dB (full scale, i.e. relative to reference level minus external attenuation)
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:IQRecorder:THReshold?')
		return Conversions.str_to_float(response)

	def set_threshold(self, threshold: float) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:THReshold \n
		Snippet: driver.trigger.iqRecorder.set_threshold(threshold = 1.0) \n
		Defines the trigger threshold for power trigger sources. \n
			:param threshold: numeric Range: -50 dB to 0 dB, Unit: dB (full scale, i.e. relative to reference level minus external attenuation)
		"""
		param = Conversions.decimal_value_to_str(threshold)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:IQRecorder:THReshold {param}')

	def get_pc_threshold(self) -> float:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:PCTHreshold \n
		Snippet: value: float = driver.trigger.iqRecorder.get_pc_threshold() \n
		No command help available \n
			:return: phase_chg_thres: No help available
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:IQRecorder:PCTHreshold?')
		return Conversions.str_to_float(response)

	def set_pc_threshold(self, phase_chg_thres: float) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:PCTHreshold \n
		Snippet: driver.trigger.iqRecorder.set_pc_threshold(phase_chg_thres = 1.0) \n
		No command help available \n
			:param phase_chg_thres: No help available
		"""
		param = Conversions.decimal_value_to_str(phase_chg_thres)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:IQRecorder:PCTHreshold {param}')

	def get_pc_time(self) -> float or bool:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:PCTime \n
		Snippet: value: float or bool = driver.trigger.iqRecorder.get_pc_time() \n
		No command help available \n
			:return: phase_chg_time: (float or boolean) No help available
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:IQRecorder:PCTime?')
		return Conversions.str_to_float_or_bool(response)

	def set_pc_time(self, phase_chg_time: float or bool) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:PCTime \n
		Snippet: driver.trigger.iqRecorder.set_pc_time(phase_chg_time = 1.0) \n
		No command help available \n
			:param phase_chg_time: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(phase_chg_time)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:IQRecorder:PCTime {param}')

	# noinspection PyTypeChecker
	def get_slope(self) -> enums.SignalSlopeExt:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:SLOPe \n
		Snippet: value: enums.SignalSlopeExt = driver.trigger.iqRecorder.get_slope() \n
		Qualifies whether the trigger event is generated at the rising or at the falling edge of the trigger pulse (valid for
		external and power trigger sources) . \n
			:return: event: REDGe | FEDGe REDGe: rising edge FEDGe: falling edge
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:IQRecorder:SLOPe?')
		return Conversions.str_to_scalar_enum(response, enums.SignalSlopeExt)

	def set_slope(self, event: enums.SignalSlopeExt) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:SLOPe \n
		Snippet: driver.trigger.iqRecorder.set_slope(event = enums.SignalSlopeExt.FALLing) \n
		Qualifies whether the trigger event is generated at the rising or at the falling edge of the trigger pulse (valid for
		external and power trigger sources) . \n
			:param event: REDGe | FEDGe REDGe: rising edge FEDGe: falling edge
		"""
		param = Conversions.enum_scalar_to_str(event, enums.SignalSlopeExt)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:IQRecorder:SLOPe {param}')

	def clone(self) -> 'IqRecorderCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IqRecorderCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
