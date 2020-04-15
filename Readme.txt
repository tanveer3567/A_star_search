Name: Tanveer Ahmed Shaik
UTA id: 1001704423
Programming Language: Python

Code Structure:

	The code has two classes:
		1. City class is used as a datas tructure for holding the infomation related to name, parent, child, distance and h_distance, 
	   	this will be used for storing information that we need while finding the path from sourse to destination.
		2. Solution class has two methods:
			a. find_route method holds the logic for find the path from source to distination.
			b. extract_children method deals with extracting children of a particular city.

How to run the code:

	Task 1 folder has 4 files:
		1. find_route.py
		2. input1.txt
		3. h_kassel.txt
		4. readme.txt

	Any python version above 2.7 need to me installed and path needs to be set before running from the command line.
	Note: Code runs successfully in omega server.

	Open command line and go to assignment1_txs4423 -> Task1 ->

	folder and then type the followiing for uninformed search 

		-> python find_route.py input1.txt Bremen Kassel

	type the following for informed search
		
		-> python find_route.py input1.txt Bremen Kassel h_kassel.txt