#1 /bin/bash -i

if [ $# -lt 1 ];then
  echo "Es wurde nichts angegeben. Du Nase!"
  echo "Verwendung: under_coverrage.sh <path to BAM1> <path to BAM2> ... <path to BAM X>"
  exit
fi

# Paramter einlesen
read -e -p "Bereich (NC_XXXXXXXX.X oder chr1 etc.): " SCAFF
read -e -p "Start eingeben: " START
read -e -p "Ende eingeben: "  STOP

while [ $# -gt 0 ]; do
  PATHNAME=$1
  if [ -f $PATHNAME ]; then
    echo "$PATHNAME"
    mkdir tmp
    cd ./tmp
    bedtools genomecov -ibam ../$PATHNAME -d > genomcov_out
    if [ ! -f ../under_coverage_out.txt ]; then
      touch ../under_coverage_out.txt
    fi
    python ../under_coverage.py genomcov_out $SCAFF $START $STOP | tee -a ../under_coverage_out.txt #2>&1
    cd ..
    rm -r tmp
  else
    echo "Bam $PATHNAME nicht gefunden..."
  fi
    shift
done
