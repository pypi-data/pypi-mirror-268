from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BCls:
	"""B commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("b", core, parent)

	def set(self, tsm_lim_yrel_lev_b: float, bandwidthC=repcap.BandwidthC.Default, band=repcap.Band.Default) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:HTOFdm:BW<bandwidth>:BAND<band>:Y:B \n
		Snippet: driver.configure.wlanMeas.multiEval.limit.tsMask.htOfdm.bw.band.y.b.set(tsm_lim_yrel_lev_b = 1.0, bandwidthC = repcap.BandwidthC.Default, band = repcap.Band.Default) \n
		Defines the relative spectral density limit for point B (frequency offset: 3/2*bandwidth) on the transmit spectrum mask
		for 802.11n signals with the specified <bandwidth> and the selected <band>. See 'Transmit spectrum mask OFDM, default
		masks' for background information. \n
			:param tsm_lim_yrel_lev_b: No help available
			:param bandwidthC: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Bw')
			:param band: optional repeated capability selector. Default value: Nr2 (settable in the interface 'Band')
		"""
		param = Conversions.decimal_value_to_str(tsm_lim_yrel_lev_b)
		bandwidthC_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthC, repcap.BandwidthC)
		band_cmd_val = self._cmd_group.get_repcap_cmd_value(band, repcap.Band)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:HTOFdm:BW{bandwidthC_cmd_val}:BAND{band_cmd_val}:Y:B {param}')

	def get(self, bandwidthC=repcap.BandwidthC.Default, band=repcap.Band.Default) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:HTOFdm:BW<bandwidth>:BAND<band>:Y:B \n
		Snippet: value: float = driver.configure.wlanMeas.multiEval.limit.tsMask.htOfdm.bw.band.y.b.get(bandwidthC = repcap.BandwidthC.Default, band = repcap.Band.Default) \n
		Defines the relative spectral density limit for point B (frequency offset: 3/2*bandwidth) on the transmit spectrum mask
		for 802.11n signals with the specified <bandwidth> and the selected <band>. See 'Transmit spectrum mask OFDM, default
		masks' for background information. \n
			:param bandwidthC: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Bw')
			:param band: optional repeated capability selector. Default value: Nr2 (settable in the interface 'Band')
			:return: tsm_lim_yrel_lev_b: No help available"""
		bandwidthC_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthC, repcap.BandwidthC)
		band_cmd_val = self._cmd_group.get_repcap_cmd_value(band, repcap.Band)
		response = self._core.io.query_str(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:HTOFdm:BW{bandwidthC_cmd_val}:BAND{band_cmd_val}:Y:B?')
		return Conversions.str_to_float(response)
