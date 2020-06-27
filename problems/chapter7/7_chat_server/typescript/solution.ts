
class Message {
    user: User;
    message: string;
    sent_date: Date;

    constructor(user: User, message: string) {
        this.user = user;
        this.message = message;
        this.sent_date = new Date();
    }
}

class User {
    id: number;
    username: string;
    chats: Chat[] = [];
    chatServer: ChatServer;
    online: boolean;
    friends: User[] = [];
    friendRequests: User[] = [];

    constructor(id: number, username: string) {
        this.id = id;
        this.username = username;
        this.online = true;
    }

    setChatServer(chatServer: ChatServer) {
        this.chatServer = chatServer;
    }

    setOnline(online: boolean) {
        this.online = online;
    }

    sendMessage(message: string, chat: Chat) {
        chat.addMessage(this, message);
    }

    signOut() {
        this.chatServer.signOutUser(this);
        this.online = false;
    }

    acceptFriendRequest(user: User) {
        let index = this.friendRequests.indexOf(user);
        if( index < -1 ) throw new Error('user not found');
        this.friendRequests.splice(index,1);

        user.friends.push(this);
        this.friends.push(user);
    }

    receiveFriendRequest(user: User) {
        this.friendRequests.push(user);
    }
}


class Chat {
    users: User[] = [];
    messages: Message[] = [];
    chatServer: ChatServer;

    leaveChat(user: User) {}
    addUser(user: User) {}

    constructor(users: User[], chatServer: ChatServer) {
        this.chatServer = chatServer;
        this.users = users;
        this.users.map(user => user.chats.push(this));
    }

    addMessage(user: User, message: string) {
        this.messages.push(new Message(user, message));
    }
}

class ChatServer {
    chats: Chat[] = [];

    createChat(users: User[]) {
        let chat = new Chat(users, this);
        this.chats.push(chat);
    }

    signOutUser(user: User) {}

    sendFriendRequest(from: User, to: User) {
        to.receiveFriendRequest(from);
    }


}