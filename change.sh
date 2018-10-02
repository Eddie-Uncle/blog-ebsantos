#!/bin/bash
echo "Searching for old value"
grep -ir www.ebsantos.com *
echo "Replacing for the new values"
cd output/
sed -i 's/www.ebsantos.com/ebstg.com/g' *
cd tag/
sed -i 's/www.ebsantos.com/ebstg.com/g' *
cd ../author/
sed -i 's/www.ebsantos.com/ebstg.com/g' *
cd ../category/
sed -i 's/www.ebsantos.com/ebstg.com/g' *
echo "Replacing pelicanconf"
cd ../../../html/
sed -i 's/www.ebsantos.com/ebstg.com/g' *.py
echo "All values should been replaced successfully"