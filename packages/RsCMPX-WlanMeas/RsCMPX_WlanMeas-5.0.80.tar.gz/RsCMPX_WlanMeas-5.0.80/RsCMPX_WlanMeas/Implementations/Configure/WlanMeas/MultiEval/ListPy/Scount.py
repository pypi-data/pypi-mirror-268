from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScountCls:
	"""Scount commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scount", core, parent)

	def get_modulation(self) -> List[int]:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SCOunt:MODulation \n
		Snippet: value: List[int] = driver.configure.wlanMeas.multiEval.listPy.scount.get_modulation() \n
		Specifies the statistical length for modulation measurements for all segments in list mode. The values in curly brackets
		{} are specified for each active segment: {...}seg 1, {...}seg 2, ..., {...}seg n. The number of active segments n is
		determined by method RsCMPX_WlanMeas.Configure.WlanMeas.MultiEval.ListPy.count. \n
			:return: stat_counts_mod: No help available
		"""
		response = self._core.io.query_bin_or_ascii_int_list('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SCOunt:MODulation?')
		return response

	def set_modulation(self, stat_counts_mod: List[int]) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SCOunt:MODulation \n
		Snippet: driver.configure.wlanMeas.multiEval.listPy.scount.set_modulation(stat_counts_mod = [1, 2, 3]) \n
		Specifies the statistical length for modulation measurements for all segments in list mode. The values in curly brackets
		{} are specified for each active segment: {...}seg 1, {...}seg 2, ..., {...}seg n. The number of active segments n is
		determined by method RsCMPX_WlanMeas.Configure.WlanMeas.MultiEval.ListPy.count. \n
			:param stat_counts_mod: No help available
		"""
		param = Conversions.list_to_csv_str(stat_counts_mod)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SCOunt:MODulation {param}')

	def get_ts_mask(self) -> List[int]:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SCOunt:TSMask \n
		Snippet: value: List[int] = driver.configure.wlanMeas.multiEval.listPy.scount.get_ts_mask() \n
		Specifies the spectrum statistical length for transmit spectrum mask measurements for all segments in list mode.
		The values in curly brackets {} are specified for each active segment: {...}seg 1, {...}seg 2, ..., {...}seg n.
		The number of active segments n is determined by method RsCMPX_WlanMeas.Configure.WlanMeas.MultiEval.ListPy.count. \n
			:return: stat_counts_sem: No help available
		"""
		response = self._core.io.query_bin_or_ascii_int_list('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SCOunt:TSMask?')
		return response

	def set_ts_mask(self, stat_counts_sem: List[int]) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SCOunt:TSMask \n
		Snippet: driver.configure.wlanMeas.multiEval.listPy.scount.set_ts_mask(stat_counts_sem = [1, 2, 3]) \n
		Specifies the spectrum statistical length for transmit spectrum mask measurements for all segments in list mode.
		The values in curly brackets {} are specified for each active segment: {...}seg 1, {...}seg 2, ..., {...}seg n.
		The number of active segments n is determined by method RsCMPX_WlanMeas.Configure.WlanMeas.MultiEval.ListPy.count. \n
			:param stat_counts_sem: No help available
		"""
		param = Conversions.list_to_csv_str(stat_counts_sem)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SCOunt:TSMask {param}')
