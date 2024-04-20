from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class YCls:
	"""Y commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("y", core, parent)

	def get_a(self) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:A \n
		Snippet: value: float = driver.configure.wlanMeas.multiEval.limit.tsMask.lofdm.y.get_a() \n
		No command help available \n
			:return: tsm_lim_yrel_lev_a: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:A?')
		return Conversions.str_to_float(response)

	def set_a(self, tsm_lim_yrel_lev_a: float) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:A \n
		Snippet: driver.configure.wlanMeas.multiEval.limit.tsMask.lofdm.y.set_a(tsm_lim_yrel_lev_a = 1.0) \n
		No command help available \n
			:param tsm_lim_yrel_lev_a: No help available
		"""
		param = Conversions.decimal_value_to_str(tsm_lim_yrel_lev_a)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:A {param}')

	def get_b(self) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:B \n
		Snippet: value: float = driver.configure.wlanMeas.multiEval.limit.tsMask.lofdm.y.get_b() \n
		No command help available \n
			:return: tsm_lim_yrel_lev_b: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:B?')
		return Conversions.str_to_float(response)

	def set_b(self, tsm_lim_yrel_lev_b: float) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:B \n
		Snippet: driver.configure.wlanMeas.multiEval.limit.tsMask.lofdm.y.set_b(tsm_lim_yrel_lev_b = 1.0) \n
		No command help available \n
			:param tsm_lim_yrel_lev_b: No help available
		"""
		param = Conversions.decimal_value_to_str(tsm_lim_yrel_lev_b)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:B {param}')

	def get_c(self) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:C \n
		Snippet: value: float = driver.configure.wlanMeas.multiEval.limit.tsMask.lofdm.y.get_c() \n
		No command help available \n
			:return: tsm_lim_yrel_lev_c: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:C?')
		return Conversions.str_to_float(response)

	def set_c(self, tsm_lim_yrel_lev_c: float) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:C \n
		Snippet: driver.configure.wlanMeas.multiEval.limit.tsMask.lofdm.y.set_c(tsm_lim_yrel_lev_c = 1.0) \n
		No command help available \n
			:param tsm_lim_yrel_lev_c: No help available
		"""
		param = Conversions.decimal_value_to_str(tsm_lim_yrel_lev_c)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:C {param}')

	def get_d(self) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:D \n
		Snippet: value: float = driver.configure.wlanMeas.multiEval.limit.tsMask.lofdm.y.get_d() \n
		No command help available \n
			:return: tsm_lim_yrel_lev_d: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:D?')
		return Conversions.str_to_float(response)

	def set_d(self, tsm_lim_yrel_lev_d: float) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:D \n
		Snippet: driver.configure.wlanMeas.multiEval.limit.tsMask.lofdm.y.set_d(tsm_lim_yrel_lev_d = 1.0) \n
		No command help available \n
			:param tsm_lim_yrel_lev_d: No help available
		"""
		param = Conversions.decimal_value_to_str(tsm_lim_yrel_lev_d)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:D {param}')
