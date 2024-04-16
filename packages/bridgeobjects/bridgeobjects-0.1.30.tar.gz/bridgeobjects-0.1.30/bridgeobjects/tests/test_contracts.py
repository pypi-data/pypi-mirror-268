"""A set of tests for the bridgeobjects Contract class."""
import pytest

from ..src.constants import SUITS
from ..src.contract import Contract, Call
from ..src.denomination import Denomination


def test_contract_name_valid():
    """Ensure that the contract name is correct: valid names."""
    assert Contract('1S').name == '1S'


def test_contract_name_invalid():
    """Ensure that the contract name is correct: invalid names."""
    with pytest.raises(ValueError):
        Contract('1Q')
    assert True


def test_contract_is_nt():
    """Ensure that the contract is_nt is correct: valid names."""
    assert not Contract('1S').is_nt
    assert Contract('3NT')
    contract = Contract()
    assert contract.is_nt is False


def test_contract_repr():
    """Ensure that the contract repr string is correct."""
    contract = Contract('4S', 'E')
    assert repr(contract) == 'Contract("4S", "E")'


def test_contract_str():
    """Ensure that the contract str string is correct."""
    contract = Contract('4S', 'E')
    assert str(contract) == 'Contract. 4S by E'


def test_contract_name_setter():
    """Ensure that the contract name is correct: invalid names."""
    contract = Contract()
    with pytest.raises(ValueError):
        contract.name = '1Q'
    assert True


def test_contract_name_setter_valid():
    """Ensure that the contract name is correct."""
    contract = Contract()
    contract.name = '5D'
    contract.declarer = 'S'
    assert repr(contract) == 'Contract("5D", "S")'


def test_contract_call_setter_valid():
    """Ensure that the contract call is correct."""
    contract = Contract()
    contract.call = Call('3H')
    contract.declarer = 'N'
    assert repr(contract) == 'Contract("3H", "N")'


def test_contract_call_setter_invalid_type():
    """Ensure that the contract call is correct."""
    contract = Contract()
    with pytest.raises(TypeError):
        contract.call = None


def test_contract_call_setter_invalid():
    """Ensure that the contract call is correct."""
    contract = Contract()
    with pytest.raises(ValueError):
        contract.call = 'W'
    assert True
    with pytest.raises(ValueError):
        contract.call = Call('8NT')
    with pytest.raises(ValueError):
        contract.call = Call('0S')
    assert True


def test_contract_call_setter_valid_double():
    """Ensure that the contract call is correct."""
    contract = Contract()
    contract.call = '3C'
    assert contract.call == Call('3C')

    # TODO why is this here?
    contract.call = Call('3NTX')
    assert contract.call.name == '3NTX'


def test_contract_trump_suit_setter_valid():
    """Ensure that the contract trump suit is correct."""
    contract = Contract()
    contract.trump_suit = SUITS['H']
    contract.declarer = 'N'
    assert contract.trump_suit.name == 'H'
    contract = Contract()
    contract.trump_suit = 'C'
    contract.declarer = 'N'
    assert contract.trump_suit.name == 'C'


def test_contract_trump_suit_setter_invalid():
    """Ensure that the contract trump suit is correct."""
    contract = Contract()
    with pytest.raises(TypeError):
        contract.trump_suit = 'W'
    assert True


def test_contract_denomination_valid():
    """Ensure that the contract trump suit is correct."""
    contract = Contract()
    contract.trump_suit = SUITS['H']
    assert contract.denomination == Denomination('H')


def test_contract_declarer_invalid():
    """Ensure that the contract trump suit is correct."""
    contract = Contract()
    with pytest.raises(ValueError):
        contract.declarer = 'M'
    assert True


def test_contract_modifier():
    contract = Contract('5C')
    contract.modifier = ''
    assert contract.doubled is False
    assert contract.redoubled is False

    contract.modifier = 'D'
    assert contract.doubled is True
    assert contract.redoubled is False

    contract.modifier = 'R'
    assert contract.doubled is False
    assert contract.redoubled is True

    contract.modifier = ''
    assert contract.doubled is False
    assert contract.redoubled is False

    with pytest.raises(AssertionError):
        contract.modifier = 'E'
    assert True
