s=0
for n in "$@"
do
	s=`expr $s + $n`
done

echo $s

