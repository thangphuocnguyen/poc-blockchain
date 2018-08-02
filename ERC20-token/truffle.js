// See <http://truffleframework.com/docs/advanced/configuration>

require('dotenv').config();

const Web3 = require("web3");
const web3 = new Web3();
const WalletProvider = require("truffle-wallet-provider");
const Wallet = require('ethereumjs-wallet');


var ropstenPrivateKey = new Buffer(process.env["ROPSTEN_PRIVATE_KEY"], "hex")
var ropstenWallet = Wallet.fromPrivateKey(ropstenPrivateKey);
var ropstenProvider = new WalletProvider(ropstenWallet, "https://ropsten.infura.io/");


module.exports = {
    networks: {
        development: {
            network_id: "*", // Match any network id
            host: "127.0.0.1",
            port: 9545
        },
        ganache: {
            network_id: "*", // Match any network id
            host: "127.0.0.1",
            port: 7545
        },
        ganache_cli: {
            network_id: "*", // Match any network id
            host: "127.0.0.1",
            port: 8545
        },
        ropsten: {
            provider: ropstenProvider,
            gas: 4600000,
            gasPrice: web3.toWei("20", "gwei"),
            network_id: "3",
        }
    }

};
