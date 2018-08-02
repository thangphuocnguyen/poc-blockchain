pragma solidity ^0.4.24;

// ----------------------------------------------------------------------------
// Safe maths
// ----------------------------------------------------------------------------
library SafeMath {
    function safeAdd(uint256 _a, uint256 _b) public pure returns (uint256 c) {
        c = _a + _b;
        assert(c >= _a);
        return c;
    }
    
    function safeSub(uint256 _a, uint256 _b) public pure returns (uint256) {
        assert(_b <= _a);
        return _a - _b;
    }
    
    function safeMul(uint256 _a, uint256 _b) public pure returns (uint c) {
        // Gas optimization: Check zero _a is cheaper than asserting 'a' not being zero,
        // Bypass checking zero _b since it is rare case and this gas optimation will lose
        // in case to check it
        if (_a == 0) {
            return 0;
        }
        
        c = _a * _b;
        assert(c / _a == _b);
        
        return c;
    }
    
    function safeDiv(uint256 _a, uint256 _b) public pure returns (uint256) {
        // assert(_b > 0); // Solidity automatically throws when dividing by 0
        // uint256 c = _a / _b;
        // assert(_a == _b * c + _a % _b); // There is no case in which this doesn't hold
        return _a / _b;
    }
}