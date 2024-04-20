from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NrSubMeasCls:
	"""NrSubMeas commands group definition. 315 total commands, 11 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nrSubMeas", core, parent)

	@property
	def multiEval(self):
		"""multiEval commands group. 16 Sub-classes, 23 commands."""
		if not hasattr(self, '_multiEval'):
			from .MultiEval import MultiEvalCls
			self._multiEval = MultiEvalCls(self._core, self._cmd_group)
		return self._multiEval

	@property
	def network(self):
		"""network commands group. 4 Sub-classes, 6 commands."""
		if not hasattr(self, '_network'):
			from .Network import NetworkCls
			self._network = NetworkCls(self._core, self._cmd_group)
		return self._network

	@property
	def bwConfig(self):
		"""bwConfig commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bwConfig'):
			from .BwConfig import BwConfigCls
			self._bwConfig = BwConfigCls(self._core, self._cmd_group)
		return self._bwConfig

	@property
	def rfSettings(self):
		"""rfSettings commands group. 2 Sub-classes, 6 commands."""
		if not hasattr(self, '_rfSettings'):
			from .RfSettings import RfSettingsCls
			self._rfSettings = RfSettingsCls(self._core, self._cmd_group)
		return self._rfSettings

	@property
	def ulDl(self):
		"""ulDl commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ulDl'):
			from .UlDl import UlDlCls
			self._ulDl = UlDlCls(self._core, self._cmd_group)
		return self._ulDl

	@property
	def cc(self):
		"""cc commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_cc'):
			from .Cc import CcCls
			self._cc = CcCls(self._core, self._cmd_group)
		return self._cc

	@property
	def ccall(self):
		"""ccall commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ccall'):
			from .Ccall import CcallCls
			self._ccall = CcallCls(self._core, self._cmd_group)
		return self._ccall

	@property
	def caggregation(self):
		"""caggregation commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_caggregation'):
			from .Caggregation import CaggregationCls
			self._caggregation = CaggregationCls(self._core, self._cmd_group)
		return self._caggregation

	@property
	def listPy(self):
		"""listPy commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPyCls
			self._listPy = ListPyCls(self._core, self._cmd_group)
		return self._listPy

	@property
	def prach(self):
		"""prach commands group. 7 Sub-classes, 12 commands."""
		if not hasattr(self, '_prach'):
			from .Prach import PrachCls
			self._prach = PrachCls(self._core, self._cmd_group)
		return self._prach

	@property
	def srs(self):
		"""srs commands group. 8 Sub-classes, 9 commands."""
		if not hasattr(self, '_srs'):
			from .Srs import SrsCls
			self._srs = SrsCls(self._core, self._cmd_group)
		return self._srs

	def get_nantenna(self) -> int:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:NANTenna \n
		Snippet: value: int = driver.configure.nrSubMeas.get_nantenna() \n
		Selects the number of UE TX antennas to be measured. \n
			:return: number: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:NANTenna?')
		return Conversions.str_to_int(response)

	def set_nantenna(self, number: int) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:NANTenna \n
		Snippet: driver.configure.nrSubMeas.set_nantenna(number = 1) \n
		Selects the number of UE TX antennas to be measured. \n
			:param number: No help available
		"""
		param = Conversions.decimal_value_to_str(number)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:NANTenna {param}')

	# noinspection PyTypeChecker
	def get_stype(self) -> enums.SignalType:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:STYPe \n
		Snippet: value: enums.SignalType = driver.configure.nrSubMeas.get_stype() \n
		No command help available \n
			:return: signal_type: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:STYPe?')
		return Conversions.str_to_scalar_enum(response, enums.SignalType)

	def set_stype(self, signal_type: enums.SignalType) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:STYPe \n
		Snippet: driver.configure.nrSubMeas.set_stype(signal_type = enums.SignalType.SL) \n
		No command help available \n
			:param signal_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(signal_type, enums.SignalType)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:STYPe {param}')

	# noinspection PyTypeChecker
	def get_band(self) -> enums.Band:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:BAND \n
		Snippet: value: enums.Band = driver.configure.nrSubMeas.get_band() \n
		Selects the operating band (OB) . The allowed input range depends on the duplex mode (FDD or TDD) . \n
			:return: band: TDD UL: OB34 | OB38 | ... | OB41 | OB46 | OB47 | OB48 | OB50 | OB51 | OB53 | OB77 | ... | OB84 | OB86 | OB89 | OB90 | OB95 | ... | OB99 | OB101 | OB104
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:BAND?')
		return Conversions.str_to_scalar_enum(response, enums.Band)

	def set_band(self, band: enums.Band) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:BAND \n
		Snippet: driver.configure.nrSubMeas.set_band(band = enums.Band.OB1) \n
		Selects the operating band (OB) . The allowed input range depends on the duplex mode (FDD or TDD) . \n
			:param band: TDD UL: OB34 | OB38 | ... | OB41 | OB46 | OB47 | OB48 | OB50 | OB51 | OB53 | OB77 | ... | OB84 | OB86 | OB89 | OB90 | OB95 | ... | OB99 | OB101 | OB104
		"""
		param = Conversions.enum_scalar_to_str(band, enums.Band)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:BAND {param}')

	# noinspection PyTypeChecker
	def get_spath(self) -> enums.SignalPath:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SPATh \n
		Snippet: value: enums.SignalPath = driver.configure.nrSubMeas.get_spath() \n
		No command help available \n
			:return: path: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:SPATh?')
		return Conversions.str_to_scalar_enum(response, enums.SignalPath)

	def set_spath(self, path: enums.SignalPath) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SPATh \n
		Snippet: driver.configure.nrSubMeas.set_spath(path = enums.SignalPath.NETWork) \n
		No command help available \n
			:param path: No help available
		"""
		param = Conversions.enum_scalar_to_str(path, enums.SignalPath)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:SPATh {param}')

	def get_ncarrier(self) -> int:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:NCARrier \n
		Snippet: value: int = driver.configure.nrSubMeas.get_ncarrier() \n
		Configures the number of contiguously aggregated UL carriers in the measured signal. \n
			:return: number: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:NCARrier?')
		return Conversions.str_to_int(response)

	def set_ncarrier(self, number: int) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:NCARrier \n
		Snippet: driver.configure.nrSubMeas.set_ncarrier(number = 1) \n
		Configures the number of contiguously aggregated UL carriers in the measured signal. \n
			:param number: No help available
		"""
		param = Conversions.decimal_value_to_str(number)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:NCARrier {param}')

	def clone(self) -> 'NrSubMeasCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NrSubMeasCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
