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

	def set(self, tsm_lim_enable: bool, bandwidthE=repcap.BandwidthE.Default) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:VHTofdm:BW<bandwidth>:ENABle \n
		Snippet: driver.configure.wlanMeas.multiEval.limit.tsMask.vhtOfdm.bw.enable.set(tsm_lim_enable = False, bandwidthE = repcap.BandwidthE.Default) \n
		Enables or disables the transmit spectrum mask for 802.11ac signals with the specified <bandwidth>, i.e. activates or
		deactivates the corresponding limit checks. \n
			:param tsm_lim_enable: No help available
			:param bandwidthE: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Bw')
		"""
		param = Conversions.bool_to_str(tsm_lim_enable)
		bandwidthE_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthE, repcap.BandwidthE)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:VHTofdm:BW{bandwidthE_cmd_val}:ENABle {param}')

	def get(self, bandwidthE=repcap.BandwidthE.Default) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:VHTofdm:BW<bandwidth>:ENABle \n
		Snippet: value: bool = driver.configure.wlanMeas.multiEval.limit.tsMask.vhtOfdm.bw.enable.get(bandwidthE = repcap.BandwidthE.Default) \n
		Enables or disables the transmit spectrum mask for 802.11ac signals with the specified <bandwidth>, i.e. activates or
		deactivates the corresponding limit checks. \n
			:param bandwidthE: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Bw')
			:return: tsm_lim_enable: No help available"""
		bandwidthE_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthE, repcap.BandwidthE)
		response = self._core.io.query_str(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:VHTofdm:BW{bandwidthE_cmd_val}:ENABle?')
		return Conversions.str_to_bool(response)
