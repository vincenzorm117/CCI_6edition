

abstract class Employee {
    bosses: Array<Employee>;
    call: Call;

    hasCall(): Boolean { return this.call != null; }
    abstract handleCall(call: Call);
}


class Respondent extends Employee {
    managers: Array<Manager>;
    

    handleCall(call: Call) {} 
    escalateCall(call: Call) {}
}
class Manager extends Employee {
    directors: Array<Director>;

    handleCall(call: Call) {} 
    escalateCall(call: Call) {}
}
class Director extends Employee {
    handleCall(call: Call) {} 
}

class Call {
    conversation: any; // audio converstation
}

class CallCenter {

    respondents = new Array<Respondent>();
    managers = new Array<Manager>();
    directors = new Array<Director>();
    

    dispatchCall(call: Call) {
        for(var respondent of this.respondents) {
            if( !respondent.hasCall() ) {
                respondent.handleCall(call);
                return;
            }
        }
        for(var manager of this.managers) {
            if( !manager.hasCall() ) {
                manager.handleCall(call);
                return;
            }
        }
        for(var director of this.directors) {
            if( !director.hasCall() ) {
                director.handleCall(call);
                return;
            }
        }
    }
}