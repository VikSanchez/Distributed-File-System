# ScalableAssignment2
Distributed File System using Sockets with Server and Client.
Implements Locking, Authentication, File Server and Directory Server

Worked on Directory Server for retreiving list of files and the details of the files going to the file server.This lets users to create, read, write and edit files from the list of the files that are available. This stores all files in a file server in which it maintains the mapping of full file names to server fileneame. This mapped File Name is passed onto the File Server.  Worked on Authenticaton Server to make sure that the user has credentials stored in the system. 

The File Server implements NFS File System. Lock Server implements locking mechanism using the status of the file using a database, which in this case is sqlite3.

Run Server.sh first and Client.py

Vikas Raj Paidimukkala CS7NS1 17304678 
