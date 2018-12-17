#!/bin/bash
set -e
cd /root/api-app

# Replace some setting on app.json
perl -pi -e "s/SETTING_INSTANCE_NAME/$(hostname)/g" app.json

/usr/bin/pm2 start ./app.json
sleep 3

# Create a database that uses genesis block
geth --datadir=$ETH_DATA_DIR init "/root/files/genesis.json"
sleep 3

# Enable Dynamic IP on Docker container
BOOTSTRAP_IP=$(getent hosts "$ETH_BOOTNODE" | cut -d" " -f1)
GETH_OPTS=${@/BOOTNODE_IP/$BOOTSTRAP_IP}

echo "GETH_OPTS=========================================================="
echo $GETH_OPTS

geth $GETH_OPTS
# geth "$@"
