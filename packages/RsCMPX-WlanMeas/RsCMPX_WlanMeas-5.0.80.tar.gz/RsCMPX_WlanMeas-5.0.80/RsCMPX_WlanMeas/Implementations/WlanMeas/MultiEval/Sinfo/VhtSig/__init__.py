from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class VhtSigCls:
	"""VhtSig commands group definition. 15 total commands, 15 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vhtSig", core, parent)

	@property
	def bw(self):
		"""bw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bw'):
			from .Bw import BwCls
			self._bw = BwCls(self._core, self._cmd_group)
		return self._bw

	@property
	def reserved(self):
		"""reserved commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reserved'):
			from .Reserved import ReservedCls
			self._reserved = ReservedCls(self._core, self._cmd_group)
		return self._reserved

	@property
	def stbc(self):
		"""stbc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stbc'):
			from .Stbc import StbcCls
			self._stbc = StbcCls(self._core, self._cmd_group)
		return self._stbc

	@property
	def gid(self):
		"""gid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gid'):
			from .Gid import GidCls
			self._gid = GidCls(self._core, self._cmd_group)
		return self._gid

	@property
	def sunsts(self):
		"""sunsts commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sunsts'):
			from .Sunsts import SunstsCls
			self._sunsts = SunstsCls(self._core, self._cmd_group)
		return self._sunsts

	@property
	def paid(self):
		"""paid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_paid'):
			from .Paid import PaidCls
			self._paid = PaidCls(self._core, self._cmd_group)
		return self._paid

	@property
	def txOp(self):
		"""txOp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_txOp'):
			from .TxOp import TxOpCls
			self._txOp = TxOpCls(self._core, self._cmd_group)
		return self._txOp

	@property
	def sgi(self):
		"""sgi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sgi'):
			from .Sgi import SgiCls
			self._sgi = SgiCls(self._core, self._cmd_group)
		return self._sgi

	@property
	def sdisambiguity(self):
		"""sdisambiguity commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sdisambiguity'):
			from .Sdisambiguity import SdisambiguityCls
			self._sdisambiguity = SdisambiguityCls(self._core, self._cmd_group)
		return self._sdisambiguity

	@property
	def fecCoding(self):
		"""fecCoding commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fecCoding'):
			from .FecCoding import FecCodingCls
			self._fecCoding = FecCodingCls(self._core, self._cmd_group)
		return self._fecCoding

	@property
	def ldpc(self):
		"""ldpc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ldpc'):
			from .Ldpc import LdpcCls
			self._ldpc = LdpcCls(self._core, self._cmd_group)
		return self._ldpc

	@property
	def smcs(self):
		"""smcs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_smcs'):
			from .Smcs import SmcsCls
			self._smcs = SmcsCls(self._core, self._cmd_group)
		return self._smcs

	@property
	def beamformed(self):
		"""beamformed commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_beamformed'):
			from .Beamformed import BeamformedCls
			self._beamformed = BeamformedCls(self._core, self._cmd_group)
		return self._beamformed

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

	def clone(self) -> 'VhtSigCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = VhtSigCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
