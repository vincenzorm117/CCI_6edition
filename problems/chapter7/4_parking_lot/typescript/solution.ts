
class Car {
    credit: number;
    ticket: Ticket;
    

    constructor(credit: number) {
        this.credit = credit;
    }
}

class Ticket {
    car: Car;
    spot: number;
    parkingLot: ParkingLot;

    constructor(car: Car, spot: number, parkingLot: ParkingLot) {
        this.car = car;
        this.spot = spot;
        this.parkingLot = parkingLot;
    }
}

class ParkingLot {

    size: number;
    parkingSpaces: Ticket[];
    filledSpaces: number = 0;
    price: number;

    
    constructor(size: number, price: number) {
        this.size = size;
        this.price = price;
    }

    updatePrice(price: number) {
        this.price = price;
    }

    findEmptyParkingSpace() {
        for(let i = 0; i < this.size; i++) {
            if( !(this.parkingSpaces[i] instanceof Ticket) ) {
                return i;
            }
        }
        return null;
    }

    isFull() {
        return this.size == this.filledSpaces;
    }

    admitCar(car: Car) {
        if( this.isFull() ) {
            return false;
        }
        if( car.credit < this.price ) {
            return false;
        }
        car.credit -= this.price;
        let index = this.findEmptyParkingSpace();

        let ticket = new Ticket(car, index, this);
        car.ticket = ticket;
        this.parkingSpaces[index] = ticket;
        this.filledSpaces += 1;
        return true;
    }

    exitCar(ticket: Ticket) {
        delete this.parkingSpaces[ticket.spot];
        this.filledSpaces -= 1;
        ticket.car.ticket = null;
    }


}