from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FftSpecAnCls:
	"""FftSpecAn commands group definition. 9 total commands, 2 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fftSpecAn", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import CatalogCls
			self._catalog = CatalogCls(self._core, self._cmd_group)
		return self._catalog

	@property
	def osStop(self):
		"""osStop commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_osStop'):
			from .OsStop import OsStopCls
			self._osStop = OsStopCls(self._core, self._cmd_group)
		return self._osStop

	def get_source(self) -> str:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:SOURce \n
		Snippet: value: str = driver.trigger.fftSpecAn.get_source() \n
		Selects the source of the trigger events. Some values are always available. They are listed below. Depending on the
		installed options, additional values are available. You can query a list of all supported values via TRIGger:...
		:CATalog:SOURce?. \n
			:return: source: string 'IF Power': IF power trigger 'Free Run': free run (untriggered)
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:SOURce?')
		return trim_str_response(response)

	def set_source(self, source: str) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:SOURce \n
		Snippet: driver.trigger.fftSpecAn.set_source(source = 'abc') \n
		Selects the source of the trigger events. Some values are always available. They are listed below. Depending on the
		installed options, additional values are available. You can query a list of all supported values via TRIGger:...
		:CATalog:SOURce?. \n
			:param source: string 'IF Power': IF power trigger 'Free Run': free run (untriggered)
		"""
		param = Conversions.value_to_quoted_str(source)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:SOURce {param}')

	# noinspection PyTypeChecker
	def get_omode(self) -> enums.OffsetMode:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:OMODe \n
		Snippet: value: enums.OffsetMode = driver.trigger.fftSpecAn.get_omode() \n
		Selects the trigger offset mode. \n
			:return: offset_mode: VARiable | FIXed
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:OMODe?')
		return Conversions.str_to_scalar_enum(response, enums.OffsetMode)

	def set_omode(self, offset_mode: enums.OffsetMode) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:OMODe \n
		Snippet: driver.trigger.fftSpecAn.set_omode(offset_mode = enums.OffsetMode.FIXed) \n
		Selects the trigger offset mode. \n
			:param offset_mode: VARiable | FIXed
		"""
		param = Conversions.enum_scalar_to_str(offset_mode, enums.OffsetMode)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:OMODe {param}')

	def get_mgap(self) -> float:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:MGAP \n
		Snippet: value: float = driver.trigger.fftSpecAn.get_mgap() \n
		Sets a minimum time during which the IF signal must be below the trigger threshold before the trigger is armed so that an
		IF power trigger event can be generated. \n
			:return: minimum_gap: numeric Range: 0 s to 0.01 s, Unit: s
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:MGAP?')
		return Conversions.str_to_float(response)

	def set_mgap(self, minimum_gap: float) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:MGAP \n
		Snippet: driver.trigger.fftSpecAn.set_mgap(minimum_gap = 1.0) \n
		Sets a minimum time during which the IF signal must be below the trigger threshold before the trigger is armed so that an
		IF power trigger event can be generated. \n
			:param minimum_gap: numeric Range: 0 s to 0.01 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(minimum_gap)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:MGAP {param}')

	def get_timeout(self) -> float or bool:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:TOUT \n
		Snippet: value: float or bool = driver.trigger.fftSpecAn.get_timeout() \n
		Selects the maximum time that the measurement waits for a trigger event before it stops in remote control mode or
		indicates a trigger timeout in manual operation mode. This setting has no influence on 'Free Run' measurements. \n
			:return: timeout: (float or boolean) numeric | ON | OFF Range: 0.01 s to 300 s, Unit: s ON | OFF enables or disables the timeout check.
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:TOUT?')
		return Conversions.str_to_float_or_bool(response)

	def set_timeout(self, timeout: float or bool) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:TOUT \n
		Snippet: driver.trigger.fftSpecAn.set_timeout(timeout = 1.0) \n
		Selects the maximum time that the measurement waits for a trigger event before it stops in remote control mode or
		indicates a trigger timeout in manual operation mode. This setting has no influence on 'Free Run' measurements. \n
			:param timeout: (float or boolean) numeric | ON | OFF Range: 0.01 s to 300 s, Unit: s ON | OFF enables or disables the timeout check.
		"""
		param = Conversions.decimal_or_bool_value_to_str(timeout)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:TOUT {param}')

	def get_offset(self) -> float:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:OFFSet \n
		Snippet: value: float = driver.trigger.fftSpecAn.get_offset() \n
		Defines the trigger offset for the trigger offset mode FIXed. The trigger offset defines the center of the measurement
		interval relative to the trigger event. \n
			:return: offset: numeric Range: -0.15 s to 0.15 s, Unit: s
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:OFFSet?')
		return Conversions.str_to_float(response)

	def set_offset(self, offset: float) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:OFFSet \n
		Snippet: driver.trigger.fftSpecAn.set_offset(offset = 1.0) \n
		Defines the trigger offset for the trigger offset mode FIXed. The trigger offset defines the center of the measurement
		interval relative to the trigger event. \n
			:param offset: numeric Range: -0.15 s to 0.15 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:OFFSet {param}')

	def get_threshold(self) -> float:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:THReshold \n
		Snippet: value: float = driver.trigger.fftSpecAn.get_threshold() \n
		Defines the trigger threshold for power trigger sources. \n
			:return: threshold: numeric Range: -50 dB to 0 dB, Unit: dB (full scale, i.e. relative to reference level minus external attenuation)
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:THReshold?')
		return Conversions.str_to_float(response)

	def set_threshold(self, threshold: float) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:THReshold \n
		Snippet: driver.trigger.fftSpecAn.set_threshold(threshold = 1.0) \n
		Defines the trigger threshold for power trigger sources. \n
			:param threshold: numeric Range: -50 dB to 0 dB, Unit: dB (full scale, i.e. relative to reference level minus external attenuation)
		"""
		param = Conversions.decimal_value_to_str(threshold)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:THReshold {param}')

	# noinspection PyTypeChecker
	def get_slope(self) -> enums.SignalSlopeExt:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:SLOPe \n
		Snippet: value: enums.SignalSlopeExt = driver.trigger.fftSpecAn.get_slope() \n
		Qualifies whether the trigger event is generated at the rising or at the falling edge of the trigger pulse (valid for
		external and power trigger sources) . \n
			:return: event: REDGe | FEDGe REDGe: rising edge FEDGe: falling edge
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:SLOPe?')
		return Conversions.str_to_scalar_enum(response, enums.SignalSlopeExt)

	def set_slope(self, event: enums.SignalSlopeExt) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:SLOPe \n
		Snippet: driver.trigger.fftSpecAn.set_slope(event = enums.SignalSlopeExt.FALLing) \n
		Qualifies whether the trigger event is generated at the rising or at the falling edge of the trigger pulse (valid for
		external and power trigger sources) . \n
			:param event: REDGe | FEDGe REDGe: rising edge FEDGe: falling edge
		"""
		param = Conversions.enum_scalar_to_str(event, enums.SignalSlopeExt)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:SLOPe {param}')

	def clone(self) -> 'FftSpecAnCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FftSpecAnCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
