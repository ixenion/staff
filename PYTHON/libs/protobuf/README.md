## PURPOSE
easy serialisation and parsing of structured data

## LINKS
https://developers.google.com/protocol-buffers/docs/pythontutorial




# Download latest version of protobuf-complier from
https://github.com/protocolbuffers/protobuf/releases

# Then just unzip it:
unzip protoc-.... -d protoc-compiler

# And use ./bin/protoc
./protoc-compiler/bin/protoc -I=. --python_out=. addressbook.proto
