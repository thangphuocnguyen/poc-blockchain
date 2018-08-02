pragma solidity ^0.4.24;


import "./ERC20Interface.sol";
import "./SafeMath.sol";

// ----------------------------------------------------------------------------
// 'tpndemo' token contract
//
// Deployed to : 0x91F4bE2426A700AA6fdF0B29AF970818761717A6
// Symbol      : TPNDEMO
// Name        : TPN Demo Token
// Total supply: 100000000000000000000000000
// Decimals    : 18
// ----------------------------------------------------------------------------


// ----------------------------------------------------------------------------
// ERC20 Token, with the addition of symbol, name and decimals and assisted
// token transfers
// ----------------------------------------------------------------------------
contract TPNDemoToken is ERC20Interface {
    using SafeMath for uint256;

    // uint256 constant private MAX_UINT256 = 2**256 - 1;
    mapping(address => uint256) balances;
    mapping(address => mapping(address => uint256)) public allowed;

    string public  name;
    string public symbol;
    uint8 public decimals;
    uint _totalSupply;

    // ------------------------------------------------------------------------
    // Constructor
    // ------------------------------------------------------------------------
    constructor(
        uint256 _initialAmount, 
        string _tokenName, 
        string _tokenSymbol, 
        uint8 _decimalUnits
        ) public {

        // Update total suppply
        // _totalSupply = 100 000000 000000 000000; // in case to make 100 tokens
        _totalSupply = _initialAmount * (10 ** uint256(_decimalUnits));

        // Give the creator all initial tokens
        balances[msg.sender] = _totalSupply; 
        
        // Token Name
        // name = "TPN Demo Token";
        name = _tokenName;
        // the standard (and max) is 18 decimals, meaning that a coin can be splitted in 18 parts
        // In case that we want issue 100 tokens, then 100 + number of decimals
        // decimals = 18;
        decimals = _decimalUnits;
        // Set the symbol for display
        // symbol = "TPNDemo";
        symbol = _tokenSymbol;
    }

    function totalSupply() public view returns (uint) {
        return _totalSupply.safeSub(balances[address(0)]);
    }

    // ------------------------------------------------------------------------
    // Transfer the balance from token owner's account to another account
    // - Owner's account must have sufficient balance to transfer
    // - 0 value transfers are allowed
    // ------------------------------------------------------------------------
    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(balances[msg.sender] >= _value);
        
        balances[msg.sender] = SafeMath.safeSub(balances[msg.sender], _value);
        balances[_to] = SafeMath.safeAdd(balances[_to], _value);
        
        emit Transfer(msg.sender, _to, _value);
        
        return true;
    }

    // ------------------------------------------------------------------------
    // Transfer tokens from the 'from' account to the 'to' account
    // 
    // transferFrom method is used for a withdraw workflow!
    // 
    // The calling account must already have sufficient tokens approve(...)-d
    // for spending from the from account and
    // - From account must have sufficient balance to transfer
    // - Spender must have sufficient allowance to transfer
    // - 0 value transfers are allowed
    // ------------------------------------------------------------------------
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {

        require(balances[_from] >= _value);
        require(allowed[_from][msg.sender] >= _value);
        require(_to != address(0));

        balances[_from] = balances[_from].safeSub(_value);
        balances[_to] = balances[_to].safeAdd(_value);

        allowed[_from][msg.sender] = allowed[_from][msg.sender].safeSub(_value);
        
        emit Transfer(_from, _to, _value);
        
        return true;
    }


    // ------------------------------------------------------------------------
    // Returns the amount of tokens approved by the owner that can be
    // transferred to the spender's account
    // ------------------------------------------------------------------------
    function allowance(address _owner, address _spender) public view returns (uint256 remaining) {
        return allowed[_owner][_spender];
    }


    // ------------------------------------------------------------------------
    // Get the token balance for account tokenOwner
    // ------------------------------------------------------------------------
    function balanceOf(address _tokenOwner) public view returns (uint256 balance) {
        return balances[_tokenOwner];
    }

    // // ------------------------------------------------------------------------
    // // Token owner can approve for spender to transferFrom(...) tokens
    // // from the token owner's account
    // //
    // // https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20-token-standard.md
    // // recommends that there are no checks for the approval double-spend attack
    // // as this should be implemented in user interfaces 
    // // ------------------------------------------------------------------------
    function approve(address _spender, uint256 _value) public returns (bool success) {
        allowed[msg.sender][_spender] = _value;
        
        emit Approval(msg.sender, _spender, _value);
        
        return true;
    }
}