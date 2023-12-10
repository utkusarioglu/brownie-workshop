// SPDX-License-Identifier: MIT

pragma solidity 0.8.18;

contract Sample {
  uint256 private valueStorage;

  function setValue(uint256 value) public {
    valueStorage = value;
  }

  function getValueStorage() public view returns(uint256) {
    return valueStorage;
  }
}
