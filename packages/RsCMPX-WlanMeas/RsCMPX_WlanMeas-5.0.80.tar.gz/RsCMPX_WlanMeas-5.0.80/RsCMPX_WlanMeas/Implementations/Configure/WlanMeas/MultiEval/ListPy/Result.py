from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResultCls:
	"""Result commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def get_modulation(self) -> List[bool]:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:RESult:MODulation \n
		Snippet: value: List[bool] = driver.configure.wlanMeas.multiEval.listPy.result.get_modulation() \n
		Enables or disables the evaluation of results for modulation (..:MODulation) and transmit spectrum mask (..
		:TSMask) measurements in list mode. The values in curly brackets {} are specified for each active segment: {...}seg 1, {..
		.}seg 2, ..., {...}seg n. The number of active segments n is determined by method RsCMPX_WlanMeas.Configure.WlanMeas.
		MultiEval.ListPy.count. \n
			:return: enable_mod: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:RESult:MODulation?')
		return Conversions.str_to_bool_list(response)

	def set_modulation(self, enable_mod: List[bool]) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:RESult:MODulation \n
		Snippet: driver.configure.wlanMeas.multiEval.listPy.result.set_modulation(enable_mod = [True, False, True]) \n
		Enables or disables the evaluation of results for modulation (..:MODulation) and transmit spectrum mask (..
		:TSMask) measurements in list mode. The values in curly brackets {} are specified for each active segment: {...}seg 1, {..
		.}seg 2, ..., {...}seg n. The number of active segments n is determined by method RsCMPX_WlanMeas.Configure.WlanMeas.
		MultiEval.ListPy.count. \n
			:param enable_mod: No help available
		"""
		param = Conversions.list_to_csv_str(enable_mod)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:RESult:MODulation {param}')

	def get_ts_mask(self) -> List[bool]:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:RESult:TSMask \n
		Snippet: value: List[bool] = driver.configure.wlanMeas.multiEval.listPy.result.get_ts_mask() \n
		Enables or disables the evaluation of results for modulation (..:MODulation) and transmit spectrum mask (..
		:TSMask) measurements in list mode. The values in curly brackets {} are specified for each active segment: {...}seg 1, {..
		.}seg 2, ..., {...}seg n. The number of active segments n is determined by method RsCMPX_WlanMeas.Configure.WlanMeas.
		MultiEval.ListPy.count. \n
			:return: enable_sem: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:RESult:TSMask?')
		return Conversions.str_to_bool_list(response)

	def set_ts_mask(self, enable_sem: List[bool]) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:RESult:TSMask \n
		Snippet: driver.configure.wlanMeas.multiEval.listPy.result.set_ts_mask(enable_sem = [True, False, True]) \n
		Enables or disables the evaluation of results for modulation (..:MODulation) and transmit spectrum mask (..
		:TSMask) measurements in list mode. The values in curly brackets {} are specified for each active segment: {...}seg 1, {..
		.}seg 2, ..., {...}seg n. The number of active segments n is determined by method RsCMPX_WlanMeas.Configure.WlanMeas.
		MultiEval.ListPy.count. \n
			:param enable_sem: No help available
		"""
		param = Conversions.list_to_csv_str(enable_sem)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:RESult:TSMask {param}')
