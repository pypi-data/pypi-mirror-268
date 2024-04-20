from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SreliabilityCls:
	"""Sreliability commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sreliability", core, parent)

	def fetch(self) -> List[int]:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:LIST:SRELiability \n
		Snippet: value: List[int] = driver.wlanMeas.multiEval.listPy.sreliability.fetch() \n
		Returns the segment reliability for all measured list mode segments. The number of active segments n is determined by
		method RsCMPX_WlanMeas.Configure.WlanMeas.MultiEval.ListPy.count. \n
		Suppressed linked return values: reliability \n
			:return: seg_reliabilities: Comma-separated list of n values, one per measured segment The meaning of the returned values is the same as for the common reliability indicator, see previous parameter."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:LIST:SRELiability?', suppressed)
		return response
