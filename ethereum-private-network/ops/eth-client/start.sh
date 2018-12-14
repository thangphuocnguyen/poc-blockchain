#!/bin/bash
set -e
cd /root/api-app
# perl -pi -e "s/XXX/$(hostname)/g" app.json
/usr/bin/pm2 start ./app.json
sleep 3

# Create a database that uses genesis block
geth --datadir=$ETH_DATA_DIR init "/root/files/genesis.json"
sleep 3

# BOOTSTRAP_IP='getent hosts "$ETH_MONITORED_HOST" | cut -d" " -f1'

# GETH_OPTS=${@/XXX/$BOOTSTRAP_IP}

# echo "GETH_OPTS=========================================================="
# echo $GETH_OPTS
# echo "GETH_OPTS=========================================================="

# echo $ETH_MONITORED_HOST
echo "OPTs======================================================"
echo "$@"
echo "=========================================================="

# geth $GETH_OPTS
geth "$@"
