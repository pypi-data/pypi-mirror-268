from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DsssCls:
	"""Dsss commands group definition. 40 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dsss", core, parent)

	@property
	def bpower(self):
		"""bpower commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_bpower'):
			from .Bpower import BpowerCls
			self._bpower = BpowerCls(self._core, self._cmd_group)
		return self._bpower

	@property
	def evmPeak(self):
		"""evmPeak commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_evmPeak'):
			from .EvmPeak import EvmPeakCls
			self._evmPeak = EvmPeakCls(self._core, self._cmd_group)
		return self._evmPeak

	@property
	def evmEms(self):
		"""evmEms commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_evmEms'):
			from .EvmEms import EvmEmsCls
			self._evmEms = EvmEmsCls(self._core, self._cmd_group)
		return self._evmEms

	@property
	def cfError(self):
		"""cfError commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_cfError'):
			from .CfError import CfErrorCls
			self._cfError = CfErrorCls(self._core, self._cmd_group)
		return self._cfError

	@property
	def ccError(self):
		"""ccError commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_ccError'):
			from .CcError import CcErrorCls
			self._ccError = CcErrorCls(self._core, self._cmd_group)
		return self._ccError

	@property
	def iqOffset(self):
		"""iqOffset commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqOffset'):
			from .IqOffset import IqOffsetCls
			self._iqOffset = IqOffsetCls(self._core, self._cmd_group)
		return self._iqOffset

	@property
	def gimbalance(self):
		"""gimbalance commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_gimbalance'):
			from .Gimbalance import GimbalanceCls
			self._gimbalance = GimbalanceCls(self._core, self._cmd_group)
		return self._gimbalance

	@property
	def qerror(self):
		"""qerror commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_qerror'):
			from .Qerror import QerrorCls
			self._qerror = QerrorCls(self._core, self._cmd_group)
		return self._qerror

	def clone(self) -> 'DsssCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DsssCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
