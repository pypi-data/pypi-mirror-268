from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SinfoCls:
	"""Sinfo commands group definition. 95 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sinfo", core, parent)

	@property
	def lsig(self):
		"""lsig commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_lsig'):
			from .Lsig import LsigCls
			self._lsig = LsigCls(self._core, self._cmd_group)
		return self._lsig

	@property
	def htsig(self):
		"""htsig commands group. 13 Sub-classes, 0 commands."""
		if not hasattr(self, '_htsig'):
			from .Htsig import HtsigCls
			self._htsig = HtsigCls(self._core, self._cmd_group)
		return self._htsig

	@property
	def vhtSig(self):
		"""vhtSig commands group. 15 Sub-classes, 0 commands."""
		if not hasattr(self, '_vhtSig'):
			from .VhtSig import VhtSigCls
			self._vhtSig = VhtSigCls(self._core, self._cmd_group)
		return self._vhtSig

	@property
	def hesu(self):
		"""hesu commands group. 21 Sub-classes, 0 commands."""
		if not hasattr(self, '_hesu'):
			from .Hesu import HesuCls
			self._hesu = HesuCls(self._core, self._cmd_group)
		return self._hesu

	@property
	def hemu(self):
		"""hemu commands group. 19 Sub-classes, 0 commands."""
		if not hasattr(self, '_hemu'):
			from .Hemu import HemuCls
			self._hemu = HemuCls(self._core, self._cmd_group)
		return self._hemu

	@property
	def hetb(self):
		"""hetb commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_hetb'):
			from .Hetb import HetbCls
			self._hetb = HetbCls(self._core, self._cmd_group)
		return self._hetb

	@property
	def heb(self):
		"""heb commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_heb'):
			from .Heb import HebCls
			self._heb = HebCls(self._core, self._cmd_group)
		return self._heb

	def clone(self) -> 'SinfoCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SinfoCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
