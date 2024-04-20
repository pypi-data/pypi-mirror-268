from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModulationCls:
	"""Modulation commands group definition. 144 total commands, 14 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	@property
	def cmimo(self):
		"""cmimo commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_cmimo'):
			from .Cmimo import CmimoCls
			self._cmimo = CmimoCls(self._core, self._cmd_group)
		return self._cmimo

	@property
	def evMagnitude(self):
		"""evMagnitude commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_evMagnitude'):
			from .EvMagnitude import EvMagnitudeCls
			self._evMagnitude = EvMagnitudeCls(self._core, self._cmd_group)
		return self._evMagnitude

	@property
	def cfoDistribution(self):
		"""cfoDistribution commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_cfoDistribution'):
			from .CfoDistribution import CfoDistributionCls
			self._cfoDistribution = CfoDistributionCls(self._core, self._cmd_group)
		return self._cfoDistribution

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
	def standardDev(self):
		"""standardDev commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_standardDev'):
			from .StandardDev import StandardDevCls
			self._standardDev = StandardDevCls(self._core, self._cmd_group)
		return self._standardDev

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
	def dsss(self):
		"""dsss commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_dsss'):
			from .Dsss import DsssCls
			self._dsss = DsssCls(self._core, self._cmd_group)
		return self._dsss

	@property
	def mimo(self):
		"""mimo commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_mimo'):
			from .Mimo import MimoCls
			self._mimo = MimoCls(self._core, self._cmd_group)
		return self._mimo

	@property
	def smimo(self):
		"""smimo commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_smimo'):
			from .Smimo import SmimoCls
			self._smimo = SmimoCls(self._core, self._cmd_group)
		return self._smimo

	@property
	def acsiso(self):
		"""acsiso commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_acsiso'):
			from .Acsiso import AcsisoCls
			self._acsiso = AcsisoCls(self._core, self._cmd_group)
		return self._acsiso

	@property
	def ofdm(self):
		"""ofdm commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_ofdm'):
			from .Ofdm import OfdmCls
			self._ofdm = OfdmCls(self._core, self._cmd_group)
		return self._ofdm

	def clone(self) -> 'ModulationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ModulationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
