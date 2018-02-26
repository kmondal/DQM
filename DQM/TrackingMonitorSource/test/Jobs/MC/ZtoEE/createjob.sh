#!/bin/bash
mkdir -p step1_output log
workdir=$(echo $PWD)
echo $workdir
i=1
while [ $i -lt 10 ]
  do
    j=$(($i+1))
    fnames=$(echo $(sed -n "$i,$j p" ZtoEE.txt))
    echo $i,$j
    echo $fnames
    sed -e "s@PWD@$workdir@g" \
	-e "s@INPUTFILES@$fnames@g" \
        -e "s@INDEX@$i@g" step1_cfg.py.tmpl > "step1_"$i"_cfg.py"
    sed -e "s@PWD@$workdir@g" \
	-e "s@INDEX@$i@g" submit.sh.tmpl > "submit_"$i".sh"
    chmod 755 "submit_"$i".sh"
    bsub -q 1nd -J "job"$i < "submit_"$i".sh"
    i=$(($i+2))
done
