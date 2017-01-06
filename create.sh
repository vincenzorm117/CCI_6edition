#!/usr/local/bin/bash

type=$1
ps_name="problem_statement.txt"


function prep_python_project() {
    mkdir python
    content="#!/usr/local/bin/python3"
    echo $content > python/solution.py
}



echo "Project name:"
read name

mkdir $name
cd $name

touch $ps_name


case "$type" in
"python")
    prep_python_project
    ;;
*)
    prep_python_project
esac
cd ../../
