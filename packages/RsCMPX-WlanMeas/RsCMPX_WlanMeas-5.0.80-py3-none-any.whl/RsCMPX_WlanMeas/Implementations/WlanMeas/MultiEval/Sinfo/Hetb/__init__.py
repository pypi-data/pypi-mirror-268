from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HetbCls:
	"""Hetb commands group definition. 8 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hetb", core, parent)

	@property
	def formatPy(self):
		"""formatPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_formatPy'):
			from .FormatPy import FormatPyCls
			self._formatPy = FormatPyCls(self._core, self._cmd_group)
		return self._formatPy

	@property
	def bssColor(self):
		"""bssColor commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bssColor'):
			from .BssColor import BssColorCls
			self._bssColor = BssColorCls(self._core, self._cmd_group)
		return self._bssColor

	@property
	def spatialReuse(self):
		"""spatialReuse commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spatialReuse'):
			from .SpatialReuse import SpatialReuseCls
			self._spatialReuse = SpatialReuseCls(self._core, self._cmd_group)
		return self._spatialReuse

	@property
	def reserved(self):
		"""reserved commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reserved'):
			from .Reserved import ReservedCls
			self._reserved = ReservedCls(self._core, self._cmd_group)
		return self._reserved

	@property
	def bw(self):
		"""bw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bw'):
			from .Bw import BwCls
			self._bw = BwCls(self._core, self._cmd_group)
		return self._bw

	@property
	def txOp(self):
		"""txOp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_txOp'):
			from .TxOp import TxOpCls
			self._txOp = TxOpCls(self._core, self._cmd_group)
		return self._txOp

	@property
	def crc(self):
		"""crc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crc'):
			from .Crc import CrcCls
			self._crc = CrcCls(self._core, self._cmd_group)
		return self._crc

	@property
	def tail(self):
		"""tail commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tail'):
			from .Tail import TailCls
			self._tail = TailCls(self._core, self._cmd_group)
		return self._tail

	def clone(self) -> 'HetbCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HetbCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
