#!/bin/bash

experiments=2000

echo "\$(function() {" > g.js
d1="["
d2="["

for i in {1..100}
do
	`python generator.py 5`
	d1="$d1[$i, `python main.py`]"
	d2="$d2[$i, `python closer.py`]"

	if [ $i -le 99 ] 
	then
		d1="$d1, "
		d2="$d2, "
	fi

done

d1="$d1]"
d2="$d2]"

echo "		var d1 = $d1;" >> g.js
echo "		var d2 = $d2;" >> g.js
echo "		var data1 = [{data: d1, label: \"Permutations\"},
				{data: d2, label: \"Closer neighbour\"}];" >> g.js
echo "		$.plot(\$(\"#accuracy\"), data1);" >> g.js
echo " });" >> g.js
