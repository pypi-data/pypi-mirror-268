from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TsMaskCls:
	"""TsMask commands group definition. 140 total commands, 12 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tsMask", core, parent)

	@property
	def obw(self):
		"""obw commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_obw'):
			from .Obw import ObwCls
			self._obw = ObwCls(self._core, self._cmd_group)
		return self._obw

	@property
	def ofdm(self):
		"""ofdm commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ofdm'):
			from .Ofdm import OfdmCls
			self._ofdm = OfdmCls(self._core, self._cmd_group)
		return self._ofdm

	@property
	def dsss(self):
		"""dsss commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_dsss'):
			from .Dsss import DsssCls
			self._dsss = DsssCls(self._core, self._cmd_group)
		return self._dsss

	@property
	def nsiso(self):
		"""nsiso commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_nsiso'):
			from .Nsiso import NsisoCls
			self._nsiso = NsisoCls(self._core, self._cmd_group)
		return self._nsiso

	@property
	def acsiso(self):
		"""acsiso commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_acsiso'):
			from .Acsiso import AcsisoCls
			self._acsiso = AcsisoCls(self._core, self._cmd_group)
		return self._acsiso

	@property
	def mimo(self):
		"""mimo commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_mimo'):
			from .Mimo import MimoCls
			self._mimo = MimoCls(self._core, self._cmd_group)
		return self._mimo

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_current'):
			from .Current import CurrentCls
			self._current = CurrentCls(self._core, self._cmd_group)
		return self._current

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_average'):
			from .Average import AverageCls
			self._average = AverageCls(self._core, self._cmd_group)
		return self._average

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_maximum'):
			from .Maximum import MaximumCls
			self._maximum = MaximumCls(self._core, self._cmd_group)
		return self._maximum

	@property
	def minimum(self):
		"""minimum commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_minimum'):
			from .Minimum import MinimumCls
			self._minimum = MinimumCls(self._core, self._cmd_group)
		return self._minimum

	@property
	def segments(self):
		"""segments commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_segments'):
			from .Segments import SegmentsCls
			self._segments = SegmentsCls(self._core, self._cmd_group)
		return self._segments

	@property
	def frequency(self):
		"""frequency commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	def clone(self) -> 'TsMaskCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TsMaskCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
