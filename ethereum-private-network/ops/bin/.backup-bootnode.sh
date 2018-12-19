#!/bin/sh

# Read parameters
while test $# -gt 0; do

  case "$1" in

    -h|--help)
      echo "----------------------------------------------------------------------"
      echo "Backup datadir from bootnode"
      echo ""
      echo "Usage: bash .backup.sh {arguments} [options]"
      echo " "
      echo "arguments:"
      echo "-h, --help                               show brief help"
      echo "-d, --datadir={/root/enpichain}          (required) specify geth datadir"
      echo "----------------------------------------------------------------------"
      exit 0
      ;;

    -d|--datadir)
      shift
      datadir=$1
      shift
      ;;

    *)
      break
      ;;

  esac

done

# Validation
if [ -z "$datadir" ]
  then
    echo "Please specify: datadir(-d|--datadir)"
    echo "Run command with --help for more details"
    exit 0
fi

mkdir -p ./eth_backup/raw/datadir ./eth_backup/raw/ethash
NOW=$(date +"%y-%m-%d_%H-%M")

echo "Processing datadir -----"
docker cp eth-bootnode:$datadir/ ./eth_backup/raw
echo "Processing .ethash -----"
docker cp eth-bootnode:/root/.ethash/ ./eth_backup/raw

echo "Compressing -----"
tar -cvzf ./eth_backup/backup.$NOW.tar.gz ./eth_backup/raw
rm -rf ./eth_backup/raw

echo "-------"
echo "DONE..!"
echo "-------"
