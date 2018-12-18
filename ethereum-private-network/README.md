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
	
	