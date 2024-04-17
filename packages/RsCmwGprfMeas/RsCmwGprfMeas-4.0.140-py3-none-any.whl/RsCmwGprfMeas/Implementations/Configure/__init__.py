from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConfigureCls:
	"""Configure commands group definition. 152 total commands, 10 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("configure", core, parent)

	@property
	def rfSettings(self):
		"""rfSettings commands group. 1 Sub-classes, 7 commands."""
		if not hasattr(self, '_rfSettings'):
			from .RfSettings import RfSettingsCls
			self._rfSettings = RfSettingsCls(self._core, self._cmd_group)
		return self._rfSettings

	@property
	def power(self):
		"""power commands group. 5 Sub-classes, 7 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def iqVsSlot(self):
		"""iqVsSlot commands group. 2 Sub-classes, 7 commands."""
		if not hasattr(self, '_iqVsSlot'):
			from .IqVsSlot import IqVsSlotCls
			self._iqVsSlot = IqVsSlotCls(self._core, self._cmd_group)
		return self._iqVsSlot

	@property
	def extPwrSensor(self):
		"""extPwrSensor commands group. 1 Sub-classes, 5 commands."""
		if not hasattr(self, '_extPwrSensor'):
			from .ExtPwrSensor import ExtPwrSensorCls
			self._extPwrSensor = ExtPwrSensorCls(self._core, self._cmd_group)
		return self._extPwrSensor

	@property
	def nrpm(self):
		"""nrpm commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_nrpm'):
			from .Nrpm import NrpmCls
			self._nrpm = NrpmCls(self._core, self._cmd_group)
		return self._nrpm

	@property
	def iqRecorder(self):
		"""iqRecorder commands group. 4 Sub-classes, 8 commands."""
		if not hasattr(self, '_iqRecorder'):
			from .IqRecorder import IqRecorderCls
			self._iqRecorder = IqRecorderCls(self._core, self._cmd_group)
		return self._iqRecorder

	@property
	def spectrum(self):
		"""spectrum commands group. 3 Sub-classes, 4 commands."""
		if not hasattr(self, '_spectrum'):
			from .Spectrum import SpectrumCls
			self._spectrum = SpectrumCls(self._core, self._cmd_group)
		return self._spectrum

	@property
	def fftSpecAn(self):
		"""fftSpecAn commands group. 1 Sub-classes, 8 commands."""
		if not hasattr(self, '_fftSpecAn'):
			from .FftSpecAn import FftSpecAnCls
			self._fftSpecAn = FftSpecAnCls(self._core, self._cmd_group)
		return self._fftSpecAn

	@property
	def ploss(self):
		"""ploss commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_ploss'):
			from .Ploss import PlossCls
			self._ploss = PlossCls(self._core, self._cmd_group)
		return self._ploss

	@property
	def canalyzer(self):
		"""canalyzer commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_canalyzer'):
			from .Canalyzer import CanalyzerCls
			self._canalyzer = CanalyzerCls(self._core, self._cmd_group)
		return self._canalyzer

	# noinspection PyTypeChecker
	def get_display(self) -> enums.MeasTab:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:DISPlay \n
		Snippet: value: enums.MeasTab = driver.configure.get_display() \n
		Selects the displayed measurement tab. This command is useful, if you want to observe the GUI during remote control. The
		GUI controls are disabled in that case, so that you cannot select a tab via the GUI. To display the GUI,
		use SYSTem:DISPlay:UPDate ON. \n
			:return: meas_tab: POWer | SPECtrum | FFTSanalyzer | IQRecorder | IQVSlot | EPSensor
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:DISPlay?')
		return Conversions.str_to_scalar_enum(response, enums.MeasTab)

	def set_display(self, meas_tab: enums.MeasTab) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:DISPlay \n
		Snippet: driver.configure.set_display(meas_tab = enums.MeasTab.EPSensor) \n
		Selects the displayed measurement tab. This command is useful, if you want to observe the GUI during remote control. The
		GUI controls are disabled in that case, so that you cannot select a tab via the GUI. To display the GUI,
		use SYSTem:DISPlay:UPDate ON. \n
			:param meas_tab: POWer | SPECtrum | FFTSanalyzer | IQRecorder | IQVSlot | EPSensor
		"""
		param = Conversions.enum_scalar_to_str(meas_tab, enums.MeasTab)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:DISPlay {param}')

	def clone(self) -> 'ConfigureCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ConfigureCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
