from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PlcIdCls:
	"""PlcId commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plcId", core, parent)

	def set(self, physical_cell_id: int, carrierComponent=repcap.CarrierComponent.Nr1) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:PLCid \n
		Snippet: driver.configure.nrSubMeas.cc.plcId.set(physical_cell_id = 1, carrierComponent = repcap.CarrierComponent.Nr1) \n
		Specifies the physical cell ID of carrier <no>. \n
			:param physical_cell_id: No help available
			:param carrierComponent: optional repeated capability selector. Default value: Nr1
		"""
		param = Conversions.decimal_value_to_str(physical_cell_id)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponent_cmd_val}:PLCid {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Nr1) -> int:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:PLCid \n
		Snippet: value: int = driver.configure.nrSubMeas.cc.plcId.get(carrierComponent = repcap.CarrierComponent.Nr1) \n
		Specifies the physical cell ID of carrier <no>. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1
			:return: physical_cell_id: No help available"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponent_cmd_val}:PLCid?')
		return Conversions.str_to_int(response)
