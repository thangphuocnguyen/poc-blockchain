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

    // The total token supply
    function totalSupply() public view returns (uint);
    // Returns the account balance of another account with address _owner
    function balanceOf(address _owner) public view returns (uint balance);
    // The amount which _spender is still allowed to withdraw from _owner
    function allowance(address _owner, address _to) public view returns (uint remaining);
    
    // Transfers _value amount of tokens to address _to, (fire the Transfer event also)
    function transfer(address _to, uint _value) public returns (bool success);
    // Transfers _value amount of tokens from address _from to address _to, (fire the Transfer event also)
    function transferFrom(address _from, address _to, uint tokens) public returns (bool success);
    // Allows _spender to withdraw from your account multiple times, up to the _value amount. 
    // If this function is called again it overwrites the current allowance with _value
    function approve(address _spender, uint _value) public returns (bool success);

    event Transfer(address indexed _from, address indexed _to, uint _value);
    event Approval(address indexed _owner, address indexed _spender, uint _value);
}