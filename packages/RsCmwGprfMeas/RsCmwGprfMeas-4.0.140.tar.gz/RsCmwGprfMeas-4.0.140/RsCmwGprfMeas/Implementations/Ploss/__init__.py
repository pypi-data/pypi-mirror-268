from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PlossCls:
	"""Ploss commands group definition. 12 total commands, 5 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ploss", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def clear(self):
		"""clear commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_clear'):
			from .Clear import ClearCls
			self._clear = ClearCls(self._core, self._cmd_group)
		return self._clear

	@property
	def open(self):
		"""open commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_open'):
			from .Open import OpenCls
			self._open = OpenCls(self._core, self._cmd_group)
		return self._open

	@property
	def short(self):
		"""short commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_short'):
			from .Short import ShortCls
			self._short = ShortCls(self._core, self._cmd_group)
		return self._short

	@property
	def eval(self):
		"""eval commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_eval'):
			from .Eval import EvalCls
			self._eval = EvalCls(self._core, self._cmd_group)
		return self._eval

	def stop(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: STOP:GPRF:MEASurement<Instance>:PLOSs \n
		Snippet: driver.ploss.stop() \n
		No command help available \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'STOP:GPRF:MEASurement<Instance>:PLOSs', opc_timeout_ms)

	def abort(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: ABORt:GPRF:MEASurement<Instance>:PLOSs \n
		Snippet: driver.ploss.abort() \n
		No command help available \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt:GPRF:MEASurement<Instance>:PLOSs', opc_timeout_ms)

	def clone(self) -> 'PlossCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PlossCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
