from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScountCls:
	"""Scount commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scount", core, parent)

	def fetch(self) -> List[int]:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:LIST:TSMask:SCOunt \n
		Snippet: value: List[int] = driver.wlanMeas.multiEval.listPy.tsMask.scount.fetch() \n
		Returns the expired statistic counts for transmit spectrum mask results over all segments in list mode. The values in
		curly brackets {} are specified for each active segment: {...}seg 1, {...}seg 2, ..., {...}seg n. The number of active
		segments n is determined by method RsCMPX_WlanMeas.Configure.WlanMeas.MultiEval.ListPy.count. \n
		Suppressed linked return values: reliability \n
			:return: exp_stat_counts_tsm: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:LIST:TSMask:SCOunt?', suppressed)
		return response
