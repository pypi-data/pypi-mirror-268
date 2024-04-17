from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PlossCls:
	"""Ploss commands group definition. 4 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ploss", core, parent)

	@property
	def view(self):
		"""view commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_view'):
			from .View import ViewCls
			self._view = ViewCls(self._core, self._cmd_group)
		return self._view

	@property
	def listPy(self):
		"""listPy commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPyCls
			self._listPy = ListPyCls(self._core, self._cmd_group)
		return self._listPy

	@property
	def mpath(self):
		"""mpath commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mpath'):
			from .Mpath import MpathCls
			self._mpath = MpathCls(self._core, self._cmd_group)
		return self._mpath

	def get_trace(self) -> bool:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:PLOSs:TRACe \n
		Snippet: value: bool = driver.configure.ploss.get_trace() \n
		No command help available \n
			:return: trace_mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:PLOSs:TRACe?')
		return Conversions.str_to_bool(response)

	def set_trace(self, trace_mode: bool) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:PLOSs:TRACe \n
		Snippet: driver.configure.ploss.set_trace(trace_mode = False) \n
		No command help available \n
			:param trace_mode: No help available
		"""
		param = Conversions.bool_to_str(trace_mode)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:PLOSs:TRACe {param}')

	def clone(self) -> 'PlossCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PlossCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
