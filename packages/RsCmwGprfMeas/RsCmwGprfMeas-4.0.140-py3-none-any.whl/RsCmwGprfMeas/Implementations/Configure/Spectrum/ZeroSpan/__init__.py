from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ZeroSpanCls:
	"""ZeroSpan commands group definition. 6 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("zeroSpan", core, parent)

	@property
	def rbw(self):
		"""rbw commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_rbw'):
			from .Rbw import RbwCls
			self._rbw = RbwCls(self._core, self._cmd_group)
		return self._rbw

	@property
	def vbw(self):
		"""vbw commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_vbw'):
			from .Vbw import VbwCls
			self._vbw = VbwCls(self._core, self._cmd_group)
		return self._vbw

	def get_swt(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:ZSPan:SWT \n
		Snippet: value: float = driver.configure.spectrum.zeroSpan.get_swt() \n
		Configures the duration of one measurement interval for the zero span mode. \n
			:return: sweep_time: numeric Range: 0 s to 2000 s, Unit: s
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:ZSPan:SWT?')
		return Conversions.str_to_float(response)

	def set_swt(self, sweep_time: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:ZSPan:SWT \n
		Snippet: driver.configure.spectrum.zeroSpan.set_swt(sweep_time = 1.0) \n
		Configures the duration of one measurement interval for the zero span mode. \n
			:param sweep_time: numeric Range: 0 s to 2000 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(sweep_time)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:ZSPan:SWT {param}')

	def clone(self) -> 'ZeroSpanCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ZeroSpanCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
