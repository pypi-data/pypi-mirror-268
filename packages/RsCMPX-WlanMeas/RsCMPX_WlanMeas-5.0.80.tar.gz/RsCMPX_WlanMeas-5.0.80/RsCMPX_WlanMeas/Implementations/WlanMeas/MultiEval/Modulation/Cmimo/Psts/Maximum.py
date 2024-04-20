from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:WLAN:MEASurement<instance>:MEValuation:MODulation:CMIMo:PSTS:MAXimum \n
		Snippet: value: List[float] = driver.wlanMeas.multiEval.modulation.cmimo.psts.maximum.read() \n
		Return the single value RMS power results for the individual space-time streams. The current, average, minimum, maximum,
		and standard deviation results can be retrieved. For a meaningful result, set the spatial mapping matrix in the DUT to
		direct mapping. It causes a one-to-one mapping of space time streams to TX antennas. Thus a broken TX chain (no power) is
		detected and a damaged chain is identified by its bad EVM. \n
		Suppressed linked return values: reliability \n
			:return: power_sts_tx: Four values, one value per space-time stream"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WLAN:MEASurement<Instance>:MEValuation:MODulation:CMIMo:PSTS:MAXimum?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:WLAN:MEASurement<instance>:MEValuation:MODulation:CMIMo:PSTS:MAXimum \n
		Snippet: value: List[float] = driver.wlanMeas.multiEval.modulation.cmimo.psts.maximum.fetch() \n
		Return the single value RMS power results for the individual space-time streams. The current, average, minimum, maximum,
		and standard deviation results can be retrieved. For a meaningful result, set the spatial mapping matrix in the DUT to
		direct mapping. It causes a one-to-one mapping of space time streams to TX antennas. Thus a broken TX chain (no power) is
		detected and a damaged chain is identified by its bad EVM. \n
		Suppressed linked return values: reliability \n
			:return: power_sts_tx: Four values, one value per space-time stream"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:MODulation:CMIMo:PSTS:MAXimum?', suppressed)
		return response
