from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HtsigCls:
	"""Htsig commands group definition. 13 total commands, 13 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("htsig", core, parent)

	@property
	def mcs(self):
		"""mcs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcs'):
			from .Mcs import McsCls
			self._mcs = McsCls(self._core, self._cmd_group)
		return self._mcs

	@property
	def cbw(self):
		"""cbw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbw'):
			from .Cbw import CbwCls
			self._cbw = CbwCls(self._core, self._cmd_group)
		return self._cbw

	@property
	def htLength(self):
		"""htLength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_htLength'):
			from .HtLength import HtLengthCls
			self._htLength = HtLengthCls(self._core, self._cmd_group)
		return self._htLength

	@property
	def smoothing(self):
		"""smoothing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_smoothing'):
			from .Smoothing import SmoothingCls
			self._smoothing = SmoothingCls(self._core, self._cmd_group)
		return self._smoothing

	@property
	def nsounding(self):
		"""nsounding commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nsounding'):
			from .Nsounding import NsoundingCls
			self._nsounding = NsoundingCls(self._core, self._cmd_group)
		return self._nsounding

	@property
	def reserved(self):
		"""reserved commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reserved'):
			from .Reserved import ReservedCls
			self._reserved = ReservedCls(self._core, self._cmd_group)
		return self._reserved

	@property
	def aggregation(self):
		"""aggregation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aggregation'):
			from .Aggregation import AggregationCls
			self._aggregation = AggregationCls(self._core, self._cmd_group)
		return self._aggregation

	@property
	def stbCoding(self):
		"""stbCoding commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stbCoding'):
			from .StbCoding import StbCodingCls
			self._stbCoding = StbCodingCls(self._core, self._cmd_group)
		return self._stbCoding

	@property
	def fecCoding(self):
		"""fecCoding commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fecCoding'):
			from .FecCoding import FecCodingCls
			self._fecCoding = FecCodingCls(self._core, self._cmd_group)
		return self._fecCoding

	@property
	def shortGi(self):
		"""shortGi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_shortGi'):
			from .ShortGi import ShortGiCls
			self._shortGi = ShortGiCls(self._core, self._cmd_group)
		return self._shortGi

	@property
	def ness(self):
		"""ness commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ness'):
			from .Ness import NessCls
			self._ness = NessCls(self._core, self._cmd_group)
		return self._ness

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

	def clone(self) -> 'HtsigCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HtsigCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
