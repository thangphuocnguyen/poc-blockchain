var SafeMath = artifacts.require("./SafeMath.sol");
var TPNDemoToken = artifacts.require("./TPNDemoToken.sol");

module.exports = function (deployer) {
    deployer.deploy(SafeMath);

    deployer.link(SafeMath, TPNDemoToken);
    deployer.deploy(TPNDemoToken, 100, 'TPN Demo Token', 'TPNDEMO', 18);
};