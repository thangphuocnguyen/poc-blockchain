# Ethereum Private Network
*This repository contains all resources for practice Ethereum-Private-Network*

## Targets:

* Setup an Ethereum Network as a Private network as nodes that not connected to the main network nodes. 
* Ethereum Version: [Ethereum Homestead](http://ethdocs.org/en/latest/introduction/the-homestead-release.html)
* Ethereum Client: [go-ethereum (geth)](https://github.com/ethereum/go-ethereum)
* Apply [docker-component](https://docs.docker.com/compose/) - isolated Private Network based docker environment
* Apply [Ethereum Network Intelligence API](https://github.com/cubedro/eth-net-intelligence-api) that alow to tracking each node's network activity
* Apply [Ethereum Netstats](https://github.com/cubedro/eth-netstats) as visualization for Private Network
* Apply [Metamask](https://metamask.io/) to interacting/demo the Ethereum Transaction


## Run up:

1. **Setting Environments**

	In `ops` directory, create an `.env` file by follow the `.env.example`

2. **Setting genesis.json specs**

	This settup already includes an `genesis.json` specs.
	
	In case you want to spes your own genesis, follow [Create The Genesis Block](https://github.com/ethereum/go-ethereum/wiki/Private-network#creating-the-genesis-block)	

2. **Init account**
   
   This setup already includes 5 accounts that already pre-alocating with 20 Eth on `genesis.json`
   
   In case you want to manual create your own account, you can create as manual via:
   
   `$ geth account new --keystore "[keystore-dir]"`
   

3. **Run up the cluster**

	`$ docker-compose up -d --scale eth=4`

	Above step alreay includes:

	* An eth-bootnodes that works as a bootnode which allow others find each other in Private Network
	* An eth-netstats that allow to monitoring all node activity on network.
	* Four eth (Ethereum Node) client that connected to Bootnode and auto mining (Those node already include Ethereum Network Intelligence API extension).


4. **Access Netstats Monitoring**

	Acess [http://localhost:3000](http://localhost:3000)
	
5. **Use Metamask as Account Manager**
	
* Setting Custom RPC on [Metamask](https://metamask.io/) as `http://localhost:8445`
* Import Account to Metamask and see the balance or testing with sending Ether.
	


## Other Configurations/Interactive 

* **Generate nodekeyhex/enode address for bootnode**
	
	*Generate nodekeyhex*
	
	`$ bootnode --genkey=boot.key`
	
	*Generate enode adress from nodekeyhex*
	
	`$ bootnode --nodekey=boot.key -writeaddress`
	

* *List accounts*

	`$ geth account --datadir=[datadir] list`
	
* *Attach to ETH node ([geth javascript console](https://github.com/ethereum/go-ethereum/wiki/JavaScript-Console))*
	
	
	`$ docker exec -it [container name] geth attach --datadir=[Data Directory that configured by ETH_DATA_DIR`
	
## Techstacks

* [Ethereum](https://www.ethereum.org/)

	> Ethereum is a decentralized platform that runs smart contracts, applications that run exactly as programmed without possibility of downtime, censorship, fraud or third party interference.
	
	> [The Homestead Release](http://ethdocs.org/en/latest/introduction/the-homestead-release.html) is the second major version of the Ethereum platform and is the first production release of Ethereum. It includes several protocol changes and a networking change that provides the ability to do further network upgrades.

* [Go-Ethereum - Geth v1.8.19](https://geth.ethereum.org/)

	> Official Go implementation of the Ethereum protocol 

* [Docker](https://www.docker.com/)

	> Docker provides a way to run applications securely isolated in a container, packaged with all its dependencies and libraries.

* [Docker-Compose](https://docs.docker.com/compose/overview/)

	> Compose is a tool for defining and running multi-container Docker applications

* [Ethereum Network Intelligence API](https://github.com/cubedro/eth-net-intelligence-api)

	> This is the backend service which runs along with ethereum and tracks the network status, fetches information through JSON-RPC and connects through WebSockets to eth-netstats to feed information

* [Ethereum Netstats](https://github.com/cubedro/eth-netstats)

	> A visual interface for tracking ethereum network status. It uses WebSockets to receive stats from running nodes and output them through an angular interface. It is the front-end implementation for eth-net-intelligence-api
 
