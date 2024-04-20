from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnableCls:
	"""Enable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enable", core, parent)

	def set(self, tsm_lim_enable: bool, bandwidthC=repcap.BandwidthC.Default) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:HTOFdm:BW<bandwidth>:ENABle \n
		Snippet: driver.configure.wlanMeas.multiEval.limit.tsMask.htOfdm.bw.enable.set(tsm_lim_enable = False, bandwidthC = repcap.BandwidthC.Default) \n
		Enables or disables the transmit spectrum mask for 802.11n signals with the specified <bandwidth>, i.e. activates or
		deactivates the corresponding limit check. \n
			:param tsm_lim_enable: No help available
			:param bandwidthC: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Bw')
		"""
		param = Conversions.bool_to_str(tsm_lim_enable)
		bandwidthC_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthC, repcap.BandwidthC)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:HTOFdm:BW{bandwidthC_cmd_val}:ENABle {param}')

	def get(self, bandwidthC=repcap.BandwidthC.Default) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:HTOFdm:BW<bandwidth>:ENABle \n
		Snippet: value: bool = driver.configure.wlanMeas.multiEval.limit.tsMask.htOfdm.bw.enable.get(bandwidthC = repcap.BandwidthC.Default) \n
		Enables or disables the transmit spectrum mask for 802.11n signals with the specified <bandwidth>, i.e. activates or
		deactivates the corresponding limit check. \n
			:param bandwidthC: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Bw')
			:return: tsm_lim_enable: No help available"""
		bandwidthC_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthC, repcap.BandwidthC)
		response = self._core.io.query_str(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:HTOFdm:BW{bandwidthC_cmd_val}:ENABle?')
		return Conversions.str_to_bool(response)
