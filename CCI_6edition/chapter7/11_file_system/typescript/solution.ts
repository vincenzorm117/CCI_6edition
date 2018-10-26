
enum SocketProtocol { TCP, UDP };

class Process {};

enum NodeType {
    Directory, File, Link, Pipe, Socket
}

// Matches Unix like setup for permissions
enum Permission {
    Read = 1, // Binary: 1__
    Write = 2, // Binary: _1_
    Execute = 4 // Binary: __1
}

class User {
    name: string;
    groups: Group[];
}

class Group {
    name: string;
    users: User[];
}

// Base file system node class
abstract class SysNode {
    type: NodeType;
    name: string; // ASCII only
    owner: User;
    group: Group;
    // Permissions for User, Group, and World/Other
    permissions: Permission[] = [0,0,0];
    last_modification: Date;
    linkCount: Number = 0;

    abstract size();
}

// Node for Directories
class DirNode extends SysNode {
    type = NodeType.Directory;

    children: SysNode[] = [];

    size() {
        var size = 0;
        for(var child of this.children) {
            size += child.size();
        }
        return size;
    }
}

// Node for Links
class LinkNode extends SysNode {
    type = NodeType.Link;

    sourceNode: SysNode;

    size() {
        return this.sourceNode.size();
    }
}

// Node for Files
class FileNode extends SysNode {
    type = NodeType.File;

    data: Buffer;

    size() {
        return this.data.size();
    }
}

// Node for Pipes
class PipeNode extends SysNode {
    type = NodeType.Pipe;

    readProcess: Process;
    writeProcess: Process;

    size() {
        return 0;
    }
}

// Node for Sockets
class SocketNode extends SysNode {
    type = NodeType.Socket;

    port: Number;
    protocol: SocketProtocol;
    
    size() {
        return 0;
    }
}