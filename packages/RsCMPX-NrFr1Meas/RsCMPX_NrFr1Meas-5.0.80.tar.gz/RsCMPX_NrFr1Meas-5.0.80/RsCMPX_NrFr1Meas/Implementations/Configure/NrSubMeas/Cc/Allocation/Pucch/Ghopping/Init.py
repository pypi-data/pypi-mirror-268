from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InitCls:
	"""Init commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("init", core, parent)

	def set(self, initialization: enums.GhopingInit, carrierComponentFour=repcap.CarrierComponentFour.Nr1, allocation=repcap.Allocation.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUCCh:GHOPping:INIT \n
		Snippet: driver.configure.nrSubMeas.cc.allocation.pucch.ghopping.init.set(initialization = enums.GhopingInit.CID, carrierComponentFour = repcap.CarrierComponentFour.Nr1, allocation = repcap.Allocation.Default) \n
		Specifies the type of ID used to initialize group hopping and sequence hopping, for carrier <no>, allocation <a>. \n
			:param initialization: Cell ID or hopping ID
			:param carrierComponentFour: optional repeated capability selector. Default value: Nr1
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
		"""
		param = Conversions.enum_scalar_to_str(initialization, enums.GhopingInit)
		carrierComponentFour_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentFour, repcap.CarrierComponentFour)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponentFour_cmd_val}:ALLocation{allocation_cmd_val}:PUCCh:GHOPping:INIT {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponentFour=repcap.CarrierComponentFour.Nr1, allocation=repcap.Allocation.Default) -> enums.GhopingInit:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUCCh:GHOPping:INIT \n
		Snippet: value: enums.GhopingInit = driver.configure.nrSubMeas.cc.allocation.pucch.ghopping.init.get(carrierComponentFour = repcap.CarrierComponentFour.Nr1, allocation = repcap.Allocation.Default) \n
		Specifies the type of ID used to initialize group hopping and sequence hopping, for carrier <no>, allocation <a>. \n
			:param carrierComponentFour: optional repeated capability selector. Default value: Nr1
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
			:return: initialization: Cell ID or hopping ID"""
		carrierComponentFour_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentFour, repcap.CarrierComponentFour)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		response = self._core.io.query_str(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponentFour_cmd_val}:ALLocation{allocation_cmd_val}:PUCCh:GHOPping:INIT?')
		return Conversions.str_to_scalar_enum(response, enums.GhopingInit)
