from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HesuCls:
	"""Hesu commands group definition. 21 total commands, 21 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hesu", core, parent)

	@property
	def formatPy(self):
		"""formatPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_formatPy'):
			from .FormatPy import FormatPyCls
			self._formatPy = FormatPyCls(self._core, self._cmd_group)
		return self._formatPy

	@property
	def beamChange(self):
		"""beamChange commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_beamChange'):
			from .BeamChange import BeamChangeCls
			self._beamChange = BeamChangeCls(self._core, self._cmd_group)
		return self._beamChange

	@property
	def ulDl(self):
		"""ulDl commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ulDl'):
			from .UlDl import UlDlCls
			self._ulDl = UlDlCls(self._core, self._cmd_group)
		return self._ulDl

	@property
	def mcs(self):
		"""mcs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcs'):
			from .Mcs import McsCls
			self._mcs = McsCls(self._core, self._cmd_group)
		return self._mcs

	@property
	def dcm(self):
		"""dcm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dcm'):
			from .Dcm import DcmCls
			self._dcm = DcmCls(self._core, self._cmd_group)
		return self._dcm

	@property
	def bssColor(self):
		"""bssColor commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bssColor'):
			from .BssColor import BssColorCls
			self._bssColor = BssColorCls(self._core, self._cmd_group)
		return self._bssColor

	@property
	def reserved(self):
		"""reserved commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reserved'):
			from .Reserved import ReservedCls
			self._reserved = ReservedCls(self._core, self._cmd_group)
		return self._reserved

	@property
	def spatialReuse(self):
		"""spatialReuse commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spatialReuse'):
			from .SpatialReuse import SpatialReuseCls
			self._spatialReuse = SpatialReuseCls(self._core, self._cmd_group)
		return self._spatialReuse

	@property
	def bw(self):
		"""bw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bw'):
			from .Bw import BwCls
			self._bw = BwCls(self._core, self._cmd_group)
		return self._bw

	@property
	def giltfSize(self):
		"""giltfSize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_giltfSize'):
			from .GiltfSize import GiltfSizeCls
			self._giltfSize = GiltfSizeCls(self._core, self._cmd_group)
		return self._giltfSize

	@property
	def nsts(self):
		"""nsts commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nsts'):
			from .Nsts import NstsCls
			self._nsts = NstsCls(self._core, self._cmd_group)
		return self._nsts

	@property
	def txOp(self):
		"""txOp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_txOp'):
			from .TxOp import TxOpCls
			self._txOp = TxOpCls(self._core, self._cmd_group)
		return self._txOp

	@property
	def coding(self):
		"""coding commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_coding'):
			from .Coding import CodingCls
			self._coding = CodingCls(self._core, self._cmd_group)
		return self._coding

	@property
	def ldpc(self):
		"""ldpc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ldpc'):
			from .Ldpc import LdpcCls
			self._ldpc = LdpcCls(self._core, self._cmd_group)
		return self._ldpc

	@property
	def stbc(self):
		"""stbc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stbc'):
			from .Stbc import StbcCls
			self._stbc = StbcCls(self._core, self._cmd_group)
		return self._stbc

	@property
	def txBf(self):
		"""txBf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_txBf'):
			from .TxBf import TxBfCls
			self._txBf = TxBfCls(self._core, self._cmd_group)
		return self._txBf

	@property
	def pfecPadding(self):
		"""pfecPadding commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pfecPadding'):
			from .PfecPadding import PfecPaddingCls
			self._pfecPadding = PfecPaddingCls(self._core, self._cmd_group)
		return self._pfecPadding

	@property
	def peDisambiguity(self):
		"""peDisambiguity commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_peDisambiguity'):
			from .PeDisambiguity import PeDisambiguityCls
			self._peDisambiguity = PeDisambiguityCls(self._core, self._cmd_group)
		return self._peDisambiguity

	@property
	def doppler(self):
		"""doppler commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_doppler'):
			from .Doppler import DopplerCls
			self._doppler = DopplerCls(self._core, self._cmd_group)
		return self._doppler

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

	def clone(self) -> 'HesuCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HesuCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
