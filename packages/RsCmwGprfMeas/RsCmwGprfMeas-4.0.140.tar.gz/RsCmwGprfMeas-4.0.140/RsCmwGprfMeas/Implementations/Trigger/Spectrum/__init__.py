from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpectrumCls:
	"""Spectrum commands group definition. 7 total commands, 1 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spectrum", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import CatalogCls
			self._catalog = CatalogCls(self._core, self._cmd_group)
		return self._catalog

	def get_source(self) -> str:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:SPECtrum:SOURce \n
		Snippet: value: str = driver.trigger.spectrum.get_source() \n
		Selects the source of the trigger events. Some values are always available. They are listed below. Depending on the
		installed options, additional values are available. You can query a list of all supported values via TRIGger:...
		:CATalog:SOURce?. \n
			:return: source: string 'Free Run': free run (untriggered) 'Video': power trigger at video band
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:SPECtrum:SOURce?')
		return trim_str_response(response)

	def set_source(self, source: str) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:SPECtrum:SOURce \n
		Snippet: driver.trigger.spectrum.set_source(source = 'abc') \n
		Selects the source of the trigger events. Some values are always available. They are listed below. Depending on the
		installed options, additional values are available. You can query a list of all supported values via TRIGger:...
		:CATalog:SOURce?. \n
			:param source: string 'Free Run': free run (untriggered) 'Video': power trigger at video band
		"""
		param = Conversions.value_to_quoted_str(source)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:SPECtrum:SOURce {param}')

	def get_threshold(self) -> float:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:SPECtrum:THReshold \n
		Snippet: value: float = driver.trigger.spectrum.get_threshold() \n
		Defines the trigger threshold for power trigger sources. \n
			:return: threshold: numeric Range: -50 dB to 0 dB, Unit: dB (full scale, i.e. relative to reference level minus external attenuation)
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:SPECtrum:THReshold?')
		return Conversions.str_to_float(response)

	def set_threshold(self, threshold: float) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:SPECtrum:THReshold \n
		Snippet: driver.trigger.spectrum.set_threshold(threshold = 1.0) \n
		Defines the trigger threshold for power trigger sources. \n
			:param threshold: numeric Range: -50 dB to 0 dB, Unit: dB (full scale, i.e. relative to reference level minus external attenuation)
		"""
		param = Conversions.decimal_value_to_str(threshold)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:SPECtrum:THReshold {param}')

	# noinspection PyTypeChecker
	def get_slope(self) -> enums.SignalSlopeExt:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:SPECtrum:SLOPe \n
		Snippet: value: enums.SignalSlopeExt = driver.trigger.spectrum.get_slope() \n
		Qualifies whether the trigger event is generated at the rising or at the falling edge of the trigger pulse (valid for
		external and power trigger sources) . \n
			:return: slope: REDGe | FEDGe REDGe: rising edge FEDGe: falling edge
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:SPECtrum:SLOPe?')
		return Conversions.str_to_scalar_enum(response, enums.SignalSlopeExt)

	def set_slope(self, slope: enums.SignalSlopeExt) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:SPECtrum:SLOPe \n
		Snippet: driver.trigger.spectrum.set_slope(slope = enums.SignalSlopeExt.FALLing) \n
		Qualifies whether the trigger event is generated at the rising or at the falling edge of the trigger pulse (valid for
		external and power trigger sources) . \n
			:param slope: REDGe | FEDGe REDGe: rising edge FEDGe: falling edge
		"""
		param = Conversions.enum_scalar_to_str(slope, enums.SignalSlopeExt)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:SPECtrum:SLOPe {param}')

	def get_mgap(self) -> float:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:SPECtrum:MGAP \n
		Snippet: value: float = driver.trigger.spectrum.get_mgap() \n
		Sets a minimum time during which the IF signal must be below the trigger threshold before the trigger is armed so that an
		IF power trigger event can be generated. \n
			:return: minimum_gap: numeric Range: 0 s to 0.01 s, Unit: s
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:SPECtrum:MGAP?')
		return Conversions.str_to_float(response)

	def set_mgap(self, minimum_gap: float) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:SPECtrum:MGAP \n
		Snippet: driver.trigger.spectrum.set_mgap(minimum_gap = 1.0) \n
		Sets a minimum time during which the IF signal must be below the trigger threshold before the trigger is armed so that an
		IF power trigger event can be generated. \n
			:param minimum_gap: numeric Range: 0 s to 0.01 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(minimum_gap)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:SPECtrum:MGAP {param}')

	def get_offset(self) -> float:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:SPECtrum:OFFSet \n
		Snippet: value: float = driver.trigger.spectrum.get_offset() \n
		Defines the trigger offset, i.e. the offset of a triggered zero span measurement relative to the corresponding trigger
		event. \n
			:return: trigger_offset: numeric Range: -0.5 s to 0.5 s, Unit: s
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:SPECtrum:OFFSet?')
		return Conversions.str_to_float(response)

	def set_offset(self, trigger_offset: float) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:SPECtrum:OFFSet \n
		Snippet: driver.trigger.spectrum.set_offset(trigger_offset = 1.0) \n
		Defines the trigger offset, i.e. the offset of a triggered zero span measurement relative to the corresponding trigger
		event. \n
			:param trigger_offset: numeric Range: -0.5 s to 0.5 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(trigger_offset)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:SPECtrum:OFFSet {param}')

	def get_timeout(self) -> float or bool:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:SPECtrum:TOUT \n
		Snippet: value: float or bool = driver.trigger.spectrum.get_timeout() \n
		Selects the maximum time that the measurement waits for a trigger event before it stops in remote control mode or
		indicates a trigger timeout in manual operation mode. This setting has no influence on 'Free Run' measurements. \n
			:return: trigger_timeout: (float or boolean) numeric | ON | OFF Range: 0.01 s to 300 s, Unit: s ON | OFF enables or disables the timeout check.
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:SPECtrum:TOUT?')
		return Conversions.str_to_float_or_bool(response)

	def set_timeout(self, trigger_timeout: float or bool) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:SPECtrum:TOUT \n
		Snippet: driver.trigger.spectrum.set_timeout(trigger_timeout = 1.0) \n
		Selects the maximum time that the measurement waits for a trigger event before it stops in remote control mode or
		indicates a trigger timeout in manual operation mode. This setting has no influence on 'Free Run' measurements. \n
			:param trigger_timeout: (float or boolean) numeric | ON | OFF Range: 0.01 s to 300 s, Unit: s ON | OFF enables or disables the timeout check.
		"""
		param = Conversions.decimal_or_bool_value_to_str(trigger_timeout)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:SPECtrum:TOUT {param}')

	def clone(self) -> 'SpectrumCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SpectrumCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
