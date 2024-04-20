from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HemuCls:
	"""Hemu commands group definition. 19 total commands, 19 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hemu", core, parent)

	@property
	def ulDl(self):
		"""ulDl commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ulDl'):
			from .UlDl import UlDlCls
			self._ulDl = UlDlCls(self._core, self._cmd_group)
		return self._ulDl

	@property
	def bmcs(self):
		"""bmcs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bmcs'):
			from .Bmcs import BmcsCls
			self._bmcs = BmcsCls(self._core, self._cmd_group)
		return self._bmcs

	@property
	def bdcm(self):
		"""bdcm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bdcm'):
			from .Bdcm import BdcmCls
			self._bdcm = BdcmCls(self._core, self._cmd_group)
		return self._bdcm

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
	def bw(self):
		"""bw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bw'):
			from .Bw import BwCls
			self._bw = BwCls(self._core, self._cmd_group)
		return self._bw

	@property
	def nsbSymbols(self):
		"""nsbSymbols commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nsbSymbols'):
			from .NsbSymbols import NsbSymbolsCls
			self._nsbSymbols = NsbSymbolsCls(self._core, self._cmd_group)
		return self._nsbSymbols

	@property
	def sbCompress(self):
		"""sbCompress commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sbCompress'):
			from .SbCompress import SbCompressCls
			self._sbCompress = SbCompressCls(self._core, self._cmd_group)
		return self._sbCompress

	@property
	def giltfSize(self):
		"""giltfSize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_giltfSize'):
			from .GiltfSize import GiltfSizeCls
			self._giltfSize = GiltfSizeCls(self._core, self._cmd_group)
		return self._giltfSize

	@property
	def doppler(self):
		"""doppler commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_doppler'):
			from .Doppler import DopplerCls
			self._doppler = DopplerCls(self._core, self._cmd_group)
		return self._doppler

	@property
	def txOp(self):
		"""txOp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_txOp'):
			from .TxOp import TxOpCls
			self._txOp = TxOpCls(self._core, self._cmd_group)
		return self._txOp

	@property
	def reserved(self):
		"""reserved commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reserved'):
			from .Reserved import ReservedCls
			self._reserved = ReservedCls(self._core, self._cmd_group)
		return self._reserved

	@property
	def nltfSymbols(self):
		"""nltfSymbols commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nltfSymbols'):
			from .NltfSymbols import NltfSymbolsCls
			self._nltfSymbols = NltfSymbolsCls(self._core, self._cmd_group)
		return self._nltfSymbols

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

	def clone(self) -> 'HemuCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HemuCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
