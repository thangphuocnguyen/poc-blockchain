pragma solidity ^0.4.24;

// ----------------------------------------------------------------------------
// Follow https://theethereum.wiki/w/index.php/ERC20_Token_Standard
// ----------------------------------------------------------------------------
// ERC Token Standard #20 Interface
// https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20-token-standard.md
// ----------------------------------------------------------------------------
// @tpn: Be noticed that by suggest of EIPs, ERC20Interface should separated to 
// 2 parts, ERC20Basic and ERC20 that inheritance from ERC20Basic in order to 
// make more reuseable.
contract ERC20Interface {
    function totalSupply() public view returns (uint);
    function balanceOf(address _owner) public view returns (uint256 balance);
    function allowance(address _owner, address _to) public view returns (uint256 remaining);
    
    function transfer(address _to, uint _value) public returns (bool success);
    function approve(address _spender, uint _value) public returns (bool success);
    function transferFrom(address _from, address _to, uint256 tokens) public returns (bool success);

    event Transfer(address indexed _from, address indexed _to, uint256 _value);
    event Approval(address indexed _owner, address indexed _spender, uint256 _value);
}