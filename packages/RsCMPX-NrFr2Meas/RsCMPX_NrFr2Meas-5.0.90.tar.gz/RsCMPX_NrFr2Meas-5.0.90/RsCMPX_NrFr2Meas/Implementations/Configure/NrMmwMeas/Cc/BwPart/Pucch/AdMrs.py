from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AdMrsCls:
	"""AdMrs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("adMrs", core, parent)

	def set(self, bwp: enums.BandwidthPart, additional_dmrs: bool, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:BWPart:PUCCh:ADMRs \n
		Snippet: driver.configure.nrMmwMeas.cc.bwPart.pucch.adMrs.set(bwp = enums.BandwidthPart.BWP0, additional_dmrs = False, carrierComponent = repcap.CarrierComponent.Default) \n
		Specifies whether the PUCCH in the <BWP> on carrier <no> uses an additional DMRS. For Signal Path = Network, the setting
		is not configurable. \n
			:param bwp: No help available
			:param additional_dmrs: No help available
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('bwp', bwp, DataType.Enum, enums.BandwidthPart), ArgSingle('additional_dmrs', additional_dmrs, DataType.Boolean))
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:BWPart:PUCCh:ADMRs {param}'.rstrip())

	def get(self, bwp: enums.BandwidthPart, carrierComponent=repcap.CarrierComponent.Default) -> bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:BWPart:PUCCh:ADMRs \n
		Snippet: value: bool = driver.configure.nrMmwMeas.cc.bwPart.pucch.adMrs.get(bwp = enums.BandwidthPart.BWP0, carrierComponent = repcap.CarrierComponent.Default) \n
		Specifies whether the PUCCH in the <BWP> on carrier <no> uses an additional DMRS. For Signal Path = Network, the setting
		is not configurable. \n
			:param bwp: No help available
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: additional_dmrs: No help available"""
		param = Conversions.enum_scalar_to_str(bwp, enums.BandwidthPart)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:BWPart:PUCCh:ADMRs? {param}')
		return Conversions.str_to_bool(response)
