# TPN

## Init Demo

### Init Development Environment

Moving to directory!

```
$ cd ERC20-token
```

Install packages

```
$ npm install
```

Complile Solidity Contract (TPNDemoToken)

```
$ npm run compile
```

Deploy Demo Contract to Local Ganache:

```
$ npm run migrate-ganache
```

Deploy Demo Contract to Local Ganache CLI:

```
$ ganache-cli

$ npm run migrate-ganache-cli
```

Deploy Demo Contract to Ropsten Testnet:

```
$ npm run migrate-ropsten
```

## Techstacks

* [solidity v0.4.24](http://solidity.readthedocs.io/en/v0.4.24/) Solidity is a contract-oriented, high-level language for implementing smart contracts.

* [truffle v4.1.12](https://truffleframework.com/) Truffle is a development environment, testing framework and asset pipeline for Ethereum

* [node v9.11.1](https://nodejs.org/) Node.js is an open-source, cross-platform JavaScript run-time environment that executes JavaScript code outside the browser.

* [ganache-cli v6.1.6](https://github.com/trufflesuite/ganache-cli) (for TestRPC) Fast Ethereum RPC client for testing and development

* [ganache v1.2.1 (MacOS)](https://truffleframework.com/ganache) Quickly fire up a personal Ethereum blockchain which you can use to run tests, execute commands, and inspect state while controlling how the chain operates.

## References:

*Folow ERC-20 Standard from Ethereum (EIPs - Ethereum Improvement Proposal) :*
* https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20.md

*Follow ERC-20 Standard wiki*
* https://theethereum.wiki/w/index.php/ERC20_Token_Standard

*Sample from OpenZeppelin*

* https://github.com/OpenZeppelin/openzeppelin-solidity